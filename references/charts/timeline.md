# Glyph · Timeline

Events on a time axis — sequence, causality, milestones, life stories.

## Chronicle mode — large event sets (15–60 events)

A horizontal track: the reader scrolls the rail while each event card
carries a one-line identity and click reveals the full detail.

- **Time maps linearly and honestly** on the x-axis (a date → a
  position). No fake spacing for drama; if dates are approximate, say so
  in the caption.
- Events alternate **above/below the rail** so adjacent cards never
  overlap (a layout, not a style).
- Cards are compact: org/date + name. Full detail lives in a detail
  panel opened by **click**, not in the card.
- The rail is a DOM element of explicit width (scrollable), not a
  squeezed SVG — labels must stay readable.
- The protagonist line gets the accent; other camps stay on the ladder.
- Pivotal events may get a marker on the rail even before they are
  reached; no decoration beyond that.

## Vertical step form — short spans (5–15 events)

When the span is short and the events carry weight, the vertical spine
reads better than the horizontal rail:

- A vertical spine with event cards on the right side, top = first,
  bottom = last (honest order, equal spacing unless the axis is declared
  a sequence).
- Cards carry name + short detail; the tooltip holds the full detail.
- Adjacent short spans: alternate skeleton direction (one horizontal,
  one vertical) so the page never repeats itself.

## Data contract

- The sequence must trace to the input — every event, its order, and its
  detail come from the source; nothing invented.
- If the input has no real dates, the axis is a **sequence, not a time
  scale** — say so in the caption, never fake dates.
- Hover-to-read is the detail carrier: short labels on the chart, full
  detail in the tooltip (event-step hover variant).
- Pivotal events get the accent; others stay on the ladder.

## Constraints (what must never happen)

- A flat row of dots pinned to the baseline with no hierarchy — reads as
  structureless. Events need a spine, labels with hierarchy, and
  breathing room.
- Crowded overlapping labels — alternate or trim to pivotal events.
- Non-linear spacing for "dramatic" effect — unless the caption declares
  the axis is a sequence.

## Pitfalls

- Labels overlap when events cluster (alternate, or keep only pivotal).
- Dots-only rendering reads as decoration, not chronology.
