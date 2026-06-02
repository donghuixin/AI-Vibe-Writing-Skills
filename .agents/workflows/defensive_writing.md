---
description: Run defensive-writing-agent to red-team reviewer objections before submission
---

# Defensive Writing Workflow

This workflow runs a focused defensive-writing pass for academic paper sections, experiments, limitations, discussion, and rebuttal drafts.

## Steps

1. **Analyze the Target Section**:
   - Identify whether the user is working on Introduction, Related Work, Methodology, Experiments, Discussion, Limitations, Rebuttal, or Abstract.
   - Read `.ai_context/custom_specs.md`, especially Defensive Writing Settings, Evidence Requirements, Review Settings, and Flow Appraisal Settings.
   - Read `.ai_context/document_spec.md` if it exists; otherwise ask the workflow coordinator to derive a temporary contribution boundary from the user input.

2. **Load Defensive Writing Agent**:
   - Read `.ai_context/prompts/14_defensive_writing_agent.md`.
   - Read `.ai_context/style_profile.md` and `.ai_context/error_log.md` to keep the tone candid, restrained, and non-AI-sounding.
   - Read `.ai_context/memory/hard_memory.json`, `.ai_context/memory/soft_memory.json`, and `.ai_context/memory/reference_library.json` for terms, venue norms, and evidence anchors.

3. **Build Reviewer Attack Surface**:
   - Classify risks using the 10 default attack categories: experimental range, sample size, baseline fairness, ablation, generalizability, statistical significance, deployment cost, energy, real-time latency, and novelty.
   - For each risk, output: `Attack -> Validity Threat -> Boundary Reframing -> Evidence Anchor`.

4. **Select Strategy Tier**:
   - For each attack point, try 上策 first: reframe the issue as a scenario-aligned feature or design choice.
   - If 上策 is not supported by the actual scenario, use 中策: analyze the limitation as an engineering boundary with causes, optimization variables, and feasible improvement directions.
   - Use 下策 only when the issue cannot be reframed or bounded in the manuscript; prepare rebuttal fallback, claim narrowing, or additional evidence requests.

5. **Generate Defensive Framing**:
   - Separate core contributions from non-core deployment variables.
   - Produce a Strategy Ladder showing 上策 / 中策 / 下策 options and the selected tier.
   - Produce Suggested Insertions for the target section.
   - Produce Rebuttal Backup for likely reviewer comments.
   - Produce Defensive DoD for final review.

6. **Escalate True Core Risks**:
   - If a risk genuinely weakens the core contribution, do not hide it.
   - Mark severity as `high` and recommend claim narrowing, new evidence, new analysis, or additional experiments.

7. **Report to User**:
   - Present Reviewer Attack Surface, Core Contribution Boundary, Strategy Ladder, Defensive Framing Plan, Suggested Insertions, Rebuttal Backup, and Defensive DoD.
