---
name: prd
description: Create or update product requirements (PRD entries) in a project knowledge page. Structures problem/outcome-level requirements with evidence references.
---

# /prd — Product Requirements Creator/Updater

## When to use
- Add a new product requirement to a project knowledge page
- Update an existing PRD entry with new evidence or scope changes
- Restructure PRD entries based on new insights

## Intake questions (ask only what's missing)
1. Which project? (project_id)
2. What problem does this address?
3. What is the desired outcome?
4. What is in scope? What is explicitly out of scope (non-goals)?
5. How will success be measured?
6. What evidence supports this? (link to SRC-### entries)

## Workflow

### 1. Find the project page
Open `knowledge/projects/<project_id>/PROJECT_KNOWLEDGE.md`.

### 2. Determine next ID
Check existing PRD entries and use the next sequential ID (PRD-001, PRD-002, etc.).

### 3. Write PRD using snippet format

```markdown
### PRD-###
- Problem:
- Outcome:
- Scope:
- Non-goals:
- Success metrics:
- Evidence refs: `SRC-...`
```

### 4. Update the page
- Add or update the PRD entry in `## Product Requirements`.
- Add new source entries in `## Sources` if not already listed.
- Append a timestamped note in `## Notes & Decisions`.
- Update `last_updated` in frontmatter.

### 5. Validate
Run: `python3 scripts/knowledge_validate.py --file <project-page>`

## Quality rules
- Each PRD should be problem-driven, not solution-driven.
- Non-goals are as important as scope — be explicit about what's excluded.
- Success metrics should be measurable where possible.
- Always reference evidence sources.
- Respect project `language_mode`.
