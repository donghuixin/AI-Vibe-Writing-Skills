"""Offline, read-only editing prompts. This module does not infer authorship."""
from __future__ import annotations

import argparse
from bisect import bisect_right
from dataclasses import asdict, dataclass
import json
import os
from pathlib import Path
import re
import sys
from typing import Mapping, Sequence


@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    column: int
    excerpt: str
    rule: str
    reason: str


@dataclass(frozen=True)
class Rule:
    id: str
    pattern: str
    reason: str


RULES = (
    Rule("preface-en", r"\b(?:it\s+is\s+(?:worth\s+noting|important\s+to\s+note)|it\s+should\s+be\s+noted)\s+that\b",
         "This lead-in delays the proposition. Consider starting with the point; keep it if the emphasis serves a purpose."),
    Rule("preface-zh", r"(?:值得注意的是|需要指出的是|需要強調的是|需要强调的是)",
         "這個引導語延後了實際要點；可考慮直接陳述，但應保留有明確用途的強調。"),
    Rule("broad-applications", r"\ba\s+wide\s+range\s+of\s+(?:[a-z]+\s+){0,3}(?:applications|use\s+cases)\b",
         "Check whether the surrounding text identifies the applications and supports this scope. This phrase alone does not establish an evidence gap."),
)
REPEATED_REASON = "The same transition opens at least three sentences in this paragraph. Consider whether each transition is needed; repetition can also be intentional."

# Mandatory argument counts, after any optional arguments. Unknown macros retain
# their prose arguments. Custom review templates can extend this mapping.
SKIP_MACROS = {
    "reviewcomment": 2, "reviewercomment": 2, "overallcomment": 1,
    "closingcomment": 1, "reviewheading": 1, "reviewerquote": 1,
    "enquote": 1, "textquote": 1, "blockquote": 1,
    "foreignquote": 2, "hyphenquote": 2,
    "pending": 1, "authoraction": 1, "location": 1, "changelocation": 1,
    "cite": 1, "citep": 1, "citet": 1, "citeauthor": 1,
    "citeyear": 1, "citeyearpar": 1, "parencite": 1,
    "textcite": 1, "autocite": 1, "footcite": 1, "nocite": 1,
    "ref": 1, "eqref": 1, "autoref": 1, "pageref": 1, "cref": 1,
    "vref": 1, "label": 1, "hyperref": 1, "href": 2, "url": 1,
    "path": 1, "ensuremath": 1, "bibliography": 1,
    "bibliographystyle": 1, "bibitem": 1, "input": 1, "include": 1,
    "includegraphics": 1, "lstinputlisting": 1, "inputminted": 2,
}
SKIP_ENVS = {
    "equation", "equation*", "align", "align*", "alignat", "alignat*",
    "aligned", "alignedat", "gather", "gather*", "gathered",
    "multline", "multline*", "flalign", "flalign*", "eqnarray", "eqnarray*",
    "math", "displaymath", "split", "cases", "array", "subequations",
    "verbatim", "verbatim*", "Verbatim", "BVerbatim", "LVerbatim",
    "SaveVerbatim", "lstlisting", "minted", "comment", "filecontents",
    "filecontents*", "quote", "quotation", "displayquote", "thebibliography",
}
PRUNED_DIRS = {".git", ".hg", ".svn", ".venv", "venv", "node_modules", "__pycache__"}


def _blank(chars: list[str], start: int, end: int, *, syntax: bool = False) -> None:
    # A NUL barrier prevents a rule from joining prose across excluded content.
    for i in range(start, min(end, len(chars))):
        if chars[i] not in "\r\n":
            chars[i] = " " if syntax else "\x00"


def _space(text: str, pos: int) -> int:
    while pos < len(text):
        if text[pos].isspace():
            pos += 1
        elif text[pos] == "%":
            end = text.find("\n", pos)
            pos = len(text) if end < 0 else end + 1
        else:
            break
    return pos


def _group_end(text: str, start: int) -> int:
    """Return end of a braced/optional group; fail closed if it is unbalanced."""
    if start >= len(text) or text[start] not in "{[":
        return start
    closer = "}" if text[start] == "{" else "]"
    depth = 1
    pos = start + 1
    while pos < len(text):
        ch = text[pos]
        if ch == "\\":
            pos += 2
            continue
        if ch == "%":
            end = text.find("\n", pos)
            pos = len(text) if end < 0 else end + 1
            continue
        if closer == "]" and ch == "{":
            pos = _group_end(text, pos)
            continue
        if ch == text[start]:
            depth += 1
        elif ch == closer:
            depth -= 1
            if depth == 0:
                return pos + 1
        pos += 1
    return len(text)


def _arguments_end(text: str, pos: int, count: int) -> int:
    for _ in range(count):
        pos = _space(text, pos)
        while pos < len(text) and text[pos] == "[":
            pos = _space(text, _group_end(text, pos))
        if pos >= len(text) or text[pos] != "{":
            return pos
        pos = _group_end(text, pos)
    return pos


def _environment_end(text: str, start: int, name: str) -> int:
    pattern = re.compile(r"\\(begin|end)\s*\{" + re.escape(name) + r"\}")
    depth = 1
    for match in pattern.finditer(text, start):
        depth += 1 if match[1] == "begin" else -1
        if depth == 0:
            return match.end()
    return len(text)


def _definition_end(text: str, pos: int, name: str) -> int:
    if name in {"def", "gdef", "edef", "xdef"}:
        body = text.find("{", pos)
        return len(text) if body < 0 else _group_end(text, body)
    pos = _space(text, pos)
    if pos < len(text) and text[pos] == "{":
        pos = _group_end(text, pos)
    else:
        macro = re.match(r"\\[A-Za-z@]+", text[pos:])
        if macro:
            pos += macro.end()
    return _arguments_end(text, pos, 2 if "environment" in name else 1)


def mask_latex(text: str, skip_macros: Mapping[str, int] | None = None,
               skip_environments: Sequence[str] = (), *, comments: bool = True) -> str:
    """Conservatively hide common non-author prose while preserving offsets."""
    macros = dict(SKIP_MACROS)
    for name, count in (skip_macros or {}).items():
        if not re.fullmatch(r"[A-Za-z@]+", name) or not isinstance(count, int) or count < 1:
            raise ValueError("skip_macros requires command names and positive argument counts")
        macros[name.lower()] = count
    envs = SKIP_ENVS | set(skip_environments)
    chars = list(text)
    pos = 0
    while pos < len(text):
        ch = text[pos]
        if ch == "%" and comments:
            end = text.find("\n", pos)
            end = len(text) if end < 0 else end
            _blank(chars, pos, end)
            pos = end
        elif ch == "$":
            delimiter = "$$" if text.startswith("$$", pos) else "$"
            end = pos + len(delimiter)
            while end < len(text):
                if text[end] == "\\":
                    end += 2
                elif text.startswith(delimiter, end):
                    end += len(delimiter)
                    break
                else:
                    end += 1
            _blank(chars, pos, end)
            pos = end
        elif text.startswith("``", pos) or ch in {'"', "“", "‘"}:
            opener = "``" if text.startswith("``", pos) else ch
            closer = {"``": "''", '"': '"', "“": "”", "‘": "’"}[opener]
            end = text.find(closer, pos + len(opener))
            while end > 0 and text[end - 1] == "\\":
                end = text.find(closer, end + len(closer))
            if end < 0:
                pos += len(opener)
            else:
                end += len(closer)
                _blank(chars, pos, end)
                pos = end
        elif ch in "{}":
            _blank(chars, pos, pos + 1, syntax=True)
            pos += 1
        elif ch != "\\":
            pos += 1
        elif text.startswith((r"\(", r"\["), pos):
            closer = r"\)" if text[pos + 1] == "(" else r"\]"
            end = text.find(closer, pos + 2)
            end = len(text) if end < 0 else end + 2
            _blank(chars, pos, end)
            pos = end
        else:
            command = re.match(r"\\([A-Za-z@]+)(\*)?", text[pos:])
            if not command:
                _blank(chars, pos, pos + 2)
                pos += 2
                continue
            name = command[1]
            lower = name.lower()
            end = pos + command.end()
            if lower in {"begin", "end"}:
                arg = _space(text, end)
                arg_end = _group_end(text, arg)
                env = text[arg + 1:arg_end - 1] if arg_end > arg else ""
                end = arg_end
                if lower == "begin" and env in envs:
                    end = _environment_end(text, end, env)
                    _blank(chars, pos, end)
                else:
                    _blank(chars, pos, end, syntax=True)
            elif lower in {"newcommand", "renewcommand", "providecommand", "declarerobustcommand",
                           "newenvironment", "renewenvironment", "def", "gdef", "edef", "xdef"}:
                end = _definition_end(text, end, lower)
                _blank(chars, pos, end)
            elif lower in {"verb", "lstinline", "mintinline"}:
                at = _space(text, end)
                if at < len(text) and text[at] == "[":
                    at = _space(text, _group_end(text, at))
                if lower == "mintinline":
                    at = _space(text, _arguments_end(text, at, 1))
                if at < len(text) and text[at] == "{":
                    end = _group_end(text, at)
                elif at < len(text):
                    close = text.find(text[at], at + 1)
                    end = len(text) if close < 0 else close + 1
                else:
                    end = len(text)
                _blank(chars, pos, end)
            elif lower in macros:
                end = _arguments_end(text, end, macros[lower])
                _blank(chars, pos, end)
            else:
                _blank(chars, pos, end, syntax=True)
            pos = max(end, pos + 1)
    return "".join(chars)


def mask_markdown(text: str) -> str:
    chars = list(text)
    offset = 0
    fence: tuple[str, int] | None = None
    lazy_quote = False
    for line in text.splitlines(keepends=True):
        opening = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)", line)
        quoted = bool(re.match(r"^ {0,3}>", line))
        hidden = False
        if fence:
            hidden = True
            if opening and opening[1][0] == fence[0] and len(opening[1]) >= fence[1] and not opening[2].strip():
                fence = None
        elif opening:
            fence = (opening[1][0], len(opening[1]))
            hidden = True
        elif quoted or (lazy_quote and line.strip()):
            lazy_quote = True
            hidden = True
        elif re.match(r"^(?: {4}|\t)|^ {0,3}\[[^\]]+\]:", line):
            hidden = True
        if not line.strip():
            lazy_quote = False
        if hidden:
            _blank(chars, offset, offset + len(line))
        offset += len(line)
    # Protect inline code before interpreting HTML comment delimiters in prose.
    intermediate = "".join(chars)
    inline_code = r"(?<!`)(`+)(?!`)[\s\S]*?(?<!`)\1(?!`)"
    for match in re.finditer(inline_code, intermediate):
        _blank(chars, match.start(), match.end())
    intermediate = "".join(chars)
    html = r"<!--[\s\S]*?(?:-->|\Z)|<(pre|code|blockquote|script)\b[^>]*>[\s\S]*?(?:</\1\s*>|\Z)"
    for match in re.finditer(html, intermediate, re.IGNORECASE):
        _blank(chars, match.start(), match.end())
    intermediate = "".join(chars)
    # Link text is conservatively excluded along with its destination.
    links = r"!?\[[^\]\n]*\](?:\([^\n)]*\)|\[[^\]\n]*\])|\[(?:@|\^)[^\]\n]*\]|\[\d+(?:\s*[,;-]\s*\d+)*\]"
    for match in re.finditer(links, intermediate):
        _blank(chars, match.start(), match.end())
    return "".join(chars)


def lint_text(text: str, *, path: str = "<memory>", syntax: str = "tex",
              skip_macros: Mapping[str, int] | None = None,
              skip_environments: Sequence[str] = ()) -> list[Finding]:
    if syntax not in {"tex", "md"}:
        raise ValueError("syntax must be 'tex' or 'md'")
    masked = mask_markdown(text) if syntax == "md" else text
    masked = mask_latex(masked, skip_macros, skip_environments, comments=(syntax == "tex"))
    matches: list[tuple[int, int, str, str]] = []
    for rule in RULES:
        matches.extend((m.start(), m.end(), rule.id, rule.reason)
                       for m in re.finditer(rule.pattern, masked, re.IGNORECASE))
    boundaries = [m.end() for m in re.finditer(r"\n[ \t\r\x00]*\n", masked)]
    counts: dict[tuple[int, str], int] = {}
    opener = r"(?:^|(?<=[.!?]))[ \t]*(?P<opener>Furthermore|Moreover|Additionally|Importantly|In addition)[ \t]*,"
    for match in re.finditer(opener, masked, re.IGNORECASE | re.MULTILINE):
        key = (bisect_right(boundaries, match.start("opener")), match["opener"].lower())
        counts[key] = counts.get(key, 0) + 1
        if counts[key] >= 3:
            matches.append((match.start("opener"), match.end(), "repeated-opener", REPEATED_REASON))
    newlines = [-1] + [m.start() for m in re.finditer("\n", text)]
    findings = []
    for start, end, rule, reason in sorted(matches, key=lambda item: (item[0], item[2])):
        line = bisect_right(newlines, start - 1)
        excerpt = re.sub(r"\s+", " ", text[start:end])
        if len(excerpt) > 180:
            excerpt = excerpt[:177] + "..."
        findings.append(Finding(str(path), line, start - newlines[line - 1], excerpt, rule, reason))
    return findings


def lint_file(path: str | Path, **options: object) -> list[Finding]:
    source = Path(path)
    suffix = source.suffix.lower()
    if suffix not in {".tex", ".md"}:
        raise ValueError("only .tex and .md files are supported")
    return lint_text(source.read_text(encoding="utf-8-sig"), path=str(source), syntax=suffix[1:], **options)


def _collect(paths: Sequence[str], recursive: bool) -> tuple[list[Path], list[dict[str, str]]]:
    files: set[Path] = set()
    errors = []
    for raw in paths:
        source = Path(raw)
        if source.is_file():
            if source.suffix.lower() in {".tex", ".md"}:
                files.add(source.resolve())
            else:
                errors.append({"path": raw, "message": "only .tex and .md files are supported"})
        elif source.is_dir():
            found = False
            def onerror(error: OSError) -> None:
                errors.append({"path": str(error.filename or source), "message": str(error)})
            for root, dirs, names in os.walk(source, followlinks=False, onerror=onerror):
                dirs[:] = sorted(d for d in dirs if d not in PRUNED_DIRS) if recursive else []
                for name in sorted(names):
                    candidate = Path(root) / name
                    if candidate.suffix.lower() in {".tex", ".md"}:
                        files.add(candidate.resolve())
                        found = True
            if not found:
                errors.append({"path": raw, "message": "no eligible .tex or .md files found"})
        else:
            errors.append({"path": raw, "message": "path does not exist or is not a regular file/directory"})
    return sorted(files, key=str), errors


def _macro_argument(value: str) -> tuple[str, int]:
    match = re.fullmatch(r"([A-Za-z@]+)=([1-9][0-9]*)", value)
    if not match:
        raise argparse.ArgumentTypeError("use NAME=N, e.g. reviewertext=2")
    return match[1], int(match[2])


def main(argv: Sequence[str] | None = None) -> int:
    # CLI output has a predictable encoding, including when redirected on Windows.
    # Do not alter streams when the module is merely imported as a library.
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Read-only local style prompts; no models, network requests, or authorship judgments.")
    parser.add_argument("paths", nargs="*", help="UTF-8 .tex/.md files or directories")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--json", dest="format", action="store_const", const="json", help="alias for --format json")
    parser.add_argument("--no-recursive", action="store_true", help="scan only the top level of input directories")
    parser.add_argument("--skip-macro", action="append", type=_macro_argument, default=[], metavar="NAME=N")
    parser.add_argument("--skip-env", action="append", default=[], metavar="NAME")
    parser.add_argument("--list-rules", action="store_true")
    args = parser.parse_args(argv)
    if args.list_rules:
        catalog = [asdict(rule) for rule in RULES] + [{"id": "repeated-opener", "pattern": "third and later identical sentence transition in one paragraph", "reason": REPEATED_REASON}]
        print(json.dumps(catalog, ensure_ascii=False, indent=2) if args.format == "json" else "\n".join(f"{r['id']}: {r['reason']}" for r in catalog))
        return 0
    if not args.paths:
        parser.error("provide at least one file or directory (or use --list-rules)")
    files, errors = _collect(args.paths, not args.no_recursive)
    findings = []
    scanned = []
    for source in files:
        try:
            findings.extend(lint_file(source, skip_macros=dict(args.skip_macro), skip_environments=args.skip_env))
            scanned.append(str(source))
        except (OSError, UnicodeError, ValueError) as error:
            errors.append({"path": str(source), "message": str(error)})
    if args.format == "json":
        print(json.dumps({"schema_version": 1, "tool": "local-style-lint", "files_scanned": scanned,
                          "findings": [asdict(finding) for finding in findings], "errors": errors}, ensure_ascii=False, indent=2))
    else:
        for finding in findings:
            print(f"{finding.path}:{finding.line}:{finding.column} [{finding.rule}] {finding.excerpt}\n  {finding.reason}")
        for error in errors:
            print(f"{error['path']}: {error['message']}", file=sys.stderr)
        print(f"Scanned {len(scanned)} file(s); {len(findings)} style prompt(s). These are editing suggestions, not authorship judgments.")
    return 2 if errors else 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
