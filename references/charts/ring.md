# Glyph · Ring

Share / composition — parts of a whole. The default replacement for pie
charts: a donut with the total in the center.

## When to use

- One metric split into 2–6 categories (share of revenue, share of
  respondents, budget allocation).
- When the *whole* matters as much as the parts (center number).
- >6 categories: collapse into "other" or switch to bars.

## How to draw

- Donut (not pie): stroke-based arc segments, `stroke-width` ~34 in a
  250-height viewBox; center shows the total (serif, tabular).
- Segment angle ∝ value, start at 12 o'clock, clockwise. The accent
  segment is the story category; others on the gray ladder.
- Segment labels outside the ring with leader lines (muted 10.5px), or
  in a legend row under the chart — never inside thin segments.
- Caption: unit + total + period.

## Rules

- Angles encode value exactly — no "exploded" decorative segments.
- Rounded segment ends only if segments are ≥6% (else they obscure
  neighbors).
- Count-up the center total on enter.
- Segment colors from `--accent` / `--ink` / `--muted` — never
  `--faint` (data color rule in `tokens.md`). Small segments need MORE
  ink: largest share gets `--accent`, smallest visible share gets
  `--ink`. (A 4.5% segment in faint is invisible on paper, ≈1.4:1.)

## Pitfalls

- Very thin segments with inside labels (unreadable — label outside).
- Exploding slices for decoration (breaks the angle contract).
- A segment drawn in `--faint` or another low-contrast color — it
  disappears on paper. See Rules.
