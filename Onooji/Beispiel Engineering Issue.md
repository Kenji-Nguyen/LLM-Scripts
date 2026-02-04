# Beispiel Engineering Issue

**Titel:** Mood-Slider aktualisiert Wert nicht beim Ziehen

**Labels:** `bug`, `frontend`, `Prio 1`

---

## Problem

Die Mood-Slider-Komponente aktualisiert ihren Wert nicht beim Ziehen. Die visuelle Position ändert sich, aber der tatsächliche Wert bleibt beim Anfangszustand.

---

## Ort

`src/components/mood-slider/MoodSlider.tsx`

---

## Architektur-Ebene

Component (Hooks-Problem)

---

## Technische Details

Wahrscheinlich fehlt ein State-Update im `onChange`-Handler. Prüfen ob der `useMoodSlider()` Hook die `setMoodValue()` Mutation richtig handhabt.

**Fehler reproduzieren:**
1. Chat öffnen
2. Mood-Check-Overlay öffnen
3. Slider ziehen
4. Wert bleibt bei 0, obwohl Slider sich bewegt

---

## Vorgeschlagene Lösung

```typescript
// In MoodSlider.tsx
const handleChange = (value: number[]) => {
  const moodValue = value[0]
  setLocalValue(moodValue) // ✅ Lokalen State aktualisieren
  onValueChange?.(moodValue) // ✅ Parent benachrichtigen
}
```

---

## Repository Info

- **Organisation:** Maji-Studio
- **Repository:** onooji-app
- **Related Docs:** `.claude/CLAUDE.md` (Architektur-Pattern)
