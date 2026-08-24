# Glyph · Scoreboard (qualitative verdicts)

Rows of verdicts when the source gives QUALITATIVE judgments, not
scores: "sets the benchmark / beats the baseline / trade wins".

## When to use

A comparison whose evidence is stated as verdicts — benchmark claims,
leaderboards without numbers, evaluation sections that grade in words.
**Never** when the source HAS scores: scores get bars or dots.

## How to draw

- Rows = [domain + verdict chip + key battlefield (one line each)].
- Chips are solid fills: `--accent` for 立标杆 (sets the benchmark),
  `--ink` for 超基准/可用 (beats / usable), `--muted` for 互有胜负
  (trade wins). Chip text in `var(--bg)` — readable in both themes.
- The caption must state the source gave no scores
  ("原文未给具体分数"), and the row order follows the source's order.

## Data contract

- Every verdict traces to a stated judgment in the source. No
  scoring invented from words — a "better" in prose does not become
  a bar length.
- The battlefield column carries the concrete evidence (which task,
  which metric family, which regime).

## Constraints

- **Never fake a bar chart from qualitative comparisons.** Words are
  not quantities; the chip's fill encodes the verdict CLASS, not a
  magnitude.
- Max ~6 rows; more → split by theme or collapse to the pivotal ones.
- Chips must stay readable in both themes (solid fill + `--bg` text,
  never outline-only chips that vanish on one ground).

## Pitfalls

- Treating "trade wins" as a loss — the chip ladder must map the
  source's own verdicts, one chip class per verdict class.
