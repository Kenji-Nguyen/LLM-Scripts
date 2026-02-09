# Export Strategy

## Supported Outputs (v1)
- Markdown for Google Docs copy/paste.
- JSON export for plugin integrations (for example Figma helpers).

## Export Location
Keep all exports in a central folder, never inside `knowledge/projects/`:
- `exports/manifest.jsonl`
- `exports/<project_id>/manifest.jsonl`
- `exports/<project_id>/json/`
- `exports/<project_id>/persona/`
- `exports/<project_id>/prd/`
- `exports/<project_id>/frd/`
- `exports/<project_id>/interview/`
- `exports/<project_id>/test/`

Retention policy: keep all exports forever.

## Naming Convention
`YYYY-MM-DD_HHMMSS__<project_id>__<type>__<title-slug>__<lang>__rNN.<ext>`

Example:
`2026-02-09_214530__manukai__json__manukai-project-knowledge__EN__r01.json`

## Commands (JSON)
- Validate a project page:
  - `python3 scripts/knowledge_validate.py --file "knowledge/projects/_template/PROJECT_KNOWLEDGE.md"`
- Export page to JSON:
  - `python3 scripts/knowledge_export.py --input "knowledge/projects/manukai/PROJECT_KNOWLEDGE.md"`
  - This auto-generates a unique path in `exports/<project_id>/json/` and appends to both:
    - `exports/manifest.jsonl`
    - `exports/<project_id>/manifest.jsonl`

## Notes
- Keep markdown as source of truth.
- Generated JSON is a derivative artifact and can be regenerated anytime.
