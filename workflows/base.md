# Workflow · Base (generic)

The default processing path for ANY input. Other workflows inherit
from this card and declare only what is special about their input
type (see `paper.md`, `data.md`, `transcript.md`, `news.md` — each
starts with `继承: base` semantics: read this card plus the derived
card, nothing else). An article / long-read / analysis piece IS the
base shape: no derived card exists for it, run base directly.

## Processing skeleton

Follow the five pipeline stages in SKILL.md. No special handling —
this card adds the generic extraction and honesty rules below.

## Generic extraction rules

- **Core claim** — the input's one-sentence argument. If you can't say
  it in one sentence, you haven't understood the input yet.
- **Evidence** — the 2–6 facts/numbers/events that actually support
  the claim, ranked by weight.
- **Argument intents** — for each piece of evidence, what it CLAIMS
  (media reposts far outnumber originals; this series turned in Q2).
  The section structure of the narrative plan is built from these
  intents and the relations between them. Data shape / chart type is
  NOT decided here — that is the expression stage's freedom.
- **Sources** — every number's origin with date; the page's source
  line comes from here.

## Generic honesty discipline

- No fabricated data; every number traces to the input or a cited
  source (SKILL.md rule 1).
- The figcaption carries the honesty load: unit · scale · period ·
  sampling · rounding notes.
- A chart without a source line is unfinished.

## Generic glyph tendency

None — the expression stage decides freely from the narrative plan; the
glyph docs are a reference, never a menu. Derived cards may override
with a note.

## Recorded gaps

Runtime notes accumulate what base cannot predict; new derived cards
grow from real gaps, not from imagining (decisions.md D8).
