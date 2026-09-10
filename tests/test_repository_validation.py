"""Behavioral tests for the standard-library repository validator."""

from __future__ import annotations

import contextlib
import importlib.util
import io
from pathlib import Path
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_repository.py"
SPEC = importlib.util.spec_from_file_location("repository_validator", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)


class RepositoryValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repository"
        self.root.mkdir()
        self.write("SKILL.md", "---\nname: sample-skill\ndescription: A sample skill.\n---\n")

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")
        return path

    def check(self):
        return validator.validate_repository(self.root)

    def messages(self, result):
        return "\n".join(str(issue) for issue in result.issues)

    def assertPass(self):
        result = self.check()
        self.assertTrue(result.ok, self.messages(result))
        return result

    def test_valid_repository_and_quoted_frontmatter(self):
        self.write("SKILL.md", '---\nname: "sample-skill"\ndescription: \'Author\'\'s sample.\'\n---\n[Guide](docs/guide.md)\n')
        self.write("docs/guide.md", '~~~json\n{"enabled": true}\n~~~\n')
        self.write(".ai_context/memory/record.json", '{"items": []}')
        result = self.assertPass()
        self.assertEqual(result.json_files, 1)
        self.assertEqual(result.json_blocks, 1)
        self.assertEqual(result.local_links, 1)

    def test_missing_resource_reports_source_line(self):
        self.write("docs/guide.md", "Introduction.\n\n[Details](missing.md)\n")
        result = self.check()
        self.assertFalse(result.ok)
        self.assertIn("docs/guide.md:3: missing local resource: missing.md", self.messages(result))

    def test_existing_target_outside_repository_is_rejected(self):
        (self.root.parent / "outside.md").write_text("outside", encoding="utf-8")
        self.write("README.md", "[Outside](../outside.md)\n")
        self.assertIn("escapes repository", self.messages(self.check()))

    def test_encoded_traversal_is_rejected(self):
        self.write("README.md", "[Outside](%2e%2e/outside.md)\n")
        self.assertIn("escapes repository", self.messages(self.check()))

    def test_portable_paths_fragment_query_title_and_images(self):
        self.write("docs/guide (draft).md", "guide")
        self.write("docs/guide(draft).md", "guide")
        self.write("assets/plot.png", "synthetic fixture")
        self.write("docs/links.md", (
            '[Draft](<guide (draft).md> "a title")\n'
            '[Encoded](guide%20%28draft%29.md#heading)\n'
            '[Escaped](guide\\(draft\\).md)\n'
            '[Balanced](../assets/plot.png?raw=1#preview)\n'
            '![Image](/assets/plot.png)\n'
        ))
        self.assertEqual(self.assertPass().local_links, 5)

    def test_balanced_parentheses_in_destination(self):
        self.write("asset(copy).md", "resource")
        self.write("README.md", "[Copy](asset(copy).md 'copy')\n")
        self.assertPass()

    def test_external_urls_fragments_and_escaped_examples_are_ignored(self):
        self.write("README.md", (
            "[Remote](https://example.invalid/page)\n"
            "[Mail](mailto:writer@example.invalid)\n"
            "[CDN](//example.invalid/file)\n"
            "[Section](#local-section)\n"
            "\\[Literal](does-not-exist.md)\n"
        ))
        self.assertEqual(self.assertPass().local_links, 0)

    def test_file_uri_and_windows_absolute_path_are_not_external_urls(self):
        self.write("README.md", (
            "[File](file:///outside/resource.md)\n"
            "[Drive](C:/outside/resource.md)\n"
        ))
        result = self.check()
        self.assertEqual(len(result.issues), 2)
        self.assertIn("repository-relative", self.messages(result))

    def test_reference_links_images_collapsed_and_shortcut(self):
        self.write("guide.md", "guide")
        self.write("README.md", (
            "[Read][guide]\n![Icon][guide]\n[guide][]\n[guide]\n"
            '[guide]: guide.md "Guide"\n'
            "[unused]: missing-but-unused.md\n"
        ))
        self.assertPass()
        self.write("README.md", "[Read][lost]\n[lost]: missing.md\n")
        self.assertIn("missing local resource", self.messages(self.check()))

    def test_code_examples_are_not_resource_links(self):
        self.write("README.md", (
            "`[Inline](missing.md)` and ``[Another](also-missing.md)``.\n"
            "    [Indented](missing.md)\n"
            "\t[Tab code](missing.md)\n"
            "````markdown\n[Example](missing.md)\n```\n````\n"
            "~~~text\n[Reference][missing]\n[missing]: absent.md\n~~~\n"
            "<!-- [Comment](absent.md)\n```json\nnot json\n-->\n"
        ))
        self.assertEqual(self.assertPass().local_links, 0)

    def test_literal_comment_inside_json_code_is_not_stripped(self):
        self.write("README.md", '```json\n{"text": "<!-- unfinished comment"}\n```\n')
        self.assertPass()

    def test_comment_inside_inline_code_does_not_hide_real_link(self):
        self.write("README.md", "`<!--` is literal.\n[Missing](missing.md)\n")
        self.assertIn("missing local resource", self.messages(self.check()))

    def test_unclosed_fence_and_wrong_closing_marker(self):
        for text in ("Before.\n```text\nunfinished\n", "~~~json\n{}\n```\n"):
            with self.subTest(text=text):
                self.write("README.md", text)
                self.assertIn("unclosed Markdown code fence", self.messages(self.check()))

    def test_shorter_fence_does_not_close_longer_block(self):
        self.write("README.md", "````text\nexample\n```\n")
        self.assertIn("unclosed Markdown code fence", self.messages(self.check()))

    def test_bad_json_file_and_code_block_are_both_reported(self):
        self.write("config.json", '{"enabled": tru}')
        self.write("README.md", "Before.\n```json\n{\n  bad\n}\n```\n")
        result = self.check()
        self.assertEqual(len(result.issues), 2)
        self.assertIn("config.json:1: invalid JSON", self.messages(result))
        self.assertIn("README.md:4: invalid JSON", self.messages(result))

    def test_non_json_numeric_constant_is_rejected(self):
        self.write("config.json", '{"value": NaN}')
        self.assertIn("non-JSON numeric constant", self.messages(self.check()))

    def test_missing_skill_frontmatter_and_required_fields(self):
        cases = (
            ("# Skill\n", "missing opening YAML"),
            ("---\nname: example\n", "unclosed YAML"),
            ("---\nname: example\n---\n", "missing required frontmatter field: description"),
            ("---\ndescription: Example\n---\n", "missing required frontmatter field: name"),
            ("---\nname: example\ndescription:\n---\n", "nonempty single-line string"),
            ("---\nname: example\ndescription: >\n  multiline\n---\n", "supported YAML subset"),
            ("---\nname: example\nname: duplicate\ndescription: Example\n---\n", "duplicate frontmatter"),
        )
        for text, expected in cases:
            with self.subTest(expected=expected):
                self.write("SKILL.md", text)
                self.assertIn(expected, self.messages(self.check()))

    def test_missing_skill_and_invalid_root(self):
        (self.root / "SKILL.md").unlink()
        self.assertIn("missing root SKILL.md", self.messages(self.check()))
        result = validator.validate_repository(self.root / "nonexistent")
        self.assertIn("not a directory", self.messages(result))

    def test_dependencies_and_hidden_caches_are_skipped_but_resources_checked(self):
        for folder in (".git", ".venv", ".hidden-model", "models", "model", "cache",
                       "node_modules", "tools/venv", "tools/__pycache__",
                       "mineru_venv", "mineru_models", "output"):
            self.write(f"{folder}/invalid.json", "not JSON")
            self.write(f"{folder}/bad.md", "```unclosed")
        self.write(".ai_context/actual.json", "{}")
        self.write(".agents/guide.md", "guide")
        result = self.assertPass()
        self.assertEqual(result.json_files, 1)
        self.write(".ai_context/actual.json", "not JSON")
        self.assertIn(".ai_context/actual.json", self.messages(self.check()))

    def test_invalid_utf8_is_reported(self):
        path = self.root / "bad.md"
        path.write_bytes(b"\xff\xfeinvalid")
        self.assertIn("cannot read UTF-8 resource", self.messages(self.check()))

    def test_symlink_cannot_make_outside_resource_look_local(self):
        outside = self.root.parent / "outside.md"
        outside.write_text("outside", encoding="utf-8")
        try:
            (self.root / "linked.md").symlink_to(outside)
        except (OSError, NotImplementedError):
            self.skipTest("symlink creation is unavailable on this platform")
        self.write("README.md", "[Outside](linked.md)\n")
        result = self.check()
        self.assertIn("escapes repository", self.messages(result))

    def test_cli_accepts_root_and_returns_failure_for_errors(self):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(validator.main([str(self.root)]), 0)
            self.assertEqual(validator.main(["--root", str(self.root)]), 0)
            self.write("README.md", "[Missing](missing.md)\n")
            self.assertEqual(validator.main([str(self.root)]), 1)


if __name__ == "__main__":
    unittest.main()
