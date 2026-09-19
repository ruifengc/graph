# Glyph · Scoreboard (qualitative verdicts)

Rows of verdicts when the source gives QUALITATIVE judgments, not scores.

## Data contract

- Every verdict traces to a stated judgment in the source. No scoring
  invented from words — a "better" in prose never becomes a bar length.
- The battlefield column carries the concrete evidence (which task,
  which metric family, which regime).
- The caption states the source gave no scores, and the row order
  follows the source's order.

## Constraints

- **Never fake a bar chart from qualitative comparisons.** Words are
  not quantities; the chip fill encodes the verdict CLASS, not a
  magnitude.
- **Never when the source HAS scores** — scores get bars or dots.
- Chips: solid fills (`--accent` = sets benchmark, `--ink` = beats /
  usable, `--muted` = trade wins), text in `var(--bg)` — readable in
  both themes. One chip class per verdict class.
- Max ~6 rows; more → split by theme or collapse to the pivotal ones.

## Pitfalls

- Treating "trade wins" as a loss — the chip ladder maps the source's
  own verdicts.
