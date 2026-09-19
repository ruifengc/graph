# Glyph · Icons (semantic shapes, not datasets)

Hand-drawn SVG icons that carry MEANING and DIRECTION — for claims a bar
row or comparison table would flatten into "just numbers".

## Data contract

- Icons carry semantics and direction, NEVER exact values — precision
  stays in labels / hover / caption.
- Isotype counts MUST annotate the baseline ("1 颗 = 基准值"); icons
  never carry exact numbers.
- Scale rulers MUST share one scale (same px-per-unit); a different
  scale is a lie.
- Same facts as the equivalent table — icon expression is a
  presentation layer, not new claims.
- Fits these claims: multiples (isotype counts), flow / direction
  (arrows = the argument), source metaphor (draw the metaphor
  literally), order-of-magnitude contrast (same-scale rulers).

## Icon library (hand-written, token-colored)

Define each icon ONCE in `<defs>`, reference with `<use href="#id">`,
color via CSS classes (`var(--ink)` / `var(--accent)` / `var(--bg)`) so
themes just work. A reusable starter set: person (head circle + shoulder
path), institution (pediment + columns + base), house (roof + body),
stock (polyline + arrowhead corner), coin (circle + glyph). Verify every
`href` resolves to a `<defs>` id — a broken href renders nothing.

## Constraints

- Emoji are NOT an acceptable substitute — they break theme colors and
  look un-designed.
- Don't icon-ify everything: a ranked growth list is still a bar chart.
  Icons fit CLAIMS, not datasets.
- A floating average line (metaphor pattern) is a STATISTICAL claim —
  the caption states what the line means and that it belongs to no one
  depicted.
- Icons still get the hover layer (the contract applies to every chart).
