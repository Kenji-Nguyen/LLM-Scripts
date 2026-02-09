---
name: persona
description: Create or update personas in a project knowledge page. Extracts persona data from research inputs and writes structured persona entries.
---

# /persona — Persona Creator/Updater (Knowledge Pages)

## When to use
- Add a new persona to a project knowledge page
- Update an existing persona with new research evidence
- Restructure personas based on new insights

## Intake questions (ask only what's missing)
1. Which project? (project_id)
2. What research input drives this? (interview notes, test observations, sticky dump, etc.)
3. Is this a new persona or update to existing?
4. What language? (follows project `language_mode`)

## Workflow

### 1. Find the project page
Open `knowledge/projects/<project_id>/PROJECT_KNOWLEDGE.md`.

### 2. Analyze input
Extract from the research input:
- Segment / role description
- Core job to be done
- Behaviors
- Needs
- Tasks (if available)
- Pains
- Evidence references (link to `SRC-###` entries)

### 3. Write persona using snippet format
Use this format (from `knowledge/templates/SECTION_SNIPPETS.md`):

```markdown
### Persona <name>
- Segment:
- Core job to be done:
- Behaviors:
- Needs:
- Pains:
- Evidence refs: `SRC-...`
```

### 4. Update the page
- Add or update the persona entry in `## Personas`.
- Add new source entries in `## Sources` if not already listed.
- Append a timestamped note in `## Notes & Decisions`.
- Update `last_updated` in frontmatter.

### 5. Validate
Run: `python3 scripts/knowledge_validate.py --file <project-page>`

## Quality rules
- Keep persona entries concise and evidence-backed.
- Use bullet format, not prose paragraphs.
- Deduplicate needs/pains across personas.
- Respect project `language_mode`.
- Always reference evidence sources with `SRC-###` IDs.

## Important
This skill updates the knowledge page. For FigJam Persona plugin output, use `/figma-persona` instead.
