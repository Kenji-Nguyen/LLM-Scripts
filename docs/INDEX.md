# Knowledge Repository Index

## Purpose
This is the shared knowledge system for all clients and products.
Use section-based markdown pages (not many tiny files) and keep every update traceable.

## Global Navigation
- Registry: `docs/REGISTRY.md`
- Governance and update rules: `docs/GOVERNANCE.md`
- Architecture and rollout plan: `docs/ARCHITECTURE_PLAN.md`
- Workflow playbook: `docs/WORKFLOWS.md`
- Export guide: `docs/EXPORTS.md`
- Export root (generated artifacts): `exports/`
- Project page template: `knowledge/templates/PROJECT_KNOWLEDGE.template.md`
- Section snippets (Persona, PRD, FRD, etc.): `knowledge/templates/SECTION_SNIPPETS.md`
- Interview ingest template: `knowledge/templates/INTERVIEW_INGEST.template.md`

## Runtime Integration
- Codex repository rules: `AGENTS.md`
- Claude repository memory/rules: `.claude/CLAUDE.md`
- Skills (shared by both runtimes): `skills/`

## Available Skills
- `skills/knowledge/SKILL.md` — General knowledge manager
- `skills/persona/SKILL.md` — Persona creator/updater
- `skills/figma-persona/SKILL.md` — FigJam Persona plugin output
- `skills/ingest/SKILL.md` — Research note ingestion
- `skills/prd/SKILL.md` — Product requirements creator/updater
- `skills/frd/SKILL.md` — Feature requirements creator/updater
- `skills/interview/SKILL.md` — Interview script generator
- `skills/test/SKILL.md` — User test script generator

## Project Pages
- Manukai: `knowledge/projects/manukai/PROJECT_KNOWLEDGE.md`
- Template: `knowledge/projects/_template/PROJECT_KNOWLEDGE.md`
- Legacy Manukai source (archived): `manukai/MANUKAI_KNOWLEDGE.md`
- Legacy Onooji sources (pending migration): `onooji/`

## Long-Term Data Direction
- Current source of truth: Markdown pages in Git
- Planned optional backend: SQLite/PocketBase mirror fed from markdown export JSON
