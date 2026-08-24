# Glyph · Bars

Few categories compared or ranked (≤12).

## When to use

Categorical comparison: revenue by plan, response by market, share by
segment. Ranking energy. For >12 categories consider dots or a table.

## How to draw

- Horizontal bars for long category names (Chinese names >4 chars go
  horizontal); vertical for short labels.
- Bar length ∝ value — never break the axis. Extreme outlier? Let it run
  off the plot and annotate the value (or add a zoom inset), never
  truncate the axis.
- Category bars on `--ink` (ladder: most important darkest); the single
  key category on `--accent`.
- Capsule ends (rounded outer end) per tokens; hairline baseline.
- Value labels at bar end, tabular figures, 11px min.

## Rules

- Signed values (positive/negative): follow the zero-line rules in
  `charts/README.md` (signed-value section) — zero is the baseline,
  bars grow from zero toward the value end, labels at the tail.
- One conclusion per chart: the ranked order / the gap / the winner.
  Title says which ("Where we gained, where we bled").
- Count-up the value labels on enter (900ms, once).
- No 3D, no gradient, no shadow bars.

## Pitfalls

- Long Chinese labels in vertical bars → overlap (go horizontal).
- Truncated axis for outliers → dishonest (never).
