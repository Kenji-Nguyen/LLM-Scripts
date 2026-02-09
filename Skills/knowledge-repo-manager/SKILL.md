---
name: knowledge-repo-manager
description: "SUPERSEDED — Use skills/knowledge/SKILL.md instead. Original knowledge repo manager."
---

> **Superseded by**: `skills/knowledge/SKILL.md`
> This skill is kept for reference only.

# Knowledge Repo Manager

## Workflow
1. Identify target project page in `Knowledge/projects/<project_id>/PROJECT_KNOWLEDGE.md`.
2. If context is missing, ask targeted intake questions before drafting.
3. Update only relevant sections and keep language aligned with `language_mode`.
4. Record references in `## Sources` for interview/test/web inputs.
5. Append one line in `## Change Log`.
6. Run validation using `scripts/knowledge_validate.py`.
7. Export JSON when requested using `scripts/knowledge_export.py`.

## Required Structure
Use `references/repository-structure.md` and `references/content-model.md` as the canonical model.

## Update Quality Rules
- Keep evidence, assumptions, and decisions explicit and linked.
- Use stable ids for PRD, FRD, persona, assumptions, and decisions.
- Prefer section updates over creating many new files.
- Preserve history; do not remove prior decisions without marking superseded state.

## Resources
### references/
- `references/repository-structure.md`
- `references/content-model.md`
- `references/intake-questions.md`

### scripts/
- `scripts/export_json.sh`
- `scripts/validate_page.sh`
