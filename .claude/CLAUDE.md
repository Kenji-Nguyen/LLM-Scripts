# CLAUDE.md

## Available Skills
- `/knowledge` — Create, update, validate, and export project knowledge pages
- `/persona` — Create or update personas in knowledge pages
- `/figma-persona` — Generate FigJam Persona plugin markdown
- `/ingest` — Process interview/test notes into knowledge page updates
- `/prd` — Create or update product requirements
- `/frd` — Create or update feature requirements
- `/interview` — Generate interview scripts for user research
- `/test` — Generate user test scripts for usability testing

## Knowledge Repository Behavior
- Maintain section-based project pages under `knowledge/projects/`.
- Ask focused intake questions before writing major new sections.
- Respect `language_mode` in each document frontmatter.
- Append timestamped notes in `## Notes & Decisions` for significant updates.
- Keep evidence and decisions connected by source references.

## Validation + Export
- Validate structure with `python3 scripts/knowledge_validate.py --file <project-page>`.
- Export JSON with `python3 scripts/knowledge_export.py --input <project-page>`.
- Keep exports in `exports/` (centralized) and retain all versions.

## Research Enrichment
- Use web search when external facts are needed.
- Add sources in the `## Sources` section of the project page.
