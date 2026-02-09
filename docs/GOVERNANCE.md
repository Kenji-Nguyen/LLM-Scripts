# Governance

## Core Model
- Keep one section-based `PROJECT_KNOWLEDGE.md` per project as the canonical page.
- Allow agent overwrite updates.
- Append timestamped notes in `## Notes & Decisions` for significant updates.

## Required Frontmatter
- `doc_id`: stable machine-friendly id (example: `proj-manukai-main`)
- `project_id`: project key from registry
- `title`: page title
- `language_mode`: `EN`, `DE`, or `DE+EN`
- `status`: lifecycle status
- `last_updated`: ISO date
- `owners`: names/roles

## Required Sections (9)
1. Project Snapshot
2. Linked Pages
3. Sources
4. Personas
5. Product Requirements
6. Feature Requirements
7. Ideation
8. Research Notes
9. Notes & Decisions

## Evidence and Decision Tracking
Evidence, assumptions, and decisions are tracked in two places:
- **Inline with requirements**: PRD/FRD entries include `Evidence refs: SRC-###` links
- **Notes & Decisions**: Free-form timestamped log for decisions, assumptions, and general notes

This replaces the previous formal E/A/D table system. Keep it simple — one-liner entries with dates.

## Lifecycle Status (Document)
- `draft`: early working state.
- `review`: ready for stakeholder review.
- `approved`: agreed baseline.
- `archived`: inactive, retained for history.

## Quality Rules For Agent Updates
- Ask targeted intake questions before generating major sections when context is missing.
- Respect project `language_mode`.
- If external info is used, run web search and cite sources in `## Sources`.
- Keep each section concise and structured for downstream export.
- Use stable IDs (SRC-###, PRD-###, FRD-###, IDEA-###) for traceable items.
