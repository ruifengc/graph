# Glyph · Lanes

Horizontal rows that carry a layered structure — a stack of layers,
tiers, or tracks, where each lane is one distinct element with its own
identity and one line of content.

## When to use

- A system / argument / history that decomposes into a fixed set of
  stacked layers: a model's tech stack, a policy's tiers, an
  organization's tracks.
- When rows ARE the structure (order matters, hierarchy matters) and
  a bar/dot chart would flatten the layering away.
- NOT for ranked quantities (that is bars) and not for timelines
  (that is timeline.md).

## How to draw

- One lane per layer: a title (short, ≤ ~10 chars) + one line of
  content, separated by hairlines.
- The lane the story turns on gets the accent (a title accent, not a
  fill).
- **Detail lives one interaction away**: each lane is a hover target
  (event-step variant) whose tooltip holds the full paragraph — or a
  click toggle for touch devices (hover is unavailable on touch;
  click works everywhere; both is fine). The chart stays one line per
  lane, the detail stays reachable.

## Data contract

- Lane order follows the source's own layering (top = first mentioned /
  outermost, unless the source says otherwise — state which).
- Every lane's one-liner traces to the input; nothing padded to make
  rows even.

## Constraints

- Max ~6 lanes; more → collapse into groups with a group header row.
- No lane may carry a quantity it doesn't have — a lane is a layer,
  not a bar; values belong in bars or labels.
- Lane titles must not wrap (keep them short) or the row hierarchy
  blurs.

## Pitfalls

- Long lane text turns the chart into a table — the one-line + hover
  contract exists exactly to prevent that.
- Adjacent lane accents compete; one accent per chart (the story
  layer).
