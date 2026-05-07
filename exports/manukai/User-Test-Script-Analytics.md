# Manukai — User Test: Analytics

**Datum:** [Datum einfügen]  
**Moderation:** [Name einfügen]  
**Dauer:** 60 Minuten  
**Prototyp:** Analytics-Bereich (Live-App) + Figma (Use Cases 2–4)

---

## Ziele & Forschungsfragen

- Wie nützlich ist ein Analytics-Bereich für CAM-Programmierer im Alltag?
- Welche Daten und Visualisierungen sind am relevantesten?
- Wie navigieren Nutzer:innen durch Filter, KPIs und Diagramme?
- Können Nutzer:innen Operationen vergleichen und fundierte Entscheidungen treffen? (Use Case 2)
- Verstehen wir, wie viele bestehende Programme Nutzer:innen realistisch vergleichen wollen und welche Vergleichsparameter sie brauchen? (Use Case 2)
- Finden Nutzer:innen problematische Parameter, und können sie den Weg zur Korrektur nachvollziehen? (Use Case 3)
- Ist das Tab-Pattern nützlich, um aus Analytics heraus mehrere Projekte parallel zu öffnen und zu vergleichen? (Use Case 3)
- Ist der Batch-Edit-Flow für Werkzeugwechsel verständlich? (Use Case 4)
- Ist klar, was beim Ersetzen eines Werkzeugs genau ersetzt wird und wie mit abweichenden Parametern umgegangen wird? (Use Case 4)
- Wie viel Vertrauen haben Nutzer:innen in die dargestellten Daten?

---

## Setup

| Aspekt | Details |
|--------|---------|
| CAM-Programmierer:innen | 5 erfahrene CAM-Programmierer:innen (bestehende Manukai-Nutzer:innen) |
| Prototyp | Analytics: vollständig klickbare Live-App / Use Cases 2–4: Figma-Prototyp |
| Aufzeichnung | Bildschirm + Audio |
| Notizen | Moderation + ggf. Beobachter |

---

## Gesamtergebnis

| Thema | Zusammenfassung |
|-------|-----------------|
| Gesamteindruck | [nach dem Test ausfüllen] |
| Wichtigste Erkenntnisse | [nach dem Test ausfüllen] |
| Kritische Probleme | [nach dem Test ausfüllen] |

---

## Intro (5 Min.)

> Hallo [Name], danke, dass du dir die Zeit nimmst.
>
> Wir testen heute neue Funktionen von Manukai, insbesondere den Analytics-Bereich. Es geht nicht darum, dich zu testen, sondern die Software. Es gibt keine falschen Antworten.
>
> Ich gebe dir ein paar Aufgaben und stelle zwischendurch Fragen.

**Einverständnis und Aufnahme (fixer Text)**
- Ich würde das Gespräch gerne als Audio aufnehmen, ausschließlich für die interne Auswertung.
- Die Aufnahme wird nicht veröffentlicht und nicht an Dritte weitergegeben.
- Bist du damit einverstanden?

**Hinweis zum Prototyp (fixer Text)**
- Das ist teilweise ein Prototyp. Nicht alles ist klickbar.
- Wenn etwas nicht funktioniert, sag bitte kurz, was du erwartet hättest.

**Think Aloud (fixer Text)**
- Bitte denke laut: Sag, was du siehst, was du erwartest und warum du etwas anklickst.

---

## Warm-up (5 Min.)

- Wie sieht dein typischer Arbeitstag aus, wenn du ein neues Teil programmierst?
- Nutzt du heute Auswertungen oder Übersichten zu deinen Programmen, Werkzeugen oder Maschinen?
- Falls ja: Was schaust du dir an und warum?

---

## Aufgabe 1: Offene Exploration — Analytics-Bereich (15 Min.)

**Szenario:**
- Du öffnest den Analytics-Bereich von Manukai zum ersten Mal.
- Schau dich in Ruhe um.

**Anweisung:**
- Erzähl mir, was du siehst und wie du die Ansicht einschätzt.

**Follow-ups:**
- Was fällt dir als Erstes auf?
- Was davon wäre für deinen Alltag nützlich?

**Gezielte Fragen (nach der offenen Exploration):**
- Kannst du herausfinden, welches Werkzeug am häufigsten genutzt wird?
- Kannst du die Ansicht so filtern, dass nur Operationen für ein bestimmtes Material angezeigt werden?

| Thema | Frage | PSI - Mathias | Soudronic - Jan | Bosch - Kai | Bruderer - David | Mandatec - xyz |
|-------|-------|-----|-----|-----|-----|-----|
| **Erster Eindruck** | | | | | | |
| | Was verstehen sie sofort? | | | | | |
| | Was ist unklar oder verwirrend? | | | | | |
| **KPI-Karten** | | | | | | |
| | Welche Zahlen fallen besonders auf? | | | | | |
| | Fehlen Kennzahlen? | | | | | |
| **Diagramme** | | | | | | |
| | Welches Diagramm betrachten sie zuerst? | | | | | |
| | Verstehen sie Achsen und Datenpunkte? | | | | | |
| | Welches Diagramm ist aus ihrer Sicht am nützlichsten? | | | | | |
| **Filter** | | | | | | |
| | Finden sie die Filter? | | | | | |
| | Können sie nach Material filtern? | | | | | |
| | Finden sie das meistgenutzte Werkzeug? | | | | | |
| **Relevanz** | | | | | | |
| | Würden sie den Analytics-Bereich im Alltag nutzen? | | | | | |
| | Für welche Fragestellungen? | | | | | |

---

## Aufgabe 2: Operationsvergleich im Programmier-Flow (10 Min.)

**Szenario:**
- Du bist im automatisierten Programmier-Flow und hast ein Feature ausgewählt, für das du eine neue Operation anlegen willst.
- Manukai schlägt dir mehrere Kandidaten-Operationen vor, die bei ähnlichen Features verwendet wurden.
- Neben der Übersicht gibt es einen Tab **„Analyse“**, in dem du Operationen als Scatter-Plot vergleichen kannst.

**Anweisung:**
- Vergleiche die vorgeschlagenen Operationen und entscheide dich für eine.
- Nutze danach den Tab **„Analyse“** und prüfe, ob dir der Diagrammvergleich bei der Entscheidung hilft.

**Follow-ups:**
- Welche Informationen haben dir bei der Entscheidung geholfen?
- Fehlt dir etwas, um sicher entscheiden zu können?
- Wie viele bestehende Programme würdest du in so einer Situation typischerweise miteinander vergleichen?
- Welche Parameter möchtest du im Scatter-Plot vergleichen (z. B. Spindeldrehzahl, Vorschub, Zeit, Werkzeugdurchmesser)?
- Welche Achsen-Kombinationen wären für dich am sinnvollsten?
- Wann würdest du eher die Übersicht nutzen, wann den Analyse-Tab?

| Thema | Frage | PSI - Mathias | Soudronic - Jan | Bosch - Kai | Bruderer - David | Mandatec - xyz |
|-------|-------|-----|-----|-----|-----|-----|
| **Verständlichkeit** | | | | | | |
| | Verstehen sie, was die Kandidaten-Operationen sind? | | | | | |
| | Sind die angezeigten Parameter verständlich? | | | | | |
| **Entscheidungsfindung** | | | | | | |
| | Wonach entscheiden sie? (Parameter, Datum, Programmierer?) | | | | | |
| | Fühlen sie sich sicher genug für eine Entscheidung? | | | | | |
| **Vergleichsumfang** | | | | | | |
| | Wie viele Programme möchten sie realistisch parallel vergleichen? | | | | | |
| | Ab wann wird der Vergleich zu komplex oder unübersichtlich? | | | | | |
| **Analyse-Tab (Scatter-Plot)** | | | | | | |
| | Verstehen sie, was im Scatter-Plot verglichen wird? | | | | | |
| | Welche X-/Y-Parameter sind aus ihrer Sicht sinnvoll? | | | | | |
| | Unterstützt der Analyse-Tab die Entscheidung besser als die Listenansicht? | | | | | |
| **Fehlende Informationen** | | | | | | |
| | Welche zusätzlichen Daten würden sie brauchen? | | | | | |
| | Würden sie in diesem Moment Analytics-Daten nutzen wollen? | | | | | |

---

## Aufgabe 3: Werkzeuganalyse & Problemerkennung (15 Min.)

**Szenario:**
- Du möchtest für ein bestimmtes Werkzeug prüfen, welche Schnittdaten (Vorschub, Drehzahl, Kühlung) in verschiedenen Programmen verwendet wurden.
- Du hast den Verdacht, dass bei einem Programm die Parameter nicht optimal sind.
- Während der Analyse möchtest du zusätzlich ein weiteres Projekt öffnen, ohne den aktuellen Analytics-Kontext zu verlieren.

**Anweisung:**
- Finde das Werkzeug, schau dir die Operationen an und versuche herauszufinden, welches Programm problematische Parameter hat.
- Öffne danach ein weiteres Projekt in einem neuen Tab und wechsle zwischen beiden Kontexten.

**Follow-ups:**
- Wie würdest du jetzt vorgehen, um das Problem zu beheben?
- Ist der Weg vom Analytics-Bereich bis zur CAM-Korrektur nachvollziehbar?
- Ist das Tab-Pattern für dich sinnvoll, um mehrere Projekte parallel zu prüfen?
- In welchen Situationen würdest du mehrere Projekte gleichzeitig offen haben wollen?
- Welche Informationen sollten beim Tab-Wechsel erhalten bleiben?

| Thema | Frage | PSI - Mathias | Soudronic - Jan | Bosch - Kai | Bruderer - David | Mandatec - xyz |
|-------|-------|-----|-----|-----|-----|-----|
| **Navigation** | | | | | | |
| | Finden sie das richtige Werkzeug und Material? | | | | | |
| | Können sie die Operation mit verdächtigen Werten identifizieren? | | | | | |
| **Drill-down** | | | | | | |
| | Verstehen sie den Weg: Werkzeug → Operation → Programm → Teil? | | | | | |
| | Finden sie die Projekt-/Programm-Verlinkung? | | | | | |
| **Tab-Pattern** | | | | | | |
| | Erkennen sie, dass sie ein weiteres Projekt im neuen Tab öffnen können? | | | | | |
| | Können sie zwischen Tabs wechseln, ohne den Kontext zu verlieren? | | | | | |
| | Sehen sie einen klaren Nutzen in mehreren gleichzeitig geöffneten Projekten? | | | | | |
| **Korrektur-Flow** | | | | | | |
| | Verstehen sie „Zu CAM wechseln“? | | | | | |
| | Entspricht der Flow ihren Erwartungen? | | | | | |
| **Vertrauen** | | | | | | |
| | Vertrauen sie den angezeigten Parametern? | | | | | |
| | Welche Informationen stärken oder schwächen das Vertrauen? | | | | | |

---

## Aufgabe 4: Neues Werkzeug einsetzen — Batch-Edit (10 Min.)

**Szenario:**
- Du hast ein neues Werkzeug getestet, das bei einem bestimmten Feature doppelt so schnell ist wie das alte.
- Jetzt willst du alle alten Programme finden, die noch das alte Werkzeug verwenden, und es durch das neue ersetzen.
- Das neue Werkzeug unterscheidet sich teilweise in relevanten Parametern (z. B. Durchmesser, Vorschub, Spindeldrehzahl).

**Anweisung:**
- Finde die betroffenen Programme und tausche das Werkzeug aus.
- Definiere dabei, was genau ersetzt werden soll (nur Werkzeugreferenz oder auch Parameterwerte).

**Follow-ups:**
- Ist klar, was nach dem Batch-Edit passiert?
- Würdest du diesen Flow im Alltag verwenden?
- Welche Parameter sollten automatisch übernommen, angepasst oder manuell bestätigt werden?
- Welche Risiken siehst du beim Ersetzen über mehrere Programme hinweg?
- Welche Kontrolle erwartest du vor dem finalen Übernehmen (Vorschau, Konflikthinweise, Rückgängig)?

| Thema | Frage | PSI - Mathias | Soudronic - Jan | Bosch - Kai | Bruderer - David | Mandatec - xyz |
|-------|-------|-----|-----|-----|-----|-----|
| **Suche & Filter** | | | | | | |
| | Finden sie das alte Werkzeug in der Wissensdatenbank? | | | | | |
| | Können sie die betroffenen Operationen identifizieren? | | | | | |
| **Batch-Edit** | | | | | | |
| | Verstehen sie die Multi-Select-Funktion? | | | | | |
| | Ist der Batch-Edit-Dialog verständlich? | | | | | |
| **Ersetzungsumfang** | | | | | | |
| | Verstehen sie, was genau ersetzt wird? | | | | | |
| | Erwarten sie nur einen Werkzeugtausch oder auch Parameter-Anpassungen? | | | | | |
| **Parameter-Mapping** | | | | | | |
| | Welche Parameter müssen aus ihrer Sicht geprüft werden (z. B. Durchmesser, Vorschub, Drehzahl, Kühlung)? | | | | | |
| | Welche Parameter dürfen automatisch gesetzt werden, welche nur manuell? | | | | | |
| **Nachvollziehbarkeit** | | | | | | |
| | Verstehen sie den Status „Änderungsvorschlag“? | | | | | |
| | Ist klar, was beim nächsten CAM-Öffnen passiert? | | | | | |
| **Sicherheit & Kontrolle** | | | | | | |
| | Erwarten sie eine Vorschau der Auswirkungen vor dem Bestätigen? | | | | | |
| | Ist ein Rückgängig-/Rollback-Mechanismus erforderlich? | | | | | |
| **Alltagsrelevanz** | | | | | | |
| | Wie oft kommt ein Werkzeugwechsel bei ihnen vor? | | | | | |
| | Würden sie den Flow nutzen oder lieber manuell vorgehen? | | | | | |

---

## Abschluss (5 Min.)

> Danke, das war die letzte Aufgabe. Zum Abschluss noch ein paar kurze Fragen.

**Offene Fragen:**
- Wenn du den Analytics-Bereich mit einem Wort beschreiben müsstest: Welches wäre es?
- Gibt es etwas, das du vermisst hast?
- Welche der gezeigten Funktionen wäre für dich am nützlichsten?

**Abschlussbewertung (Skala 1–5):**

| Frage | PSI - Mathias | Soudronic - Jan | Bosch - Kai | Bruderer - David | Mandatec - xyz |
|-------|-----|-----|-----|-----|-----|
| Gesamteindruck: Wie bewertest du den Analytics-Bereich insgesamt? (1 = sehr schlecht, 5 = sehr gut) | | | | | |
| Visuelles Design: Wie bewertest du das visuelle Design? (1 = sehr schlecht, 5 = sehr gut) | | | | | |
| Verständlichkeit: Wie klar und verständlich war die Bedienung? (1 = sehr unklar, 5 = sehr klar) | | | | | |

> Danke für deine Zeit und dein Feedback!
