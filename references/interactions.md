# Interactions

Two interactions are the default; a third is author-optional for
comparison-driven content. Anything beyond needs a stated reason and a
runtime note.

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
(Learned from transcript run 1.)

### Node hover (variant for relation maps)

For relation maps, hover targets are the **nodes** (2D nearest-point
search over node positions), not the edges: hovering a node highlights
it and shows its full relation detail in the tooltip. This is what
keeps edge labels short on the chart while detail stays reachable
(validated in run 5, paired with the relations.md label hygiene rule).

## 2. Theme toggle

Purpose: day/night reading. A pill toggle in the page corner.

- `body[data-theme="day|night"]` switches the token block; CSS
  `transition: background-color .35s, color .35s` animates the switch.
- Toggle styles: pill, 999px radius, 1px `--grid` border; active segment
  = `--ink` background, `--bg` text.
- `localStorage` persistence is optional; default to day on first visit.
- Charts must be readable in both themes: SVG elements use `var(--...)`
  tokens, never hardcoded colors.

## 3. Interactive comparison (author-optional)

A reader-operable comparison — two approaches, two decoders, two
generations — where the reader drives the switch (a lever, a slider, a
toggle between two modes). Its purpose is understanding: "see both
sides with your own hands".

- **Use only when the content's core IS a comparison** (two strategies,
  two decoding schemes, old vs new pipeline). If the page's argument
  doesn't hinge on contrast, don't add it.
- Must serve the explanation: each side gets the same honest encoding,
  the same caption duty, the same source line. It is two charts sharing
  one frame, not a toy.
- Degrades under `prefers-reduced-motion` to a static both-sides view.
- The author records the reason in runtime notes (this is the one
  interaction that exists only because the content demanded it).

## Motion (the only two effects)

| Effect | Trigger | Params |
|---|---|---|
| Draw-in | chart enters viewport | 2.4s, `cubic-bezier(.4,0,.15,1)`, once |
| Count-up | numbers enter viewport | 900ms, cubic-out, once |

Both via IntersectionObserver (threshold ~0.15), disconnect after firing.
Both disabled under `prefers-reduced-motion`:

```css
@media (prefers-reduced-motion:reduce){
  .draw{animation:none;stroke-dasharray:none;stroke-dashoffset:0}
}
```

and a JS guard before starting count-up / draw-in.

## Contract checklist (validate.py also checks the static parts)

- [ ] Every chart has a hover layer and tooltip (continuous charts)
- [ ] Tooltip values match the nearest real data point
- [ ] Theme toggle present and both themes readable
- [ ] No looping or decorative animation
- [ ] `prefers-reduced-motion` honored
- [ ] No hardcoded colors in SVG (all `var(--...)`)
