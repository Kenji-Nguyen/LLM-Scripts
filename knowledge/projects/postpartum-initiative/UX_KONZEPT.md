# UX Konzept — Postpartum Initiative

**Leitplanken fuer Produktlogik und Nutzerfuehrung als Grundlage fuer Design und Engineering**

---

## 1. Praezisierung von UX-Flows mittels erarbeiteter User Journeys

### 1.1 Uebergreifende Designprinzipien

| Prinzip | Bedeutung fuer UX |
|---|---|
| Niederschwelligkeit zuerst | Jeder Einstieg muss ohne Account, ohne Erklaerung, ohne Wartezeit funktionieren. Erster Wert in <60 Sekunden. |
| Kein Informationsoverload | Frauen sind erschoepft, ueberfordert (~60%), und haben wenig kognitive Kapazitaet. Jeder Screen zeigt genau eine Entscheidung. |
| Ton: Hebamme, nicht Klinik | Die Hebamme ist der Vertrauensanker (92% im Wochenbett). UX-Sprache imitiert diesen Ton: warm, einordnend, validierend — "Deine Gefuehle sind in Ordnung." |
| Scham reduzieren | ~29% haben Themen, ueber die sie mit niemandem sprechen konnten. UI normalisiert aktiv: "Viele Muetter erleben das." |
| Orientierung vor Aktion | 61% wuenschen sich zuerst Einordnung ("Was ist normal?"), nicht sofort einen Termin. |
| Kontinuitaet, nicht Einmalkontakt | Die Luecke ist nicht ein fehlendes Angebot, sondern fehlende Begleitung ueber Monate. UX baut auf Wiederkommlogik. |

### 1.2 User Journey: Erstnutzung bis laufende Begleitung

```
Phase 1               Phase 2                Phase 3               Phase 4
ANKOMMEN               VERSTEHEN              HANDELN               DRANBLEIBEN
(Tag 1)                (Tag 1–3)              (Woche 1–2)           (Monat 1–12)
                                                                    
Einstieg               Check-in               Empfehlung            Begleitung
"Ich fuehle mich       "Was beschaeftigt       "Das passt zu         "Wie geht es
ueberfordert"          dich gerade?"           deiner Situation"     dir diese Woche?"
                                                                    
┌─────────────┐       ┌─────────────┐        ┌─────────────┐       ┌─────────────┐
│ Landing /   │──────▶│ Strukturier-│───────▶│ Ergebnis:   │──────▶│ Regelmaess- │
│ Einstiegs-  │       │ ter Check-in│        │ Einordnung  │       │ ige Re-     │
│ frage       │       │ (3–5 Min)   │        │ + Optionen  │       │ Check-ins   │
└─────────────┘       └─────────────┘        └─────────────┘       └─────────────┘
                                                │                       │
                                                ▼                       ▼
                                          ┌───────────┐          ┌───────────┐
                                          │ Selbst-   │          │ Alltags-  │
                                          │ hilfe /   │          │ uebungen  │
                                          │ Fach-     │          │ + Impulse │
                                          │ person /  │          │           │
                                          │ Peer      │          │           │
                                          └───────────┘          └───────────┘
```

### 1.3 Detaillierte Journey-Phasen

#### Phase 1 — ANKOMMEN

**Trigger:** Frau sucht online nach Symptom, erhaelt Empfehlung von Hebamme/MVB, sieht Social-Media-Beitrag, oder scannt QR-Code bei Gynaekologin/Kinderarzt.

**UX-Flow:**
1. Landing Screen mit einer einzigen Frage: "Wie geht es dir gerade?" — Freitext oder vordefinierte Auswahl (z.B. "Erschoepft", "Unsicher", "Ueberfordert", "Einsam", "Koerperlich belastet", "Eigentlich ganz gut")
2. Keine Registrierung noetig fuer erste Einordnung
3. Sofortige Rueckmeldung: Validierung + Einladung zum Check-in

**Designregel:** Maximal 1 Tap/Klick bis zum ersten Wert. Kein Onboarding-Carousel, kein Feature-Ueberblick.

#### Phase 2 — VERSTEHEN (Strukturierter Check-in)

**UX-Flow:**
1. Kurzer Fragebogen (3–5 Minuten, max. 10–12 Fragen)
2. Themenabdeckung entlang validierter Cluster:
   - Koerperliche Erholung (Beckenboden, Schmerzen, Stillen)
   - Emotionale Belastung / Stimmung
   - Schlaf & Erschoepfung
   - Unsicherheit ("Was ist normal?")
   - Soziale Unterstuetzung & Isolation
   - Vereinbarkeit / Rueckkehr zur Arbeit (ab Monat 3+)
3. Eingabe: Slider, Einfachauswahl, ggf. Freitext — keine klinischen Skalen, sondern alltagsnahe Sprache
4. Kontext-Erfassung: Geburtsdatum Kind, Erst-/Mehrgebaerende, aktuelle Woche postpartum

**Designregel:** Jede Frage passt auf einen Screen. Progress-Anzeige zeigt Fortschritt. "Ueberspringen" ist immer moeglich.

#### Phase 3 — HANDELN (Einordnung + Empfehlung)

**UX-Flow:**
1. Ergebnisscreen: Zusammenfassung in 2–3 Saetzen, nicht als Diagnose, sondern als Einordnung
   - z.B. "Du beschreibst eine starke Erschoepfung und Unsicherheit beim Stillen. Das erleben viele Muetter in deiner Phase — und es gibt gute Unterstuetzung dafuer."
2. Handlungsoptionen, gestuft nach Intensitaet:
   - **Selbsthilfe:** Kuratierter Inhalt (Artikel, Video, Uebung) — sofort verfuegbar
   - **Peer-Austausch:** Verbindung zu anderen Muettern (Community / moderierte Gruppe)
   - **Fachperson:** Matching zu passender Fachberatung (Schlaf, Stillen, Beckenboden, Psyche etc.)
   - **Dringend:** Klarer Eskalationspfad (Notfallnummern, Krisenberatung, Medgate-Anbindung)
3. Jede Option zeigt: Was es ist, wie es funktioniert, was es kostet, wie schnell es verfuegbar ist

**Designregel:** Nie mehr als 3 Optionen gleichzeitig. Primaerempfehlung visuell hervorgehoben. Keine Sackgassen — jeder Screen hat einen naechsten Schritt.

#### Phase 4 — DRANBLEIBEN (Kontinuitaet)

**UX-Flow:**
1. Wiederholte Check-ins (konfigurierbar: woechentlich bis taeglich, >50% wuenschen mind. woechentlich)
2. Push-Reminder: Sanft, nicht klinisch — "Wie war deine Woche? Nimm dir 2 Minuten."
3. Verlaufssicht: Einfache Timeline zeigt Entwicklung ueber Wochen/Monate
4. Alltagsuebungen und Impulse (siehe Abschnitt 4)
5. Anpassung der Empfehlungen basierend auf Verlauf

**Designregel:** Reminder sind opt-in und anpassbar. Kein Guilt-Tripping bei verpassten Check-ins. Ton: "Schoen, dass du wieder da bist."

---

## 2. Konzeption fuer die Risiko- & Screening-Engine

### 2.1 Zweck und Abgrenzung

Die Screening-Engine ist **kein diagnostisches Instrument** und ersetzt keine aerztliche Beurteilung. Sie dient als:
- **Strukturierungshilfe** fuer die Nutzerin ("Was beschaeftigt mich eigentlich?")
- **Triage-Unterstuetzung** fuer das System ("Welche Intensitaet der Unterstuetzung ist angemessen?")
- **Eskalationslogik** fuer Risikofaelle ("Braucht diese Frau sofortige Fachunterstuetzung?")

### 2.2 Risikostufen-Modell

```
Stufe 0 — ORIENTIERUNG (gruen)
├── Nutzerin hat Fragen, fuehlt sich aber grundsaetzlich stabil
├── Angebot: Kuratierte Inhalte, Alltagsuebungen, Community
└── Kein Handlungsdruck, Wiedervorlage beim naechsten Check-in

Stufe 1 — ERHOEHTER BEDARF (gelb)
├── Belastung in mehreren Bereichen oder anhaltende Einzelbelastung
├── Angebot: Gezielte Fachberatung (Schlaf, Stillen, Beckenboden, Psyche)
├── Aktives Matching + Follow-up ob Kontakt zustande kam
└── Re-Check-in nach 1–2 Wochen

Stufe 2 — HOHER BEDARF (orange)
├── Deutliche psychische Belastung, Isolation, oder koerperliche Beschwerden
├── Angebot: Priorisiertes Matching zu Fachperson + Case Management light
├── Systemseitig: Flag fuer intensiveres Follow-up
└── Re-Check-in nach 3–7 Tagen

Stufe 3 — KRISE / DRINGEND (rot)
├── Hinweise auf akute Krise (Suizidalitaet, schwere PPD, Kindsgefaehrdung)
├── Sofortige Anzeige: Notfallnummern, Krisenberatung, Dargebotene Hand (143)
├── Optional: Direkte Weiterleitung an Medgate (24/7)
├── KEIN Warten auf naechsten Check-in
└── System informiert ggf. hinterlegte Vertrauensperson (nur mit Consent)
```

### 2.3 Screening-Logik: Eingabe → Bewertung → Ausgabe

**Eingabe-Dimensionen (pro Check-in):**

| Dimension | Erfassung | Gewicht |
|---|---|---|
| Emotionale Belastung / Stimmung | 5-Stufen-Skala + Freitext | Hoch |
| Schlaf & Erschoepfung | Quantitativ (Stunden) + qualitativ | Mittel |
| Koerperliche Beschwerden | Ja/Nein + Auswahl (Beckenboden, Schmerzen, Stillen) | Mittel |
| Soziale Isolation | 5-Stufen-Skala | Hoch |
| Ueberforderung im Alltag | 5-Stufen-Skala | Hoch |
| Beziehung / Partnerschaft | Optional, 5-Stufen-Skala | Mittel |
| "Gibt es etwas, das du niemandem sagen kannst?" | Ja/Nein + Freitext (optional) | Hoch (Trigger fuer Stufe 2+) |

**Bewertungslogik:**
- Schwellenwerte pro Dimension (konfigurierbar, nicht hartcodiert)
- Kombinations-Regeln: Einzelne moderate Belastung = Stufe 0–1; mehrere moderate = Stufe 1–2; einzelne hohe = Stufe 2
- Rote Trigger-Woerter/Antworten (z.B. bei Frage zu Suizidalitaet, Gewalt) → sofortige Eskalation zu Stufe 3, unabhaengig vom Gesamtscore
- Verlaufslogik: Verschlechterung gegenueber letztem Check-in erhoeht Stufe; stabiler Verlauf kann Stufe senken

**Ausgabe:**
- Risikostufe (intern, wird der Nutzerin NICHT als Zahl/Label angezeigt)
- Einordnungstext (empathisch, normalisierend)
- Empfohlene Handlungsoptionen (gestuft, siehe Phase 3)
- Follow-up-Intervall

### 2.4 Regulatorische Leitplanken

- Die Engine gibt **keine medizinischen Diagnosen** und **keine Therapieempfehlungen**
- Bei Stufe 3 wird **immer** ein menschlicher Kontakt angeboten, nie nur ein Chatbot
- Alle Screening-Antworten sind **verschluesselt** und werden **nicht an Dritte weitergegeben**
- Nutzerin kann jederzeit alle Daten loeschen
- Disclaimer bei jedem Check-in: "Dies ersetzt keine aerztliche Beratung. Im Notfall: 144 (Sanitaet) / 143 (Dargebotene Hand)."

---

## 3. Synthese von User Journeys in User Flows

### 3.1 Uebersicht der Kern-Flows

```
                    ┌──────────────────────────────────────────┐
                    │              EINSTIEG                     │
                    │    Landing / QR / Empfehlung / Social     │
                    └──────────────┬───────────────────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────────────────┐
                    │         ERSTER CHECK-IN                   │
                    │    Kurzfragebogen (3–5 Min)               │
                    │    → Risikostufe wird ermittelt           │
                    └──────────────┬───────────────────────────┘
                                   │
                    ┌──────────────┼───────────────┐
                    ▼              ▼               ▼
             ┌────────────┐ ┌────────────┐  ┌────────────┐
             │ Stufe 0–1  │ │ Stufe 2    │  │ Stufe 3    │
             │ Orientie-  │ │ Fach-      │  │ Krisen-    │
             │ rung       │ │ anbindung  │  │ pfad       │
             └─────┬──────┘ └─────┬──────┘  └─────┬──────┘
                   │              │               │
                   ▼              ▼               ▼
             ┌────────────┐ ┌────────────┐  ┌────────────┐
             │ Inhalte    │ │ Matching   │  │ Sofort-    │
             │ Uebungen   │ │ Fachperson │  │ kontakt    │
             │ Community  │ │ + Follow-  │  │ Notfall-   │
             │            │ │ up         │  │ nummern    │
             └─────┬──────┘ └─────┬──────┘  └────────────┘
                   │              │
                   └──────┬───────┘
                          ▼
             ┌──────────────────────────────┐
             │     LAUFENDE BEGLEITUNG       │
             │  Re-Check-ins + Uebungen +    │
             │  Verlaufssicht + Anpassung     │
             └──────────────────────────────┘
```

### 3.2 Flow A — Erstnutzung ohne Account

```
1. Landing Screen
   └── "Wie geht es dir gerade?" (Einzel-Tap-Auswahl)
       └── Sofortige Validierung + Einladung zum Check-in
           └── Check-in (ohne Registrierung)
               └── Ergebnis + Empfehlungen
                   └── Optional: Account erstellen fuer Verlauf
```

**Rationale:** 46% suchen ueber Google; 6% nutzen gar kein Angebot. Der Einstieg muss maximal barrierefrei sein. Account erst nach erstem Wert.

### 3.3 Flow B — Wiederkehrender Check-in

```
1. Push-Notification / App-Oeffnung
   └── "Wie war deine Woche?" (Kurzversion: 3–5 Fragen)
       └── Vergleich mit letztem Check-in
           ├── Stabil/Besser → Positive Rueckmeldung + naechste Uebung
           ├── Verschlechterung → Angepasste Empfehlung + kuerzeres Intervall
           └── Neue Themen → Erweiterte Fragen + neues Matching
```

### 3.4 Flow C — Akutes Thema ("Ich brauche jetzt Hilfe")

```
1. "Ich brauche jetzt Hilfe"-Button (immer sichtbar)
   └── Themenauswahl: Psyche / Koerper / Stillen / Schlaf / Beziehung / Sonstiges
       └── 2–3 Einordnungsfragen
           ├── Kein Notfall → Passendes Angebot + Terminvermittlung
           └── Notfall → Sofortige Eskalation (Notfallnummern, Medgate 24/7)
```

### 3.5 Flow D — Fachperson-Matching

```
1. Empfehlung aus Check-in oder Akut-Flow
   └── Anzeige: Fachrichtung, Verfuegbarkeit, Region, Format (vor Ort/online), Kosten
       └── Auswahl oder "Andere zeigen"
           └── Kontaktaufnahme (Formular / Telefon / Chat)
               └── Follow-up nach 5–7 Tagen: "Hast du den Kontakt aufnehmen koennen?"
                   ├── Ja → Rueckmeldung zur Erfahrung
                   └── Nein → Barrieren erfragen + Alternative anbieten
```

### 3.6 Flow E — Partner-Modus (35% wuenschen dies)

```
1. Nutzerin laedt Partner:in ein
   └── Partner:in erhaelt eigenen Zugang (Read-only oder eigenen Mini-Check-in)
       └── Gemeinsame Themen-Uebersicht
           └── Empfehlungen fuer gemeinsame Schritte (z.B. Paarberatung, Rollenverteilung)
```

---

## 4. Konzept fuer Einbettung der Alltagsuebungen in die Nutzung

### 4.1 Warum Alltagsuebungen?

Die Beduerfnispyramide aus dem Workshop (`SRC-001`) zeigt: Muetter brauchen nicht nur Informationen und Fachanbindung, sondern auch konkrete, alltagstaugliche Hilfe. Die oberen Pyramidenstufen (Reflexion & Selbstwahrnehmung: taegliche Impulse 12%, Tracking 8%) und die mittlere Stufe (holistische Begleitung: mentale Gesundheit 46%, Beckenboden 45%, Stillen 42%, Schlaf 41%) zeigen den Bedarf.

Alltagsuebungen sind das Bindeglied zwischen passivem Informationskonsum und aktiver Fachanbindung — sie geben der Nutzerin **Selbstwirksamkeit** in einer Phase, die von Kontrollverlust gepraegt ist.

### 4.2 Uebungskategorien (abgeleitet aus Themenclustern)

| Kategorie | Beispiele | Format | Frequenz |
|---|---|---|---|
| Beckenboden / Rueckbildung | 5-Min-Uebung, Atemtechniken, Haltungskorrektur | Video + Timer | Taeglich |
| Mentale Gesundheit | Mood-Tracking, Achtsamkeitsuebung, Dankbarkeitsimpuls, Atemtechnik | Text + Audio | Taeglich |
| Schlaf | Schlafhygiene-Tipps, Kurzentspannung fuer Ruhephasen, Schlafprotokoll | Text + Audio | Bei Bedarf |
| Stillen / Ernaehrung | Stillpositionen, Ernaehrungstipps, Entwoehnungsphasen | Bild + Text | Situativ |
| Beziehung / Partnerschaft | Gespraechsimpulse, Rollenreflexion, Appreciation-Uebung | Text-Karte | Woechentlich |
| Vereinbarkeit / Alltag | Tagesstruktur-Vorlage, Prioritaetsmatrix, Energiemanagement | Tool / Checklist | Woechentlich |

### 4.3 Einbettungslogik im UX-Flow

**Prinzip: Uebungen folgen dem Check-in, nie umgekehrt.**

```
Check-in
  │
  ▼
Einordnung + Empfehlung
  │
  ├── Fachperson-Matching (falls noetig)
  │
  └── Passende Alltagsuebung (immer)
        │
        ├── Sofort ausfuehrbar (direkt im Screen, kein externer Link)
        │
        ├── Kurzformat: 2–5 Minuten (Muetter haben keine 20 Min)
        │
        ├── Ton: Ermutigend, nicht fordernd
        │   "Eine kleine Uebung fuer heute — probier sie aus, wenn du magst."
        │
        └── Abschluss: Kurz-Feedback (1 Tap: "Hat gut getan" / "Passt gerade nicht")
              │
              └── Informiert naechste Uebungsauswahl
```

### 4.4 Personalisierungslogik

- **Check-in-basiert:** Uebungen werden basierend auf der aktuellen Belastungslage ausgewaehlt, nicht statisch nach Woche postpartum
- **Verlaufsbasiert:** Wenn Schlafbelastung ueber 3 Check-ins hoch bleibt, werden Schlaf-Uebungen priorisiert
- **Feedback-basiert:** "Hat gut getan" → aehnliche Uebungen; "Passt gerade nicht" → Alternative
- **Phasenbasiert:** Fruehe Monate (Beckenboden, Stillen, Schlaf) vs. spaetere Monate (Vereinbarkeit, Partnerschaft, Identitaet)

### 4.5 Integration mit anderen Produktebenen

| Wenn... | Dann... |
|---|---|
| Uebung wird regelmaessig genutzt | Positive Verstaerkung in der Verlaufssicht |
| Uebung wird nie abgeschlossen | Kein Guilt-Tripping; alternatives Format anbieten |
| Uebungen reichen nicht (Belastung bleibt hoch) | Sanfter Hinweis: "Moechtest du mit einer Fachperson sprechen?" |
| Nutzerin ist in Stufe 2–3 | Uebungen ergaenzen, ersetzen aber nicht die Fachanbindung |
| Partner-Modus aktiv | Gemeinsame Uebungen vorschlagen (z.B. Gespraechsimpulse) |

### 4.6 Content-Anforderungen

- Alle Uebungen muessen von Fachpersonen geprueft/erstellt sein (Physiotherapie, Psychologie, Schlafberatung etc.)
- Klare Kennzeichnung: "Erstellt mit [Fachperson/Fachrichtung]"
- Kein medizinischer Disclaimer noetig bei allgemeinen Wohlfuehluebungen
- Disclaimer bei koerperlichen Uebungen: "Hoer auf deinen Koerper. Bei Schmerzen, brich die Uebung ab."
- Content-Umfang MVP: ~30–40 Uebungen (5–7 pro Kategorie) decken die ersten Monate ab

---

## Zusammenfassung: UX-Leitplanken fuer Design & Engineering

| Leitplanke | Implikation |
|---|---|
| Erster Wert in <60 Sekunden | Landing-Screen mit einer Frage, kein Onboarding |
| Check-in < 5 Minuten | Max. 10–12 Fragen, Ueberspringen moeglich |
| Immer eine naechste Aktion | Kein Screen ohne Handlungsoption oder Uebung |
| Screening intern, nie als Score sichtbar | Nutzerin sieht Einordnungstext, nie "Risikostufe 2" |
| Eskalation bei roten Triggern sofort | Kein Warten auf naechsten Check-in, sofortige Anzeige Notfallkontakte |
| Uebungen folgen dem Check-in | Nie isoliert, immer kontextbezogen |
| Kein Guilt-Tripping | Verpasste Check-ins oder Uebungen werden nicht bestraft |
| Account optional bis Phase 4 | Erster Wert und Check-in ohne Registrierung |
| Mobile-first, aber nicht App-only | Web-App als MVP, native App spaeter (Medgate bevorzugt App) |
| Fachperson-Matching mit Follow-up | Nicht nur vermitteln, sondern nachfragen ob Kontakt zustande kam |
