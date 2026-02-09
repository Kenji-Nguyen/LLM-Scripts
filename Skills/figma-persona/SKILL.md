---
name: figma-persona
description: Generate FigJam Persona plugin markdown from research notes, persona drafts, or sticky dumps. Standalone output — does NOT update knowledge pages.
---

# /figma-persona — FigJam Persona Plugin Output

## When to use
- Convert research notes into FigJam Persona plugin format
- Reformat an existing persona draft for FigJam paste
- Process a sticky dump into structured persona markdown

## Important
This is a standalone output skill. It does NOT update knowledge pages. For updating personas in a project page, use `/persona` instead.

## Intake questions (ask only what's missing)
1. What input do you have? (research notes, persona draft, sticky dump, etc.)
2. What language should the output be? (DE or EN)

## Output contract

Output ONLY the markdown content, nothing else. One persona per output.
Use this exact DSL:

- `Chip: <text>` optional
- `# Persona: <title>` required
- `Emoji: <emoji>` optional
- For each section:
  - `## <SectionTitle>` optional, repeatable, any order
  - `Subtitle: <one line>` optional
  - `- <item text>` for stickies
  - `- (Other) <item text>` for grey stickies in the right lane

No extra formatting, no bold, no links, no nested lists, no numbering.

## How to decide the persona title

Choose a short, client-friendly label that reads like a persona segment, not a job title.
Examples: "Behandlungs-Interessierte", "Informationssuchende Angehoerige", "Zeitkritische Patient\*innen"
If a title is provided in the input, prefer it.

## Chip line rules

If the input hints at a category, use a chip:
- `Chip: Persona - Patient*innen`
- `Chip: Persona - Angehoerige`
- `Chip: Persona - Mitarbeitende`

If unclear, omit the chip.

## Emoji rules

If input includes an emoji, keep it.
Else pick a neutral one that fits the segment. Use exactly one emoji.
If unsure, omit emoji.

## Section rules

Default section set is:
- Needs
- Tasks
- Pains

Sections may be missing. If a section has no items, omit the section entirely.

If the input includes additional buckets (like "Questions", "Risks", "Opportunities"), you MAY add extra sections.
Keep section titles short (1 to 3 words).

Section color order is handled by the plugin, so do not mention colors.

## Subtitle rules

Each section SHOULD have a subtitle.
Use these defaults if input does not provide one:

- Needs: `Subtitle: Welche Beduerfnisse sind zentral?`
- Tasks: `Subtitle: Welche Aufgaben muessen gelingen?`
- Pains: `Subtitle: Was frustriert oder blockiert?`

For EN:
- Needs: `Subtitle: What are the core needs?`
- Tasks: `Subtitle: What tasks must succeed?`
- Pains: `Subtitle: What frustrates or blocks?`

Subtitle is one line only, no punctuation required, no quotes.

## Sticky item rules

Each bullet becomes one sticky.
Write in the language of the input (German if mixed and German dominates).
Keep each item:
- short
- specific
- action or outcome oriented
- max 110 characters if possible

Prefer patterns:
- Needs: "<Need>: <clarifier>" or just "<Need>"
- Tasks: verb-first (e.g. "Termin vereinbaren", "Arztprofil pruefen")
- Pains: concrete friction (e.g. "Findet Infos nicht", "Kontaktwege sind unklar")

Deduping:
- merge duplicates
- if two items differ slightly, keep the clearer one
- cap each section to 10 items if input is huge, pick the most important

## (Other) tagging rules

Use `(Other)` only for items that are:
- out of MVP scope
- nice-to-have
- unclear ownership
- long-term topics
- legal/policy deep dives
- second-order details

If unsure, do NOT tag as Other.

## Quality checklist before output

- Has `# Persona:` line
- At least one `##` section with at least one bullet
- No nested bullets, no numbering
- No extra commentary outside the DSL
- Clean grammar, concise wording
- Consistent language (avoid mixing DE and EN in the same section)

---

## Example

### Input (messy)

Persona draft: "Patientinnen die sich vor OP informieren"
Needs:
- Vertrauen in Kompetenz
- will wissen was passiert
- Datenschutz wichtig

Tasks:
- Arzt suchen
- Termin buchen
- Infos zu Besuch und Zimmer

Pains:
- Website zu voll
- Suche bringt nix

Also: Zweitmeinung Infos, Checklisten, Reminder (maybe later)

### Output

```
Chip: Persona - Patient*innen

# Persona: OP-Informationssuchende

Emoji: 🙋‍♀️

## Needs

Subtitle: Welche Beduerfnisse sind zentral?

- Vertrauen in medizinische Kompetenz
- Klarheit ueber Ablauf und naechste Schritte
- Sicherheit bei sensiblen Daten
- (Other) Detailtiefe zu Datenschutz und Einwilligung

## Tasks

Subtitle: Welche Aufgaben muessen gelingen?

- Aerzt*innen finden und vergleichen
- Termin vereinbaren oder Kontakt aufnehmen
- Infos zu Besuch, Aufenthalt und Zimmer finden
- (Other) Checklisten und Reminder nutzen
- (Other) Infos zur Zweitmeinung finden

## Pains

Subtitle: Was frustriert oder blockiert?

- Zu viele Informationen ueberfordern
- Suche liefert keine passenden Treffer
- Unklare Kontaktwege oder falsche Kontaktdaten
```
