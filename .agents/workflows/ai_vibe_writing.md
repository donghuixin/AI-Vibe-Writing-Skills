---
description: Run the fully automated multi-agent writing loop (AI Vibe Writing Skill)
---

# AI Vibe Writing Loop Workflow

This workflow orchestrates the multi-agent writing loop described in the AI Vibe Writing Skill. It automates the process of creating an outline, drafting content, reviewing, and refining it without requiring manual IDE prompting.

## Pre-requisites
- Ensure the user has an initialized `.ai_context` folder with `style_profile.md` and `custom_specs.md` customized to their needs.
- Ensure any necessary long-term memories or reference libraries are already populated.

## Steps

1. **Analyze the Request**: 
   - Read `.ai_context/custom_specs.md` and `.ai_context/style_profile.md` to understand the target audience, tone, and formatting rules.
   - Read `.ai_context/error_log.md` to understand what NOT to do.

2. **Document Spec Generation (Spec Coding)**:
   - Read `.ai_context/document_spec_template.md`.
   - Create or update `.ai_context/document_spec.md` with the core arguments, negative constraints, and evidence requirements.
   - Ask the user to review and approve the document spec. **Do NOT proceed further until the user approves.**

3. **Outline Management** (Agent Role: Outline Manager):
   - For systems-paper logic tasks, honor `Systems Paper Logic Settings.Mode` and first read `.ai_context/prompts/15_systems_paper_logic_agent.md`. Build `.ai_context/systems_paper_logic.md` from its template, linking claims, challenges, design, evidence, and boundaries. Skip for grammar-only or unrelated tasks.
   - Read `.ai_context/prompts/6_outline_manager_agent.md` and `.ai_context/outline_template.md`.
   - Before writing any full text, generate a structured outline based on the `document_spec.md`. The outline MUST contain `definition_of_done` constraints.
   - Save the approved outline to `.ai_context/memory/hard_memory.json` in `domains.outline.key_values` with key `outline:<outline_id>`, as specified by Outline Manager. Include optional `claim_ids` and `systems_logic_dod` for systems papers.

4. **Content Drafting** (Agent Role: Content Writer):
   - Read `.ai_context/prompts/7_content_writer_agent.md`.
   - Read the generated outline from Step 3 and the relevant claim-evidence rows when systems logic was triggered.
   - Read domain facts from `.ai_context/memory/hard_memory.json` and `.ai_context/memory/soft_memory.json`.
   - Draft the content section by section, strongly adhering to the style profile and avoiding words from the error log.

5. **Defensive Red-Team Pre-Review** (Agent Role: Defensive Writing):
   - Recheck the systems logic worksheet after drafting and pass unresolved C/E/B links to the defensive agent when applicable.
   - Read `.ai_context/prompts/14_defensive_writing_agent.md`.
   - For academic papers, experiments, Discussion, Limitations, or Rebuttal text, identify reviewer attack surfaces before the final review stage.
   - Apply the defensive strategy ladder: 上策 (feature reframing) → 中策 (engineering boundary map) → 下策 (rebuttal fallback).
   - Separate core contributions from non-core deployment variables.
   - Generate strategy ladder, defensive framing, suggested insertions, rebuttal backup, and Defensive DoD.
   - If the defensive agent finds a high-severity issue that truly weakens the core contribution, return to Step 4 and either narrow the claim, add evidence, or request additional experiments.

6. **Self-Review** (Agent Role: Content Review):
   - Read `.ai_context/prompts/8_content_review_agent.md`.
   - Review the generated draft for "AI Tone", grammar issues, and verify it aligns with the error log constraints.
   - Verify the draft also satisfies the Defensive DoD when defensive pre-review was triggered.
   - Audit Systems Logic DoD when triggered. Writing issues return to Step 4; missing experiments return an evidence request, not an invented result. Use `partial` for incomplete scope and `not_applicable` for skipped audits.
   - If any major issues or "AI-sounding" phrases are detected, jump back to Step 4 and revise the draft.
   - Apply the configured `Max Revision Rounds` (default 3) across this loop. Stop on unresolved evidence needs or the round limit and report remaining issues without claiming a pass.

7. **Final Output**:
   - Present the finalized text to the user. Ask if it meets expectations or if any new rules should be added to the `.ai_context/error_log.md`.
