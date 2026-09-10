---
description: Route an academic writing or revision task to the necessary prompts
---

# AI Vibe Writing

Read [SKILL.md](../../SKILL.md) and select the route matching the author's requested deliverable. This workflow is a compatibility entry, not an additional pipeline.

- Use the grammar route for minimal corrections, the Writer for scoped prose edits, and the Coordinator for work spanning planning, drafting, and review.
- Formal reviewer responses go first to [16 · Response Letter](../../.ai_context/prompts/16_response_letter_agent.md). Style learning goes to [1 · Style Extractor](../../.ai_context/prompts/1_style_extractor.md).
- Load only relevant project context. Follow the existing request and authorization; do not require a new Spec approval before an authorized edit.
- Keep task instances and private source material in the author's paper workspace. Return the requested result and concrete pending items.
