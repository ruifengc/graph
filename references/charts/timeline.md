# Glyph · Timeline

Events on a time axis — sequence, causality, milestones, life stories.

## When to use

- A narrative with dated events (company history, product life, a crisis
  unfolding, a paper's development).
- Comparing when things happened relative to each other.
- ≤12 events; more → group or highlight only the pivotal ones.

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
  feedback from run 1: "一个个小点贴在最底下" reads as structureless.
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
