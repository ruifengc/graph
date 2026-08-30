# Interactions

Interactions carry information. The reader's action either surfaces
data (hover-to-read), changes the reading context (theme toggle), or
re-judges the state (an experiment) — or focuses the comparison (a
focus toggle). The forbidden kind is the
show-off — an interaction that exists only to impress. New
interactions need a stated reason and a runtime note.

## 1. Hover-to-read

Purpose: the reader wants the exact value at a point. Applies to any
chart with a continuous axis (line, area, timeline). Implementation
reference lives in `charts/line.md`; this file states the contract.

- A transparent `<rect>` over the plot area captures `mousemove`.
- Convert cursor px → data coordinates (invert the scale), then binary-
  search the nearest data point.
- Show a `--accent` dot on the data point (r 3.5, `--bg` stroke) and a
  tooltip with **value + date**, tabular figures.
- Tooltip is `position:fixed`, follows the cursor, flips side at viewport
  edges, `pointer-events:none`.
- `mouseleave` hides both.
- The tooltip shows the *nearest actual data point* — never interpolated
  values, never a guess.

### Event-step hover (variant for timelines / event sequences)

Discrete events on a timeline get the same contract in step form:
mousemove over the chart → map px to the nearest event index (fixed hit
areas or nearest-index search) → accent dot on the event + tooltip with
**event name + full detail**. Short labels live on the chart; the
tooltip carries the detail. Same tooltip styling and edge-flip rules.

### Node hover (variant for relation maps)

For relation maps, hover targets are the **nodes** (2D nearest-point
search over node positions), not the edges: hovering a node highlights
it and shows its full relation detail in the tooltip. This is what
keeps edge labels short on the chart while detail stays reachable
(paired with the relations.md label hygiene rule).

## 2. Theme toggle

Purpose: day/night reading. A pill toggle in the page corner.

- `body[data-theme="day|night"]` switches the token block; CSS
  `transition: background-color .35s, color .35s` animates the switch.
- Toggle styles: pill, 999px radius, 1px `--grid` border; active segment
  = `--ink` background, `--bg` text.
- `localStorage` persistence is optional; default to day on first visit.
- Charts must be readable in both themes: SVG elements use `var(--...)`
  tokens, never hardcoded colors.

## 3. Interactive experiment

A reader-operable experiment: the reader changes a judgment condition
(a threshold, a caliber, a parameter) and the visualization responds
instantly. Its purpose is discovery — "move the line yourself and
watch what crosses it". The control can take any shape: a slider, a
dial, a pick, a drag, a time cursor, a caliber switch. The form is
free; the contract is not.

- **The reader's action must change the judgment, not just the view.**
  Switching between two static columns is a weak experiment. Changing
  a condition (threshold, caliber, parameter) and watching the state
  re-judge is the real thing — a live count and a dynamic conclusion
  line that re-state the current state prove the change is real. If no
  condition changes, it is a toggle, not an experiment.
- Use only when the content invites it: a comparison, a ranking, a
  threshold question. If the argument does not hinge on a condition,
  do not add it.
- Honest encoding on every state: same data, same caliber labels, same
  caption duty. The live count / dynamic conclusion must never assert
  more than the data says.
- Degrades under `prefers-reduced-motion` to a static view of the
  default condition.
- The author records the reason in runtime notes. (Validated form:
  a caliber switch + threshold slider over 11 industry growth rates.)

## 4. Focus toggle (comparison focus)

A reader-operable focus switch over a BOTH-SIDES comparison frame: two
segmented buttons, one per side; the reader can isolate either side, and
clicking the active button again restores both. The toggle is a reading
aid layered on the contrast frame (`charts/contrast.md`) — no condition
changes, so it is NOT an experiment (§3); and it never replaces the
default both-sides view (the comparison must read at a glance).

- **Both columns live in ONE viewBox with disjoint x-ranges** (e.g.
  left col x 40–388, right col x 388–728). Hiding one column then never
  repositions the other — no layout jitter, no overlap, no swap code.
  Default state = both columns visible.
- Control: segmented pill buttons (theme-toggle styling), `aria-pressed`
  synced with the state; mode classes on the svg (`mode-a` / `mode-b`)
  `display:none` the inactive column group.
- Clicking the ACTIVE button again restores both sides (the empty state
  is "both", never "nothing").
- Under `prefers-reduced-motion` the buttons are disabled and CSS forces
  both columns visible — the static both-sides view is the fallback by
  construction (the columns never move; only display toggles).
- Both sides keep identical encoding duty (shared pivot, same chain
  structure, own outcome line); one accent per chart still applies.
- Caption states that the toggle focuses one side and that reduced
  motion fixes the both-sides view.

## Motion

The only two motion effects are draw-in and count-up (parameters, plus
the theme-switch and tooltip transitions, live in `references/tokens.md`
Motion). Both play once, on enter-viewport, via IntersectionObserver
(threshold ~0.15), disconnect after firing. Both disabled under
`prefers-reduced-motion`:

**IO trigger propagation (real bug — labels-only charts).** The
observer adds `.on` only to the element it observes. Animated elements
are usually SVG children (`rect.grow`, `circle.fade-in`): either watch
every animated element, or drive them with a container rule
(`.chart.on .grow { transform: scaleX(1) }`, `.chart.on .fade-in {
animation-play-state: running }`). Watching only the holder leaves
every child at its initial hidden state (opacity 0 / scaleX(.001)) —
the chart renders as labels and axes only. DOM review must check
computed `transform`/`opacity` after scroll, never element counts.

```css
@media (prefers-reduced-motion:reduce){
  .draw{animation:none;stroke-dasharray:none;stroke-dashoffset:0}
}
```

and a JS guard before starting count-up / draw-in.

## Contract checklist (validate.py also checks the static parts)

- [ ] Every chart has a hover layer and tooltip — bars, rings, and
      multi-panel charts included, not only continuous series
- [ ] Tooltip values match the nearest real data point
- [ ] Theme toggle present and both themes readable
- [ ] No looping or decorative animation
- [ ] `prefers-reduced-motion` honored
- [ ] No hardcoded colors in SVG (all `var(--...)`)
