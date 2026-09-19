# Glyph · Bars

Categorical comparison / ranking (≤12 categories).

## Data contract

- Bar length ∝ value — never break the axis. Extreme outlier? Let it run
  off the plot and annotate the value (or add a zoom inset), never
  truncate the axis.
- Category bars on `--ink` (ladder: most important darkest); the single
  key category on `--accent`.
- Value labels at the bar end, tabular figures.

## Rules

- Signed values (positive/negative): zero is the baseline, bars grow
  from zero toward the value end, labels at the tail (charts/README
  signed-value section).
- One conclusion per chart: the ranked order / the gap / the winner.
  Title says which.
- Count-up the value labels on enter (once).
- No 3D, no gradient, no shadow bars.

## Pitfalls

- Long Chinese labels in vertical bars → overlap (go horizontal).
- Truncated axis for outliers → dishonest (never).
- More than ~12 categories → consider dots or a table.
