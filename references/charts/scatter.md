# Glyph · Scatter & Dot Plot (position-encoded)

Position on an axis IS the value. Two families: quadrant scatter (two
metrics per entity) and zero-line dot plot (one metric, few categories).

## Data contract

- **Axes carry real quantities with declared units and calibers** (e.g.
  环比 vs 同比, both in %). Declaring which metric is on which axis is
  part of the honesty duty.
- **Dual zero axes for signed data**: both axes cross at zero so the
  quadrants are real. A quadrant label names each region ("双升 / 同比
  仍涨环比已跌 / 双跌").
- **The empty quadrant is a conclusion, not a bug.** If no entity lands
  in one quadrant, say so in the caption — often the most honest visual
  statement of the page.
- Dot plot: dots sit on a zero line that stays visible; the connector
  from zero to each dot is the visual spine (draw-in).
- One accent dot per chart (the story entity); the rest on the ladder.

## Constraints

- **Zero-line dot plot: every row carries its value inline** — a small
  label next to the dot. Position-encoding alone reads as "there are no
  numbers"; hover is a supplement, not the primary read. Flip the label
  left when it would cross the right edge.
- **Quadrant scatter: label the representative few, never all.** Story
  entities and outliers get labels; the rest are read by hover.
- Dot rows must not coincide with the zero line — a row whose y equals
  the zero line hides its connector (offset rows so none coincides).
- Same-value rows: equal values stack or offset rows so connectors stay
  visible.
- One dot = one entity (or one value), position-encoded — NOT dots.md's
  unit-count semantics.

## Pitfalls (from real runs)

- Hand-computed hover arrays drift from the drawing. For 30+ points
  generate BOTH the SVG geometry and the hover arrays from one formula
  (a small gen.py).
- Truncating axes to zoom the cluster is dishonest; if the range is
  huge, let outliers run off and annotate, or say so in the caption.
