# Chart and diagram notes

Optional references for a drawing problem. Choose a form for the reading goal;
use another form when it fits better. These notes preserve useful encoding
principles and implementation pitfalls, not a mandatory visual vocabulary.

| Explaining | Notes |
|---|---|
| A measured trend | [Line](line.md) |
| Magnitudes or ranks | [Bars](bars.md), [scatter and dot plots](scatter.md) |
| Composition or countable units | [Ring](ring.md), [unit dots](dots.md) |
| Events or stages | [Timeline](timeline.md), [lanes](lanes.md) |
| Relationships or alternate paths | [Relations](relations.md), [contrast](contrast.md) |
| A qualitative account | [Conceptual](conceptual.md), [scoreboard](scoreboard.md) |
| A boundary or a visual analogy | [Threshold](threshold.md), [icons](icons.md) |

## Shared considerations

- Preserve units, sign, baseline, uncertainty, and the meaning of positions,
  lengths, areas, and counts. Label schematic geometry as schematic.
- Compare like quantities on shared scales, or make differences in scale
  explicit. Do not conceal signs or outliers to improve the composition.
- Keep labels legible at the actual rendered size. A local scroll region,
  responsive HTML, or a table may serve better than a squeezed SVG.
- Route edges away from labels; separate crowded routes and attach points.
  A marker arrowhead may remain visible while a dashed stroke draws in;
  fading the group avoids that entrance artifact if animation is useful.
- Generate marks, labels, and lookup data from the same representation in
  dense charts. Hover coordinates and drawing coordinates must share the
  same transform; convert screen pixels through the SVG coordinate system.
- Escape source text or use textContent for tooltips. CSS specificity and
  animation fill modes can override component margins, opacity, or transforms;
  inspect the computed state when an element unexpectedly disappears.

Neither hover nor animation is required. When details are interactive,
provide keyboard/touch access and preserve the main explanation without
operating them; see [interactions.md](../interactions.md).
