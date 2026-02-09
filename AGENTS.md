# AGENTS.md

## Scope
Repository for creating, maintaining, and exporting section-based knowledge pages for products and clients.

## Available Skills (in skills/)
- `skills/knowledge/SKILL.md` — General knowledge manager (create, update, validate, export)
- `skills/persona/SKILL.md` — Persona creator/updater (knowledge pages)
- `skills/figma-persona/SKILL.md` — FigJam Persona plugin output
- `skills/ingest/SKILL.md` — Research note ingestion
- `skills/prd/SKILL.md` — Product requirements creator/updater
- `skills/frd/SKILL.md` — Feature requirements creator/updater
- `skills/interview/SKILL.md` — Interview script generator
- `skills/test/SKILL.md` — User test script generator

## Operating Rules
- Keep `knowledge/projects/<project_id>/PROJECT_KNOWLEDGE.md` as canonical source.
- Ask targeted clarifying questions when required context is missing.
- Respect `language_mode` in frontmatter (`EN`, `DE`, `DE+EN`).
- Append a timestamped note in `## Notes & Decisions` for significant updates.
- Use stable machine-friendly IDs for PRD/FRD/Persona/Source items.

## Quality Rules
- Prefer concise sections over long prose.
- Keep evidence and decisions connected by source references.
- If external context is needed or requested, run web search and cite sources.
- Run validation before finalizing major edits:
  - `python3 scripts/knowledge_validate.py --file <project-page>`

## Export Rules
- Markdown is source of truth.
- JSON exports are generated artifacts via:
  - `python3 scripts/knowledge_export.py --input <project-page> --output <json-file>`
