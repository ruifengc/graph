# Glyph · Dots

Countable units: one dot = one real thing (person, answer, dollar, unit).
The densest honest encoding for small data.

## Data contract

- One dot = one unit; only real units. If rounding loses units
  (49.0 + 27.4 + 13.9 + 5.0 + 3.2 → 98), state it in the caption —
  never add phantom units to make 100.
- Color: gray ladder by importance; the story category on `--accent`.
- Caption states the unit ("one dot = one person in a hundred").

## Multi-group variant (groups of counted objects)

Counting comparison across groups — groups stacked as rows with generous
inter-group spacing. Same contract: one dot = one real thing, unit
stated, group labels on the left.

## Constraints

- Unit meaning in the caption, always.
- Only decomposable, honest units — never invent records from
  aggregates.
- Keep ≤200 units; beyond that switch glyph.
- Count-up the headline number on enter.
- Density is the aesthetic: furniture (grid lines, rim ticks) allowed;
  fake individual records are not.

## Pitfalls

- Inventing individual records from aggregates (never — only honest
  decomposable units).
- Dots too dense to count (keep ≤200).
