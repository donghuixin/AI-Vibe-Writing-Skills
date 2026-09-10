"""Compatibility CLI for the local style linter.

The old model-based LocalPaperDetector API and authorship scores were removed.
Use style_lint.lint_text/lint_file for programmatic editing prompts.
"""
if __package__:
    from .style_lint import main
else:
    from style_lint import main


if __name__ == "__main__":
    raise SystemExit(main())
