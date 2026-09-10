"""Synthetic behavior tests. No paper, review, or identity data is used."""
from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "Local_AI_Style_Check" / "style_lint.py"
LEGACY = TOOL.with_name("paper_ai_detector.py")
SPEC = importlib.util.spec_from_file_location("local_style_lint_under_test", TOOL)
assert SPEC is not None and SPEC.loader is not None
lint = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = lint
SPEC.loader.exec_module(lint)
PHRASE = "It is worth noting that"


class StyleLintTextTests(unittest.TestCase):
    def test_exact_line_column_and_repeated_phrase_locations(self):
        source = "A neutral sentence.\r\n  " + PHRASE + " the queue is bounded.\r\n" + PHRASE + " its size is fixed."
        findings = lint.lint_text(source, path="synthetic.tex")
        self.assertEqual([(f.path, f.line, f.column, f.excerpt, f.rule) for f in findings], [
            ("synthetic.tex", 2, 3, PHRASE, "preface-en"),
            ("synthetic.tex", 3, 1, PHRASE, "preface-en"),
        ])

    def test_wrapped_and_formatted_prose_keeps_source_position(self):
        source = "Heading\n  It is \\emph{worth\nnoting} that the queue is bounded."
        finding, = lint.lint_text(source)
        self.assertEqual((finding.line, finding.column), (2, 3))
        self.assertEqual(finding.excerpt, r"It is \emph{worth noting} that")

    def test_original_review_macro_shapes_hide_quotes_but_scan_responses(self):
        source = (
            "\\reviewheading{" + PHRASE + "}\n"
            "\\overallcomment{" + PHRASE + " the finding is useful.}\n"
            "\\reviewcomment{1}{" + PHRASE + " {the nested note} merits attention.}\n"
            "\\reviewercomment{2}{" + PHRASE + " another point matters.}\n"
            "\\closingcomment{" + PHRASE + "}\n"
            "\\reviewresponse{" + PHRASE + " the buffer is bounded.}"
        )
        finding, = lint.lint_text(source)
        self.assertEqual((finding.line, finding.column), (6, 17))

    def test_latex_comments_citations_and_refs_are_hidden(self):
        source = (
            "% " + PHRASE + "\n"
            "\\citep[" + PHRASE + "][p.~2]{demo}\n"
            "\\Cref{" + PHRASE + "} \\href{https://example.invalid}{" + PHRASE + "}\n"
            "\\label{" + PHRASE + "}\n"
            "An escaped \\% keeps prose. " + PHRASE + " the buffer is bounded."
        )
        finding, = lint.lint_text(source)
        self.assertEqual(finding.line, 5)

    def test_math_forms_are_hidden(self):
        source = "\n".join([
            "$\\text{" + PHRASE + "}$", "$$" + PHRASE + "$$",
            "\\(" + PHRASE + "\\)", "\\[" + PHRASE + "\\]",
            "\\begin{equation*}\\text{" + PHRASE + "}\\end{equation*}",
            "\\begin{align}" + PHRASE + "\\end{align}",
            "\\ensuremath{" + PHRASE + "}", PHRASE + " the buffer is bounded.",
        ])
        finding, = lint.lint_text(source)
        self.assertEqual(finding.line, 8)

    def test_quotes_verbatim_and_definitions_are_hidden(self):
        source = "\n".join([
            '"' + PHRASE + '"', "``" + PHRASE + "''", "“" + PHRASE + "”",
            "\\enquote{" + PHRASE + "}",
            "\\begin{quotation}" + PHRASE + "\\end{quotation}",
            "\\begin{verbatim}" + PHRASE + "\\end{verbatim}",
            "\\verb|" + PHRASE + "|", "\\lstinline[language=Python]|" + PHRASE + "|",
            "\\mintinline{python}{" + PHRASE + "}",
            "\\newcommand{\\demo}[2]{" + PHRASE + " #1 {#2}}",
            "\\def\\demo#1{" + PHRASE + " {#1}}",
            "\\newenvironment{demo}[1]{" + PHRASE + "}{" + PHRASE + "}",
        ])
        self.assertEqual(lint.lint_text(source), [])

    def test_nested_groups_and_custom_exclusions(self):
        source = (
            "\\customreview[tag]{id}{" + PHRASE + " a (partial label has {nested braces}.}\n"
            "\\begin{customquote}" + PHRASE + "\\end{customquote}\n"
            "\\reviewresponse{" + PHRASE + " the buffer is bounded.}"
        )
        findings = lint.lint_text(source, skip_macros={"customreview": 2}, skip_environments=["customquote"])
        self.assertEqual([f.line for f in findings], [3])

    def test_excluded_content_is_a_barrier_not_a_joiner(self):
        source = "It is $x$ worth noting that.\nIt is \\cite{demo} worth noting that.\nIt is % hidden\nworth noting that."
        self.assertEqual(lint.lint_text(source), [])

    def test_markdown_quotes_code_links_and_embedded_math(self):
        source = "\n".join([
            "> " + PHRASE, PHRASE + " (lazy continuation)", "",
            "```tex", PHRASE, "```", "~~~", PHRASE, "~~~",
            "`" + PHRASE + "`", "    " + PHRASE,
            "<!-- " + PHRASE + " -->", "<blockquote>" + PHRASE + "</blockquote>",
            "[" + PHRASE + "](https://example.invalid)",
            "[" + PHRASE + "][demo]", "[demo]: https://example.invalid '" + PHRASE + "'",
            "[@" + PHRASE + "]", "$\\text{" + PHRASE + "}$", "",
            PHRASE + " the buffer is bounded.",
        ])
        finding, = lint.lint_text(source, syntax="md")
        self.assertEqual(finding.line, 20)

    def test_normal_academic_and_technical_words_are_not_signals(self):
        source = ("An orthogonal basis yields a robust estimator. The landscape has two minima. "
                  "The paradigm uses a significant coefficient and a crucial boundary condition. "
                  "The innovative method improves throughput by 12% in this setup.\n"
                  "本方法旨在估計正交基，採用鲁棒优化；結果表明此參數影響吞吐率。")
        self.assertEqual(lint.lint_text(source), [])

    def test_markdown_percentage_does_not_start_a_tex_comment(self):
        source = "CPU load is 80%. " + PHRASE + " queues shrink."
        finding, = lint.lint_text(source, syntax="md")
        self.assertEqual((finding.line, finding.column), (1, 18))
        self.assertEqual(lint.lint_text(source, syntax="tex"), [])

    def test_markdown_inline_code_cannot_start_a_false_html_comment(self):
        source = "The delimiter is `<!--`.\n\n" + PHRASE + " the buffer is bounded."
        finding, = lint.lint_text(source, syntax="md")
        self.assertEqual(finding.line, 3)

    def test_finite_chinese_and_scope_prompts(self):
        findings = lint.lint_text("需要指出的是，緩衝區大小固定。\nThe method serves a wide range of sensing applications.")
        self.assertEqual([(f.line, f.rule) for f in findings], [(1, "preface-zh"), (2, "broad-applications")])

    def test_repeated_opener_is_local_and_reports_third_and_later(self):
        source = "Moreover, A. Moreover, B.\nMoreover, C. Moreover, D.\n\nMoreover, E. Moreover, F."
        findings = lint.lint_text(source)
        self.assertEqual([(f.line, f.column, f.rule) for f in findings], [(2, 1, "repeated-opener"), (2, 14, "repeated-opener")])

    def test_bad_api_options_fail_instead_of_silently_succeeding(self):
        with self.assertRaises(ValueError):
            lint.lint_text("text", syntax="pdf")
        with self.assertRaises(ValueError):
            lint.lint_text("text", skip_macros={"bad": 0})


class StyleLintCliTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="style lint synthetic ")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)

    def write(self, relative, text):
        path = self.base / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def run_cli(self, *args, legacy=False):
        env = dict(os.environ, PYTHONIOENCODING="utf-8")
        return subprocess.run([sys.executable, "-S", str(LEGACY if legacy else TOOL), *map(str, args)],
                              capture_output=True, text=True, encoding="utf-8", env=env, check=False)

    def test_recursive_json_locates_files_and_leaves_sources_unchanged(self):
        first = self.write("a.tex", "A neutral sentence.\n" + PHRASE + " the buffer is bounded.")
        second = self.write("nested/b.md", "需要指出的是，緩衝區大小固定。")
        self.write("nested/ignored.pdf", PHRASE)
        self.write(".git/ignored.md", PHRASE)
        before = {path: path.read_bytes() for path in (first, second)}
        result = self.run_cli(self.base, "--json")
        self.assertEqual(result.returncode, 1, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["errors"], [])
        self.assertEqual(report["files_scanned"], sorted(str(p.resolve()) for p in (first, second)))
        self.assertEqual([(f["line"], f["rule"]) for f in report["findings"]], [(2, "preface-en"), (1, "preface-zh")])
        for path, data in before.items():
            self.assertEqual(path.read_bytes(), data)

    def test_clean_and_no_recursive_exit_zero(self):
        self.write("a.TEX", "An orthogonal basis represents the signal.")
        self.write("nested/b.md", PHRASE)
        result = self.run_cli(self.base, "--no-recursive", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(len(report["files_scanned"]), 1)
        self.assertEqual(report["findings"], [])

    def test_missing_empty_unsupported_paths_fail_honestly(self):
        unsupported = self.write("input.pdf", "synthetic")
        empty = self.base / "empty"
        empty.mkdir()
        for path in (self.base / "missing", empty, unsupported):
            with self.subTest(path=path):
                result = self.run_cli(path, "--json")
                self.assertEqual(result.returncode, 2)
                self.assertTrue(json.loads(result.stdout)["errors"])

    def test_usage_errors_are_nonzero(self):
        for args in ((), ("--unknown-option",), ("--skip-macro", "bad"), ("--format", "xml")):
            with self.subTest(args=args):
                result = self.run_cli(*args)
                self.assertEqual(result.returncode, 2)
                self.assertIn("error:", result.stderr)

    def test_decode_error_retains_successful_results_but_returns_error(self):
        self.write("good.md", PHRASE)
        (self.base / "bad.tex").write_bytes(b"\xff\xfeinvalid utf8")
        result = self.run_cli(self.base, "--json")
        self.assertEqual(result.returncode, 2)
        report = json.loads(result.stdout)
        self.assertEqual(len(report["errors"]), 1)
        self.assertEqual(len(report["files_scanned"]), 1)
        self.assertEqual(len(report["findings"]), 1)

    def test_legacy_entrypoint_forwards_identical_cli(self):
        source = self.write("paper.tex", PHRASE)
        canonical = self.run_cli(source, "--json")
        legacy = self.run_cli(source, "--json", legacy=True)
        self.assertEqual((legacy.returncode, legacy.stdout, legacy.stderr),
                         (canonical.returncode, canonical.stdout, canonical.stderr))

    def test_list_rules_and_custom_cli_exclusions(self):
        catalog = self.run_cli("--list-rules", "--json")
        self.assertEqual(catalog.returncode, 0)
        self.assertEqual({rule["id"] for rule in json.loads(catalog.stdout)},
                         {"preface-en", "preface-zh", "broad-applications", "repeated-opener"})
        source = self.write("paper.tex", "\\custom{1}{" + PHRASE + "}\n\\begin{original}" + PHRASE + "\\end{original}")
        result = self.run_cli(source, "--skip-macro", "custom=2", "--skip-env", "original", "--json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["findings"], [])

    def test_utf8_bom_file_and_text_output(self):
        source = self.base / "bom.md"
        source.write_text("Plain.\n" + PHRASE + " the buffer is bounded.", encoding="utf-8-sig")
        result = self.run_cli(source)
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn(":2:1 [preface-en] " + PHRASE, result.stdout)

    def test_cli_json_is_utf8_even_with_ascii_environment(self):
        result = subprocess.run([sys.executable, "-S", str(TOOL), "--list-rules", "--json"],
                                capture_output=True, env=dict(os.environ, PYTHONIOENCODING="ascii"), check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        catalog = json.loads(result.stdout.decode("utf-8"))
        self.assertIn("這個引導語", next(rule["reason"] for rule in catalog if rule["id"] == "preface-zh"))


if __name__ == "__main__":
    unittest.main()
