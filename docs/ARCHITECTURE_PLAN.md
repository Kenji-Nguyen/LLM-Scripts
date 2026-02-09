# Architecture Plan

## Goal
Build a simple, long-term knowledge repository for all clients/products where LLMs can create, update, validate, and export structured markdown knowledge.

## Design Principles
- Keep one shared repository.
- Keep one section-based page per project (avoid many tiny files).
- Keep markdown as source of truth.
- Allow overwrite updates by agents, tracked via `## Notes & Decisions`.
- Support English and German per project.

## Canonical Structure
- `docs/INDEX.md`: top-level navigation.
- `docs/REGISTRY.md`: list of projects and primary pages.
- `docs/GOVERNANCE.md`: governance rules and frontmatter spec.
- `docs/ARCHITECTURE_PLAN.md`: this file.
- `docs/WORKFLOWS.md`: workflow playbook.
- `knowledge/projects/<project_id>/PROJECT_KNOWLEDGE.md`: canonical project page.
- `knowledge/templates/`: reusable section templates.
- `scripts/knowledge_validate.py`: structural validation.
- `scripts/knowledge_export.py`: markdown to JSON export.
- `exports/`: centralized generated artifacts (`exports/<project_id>/<type>/...`) with `exports/manifest.jsonl`.

## Content Model (9 Sections)
Each project page contains these sections:
1. Project Snapshot
2. Linked Pages
3. Sources
4. Personas
5. Product Requirements
6. Feature Requirements
7. Ideation
8. Research Notes
9. Notes & Decisions

## Skill Architecture

Skills live in `skills/<name>/SKILL.md` (shared root, one source of truth).

| Runtime | How it finds skills |
|---|---|
| Claude Code | `.claude/skills/<name>/SKILL.md` symlinks pointing to `skills/<name>/SKILL.md` |
| Codex | `AGENTS.md` explicitly lists skill paths under `skills/` |

### Core Skills
- `/knowledge` — General knowledge manager (create, update, validate, export)
- `/persona` — Persona creator/updater (knowledge pages)
- `/figma-persona` — FigJam Persona plugin output (standalone)
- `/ingest` — Research note ingestion

### Additional Skills
- `/prd` — Product requirements creator/updater
- `/frd` — Feature requirements creator/updater
- `/interview` — Interview script generator
- `/test` — User test script generator

## Automation / Hooks Recommendation
Keep it minimal now:
- Use skill + manual validation/export commands first.
- Add one weekly hygiene automation later.

Avoid now:
- many subagents
- complex hook chains
- automatic cross-file rewrites

## Export Policy
- Do not store exports inside `knowledge/projects/`.
- Keep exports in centralized `exports/`.
- Keep all export versions forever.
- Use timestamped unique filenames with project/type/title/lang metadata.

## Rollout Plan

### Phase 1 (Done)
- Simplified template from 12 to 9 sections
- Created all 8 skills
- Migrated Manukai to canonical format
- Standardized folder naming to lowercase

### Phase 2 (Next)
- Migrate Onooji to canonical format
- Start weekly hygiene checks

### Phase 3 (Later)
- Add lightweight SQLite/PocketBase mirror fed from exported JSON
- Keep markdown authoritative; DB remains derivative

## Primary Workflow
Research notes -> ingest skill -> update project page sections -> notes & decisions update -> validate -> optional JSON export.
