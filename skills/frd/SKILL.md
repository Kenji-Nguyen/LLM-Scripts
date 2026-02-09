---
name: frd
description: Create or update feature requirements (FRD entries) in a project knowledge page. Structures feature-level specs with user stories, acceptance criteria, and dependencies.
---

# /frd — Feature Requirements Creator/Updater

## When to use
- Add a new feature requirement to a project knowledge page
- Update an existing FRD entry with new specs or acceptance criteria
- Break down a PRD into specific feature requirements

## Intake questions (ask only what's missing)
1. Which project? (project_id)
2. What feature is this for? (name)
3. What is the user story?
4. What are the functional requirements?
5. What are the acceptance criteria?
6. What are the dependencies?
7. What evidence supports this? (link to SRC-### entries)

## Workflow

### 1. Find the project page
Open `knowledge/projects/<project_id>/PROJECT_KNOWLEDGE.md`.

### 2. Determine next ID
Check existing FRD entries and use the next sequential ID (FRD-001, FRD-002, etc.).

### 3. Write FRD using snippet format

```markdown
### FRD-###
- Feature name:
- User story:
- Functional requirements:
- Acceptance criteria:
- Dependencies:
- Evidence refs: `SRC-...`
```

### 4. Update the page
- Add or update the FRD entry in `## Feature Requirements`.
- Add new source entries in `## Sources` if not already listed.
- Append a timestamped note in `## Notes & Decisions`.
- Update `last_updated` in frontmatter.

### 5. Validate
Run: `python3 scripts/knowledge_validate.py --file <project-page>`

## Quality rules
- User stories should follow "As a [persona], I want [capability] so that [benefit]" format.
- Acceptance criteria should be testable.
- Dependencies should reference other FRDs or PRDs where applicable.
- Always reference evidence sources.
- Respect project `language_mode`.
