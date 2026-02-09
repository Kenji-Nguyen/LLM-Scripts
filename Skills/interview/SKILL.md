---
name: interview
description: Generate interview scripts for user research sessions. Outputs standalone markdown for Google Docs with fixed consent/think-aloud blocks in DE or EN.
---

# /interview — Interview Script Generator

## When to use
- Create an interview guide for user research
- Generate a topic-driven interview script
- Create an Interview + User Test combined guide

## Important
This is a standalone output skill. It generates a complete script for Google Docs. It does NOT update knowledge pages. For processing interview results back into knowledge, use `/ingest`.

## Intake questions (ask first, wait for answers)

1. Which format? (Interview, Interview + User Test, Walkthrough)
2. Language? (DE, EN)
3. Session length? (45, 60 min)
4. How many participant columns in notes tables? (number, for TP1..TPn)
5. Context in 1-2 lines: product, audience, situation
6. Persona snapshot: role + experience level
7. Goals and research questions (bullets)
8. Topic areas or conversation themes (e.g. Ablauf, Herausforderungen, Tools)
9. Options:
   - Include optional end questions? (none, short set, custom)

If the user cannot provide topics yet, propose a draft set of 3-5 topics based on goals, clearly labeled as "Draft topics".

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
8. Thema 1 / Topic 1
9. Thema 2 / Topic 2
10. Thema 3 / Topic 3
11. Additional topics if provided
12. Abschluss / Outro

## Fixed blocks (reuse verbatim in Intro)

### DE fixed blocks

**Einverständnis und Aufnahme (fixer Text)**
- Ich würde gerne eine Tonaufnahme machen, nur für interne Auswertung.
- Nichts davon wird veröffentlicht oder an Dritte weitergegeben.
- Bist du einverstanden?

**Think aloud (fixer Text)**
- Bitte denke laut: Sag, was du siehst, was du erwartest und warum du etwas anklickst.

### EN fixed blocks

**Consent and recording (fixed text)**
- I would like to record audio for internal analysis.
- Nothing will be published or shared externally.
- Are you comfortable with that?

**Think aloud instruction (fixed text)**
- Please think aloud: say what you notice, what you expect, and why you choose an action.

## Topic format

Each topic must follow:
- Heading: "Thema X: Titel" (DE) or "Topic X: Title" (EN)
- Key questions (2-4 bullets)
- Follow ups (1-2 bullets)
- Notes table (one per topic)

## Notes tables

Tables must have:
- Column 1: Thema (DE) or Topic (EN)
- Column 2: Frage (DE) or Question (EN)
- Columns 3..n: TP1..TPn

Rules:
- Use bold rows to separate sections (e.g. **Kontext**, **Pain Points**).
- Keep questions short.
- Do not pre-fill TP cells.

## Optional end questions

If enabled, add inside Outro/Abschluss:
- Keep to max 3 questions (1-5 scale).
- Render as table if TP > 1, bullets if TP = 1.

## Quality guardrails

- No leading or suggestive questions.
- Avoid "why" questions — prefer "what made that difficult" or "what was unclear".
- Keep the guide usable in-session, not a documentation artifact.
- Use placeholders like [einfügen] or [insert] for unknowns, don't invent details.
