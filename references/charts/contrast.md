# Expression · Contrast

Side-by-side comparison of two (or three) paths, sequences, or
positions — same starting point, different outcomes. Keep the conventions that worked.

## When to use

Inputs structured as a comparison: same phrase in two settings, two
characters handling the same situation, before/after of a decision.

## Proven form

- Two columns, each a **behavior chain in input order** (steps top to
  bottom), sharing a pivot element at the top (the common starting
  point: the same sentence, the same event).
- Each column ends with its **outcome** as the punchline (the last
  step is the result, visually distinct).
- Column headers name the two sides.
- Honesty note in the caption: the columns follow the source's order
  and are a comparison, not measured data.
- The dual-column frame may be plain HTML (two stacked blocks) instead
  of SVG when the columns are text-heavy — the SVG medium is not
  mandatory for this expression.

## Spec table variant (two entities, row-by-row, no metric axis)

When the comparison is a spec-sheet style row-by-row (two models /
two generations: same row dimension, columns = entities, no measured
axis), the table form carries it:

- Rows = shared dimensions; columns = the two entities.
- The column whose story the page tells gets the accent (its header
  or its cells), the other stays on the ladder.
- One row may carry the punchline (the deciding spec), accented and
  called out in the takeaway.
- Caption states it is a spec comparison, not measured data
  ("规格对照，非实测").

## Experiment variant (the fork carries the judgment)

When the source itself ends in an either/or handed to the reader, the
fork can carry the interactive experiment (interactions.md §3): two
branch buttons switch the judgment condition ("tomorrow unchanged" vs
"tomorrow changed"), and a verdict sentence under the fork rewrites
live on every switch. Contract:

- BOTH verdicts must be literal claims from the source — every state
  the reader can reach is honest by construction.
- Reduced motion disables the buttons and shows both branches.
- The dim of the inactive branch goes on the branch GROUP, never on an
  element that also carries `.fade-in` — an animation's forwards fill
  overrides a declared opacity, and the dim silently never shows.
  Group opacity multiplies the children's final state, so dim-on-group
  + fade-in-on-children composes correctly.

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
