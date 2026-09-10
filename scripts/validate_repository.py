#!/usr/bin/env python3
"""Validate this repository's Markdown resources and JSON using the standard library.

Usage: python scripts/validate_repository.py [ROOT]
       python scripts/validate_repository.py --root ROOT

This is a repository check, not a general YAML or CommonMark parser. SKILL.md
requires simple top-level, single-line string fields named name and description;
other frontmatter fields are not parsed. Markdown support covers ordinary inline
links/images, single-line reference definitions and references, fenced blocks
(backticks/tildes, up to three leading spaces), inline code and indented code.
It handles angle-bracket destinations, escaped punctuation, balanced parentheses
in destinations and optional quoted titles. It does not validate heading anchors,
HTML links, multiline link syntax, or list/blockquote-nested fences.

Leading-slash link paths are repository-root-relative. File URIs and Windows
absolute paths are rejected: resource links must be portable repository paths.
Other URL schemes, protocol-relative URLs and fragment-only links are ignored.
No URLs are fetched. Git is not required; discovery prunes dependency/cache
directories, hidden directories except the resource namespaces below, and symlink
directories. This is structural validation, not prose or scientific validation.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
import html
import json
import os
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


RESOURCE_HIDDEN_DIRS = {".ai_context", ".agents", ".codex-plugin"}
SKIP_DIRS = {
    "node_modules", "venv", "env", "__pycache__", "site-packages",
    "cache", "caches", "model", "models", "model_cache", "model-cache",
    "vendor", "build", "dist", "mineru_venv", "mineru_models", "output",
}
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
LINK_START = re.compile(r"\[(?:\\.|[^\]\\\n])*\]\(")
BRACKET = re.compile(r"\[((?:\\.|[^\]\\\n])*)\]")
REFERENCE = re.compile(r"^ {0,3}\[((?:\\.|[^\]\\])*)\]:[ \t]*(.*)$")
SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
WINDOWS_ABSOLUTE = re.compile(r"^[A-Za-z]:[\\/]")
PUNCTUATION_ESCAPE = re.compile(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\]\\^_`{|}~])")


@dataclass(frozen=True)
class Issue:
    path: str
    line: int
    message: str

    def __str__(self) -> str:
        return f"{self.path}:{self.line}: {self.message}"


@dataclass
class ValidationResult:
    issues: list[Issue] = field(default_factory=list)
    markdown_files: int = 0
    json_files: int = 0
    json_blocks: int = 0
    local_links: int = 0

    @property
    def ok(self) -> bool:
        return not self.issues


def _blank(text: str) -> str:
    return "".join("\n" if char == "\n" else " " for char in text)


def _escaped(text: str, offset: int) -> bool:
    count = 0
    offset -= 1
    while offset >= 0 and text[offset] == "\\":
        count += 1
        offset -= 1
    return bool(count % 2)


def _strict_json(text: str) -> None:
    def reject_constant(value: str) -> None:
        raise ValueError(f"non-JSON numeric constant {value}")

    json.loads(text, parse_constant=reject_constant)


def _check_json(text: str, path: str, start_line: int, result: ValidationResult) -> None:
    try:
        _strict_json(text)
    except json.JSONDecodeError as exc:
        result.issues.append(Issue(path, start_line + exc.lineno - 1,
                                   f"invalid JSON: {exc.msg}"))
    except ValueError as exc:
        result.issues.append(Issue(path, start_line, f"invalid JSON: {exc}"))


def _simple_scalar(value: str) -> str | None:
    """Parse only the required fields' documented single-line YAML subset."""
    value = value.strip()
    if value.startswith('"'):
        try:
            parsed = json.loads(value)
            return parsed if isinstance(parsed, str) else None
        except ValueError:
            return None
    if value.startswith("'"):
        if len(value) < 2 or not value.endswith("'"):
            return None
        body = value[1:-1]
        if "'" in body.replace("''", ""):
            return None
        return body.replace("''", "'")
    value = re.split(r"\s+#", value, maxsplit=1)[0].strip()
    if not value or value[0] in "|>[]{&*!":
        return None
    if value.lower() in {"null", "~", "true", "false"}:
        return None
    if re.fullmatch(r"[-+]?\d+(?:\.\d+)?", value) or re.search(r":\s", value):
        return None
    return value


def _check_frontmatter(text: str, result: ValidationResult) -> None:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        result.issues.append(Issue("SKILL.md", 1, "missing opening YAML frontmatter delimiter"))
        return
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        result.issues.append(Issue("SKILL.md", 1, "unclosed YAML frontmatter"))
        return
    found: dict[str, list[tuple[int, str]]] = {}
    for number, line in enumerate(lines[1:end], 2):
        match = re.match(r"^(name|description):[ \t]*(.*)$", line)
        if match:
            found.setdefault(match[1], []).append((number, match[2]))
    for key in ("name", "description"):
        entries = found.get(key, [])
        if not entries:
            result.issues.append(Issue("SKILL.md", 1, f"missing required frontmatter field: {key}"))
        elif len(entries) > 1:
            result.issues.append(Issue("SKILL.md", entries[1][0],
                                       f"duplicate frontmatter field: {key}"))
        elif not _simple_scalar(entries[0][1]):
            result.issues.append(Issue(
                "SKILL.md", entries[0][0],
                f"{key} must be a nonempty single-line string in the supported YAML subset",
            ))


def _mask_inline_code(text: str) -> str:
    pieces = list(text)
    offset = 0
    while offset < len(text):
        opening = re.search(r"`+", text[offset:])
        if not opening:
            break
        start = offset + opening.start()
        run = opening.group()
        offset = start + len(run)
        if _escaped(text, start):
            continue
        closing = re.search(r"(?<!`)" + re.escape(run) + r"(?!`)", text[offset:])
        if closing:
            end = offset + closing.end()
            pieces[start:end] = _blank(text[start:end])
            offset = end
    return "".join(pieces)


def _mask_comment_line(text: str, in_comment: bool) -> tuple[str, bool]:
    parts: list[str] = []
    offset = 0
    while offset < len(text):
        marker = text.find("-->" if in_comment else "<!--", offset)
        if marker < 0:
            parts.append(_blank(text[offset:]) if in_comment else text[offset:])
            break
        end = marker + (3 if in_comment else 4)
        parts.append(_blank(text[offset:end]) if in_comment
                     else text[offset:marker] + _blank(text[marker:end]))
        in_comment = not in_comment
        offset = end
    return "".join(parts), in_comment


def _markdown_prose(text: str, path: str, result: ValidationResult) -> str:
    prose: list[str] = []
    opening: tuple[str, int, int, str] | None = None
    body: list[str] = []
    in_comment = False
    for number, line in enumerate(text.splitlines(keepends=True), 1):
        match = FENCE.match(line.rstrip("\r\n"))
        if opening is not None:
            marker, size, first_line, language = opening
            if match and match[1][0] == marker and len(match[1]) >= size and not match[2].strip():
                if language == "json":
                    result.json_blocks += 1
                    _check_json("".join(body), path, first_line + 1, result)
                opening = None
                body = []
            else:
                body.append(line)
            prose.append(_blank(line))
            continue
        if not in_comment and match and not (match[1][0] == "`" and "`" in match[2]):
            info = match[2].strip().split()
            opening = (match[1][0], len(match[1]), number, info[0].lower() if info else "")
            prose.append(_blank(line))
        elif not in_comment and (line.startswith("    ") or line.startswith("\t")):
            prose.append(_blank(line))
        else:
            # Literal comment markers in code must not hide subsequent prose.
            visible, in_comment = _mask_comment_line(_mask_inline_code(line), in_comment)
            prose.append(visible)
    if opening:
        result.issues.append(Issue(path, opening[2], "unclosed Markdown code fence"))
    return _mask_inline_code("".join(prose))


def _destination(text: str, start: int) -> tuple[str, int] | None:
    """Return one destination token and its end; the caller checks its terminator."""
    offset = start
    if offset >= len(text):
        return "", offset
    if text[offset] == "<":
        offset += 1
        begin = offset
        while offset < len(text):
            if text[offset] == "\n":
                return None
            if text[offset] == ">" and not _escaped(text, offset):
                return text[begin:offset], offset + 1
            offset += 1
        return None
    depth = 0
    while offset < len(text):
        char = text[offset]
        if char.isspace():
            break
        if char == "\\" and offset + 1 < len(text) and PUNCTUATION_ESCAPE.match(text, offset):
            offset += 2
            continue
        if char == "(":
            depth += 1
        elif char == ")":
            if depth == 0:
                break
            depth -= 1
        offset += 1
    if depth:
        return None
    return text[start:offset], offset


def _tail_valid(text: str, end: int, inline: bool) -> bool:
    tail = text[end:]
    # Links in this repository use single-line destinations and optional titles.
    tail = tail.split("\n", 1)[0]
    if inline:
        return bool(re.match(r"^[ \t]*(?:(?:\"(?:\\.|[^\"\\])*\"|'(?:\\.|[^'\\])*'|\([^()]*\))[ \t]*)?\)", tail))
    return bool(re.fullmatch(r"[ \t]*(?:\"(?:\\.|[^\"\\])*\"|'(?:\\.|[^'\\])*'|\([^()]*\))?[ \t]*", tail))


def _reference_key(label: str) -> str:
    return " ".join(PUNCTUATION_ESCAPE.sub(r"\1", label).split()).casefold()


def _links(prose: str) -> list[tuple[str, int]]:
    links: list[tuple[str, int]] = []
    references: dict[str, tuple[str, int]] = {}
    body: list[str] = []
    for number, line in enumerate(prose.splitlines(keepends=True), 1):
        match = REFERENCE.match(line.rstrip("\r\n"))
        if match:
            parsed = _destination(match[2], 0)
            if parsed and _tail_valid(match[2], parsed[1], inline=False):
                references.setdefault(_reference_key(match[1]), (parsed[0], number))
                body.append(_blank(line))
                continue
        body.append(line)
    text = "".join(body)
    for match in LINK_START.finditer(text):
        if _escaped(text, match.start()):
            continue
        start = match.end()
        while start < len(text) and text[start] in " \t":
            start += 1
        parsed = _destination(text, start)
        if parsed and _tail_valid(text, parsed[1], inline=True):
            links.append((parsed[0], text.count("\n", 0, match.start()) + 1))
    used_references: set[str] = set()
    for match in BRACKET.finditer(text):
        if _escaped(text, match.start()) or text[match.end():match.end() + 1] == "(":
            continue
        label = match[1]
        following = BRACKET.match(text, match.end())
        if following:
            label = following[1] or label
        key = _reference_key(label)
        if key in references and key not in used_references:
            links.append(references[key])
            used_references.add(key)
    return links


def _check_link(target: str, source: Path, root: Path, line: int,
                result: ValidationResult) -> None:
    target = html.unescape(PUNCTUATION_ESCAPE.sub(r"\1", target))
    path = source.relative_to(root).as_posix()
    if not target or target.startswith(("#", "//")):
        return
    if WINDOWS_ABSOLUTE.match(target) or target.startswith("\\\\") or target.lower().startswith("file:"):
        result.issues.append(Issue(path, line, f"local link must be repository-relative: {target}"))
        return
    if SCHEME.match(target):
        return
    try:
        resource = unquote(urlsplit(target).path).replace("\\", "/")
        if not resource:
            return
        candidate = (root / resource.lstrip("/") if resource.startswith("/")
                     else source.parent / resource).resolve()
        result.local_links += 1
        if not candidate.is_relative_to(root):
            result.issues.append(Issue(path, line, f"local link escapes repository: {target}"))
        elif not candidate.exists():
            result.issues.append(Issue(path, line, f"missing local resource: {target}"))
    except (OSError, ValueError, RuntimeError) as exc:
        result.issues.append(Issue(path, line, f"invalid local link {target!r}: {exc}"))


def _resource_files(root: Path):
    for directory, subdirs, names in os.walk(root, followlinks=False):
        subdirs[:] = sorted(
            name for name in subdirs
            if name.lower() not in SKIP_DIRS
            and (not name.startswith(".") or name in RESOURCE_HIDDEN_DIRS)
            and not (Path(directory) / name).is_symlink()
        )
        for name in sorted(names):
            path = Path(directory) / name
            if path.suffix.lower() in {".md", ".json"}:
                yield path


def validate_repository(root: Path | str) -> ValidationResult:
    root = Path(root).resolve()
    result = ValidationResult()
    if not root.is_dir():
        result.issues.append(Issue(str(root), 1, "repository root is not a directory"))
        return result
    if not (root / "SKILL.md").is_file():
        result.issues.append(Issue("SKILL.md", 1, "missing root SKILL.md"))
    for path in _resource_files(root):
        relative = path.relative_to(root).as_posix()
        try:
            if not path.resolve().is_relative_to(root):
                result.issues.append(Issue(relative, 1, "resource symlink escapes repository"))
                continue
            text = path.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError, RuntimeError) as exc:
            result.issues.append(Issue(relative, 1, f"cannot read UTF-8 resource: {exc}"))
            continue
        if path.suffix.lower() == ".json":
            result.json_files += 1
            _check_json(text, relative, 1, result)
        else:
            result.markdown_files += 1
            if path == root / "SKILL.md":
                _check_frontmatter(text, result)
            prose = _markdown_prose(text, relative, result)
            for target, line in _links(prose):
                _check_link(target, path, root, line, result)
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("root", nargs="?", type=Path, help="repository root (default: script's parent repository)")
    parser.add_argument("--root", dest="root_option", type=Path, help="alternative named root argument")
    args = parser.parse_args(argv)
    if args.root is not None and args.root_option is not None:
        parser.error("provide ROOT or --root, not both")
    root = args.root_option or args.root or Path(__file__).resolve().parents[1]
    result = validate_repository(root)
    for issue in result.issues:
        print(issue, file=sys.stderr)
    print(f"{'PASS' if result.ok else 'FAIL'}: {result.markdown_files} Markdown files, "
          f"{result.json_files} JSON files, {result.json_blocks} JSON blocks, "
          f"{result.local_links} local links; {len(result.issues)} issue(s).")
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
