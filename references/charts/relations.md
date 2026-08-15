# Expression · Relations

Directed relationship map — who curries favor with whom, who hates
whom, who protects whom. **Validated in transcript run 1** (the
讨好链/灭口链 map was judged "不错的表达结构" by the user); keep the
conventions that worked.

## When to use

Inputs whose spine is a web of people/entities and their attitudes:
drama recaps, political/company power maps, ecosystem analyses.

## Proven form (validated in run 1)

- Nodes = people/entities; edges = directed relations.
- **Line semantics carry meaning**: solid = one kind of relation,
  dashed = another. State the mapping in the caption.
- ≤12 nodes; node labels short, relation arrows labeled with a verb
  phrase.
- The protagonist's relations on `--accent`; the rest on the ladder.
- Arrowheads as SVG `<marker>` with `fill:var(--...)` so they follow the
  theme (validated in run 5; hand-drawn polygons don't re-theme).

## Data contract

- Every node and edge traces to the input — nothing invented. If the
  input implies a relation without stating it, mark it (e.g. 推测).
- The caption states what kind of structure this is (关系示意, not a
  measured network).

## Constraints

- No node without a label; no edge without a direction.
- **Edge labels stay short.** A relation label is ≤ ~10 chars on the
  chart ("沙→陈 · 登门探望"); anything longer goes into the tooltip.
  Long labels stacked between nodes read as text dumped on the diagram
  (user feedback from run 4: "文字太多了，直接堆在这里").
- **Don't let edges of one node fan into a label pile.** When a node has
  many relations (e.g. one person connecting to everyone), stagger the
  labels, route edges through separate corridors, or keep only the
  pivotal relations on the chart and move the rest to the tooltip or a
  caption list.
- More than ~12 nodes → split into two maps or keep only the pivotal
  relations.
- Decoration (icons, portraits) only if it carries information.

## Pitfalls

- Edge labels overlapping between adjacent nodes (stagger, or tooltip).
- A hub node's labels crowding its neighbors (see constraints).
