---
name: ingest
description: Process interview or user-test notes into structured knowledge page updates. Extracts observations, insights, requirement signals, and persona signals from raw session notes.
---

# /ingest — Research Note Ingestion

## When to use
- Process raw interview notes into knowledge page updates
- Process user test observations into knowledge page updates
- Extract insights from any research session

## Intake questions (ask only what's missing)
1. Which project? (project_id)
2. Session type? (interview, user-test, workshop, other)
3. Raw notes or transcript to process
4. Participant info (role, experience, context)
5. What language? (follows project `language_mode`)

## Workflow

### 1. Collect session metadata
Fill in the ingest template structure (from `knowledge/templates/INTERVIEW_INGEST.template.md`):
- session_id (auto-generate as `SRC-###`)
- project_id
- type (interview / user-test)
- date
- moderator
- participant profile
- language

### 2. Process raw notes
Extract from the input:

**Observations** (facts only)
- What happened, what was said, what was observed
- No interpretation at this stage

**Candidate insights** (interpretation)
- Patterns, themes, implications
- Mark confidence level if uncertain

**Requirement signals**
- Product-level signals (problems, outcomes, needs) → maps to `## Product Requirements`
- Feature-level signals (specific capabilities, acceptance criteria) → maps to `## Feature Requirements`

**Persona signals**
- Needs, tasks, pains that map to existing or new personas → maps to `## Personas`

**Open questions**
- Things that need follow-up or clarification

### 3. Show proposed updates before writing
Present a summary of what will change:
- Which sections will be updated
- What will be added/modified
- New source entry details

Wait for confirmation before writing.

### 4. Update the project page
Apply updates to `knowledge/projects/<project_id>/PROJECT_KNOWLEDGE.md`:

- Add source entry in `## Sources` with session metadata
- Update `## Personas` with new signals (if any)
- Update `## Product Requirements` with new signals (if any)
- Update `## Feature Requirements` with new signals (if any)
- Add observations and insights to `## Research Notes`
- Append timestamped note in `## Notes & Decisions`
- Update `last_updated` in frontmatter

### 5. Validate
Run: `python3 scripts/knowledge_validate.py --file <project-page>`

## Quality rules
- Separate observations (facts) from insights (interpretation).
- Always create a source entry before referencing it.
- Use existing ID sequences (don't restart numbering).
- Show proposed changes before writing.
- Respect project `language_mode`.
- Keep research notes concise — link to source for full details.

## Ingest template reference
See `knowledge/templates/INTERVIEW_INGEST.template.md` for the full ingest structure:

```
## Session Metadata
- session_id:
- project_id:
- type: interview | user-test
- date:
- moderator:
- participant profile:
- language:

## Goals
## Raw Notes
## Observations (facts only)
## Candidate Insights (interpretation)
## Requirement Signals
## Persona Signals
## Open Questions
## Proposed Updates To Project Page
```
