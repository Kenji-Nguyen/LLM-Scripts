# Workflow Playbook

## Primary End-to-End Flow
1. Ingest interview or user-test notes (use `/ingest` skill).
2. Update project `Research Notes` section.
3. Update `Personas` section if new behavioral evidence appears.
4. Update `Product Requirements` or `Feature Requirements` based on validated findings.
5. Append timestamped note in `## Notes & Decisions`.
6. Validate with `python3 scripts/knowledge_validate.py`.
7. Export JSON as needed with `python3 scripts/knowledge_export.py --input <project-page>` (writes to `exports/` and logs `exports/manifest.jsonl`).

## Update Modes
- `quick_update`: patch one section + notes & decisions entry.
- `research_update`: ingest notes and refresh personas/requirements.
- `release_update`: review whole page and set status to `review` or `approved`.

## Weekly Knowledge Hygiene (Suggested)
- Check open questions older than 30 days in Research Notes.
- Check requirements missing evidence refs.
- Check missing source links for externally enriched content.
- Check language consistency against `language_mode`.
