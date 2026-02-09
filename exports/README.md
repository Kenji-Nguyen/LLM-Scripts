# Exports

Generated artifacts are stored here and retained forever.

## Structure
- `manifest.jsonl` (append-only global index)
- `<project_id>/manifest.jsonl` (append-only per-project index)
- `<project_id>/<type>/...` (artifact files)

## Filename convention
`YYYY-MM-DD_HHMMSS__<project_id>__<type>__<title-slug>__<lang>__rNN.<ext>`

Example:
`2026-02-09_214530__manukai__json__manukai-project-knowledge__EN__r01.json`

## Notes
- Canonical source remains markdown in `knowledge/projects/`.
- Exports are derivative artifacts.
