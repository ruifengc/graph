# Glyph · Line

Continuous series over time. The workhorse of graph pages.

## When to use

A value (or a few values) measured repeatedly over time: monthly index,
daily price, yearly revenue, cumulative count. If the input is a series
with >20 points, line is the default.

## Data contract

- Time on the x axis must be **honest and continuous**: equal distance =
  equal time. Fractional time (`year + (month-1)/12`) — see pitfall 1.
- Log axis only when the range demands it (max/min > ~20×), and it
  **must be declared in the figcaption** ("对数刻度").
- The series is the accent-colored element; annotations (peak/trough/
  milestones) in muted with small dots. One accent per chart.
- Sampling must be declared in the caption ("每 3 个月一个点").
- Annotations must sit on real data: if sampling missed the true
  peak/trough, insert the true point into the series (pitfall 4).
- Polyline only — never smooth or interpolate.

## Constraints (what must never happen)

- Integer-year x collapsing multiple samples onto one column (pitfall 1).
- Labels clipped at the viewBox edge — leave headroom above the highest
  annotation (pitfall 2).
- Hover lookup comparing pixels against data values (pitfall 3).
- Interpolated tooltip values — the reader gets the nearest **real**
  point or nothing.
- Value labels without thousands separators at ≥1000.

## Hover-to-read (required, continuous charts)

Per `references/interactions.md`: transparent capture area over the
plot, mousemove → convert px to data coordinates → binary search the
nearest point → accent dot + fixed tooltip (value + date, tabular
figures, flips at viewport edges). Tooltip shows a real data point,
never an interpolation.

## Pitfalls (from real runs)

1. **Trident lines** — x used integer years, collapsing the 4 samples
   per year onto one x, drawing vertical jagged forks. Fixed with
   fractional year x.
2. **Top annotation clipped** — peak label above a point near the
   viewBox top rendered outside the SVG. Fix: headroom above the top
   annotation (top margin ~34 in a 250-high viewBox).
3. **Hover always hit the leftmost point** — nearest-point search
   compared pixel x against year values. Fix: convert px → data
   coordinate first, then search.
4. **Annotation floated off the line** — true peak (10843.6) wasn't in
   the sampled series, so its dot sat above the line. Fix: insert the
   true peak/trough into the data.
