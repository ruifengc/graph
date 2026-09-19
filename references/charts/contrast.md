# Expression · Contrast

Side-by-side comparison of two (or three) paths, sequences, or
positions — same starting point, different outcomes.

## Proven form

- Two columns, each a **behavior chain in input order** (steps top to
  bottom), sharing a pivot element at the top (the common starting
  point: the same sentence, the same event).
- Each column ends with its **outcome** as the punchline (the last step
  is the result, visually distinct).
- Column headers name the two sides. Honesty note in the caption: the
  columns follow the source's order and are a comparison, not measured
  data.
- The dual-column frame may be plain HTML (two stacked blocks) instead
  of SVG when the columns are text-heavy.

## Spec table variant (two entities, row-by-row, no metric axis)

When the comparison is a spec-sheet row-by-row (same row dimension,
columns = entities, no measured axis):

- Rows = shared dimensions; columns = the two entities.
- The column whose story the page tells gets the accent; the other
  stays on the ladder.
- One row may carry the punchline (the deciding spec), accented and
  called out in the takeaway.
- Caption states it is a spec comparison, not measured data
  ("规格对照，非实测").

## Experiment variant (the fork carries the judgment)

When the source ends in an either/or handed to the reader, the fork can
carry the interactive experiment (interactions.md §3): two branch
buttons switch the judgment condition, and a verdict sentence under the
fork rewrites live. Contract:

- BOTH verdicts must be literal claims from the source — every state is
  honest by construction.
- Reduced motion disables the buttons and shows both branches.
- The dim of the inactive branch goes on the branch GROUP, never on an
  element that also carries `.fade-in` (an animation's forwards fill
  overrides a declared opacity; group opacity multiplies the children's
  final state).

## Data contract

- Both columns' steps trace to the input; the shared pivot must be the
  same real element from the source.
- No invented steps to make the columns symmetric — unequal columns are
  honest columns.

## Constraints

- Never a fake metric axis; this is a sequence comparison, not a chart
  of measurements (say so in the caption).
- 2–3 columns max; more sides → split into separate sections.
- Outcomes stated as claims, not decorations.
