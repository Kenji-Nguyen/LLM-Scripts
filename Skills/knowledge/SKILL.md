---
name: knowledge
description: Create, update, validate, and export section-based project knowledge pages. Use for managing project pages, personas, requirements, ideation, and research notes.
---

# /knowledge — General Knowledge Manager

## When to use
- Create a new project knowledge page
- Update any section of an existing project page
- Validate page structure
- Export to JSON

## Workflow

### 1. Identify target
Find the project page at `knowledge/projects/<project_id>/PROJECT_KNOWLEDGE.md`.
If it does not exist, create one from the template at `knowledge/templates/PROJECT_KNOWLEDGE.template.md`.

### 2. Ask intake questions (only what's missing)
1. Which project should be updated?
2. Which section(s) should change?
3. What new source input should be referenced?
4. Should this be EN, DE, or DE+EN wording?
5. Should we export JSON after update?

See `references/intake-questions.md` for the full list.

### 3. Update the page
- Update only the relevant sections.
- Keep language aligned with `language_mode` in frontmatter.
- Use stable IDs for items (PRD-###, FRD-###, SRC-###, IDEA-###).
- Record new sources in `## Sources`.
- Append a timestamped note in `## Notes & Decisions` for significant updates.
- Update `last_updated` in frontmatter.

### 4. Validate
Run: `python3 scripts/knowledge_validate.py --file <project-page>`

### 5. Export (if requested)
Run: `python3 scripts/knowledge_export.py --input <project-page> --output <json-file>`

## Required page structure (9 sections)
See `references/content-model.md` for the canonical section list.

## Quality rules
- Prefer concise sections over long prose.
- Use snippet formats from `knowledge/templates/SECTION_SNIPPETS.md`.
- Keep evidence and decisions connected by source references.
- Respect project `language_mode`.
- If external info is needed, run web search and cite in `## Sources`.

## References
- `references/content-model.md` — required sections and content model
- `references/repository-structure.md` — file layout
- `references/intake-questions.md` — intake question bank
- `knowledge/templates/SECTION_SNIPPETS.md` — section format snippets
- `knowledge/templates/INTERVIEW_INGEST.template.md` — ingest template
