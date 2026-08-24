# Glyph · Timeline

Events on a time axis — sequence, causality, milestones, life stories.

## When to use

- A narrative with dated events (company history, product life, a crisis
  unfolding, a paper's development).
- Comparing when things happened relative to each other.
- ≤12 events: the default step form below. Larger sets (a field's whole
  history, a product lineage of 20+ releases) use the chronicle mode.

## Chronicle mode — large event sets

A horizontal track for 15–60 events: the reader scrolls the rail while
each event card carries a one-line identity and click reveals the full
detail. This is how a "history of X" page holds a whole field.

- **Time maps linearly and honestly** on the x-axis (a date → a
  position). No fake spacing for drama; if dates are approximate, say
  so in the caption.
- Events alternate **above/below the rail** so adjacent cards never
  overlap (even index up, odd down — a layout, not a style).
- Cards are compact: org/date + name. Full detail (a paragraph, the
  significance) lives in a detail panel opened by **click**, not in the
  card itself.
- The rail itself is a DOM element of explicit width (scrollable), not
  a squeezed SVG — labels must stay readable.
- The protagonist line (the series the story follows) gets the accent;
  other camps stay on the ladder.
- Pivotal events may get a marker on the rail even before they are
  reached; no decoration beyond that.

## Vertical step form — short spans (5–15 events)

When the span is short and the events carry weight (a crisis
unfolding, a career's turning points), the vertical spine reads
better than the horizontal rail:

- A vertical spine with event cards on the right side, top = first,
  bottom = last (honest order, equal spacing unless the axis is
  declared a sequence).
- Cards carry name + short detail; the tooltip holds the full detail.
- Adjacent short spans: when two timeline sections sit next to each
  other in one page, alternate skeleton direction (one horizontal, one
  vertical) so the page never repeats itself.

## Data contract

- The sequence must trace to the input — every event, its order, and its
  detail come from the source; nothing invented.
- If the input has no real dates (e.g. drama recaps with only episode
  chronology), the axis is a **sequence, not a time scale** — say so in
  the caption ("横轴等距示意，非真实时间比例"), and never fake dates.
- Hover-to-read is the detail carrier: short labels on the chart, full
  detail in the tooltip (event-step hover variant, see
  `references/interactions.md`).
- Pivotal events (the ones the narrative turns on) get the accent;
  others stay on the ladder.

## Constraints (what must never happen)

- A flat row of dots pinned to the baseline with no hierarchy — user
  feedback: "一个个小点贴在最底下" reads as structureless.
  Events need a spine, labels with hierarchy (event name above, detail
  below or in tooltip), and breathing room. The timeline must read as a
  *sequence with weight*, not a dotted line.
- Crowded overlapping labels — alternate or trim to pivotal events.
- Non-linear spacing for "dramatic" effect (breaks the honesty rule) —
  unless the caption declares the axis is a sequence.

## Pitfalls

- Labels overlap when events cluster (alternate above/below, or keep
  only pivotal ones).
- Dots-only rendering reads as decoration, not chronology (see
  constraints).
