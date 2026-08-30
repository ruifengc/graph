---
name: graph
description: >-
  Turn an article, research report, academic paper, news digest, video
  transcript, or dataset into a single-file interactive HTML explainer page —
  a visual retelling that replaces line-by-line reading. Use when the user
  wants a piece of content or data "turned into a page / visualized / made
  into charts / an HTML report to look at" without specifying a tool. The
  output is a self-contained page with day/night themes, hand-written SVG
  charts, hover-to-read values, and all generated assets inlined.
  Schematic/technical visuals (architecture, flow, sequence) are
  allowed when the content demands them — a technical article may need
  a data-flow diagram — but never as bare diagram cards: the explainer
  framing stays.
---

# Graph — Content to Explainer HTML

Turn one piece of content into one HTML page that *explains it visually*.
The page is a tour guide, not a document: charts carry the argument, text
adds the punchlines, interaction serves readers who want to dig in.

## Division of labor: style is law, execution is free

Graph sets the **style, the information, and the constraints** — never
the specific drawing. The author — the LLM executing this skill — is
a creator, not an assembler, with full creative freedom within those
bounds:

- **Determined by the skill**: tokens (colors/type/spacing/motion),
  narrative structure (kicker → title → sub → key numbers → charts →
  sources), honesty rules, the interaction rules, technical pitfalls
  learned from real runs.
- **Free for the author**: how a chart is laid out, how events are
  expressed, what visual metaphor carries a comparison, how much
  decoration a section earns. Hand-written SVG is the medium; the
  composition is the author's.
- **The glyph library is a reference, never a menu, never a cap on
  expression.** Whenever the content calls for a structure the library
  does not offer, invent it: a new chart, a diagram, a metaphor, a
  whole new visual structure. Building a new structure is the
  expected path, not the exception — the library exists to learn
  from, and inventing extends it. The skill constrains only what it
  declares (tokens, narrative, honesty, motion/interaction rules);
  everything else is the author's to create. New expressions grow the
  library, not the other way around.
- The glyph docs in `references/charts/` state *when to use, what the
  data contract is, what must not happen* — they do not prescribe
  coordinates or a single correct drawing. Learn from their pitfalls,
  don't copy their geometry.

## What goes out

One self-contained `output.html`: hand-written SVG charts, day/night
themes (toggle in the corner), hover-to-read on every chart, and all
generated assets inlined. Explainer structure, interactions, and motion
are specified in `references/narrative.md` and
`references/interactions.md`; colors and type are locked in
`references/tokens.md` (the only allowed color source).

## Pipeline (five stages — load only what each stage needs)

Read files ON DEMAND: each stage names the files it requires; do not
pre-load the rest. Loading everything up front wastes context and
dilutes attention. **Never read `runtime/` or `examples/` while
generating** — prior pages are not style references; composing fresh
every time is what keeps the output varied (rule 7).

1. **Understand & route.** Read the whole input. Extract the core
   claim (1–3 sentences), the evidence, the data shapes, and every
   source — rules in `workflows/base.md`. Pick the matching workflow
   card (`workflows/` — paper / data / transcript / news; articles run
   base directly). A page built from skimming is a page that lies.
   *Load: the matched workflow card(s) — base + one derived, or base
   alone.*
2. **Design the narrative.** Write the kicker, conclusion title (a
   judgment, not a topic), sub-line, 2–4 key numbers, and one takeaway
   per chart. *Load: `references/narrative.md`.*
3. **Select glyphs.** Map each data shape through the decision table;
   if no glyph fits, hand-write following the closest glyph's
   conventions and note the new shape in runtime notes — new glyphs
   grow the same way (decisions.md D8). For every planned chart,
   state its claim and the visual structure that carries it (nodes,
   paths, annotations); an angle too thin to support more than a line
   and a few labels merges into a richer chart instead of spawning
   one. *Load: `charts/README.md` + only the glyph docs the content
   needs.*
4. **Assemble.** Build from the tokens and the narrative spec. Charts
   encode data faithfully: log scale only when the range demands it
   (state it in the caption), area encodes with sqrt, never fake a
   unit. *Load: `references/tokens.md`.*
5. **Build, validate, archive.** `python3 scripts/build.py page.html
   output.html`, then `python3 scripts/validate.py output.html` — the
   script is the availability floor (structure, themes, hover,
   motion-trigger mechanics, geometry bounds); fix every FAIL. Then
   `python3 scripts/deep_check.py output.html input.md` — the semantic
   floor (every number, count-up, and quote traces to the source).
   One
   fast browser pass: console clean + theme toggle flips both themes.
   That is the whole review — no screenshots, no scroll-through, no
   per-element confirmation, no pixel work. Spend the saved time on
   composition, not inspection. Archive `input.md` + `output.html` +
   `notes.md` (which workflow, what didn't fit, what was improvised)
   under `runtime/YYYY-MM-DD-<topic>/`. No archive, no completion.
   Then ask whether the page will be viewed from another machine; if
   yes, serve it with `python3 scripts/serve.py <output.html>` and
   hand over the LAN URL(s), stopping the server when the user is
   done.

## Non-negotiable rules

1. **No fabricated data.** Every number on the page traces to the input
   or a cited source. Estimates and placeholders are allowed only when
   marked as such in the caption. A chart without a source line is
   unfinished.
2. **Tokens are law.** Colors, type stack, spacing, motion parameters
   come from `references/tokens.md`. No new colors, no gradients unless
   tokens say so. The accent color is chosen by the author for the
   content, never exposed as a user-facing control.
3. **Self-contained for what we make.** All generated assets (CSS, JS,
   SVG, data) are inlined into the single HTML. External resources (web
   fonts, CDNs) are allowed only when declared and justified; the
   default token stack stays on system fonts.
4. **Honest encoding.** Bar length, dot count, ring angle, area size all
   map to real quantities. Log axes are declared in the caption. Rounded
   totals are footnoted, not silently fixed.
5. **Motion and interaction serve understanding.** Interactions carry
   information: hover-to-read, theme toggle, and — when the content
   invites it — reader-operable experiments (changing a condition —
   threshold, caliber, parameter — re-judges the state; see
   `references/interactions.md`). The forbidden kind is the show-off:
   an interaction or effect that exists only to impress. Motion never
   loops and never decorates; `prefers-reduced-motion` always honored.
   An effect that needs a new layout to exist does not deserve to
   exist.
6. **One page, one argument; chart count follows the content.** The page
   serves a single core claim. Each chart carries one independent
   conclusion — a long input with rich evidence earns more charts, a
   short input earns fewer. The constraint is ANGLE, not count: the
   same data viewed from different angles may each earn its own chart;
   the same angle drawn twice collapses into one (see
   `references/narrative.md` "Charts per section").
7. **Never read `runtime/` or `examples/` while generating.** Prior
   pages are not style references; reading them fixes the style and
   makes pages converge. The composition is fresh every run — input
   material comes only from the source, style comes only from this
   skill.

## Repository map

```
SKILL.md          this file — entry point (constitution + routing)
scripts/          build.py (multi-file → single HTML), validate.py
                  (mechanical availability floor), deep_check.py
                  (semantic floor: numbers/quotes trace to source),
                  serve.py (LAN sharing)
references/       knowledge base: tokens, narrative, interactions,
                  charts/, data-cross-check.md
workflows/        input-type cards: base + derived (paper/data/
                  transcript/news), each declaring only its differences
runtime/          run archive: input / output / notes per run (local only)
examples/         curated exemplars promoted from runtime (local only)
```

`runtime/` and `examples/` are excluded from the public repo — they
exist to evolve the skill, never to be read during generation (rule 7).

## References

- `references/tokens.md` — day/night theme tokens (the only color source)
- `references/narrative.md` — explainer structure and writing rules
- `references/interactions.md` — hover, theme toggle, experiments, motion
- `references/charts/` — glyph library: line, bars, dots, ring, timeline,
  relations, contrast, scatter, scoreboard, threshold, lanes, icons,
  conceptual
- `references/data-cross-check.md` — verify inlined numbers against the
  source before archiving
- `references/decisions.md` — design rationale archive; **maintainer
  reading only, never loaded during generation**

## Workflows (routing)

| Input | Card |
|---|---|
| Article / long-read / analysis | none — run `base.md` directly |
| Academic paper | `paper.md` (inherits base) |
| Dataset / CSV / table / official statistics | `data.md` (inherits base) |
| Video / talk transcript | `transcript.md` (inherits base) |
| News digest / batch | `news.md` (inherits base) |

Each derived card declares only what is special: recognition, special
processing steps, special glyph tendencies, special honesty discipline,
recorded gaps. If a family grows far enough apart, split a second base
card (change the `Inherits:` line in the affected cards).
