---
name: test
description: Generate user test scripts for usability testing sessions. Outputs standalone markdown for Google Docs with fixed consent/prototype/think-aloud blocks in DE or EN.
---

# /test — User Test Script Generator

## When to use
- Create a user test guide for usability testing
- Generate a task-driven test script with scenarios
- Create a User Test + Interview combined guide

## Important
This is a standalone output skill. It generates a complete script for Google Docs. It does NOT update knowledge pages. For processing test results back into knowledge, use `/ingest`.

## Intake questions (ask first, wait for answers)

1. Which format? (User Test, User Test + Interview, Walkthrough)
2. Language? (DE, EN)
3. Session length? (45, 60 min)
4. How many participant columns in notes tables? (number, for TP1..TPn)
5. Context in 1-2 lines: product, audience, situation
6. Persona snapshot: role + experience level
7. Goals and research questions (bullets)
8. Tasks or use cases (can be long, include subtasks)
9. Options:
   - Include task ease rating per task? (yes/no)
   - Include optional end questions? (none, short set, custom)

If the user cannot provide tasks yet, propose a draft set of 3 tasks based on goals, clearly labeled as "Draft tasks".

## Language rules

- Output language must be either DE or EN.
- If DE: always use "Du" (no "Sie"), unless explicitly asked for "Sie".
- If DE: headings in German. Use umlauts (ä, ö, ü), not ASCII fallbacks.
- If EN: headings in English.

## Output structure (strict order)

1. Title (project name or placeholder)
2. Date (placeholder)
3. Goals / Research Questions
4. Setup
5. Overall findings (filled later)
6. Intro
7. Warm Up
8. Aufgabe 1 / Task 1
9. Aufgabe 2 / Task 2
10. Aufgabe 3 / Task 3
11. Additional tasks if provided
12. Abschluss / Outro

## Fixed blocks (reuse verbatim in Intro)

### DE fixed blocks

**Einverständnis und Aufnahme (fixer Text)**
- Ich würde gerne eine Tonaufnahme machen, nur für interne Auswertung.
- Nichts davon wird veröffentlicht oder an Dritte weitergegeben.
- Bist du einverstanden?

**Prototyp Hinweis (fixer Text)**
- Das ist ein Prototyp. Nicht alles ist klickbar.
- Wenn etwas nicht geht, sag kurz, was du erwartet hättest.

**Think aloud (fixer Text)**
- Bitte denke laut: Sag, was du siehst, was du erwartest und warum du etwas anklickst.

### EN fixed blocks

**Consent and recording (fixed text)**
- I would like to record audio for internal analysis.
- Nothing will be published or shared externally.
- Are you comfortable with that?

**Prototype disclaimer (fixed text)**
- This is a prototype, so not everything is clickable.
- If something does not work, tell me what you expected.

**Think aloud instruction (fixed text)**
- Please think aloud: say what you notice, what you expect, and why you choose an action.

## Task format

Each task must follow:
- Heading: "Aufgabe X: Szenario-Titel" (DE) or "Task X: Scenario title" (EN)
- Scenario (1-2 bullets)
- Instruction (1 bullet)
- Follow ups (max 2 bullets unless user provided more)
- Notes table (one per task)

If the user provides subtasks:
- Keep subtasks as short bullets under the task (do not expand with extra probing).

## Notes tables

Tables must have:
- Column 1: Thema (DE) or Topic (EN)
- Column 2: Frage (DE) or Question (EN)
- Columns 3..n: TP1..TPn

Rules:
- Use bold rows to separate sections (e.g. **Flow**, **Verständlichkeit**).
- Keep questions short.
- Do not pre-fill TP cells.

## Per-task ease rating (if enabled)

Add one row at end of each task table:
- DE: `Wie einfach oder schwierig war diese Aufgabe? (1 sehr schwierig – 5 sehr einfach)`
- EN: `How easy or difficult was this task? (1 very difficult – 5 very easy)`

## Optional end questions

If enabled, add inside Outro/Abschluss:
- Keep to max 3 questions (1-5 scale).
- Render as table if TP > 1, bullets if TP = 1.

Suggested questions:
- DE: Gesamteindruck, Visuelles Design, Verständlichkeit
- EN: Overall impression, Visual design, Clarity

## Quality guardrails

- Do not over-script. The guide is orientation, not a rigid screenplay.
- Avoid leading or suggestive questions.
- If user provides long task lists, preserve them with light cleanup only.
- Use placeholders like [einfügen] or [insert] for unknowns, don't invent details.
- Keep the guide usable in-session.
