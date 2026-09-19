# Glyph · Ring

Share / composition — parts of a whole. A donut with the total in the
center (a default replacement for pie charts).

## Data contract

- Segment angle encodes the value exactly (start at 12 o'clock,
  clockwise). No "exploded" decorative segments.
- The accent segment is the story category; the rest on the gray ladder.
- The center shows the total; count-up on enter.
- Caption states unit + total + period.

## Constraints

- Rounded segment ends only if segments are ≥6% (else they obscure
  neighbors).
- Colors from `--accent` / `--ink` / `--muted`, never `--faint` (data
  color rule in `tokens.md`). Small segments need MORE ink — largest
  gets `--accent`, smallest visible gets `--ink` (a 4.5% segment in
  faint is invisible on paper, ≈1.4:1).
- More than ~6 categories: collapse into "other" or switch to bars.

## Pitfalls

- Very thin segments with inside labels (unreadable — label outside).
- Exploding slices for decoration (breaks the angle contract).
- A segment in `--faint` or another low-contrast color disappears on
  paper.
