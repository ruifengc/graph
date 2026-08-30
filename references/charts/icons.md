# Glyph · Icons (semantic shapes, not datasets)

Hand-drawn SVG icons that carry MEANING and DIRECTION — for claims that
a bar row or comparison table would flatten into "just numbers".

## When to use

- **Multiples**: a "×3" / "+200%" claim → isotype icon counts (1 grey
  unit vs 3 accent units). The COUNT is the encoding.
- **Flow / direction**: money flows, behavior loops, causality —
  arrows between icon nodes. The arrow DIRECTION is the argument.
- **Source metaphor**: when the source itself frames a claim as a
  metaphor, draw the metaphor literally — nothing added.
- **Order-of-magnitude contrast**: two values far apart → two
  same-scale rulers; length replaces reading.

## Data contract

- Icons carry semantics and direction, NEVER exact values — precision
  stays in labels / hover / caption.
- Isotype counts MUST annotate the baseline ("1 颗 = 基准值"); icons
  never carry exact numbers.
- Scale rulers MUST share one scale (same px-per-unit); a different
  scale is a lie.
- Same facts as the equivalent table — icon expression is a
  presentation layer, not new claims.

## Icon library (hand-written, token-colored)

Define each icon ONCE in `<defs>`, reference with `<use href="#id">`,
color via CSS classes (`var(--ink)` / `var(--accent)` / `var(--bg)`)
so themes just work. A reusable starter set: person (head circle +
shoulder path), institution (pediment + columns + base), house (roof +
body), stock (polyline + arrowhead corner), coin (circle + glyph).
Verify every `href` resolves to a `<defs>` id — a broken href renders
nothing silently.

## Constraints

- Emoji are NOT an acceptable substitute — they break theme colors and
  look un-designed. Hand-written SVG or nothing.
- Don't icon-ify everything: a ranked growth list is still a bar
  chart. Icons fit CLAIMS, not datasets.
- A floating average line (metaphor pattern) is a STATISTICAL claim —
  the caption must state what the line means and that it belongs to no
  one depicted.
- Icons still get the hover layer (the contract applies to every
  chart).
