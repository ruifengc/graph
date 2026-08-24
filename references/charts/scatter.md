# Glyph · Scatter & Dot Plot (position-encoded)

Position on an axis IS the value. Two families: quadrant scatter (two metrics per entity) and
zero-line dot plot (one metric, few categories).

## When to use

- **Quadrant scatter**: many entities (20–40) each with two metrics —
  industry growth × two calibers, products by price × rating, papers
  by size × quality. The x/y axes are the two metrics; both are real
  quantities, never invented scales.
- **Zero-line dot plot**: few categories (≤12) whose signed values are
  the point — the dot's horizontal position carries the reading.
  Prefer it over bars when the point is a position, not a length, and
  when rows stay readable.
- The shape is NOT dots.md's unit-count semantics: here one dot = one
  entity (or one value), position-encoded, never a count of units.

## Data contract

- **Axes carry real quantities with declared units and calibers**
  (e.g. 环比 vs 同比, both in %). Declaring which metric is on which
  axis is part of the honesty duty.
- **Dual zero axes for signed data**: both axes cross at zero so the
  quadrants are real (double-up / mixed / double-down). A quadrant
  label names each region ("双升 / 同比仍涨环比已跌 / 双跌").
- **The empty quadrant is a conclusion, not a bug.** If no entity
  lands in one quadrant, say so in the caption — it is often the most
  honest visual statement of the page (an empty bottom-right
   quadrant carried the story).
- Dot plot: dots sit on a zero line that stays visible; the connector
  from zero to each dot is the visual spine (draw-in).

## Constraints

- **Zero-line dot plot: every row carries its value inline** — a small
  label next to the dot. Position-encoding alone reads as "there are
  no numbers" to the reader; hover is a supplement, not the primary
  read. Flip the label to the dot's left when it would cross the
  right edge.
- **Quadrant scatter: label the representative few, never all.** In a
  dense 2-D field the story entities and outliers get labels; the
  rest are read by hover.
- The two families differ because rows have room for labels and
  scatter fields do not.
- One accent dot per chart (the story entity); the rest on the ladder.
- Dot rows must not coincide with the zero line — a row whose y equals
  the zero line hides its connector (real bug; offset rows so
   none coincides).
- Same-value rows: equal values stack or offset rows so connectors
  stay visible.

## Pitfalls (from real runs)

- Hand-computed hover arrays drift from the drawing. For 30+ points
  generate BOTH the SVG geometry and the hover arrays from one formula
  (a small gen.py) — see charts/README "Coordinate-dense charts".
- Truncating axes to zoom the cluster is dishonest; if the range is
  huge, let outliers run off and annotate, or say so in the caption.
