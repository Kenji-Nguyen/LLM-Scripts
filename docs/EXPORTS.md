# Export Strategy

## Supported Outputs (v1)
- Markdown for Google Docs copy/paste.
- JSON export for plugin integrations (for example Figma helpers).

## Commands
- Validate a project page:
  - `python3 scripts/knowledge_validate.py --file "knowledge/projects/_template/PROJECT_KNOWLEDGE.md"`
- Export page to JSON:
  - `python3 scripts/knowledge_export.py --input "knowledge/projects/_template/PROJECT_KNOWLEDGE.md" --output "exports/template.project.json"`

## Notes
- Keep markdown as source of truth.
- Generated JSON is a derivative artifact and can be regenerated anytime.
