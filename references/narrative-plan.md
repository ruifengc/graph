# Narrative Plan (the intent layer)

The narrative plan is the page's CONTENT blueprint — what the page
argues and in what order — written with zero expression vocabulary. It
is the handoff from *understanding the input* to *deciding how to say
it visually*. Drawing decisions do not belong here.

## Intent layer vs. expression layer

The pipeline separates two layers. The narrative plan is the INTENT
layer: it reasons about meaning. The expression stage reasons about
means. A plan that prescribes a chart type, a visual term, a
coordinate, an easing, or a library has crossed the boundary — the
author's freedom to choose the form is gone, and the plan has colluded
with the draw it was supposed to leave open.

- **Intent (this file)** — what each piece of the page CLAIMS, what
  evidence backs it, how the pieces relate, what must be declared
  honestly.
- **Expression (next stage)** — how to draw it: the chart form, the
  visual metaphor, the interaction's control shape, the technique
  (hand-written SVG / a library / 3D / single-file or not). All of it
  is the author's to choose.

## The plan's fields

Write the plan as a short document (the form is free; the fields are
the contract). Keep it lean — no decoration, no filler. It is an
argument, not an essay.

### 1. Core claim

One sentence. The single judgment this page exists to stick. If it
cannot be one sentence, the input is not yet understood.

### 2. Section structure

One block per section. Each block has three fields, all in plain
semantic language with zero visual vocabulary:

- **Argument intent** — what this section claims. Not "use a bar
  chart"; rather "media reposts far outnumber originals," "this series
  turned in Q2," "the two policies pushed in opposite directions."
- **Evidence** — the specific facts / figures / quotes that back it,
  each tagged **from-source**, **derived** (推算), or **must-omit**.
  The plan states what is true; the expression stage decides how to
  encode it.
- **Relation** — how this section relates to its neighbors: sets up,
  contrasts, turns, escalates. The spine that keeps the page one
  argument instead of a stack of separate charts.

### 3. Honesty statements

Everything that must be declared on the page, front-loaded as promises:
every number's provenance, any derived value, calibers and caveats,
omitted segments, ASR corrections. Planned here so they are never
repaired as an afterthought in a caption.

### 4. Reader-operable points

Mark only the arguments where changing a condition (threshold, caliber,
parameter, time) would genuinely re-judge the claim — and say only
that, in intent terms ("a reader switching the caliber sees the ranking
invert"). The *control form* is not decided here; that is expression.

## Forbidden in a plan (the boundary)

The plan must NOT contain: any chart or visual type name (line, bar,
scatter, ring, threshold…), any visual or animation term, any
interaction-control suggestion (slider, dial, drag…), any library, any
coordinate / pixel / spacing / color / font / motion value, any "how to
draw" advice. Encoding choices are the next stage's freedom.

## Contract

- [ ] Every section states an argument intent, not a drawing
- [ ] Evidence is tagged from-source / derived / must-omit
- [ ] Honesty statements are complete before any drawing is conceived
- [ ] Zero expression vocabulary: no chart type, no visual term, no
      control form, no library, no coordinates, no colors
- [ ] Reader-operable points reason about the judgment, never the control
