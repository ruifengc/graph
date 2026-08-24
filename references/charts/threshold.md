# Glyph · Threshold Gauge

A single value measured against a threshold — "X is one step short of
Y".

## When to use

The claim is a distance-to-threshold: 人均 GDP 39,164 vs 4 万美元
门槛; a rate 25bp vs 350bp; a score 89 vs 90. The reader needs to see
how close the value stands, not a whole series.

## How to draw

- A value ruler (one scale, one axis) with two anchor marks: the
  actual value and the threshold line.
- The condition that decides the crossing is annotated in words or a
  small formula ("汇率 < 1456.1 → 4 万美元时代") — the mechanism, not
  a decoration.
- Optionally pair with an interactive experiment when the condition
  itself is what the reader should play with (drag the threshold, see
  the verdict flip — see interactions.md §3).

## Data contract

- **Only the spoken anchor points get marks** — the value and the
  threshold, both traceable to the input. Never invent an intermediate
  series to fill the ruler.
- The ruler shares ONE scale between the value and the threshold (a
  common unit); the caption states the unit.
- The verdict sentence ("差一步" / "已跨过") is a claim from the
  input, restated, not inferred.

## Constraints

- No fake precision: the ruler's ticks only go as fine as the data's
  own precision.
- If the threshold comparison depends on another variable (a rate, a
  currency), the dependency is stated — never implied.

## Pitfalls

- Filling the ruler with a made-up trend line to make the gap look
  dramatic — the gap IS the story, draw it as a gap.
- Mixing scales: a threshold from one unit and a value from another
  on the same ruler (declared conversions only).
