# Glyph · Lanes

Horizontal rows that carry a layered structure — a stack of layers,
tiers, or tracks, each lane one distinct element with its own identity.

## Data contract

- Lane order follows the source's own layering (top = first mentioned /
  outermost, unless the source says otherwise — state which).
- Every lane's one-liner traces to the input; nothing padded to make
  rows even.
- One lane per layer: a short title + one line of content, separated by
  hairlines. The lane the story turns on gets the accent (a title
  accent, not a fill).

## Constraints

- Max ~6 lanes; more → collapse into groups with a group header row.
- No lane may carry a quantity it doesn't have — a lane is a layer, not
  a bar; values belong in bars or labels.
- Lane titles must not wrap (keep them short) or the row hierarchy
  blurs.
- Not for ranked quantities (that is bars); not for timelines (that is
  timeline.md).
- **Detail lives one interaction away**: each lane is a hover target
  whose tooltip holds the full paragraph — or a click toggle for touch
  devices. The chart stays one line per lane; the detail stays
  reachable.

## Pitfalls

- Long lane text turns the chart into a table — the one-line + hover
  contract exists exactly to prevent that.
- Adjacent lane accents compete; one accent per chart (the story layer).
