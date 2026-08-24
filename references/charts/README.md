# Glyph Library

Hand-written SVG charts. Each glyph doc states: **when to use → data
contract → constraints → pitfalls** (learned from real runs).

Per D11 (style is law, execution is free): these docs do **not**
prescribe coordinates, viewBoxes, or a single correct drawing. The
composition is the author's. What is fixed: the tokens, the data
contract (what the chart must encode honestly), the constraints (what
must never happen), and the pitfalls (what already broke in real runs).

## Shape → glyph decision table

| Data shape | Glyph | Doc |
|---|---|---|
| Continuous series over time (value per month/day/year) | Line | `line.md` |
| Few categories compared / ranked (≤12) | Bars | `bars.md` |
| Share / composition (parts of 100%) | Ring | `ring.md` |
| Countable units (1 unit = 1 real thing) | Dots | `dots.md` |
| Events on a timeline / sequence | Timeline | `timeline.md` |
| People/entities and their directed relations | Relations | `relations.md` |
| Two paths from a shared pivot, compared | Contrast | `contrast.md` |
| Many entities × two metrics (position-encoded) | Scatter / dot plot | `scatter.md` |
| Qualitative verdicts without scores | Scoreboard | `scoreboard.md` |
| A single value vs a threshold | Threshold gauge | `threshold.md` |
| Layered stacks / tracks | Lanes | `lanes.md` |
| Anything else | closest glyph + runtime note | — |

## Rules for every glyph

- Uses only tokens from `references/tokens.md`; every color via CSS var.
  **Put fill/stroke on CSS classes, not SVG attributes** —
  `fill="var(--x)"` as an attribute may not resolve in every browser;
  class-based colors (t-*/f-*/s-* helpers) always resolve.
- Plot area: viewBox `0 0 768 250` default; margins L46 R14 T34 B30
  (T34 leaves room for top annotations — labels clipped at the top edge
  was a real bug).
- Max 3–4 hairline gridlines; axis labels faint 10px.
- One accent-colored element per chart (the series / the key category).
- Annotations (peak/trough/events) in muted, 10.5px, with 3.2r dot
  (`--bg` fill, `--accent` stroke).
- Hover-to-read on every chart (contract in
  `references/interactions.md` — bars, rings, and multi-panel charts
  included, not only continuous series).
- Draw-in on the main path (2.4s, once, `prefers-reduced-motion` off).

## Geometry hygiene (applies to every chart with edges/arrows)

- **Arrows never cross text or content blocks.** An arrow ends at the
  node's rim or in open space — never through a label. (Real bug: a
  branch arrow cut straight through a lane label.)
- **Converging edges fan out.** Edges meeting at one node leave at
  distinct angles with separated control points; their mid-routes must
  not run close together or cross each other. (Real bug: three edges
  converged on one region ~12px apart.)
- If edges would collide, reroute (curved corridors), shorten labels, or
  drop non-pivotal edges into the tooltip/caption.
- **Marker arrows don't draw-in.** `stroke-dasharray` hides only the
  stroke — an SVG `<marker>` arrowhead stays visible before the path
  appears. Use a fade-in for arrowed paths, or accept the arrowhead
  early. (All arrows switched to fade.)

## Signed-value charts (positive/negative data)

For data with both signs (PPI-style 涨跌), the zero line is the base:

- **Zero line is the baseline** — positive bars grow up from it,
  negative bars grow down. Never render a -4.1% as a "positive" bar.
- Signed coloring: the ladder handles both directions (e.g. positive in
  ink, negative in muted), with the accent reserved for the story
  category — no red/green unless tokens say so.
- Draw-in animation grows each bar **from the zero line toward its own
  end** (negative bars grow downward), not from the plot bottom.
  (The grow-n variant.)
- Axes are never truncated to hide the sign change; if the range is
  huge, note it in the caption.
- Diverging bars: value labels sit at the bar **tail for both signs**;
  keep the category-name column wide enough that a short negative
  bar's tail label never reaches it (right-aligned names at x=250 kept
  a 54px gap). (Real bug: three negative labels
  overlapped their category names.)
- **Near-zero signed values stay honest at a few px.** A -0.2% value
  at 26px/% renders a 5px bar — keep true proportions, never invent a
  minimum bar width; the tail label carries the reading.
- **Zero-centered layout: labels hug the zero line.** When the plot is
  centered on zero, category names sit on the INNER side of zero
  (end-anchored left of zero for positive bars, start-anchored right
  for negative) and value labels sit at the bar tails outward — no
  wide category column needed, tails never reach the names.

## Composite charts (one section, two sub-panels)

A section with one conclusion may carry two sub-panels in one viewBox
(ruler + bars; progress + stock) when the conclusion needs both views:

- "One accent per chart" becomes ONE accent per sub-panel story point
  (the threshold line in panel A, the story bar in panel B) — two
  panels, two story points, two accents.
- **Panels share one scale and one zero line.** Different px-per-%
  across panels is a silent lie about lengths — a −6.4% bar rendered
  longer than a −8.6% bar next door. Share the scale, or stack the
  panels on one zero line; differing scales must be declared in the
  caption, never implied.
- Each sub-panel keeps its own caption duty (units, calibers) and its
  own hover.

## Coordinate-dense charts: generate, don't hand-write

30+ points, dot plots, multi-row geometry: hand-computed SVG + hover
arrays drift apart. Write a small gen.py that emits BOTH the SVG
elements and the hover arrays from ONE geometry function (hover JSON
embedded as an HTML comment, regex-extracted into main.js) — same
formula, drift impossible. A throwaway verify script then
asserts: deterministic bytes (two runs → identical), no leftover
placeholders, all hover points inside their viewBox, no hardcoded SVG
colors, key numbers present.

## Tooltip content escapes markup

Tooltip innerHTML parses `<think>` / `<|DSML|>` as unknown elements
and strips them. Escape tokens (`&lt;think&gt;`) in the generator or
the detail silently vanishes.

## Extending the library

No fitting glyph? Hand-write following the closest glyph's conventions,
then record the new shape in the runtime notes — new glyph docs grow
from real gaps (decisions.md D8).
