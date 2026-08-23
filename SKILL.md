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
the specific drawing. The author (an LLM) has full creative freedom
within those bounds:

- **Determined by the skill**: tokens (colors/type/spacing/motion),
  narrative structure (kicker → title → sub → key numbers → charts →
  sources), honesty rules, the interaction rules, technical pitfalls
  learned from real runs.
- **Free for the author**: how a chart is laid out, how events are
  expressed, what visual metaphor carries a comparison, how much
  decoration a section earns. Hand-written SVG is the medium; the
  composition is the author's.
- The glyph docs in `references/charts/` state *when to use, what the
  data contract is, what must not happen* — they do not prescribe
  coordinates or a single correct drawing. Learn from their pitfalls,
  don't copy their geometry.

## What comes in

| Input | Typical source |
|---|---|
| Article / essay | blog post, long-read, analysis piece |
| Research report / survey | industry report, survey results, whitepaper |
| Academic paper | arXiv paper, PDF, lecture notes |
| News digest | a batch of related news items |
| Video transcript | transcript of a talk / video |
| Dataset | CSV / JSON / table with a story to tell |

All inputs are normalized to **text + optional data** before anything else
happens. Graph never consumes video or PDF binaries directly.

## What goes out

One self-contained `output.html`:

- **Explainer structure** (top to bottom): kicker → conclusion title →
  sub-line → key numbers → chart blocks (title + caption + SVG + takeaway)
  → source line. Full spec in `references/narrative.md`.
- **Day/night themes**, toggle in the corner. Tokens locked in
  `references/tokens.md` — the only allowed color source.
- **Hand-written SVG charts** from `references/charts/` — no chart library,
  no framework. All generated assets (CSS, JS, SVG, data) are inlined into
  the single file; external resources (e.g. font CDN) are allowed only when
  explicitly declared and justified.
- **Interactions carry information**: hover-to-read (exact value + date
  at the nearest data point), theme toggle, and — when the content
  invites it — reader-operable experiments. The forbidden kind is the
  show-off: an interaction that exists only to impress. New
  interactions need a stated reason.
- **Motion, minimal**: the proven set is draw-in and count-up, played
  once, with `prefers-reduced-motion` honored. Motion serves
  understanding; it never loops and never decorates. A new effect needs
  the same justification as a new interaction.

## Pipeline (every run)

1. **Understand the input.** Read the whole input. Extract: the core
   argument (1–3 sentences), the evidence (what actually supports it), the
   data shapes (series / ranking / share / relation / timeline / ...), and
   every source. Never skip this step — a page built from skimming is a
   page that lies.
2. **Pick the workflow.** Match the input type against `workflows/`
   (article / paper / data / news / transcript). Follow its steps — matched
   or not, every run is archived in step 7; the notes record which workflow
   was used and where it fell short. If no workflow fits, follow the closest
   one and **record the gap** — new workflows grow from real gaps, not from
   imagining.
3. **Decide the narrative.** Write the kicker, conclusion title (a
   judgment, not a topic), sub-line, 2–4 key numbers, and one takeaway per
   chart. Rules in `references/narrative.md`.
4. **Select glyphs.** Map each data shape to a glyph in
   `references/charts/` (line / bars / dots / ring / timeline). If no glyph
   fits, hand-write SVG following the closest glyph's conventions and note
   the new shape in runtime notes — new glyphs grow the same way.
5. **Assemble the page.** Build from the tokens and narrative spec.
   Charts encode data faithfully: log scale only when the range demands it
   (state it in the caption), area encodes with sqrt, never fake a unit.
6. **Build & validate.** Run `scripts/build.py` to produce the single
   file, then `scripts/validate.py` and fix every finding. Light DOM
   check: browser console clean + theme toggle flips both themes. That
   is the whole review — no screenshots, no scroll-through verification,
   no per-element confirmation, no pixel work. Report
   `dom_review: passed`.
7. **Archive to runtime.** Save `input.md` (the source material + its
   origin), `output.html` (the artifact), and `notes.md` (which workflow
   was used, what didn't fit, what was improvised) under
   `runtime/YYYY-MM-DD-<topic>/`. No archive, no completion.
8. **Offer LAN sharing.** After archiving, ask the user whether they
   want to view the page from another machine. If yes, start
   `python3 scripts/serve.py runtime/YYYY-MM-DD-<topic>/output.html`
   in the background and hand over the printed LAN URL(s). Keep it
   running until the user says they're done, then stop the process.
   The server binds 0.0.0.0 unauthenticated — fine on a trusted LAN
   for a self-contained static page; say so when handing over the URL.

## Non-negotiable rules

1. **No fabricated data.** Every number on the page traces to the input or
   a cited source. Estimates and placeholders are allowed only when marked
   as such in the caption. A chart without a source line is unfinished.
2. **Tokens are law.** Colors, type stack, spacing, motion parameters come
   from `references/tokens.md`. No new colors, no gradients unless tokens
   say so. The accent color is chosen by the author for the content, never
   exposed as a user-facing control.
3. **Self-contained for what we make.** All generated assets (CSS, JS,
   SVG, data) are inlined into the single HTML. External resources (web
   fonts, CDNs) are allowed only when declared and justified; the default
   token stack stays on system fonts.
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
   conclusion — a long input with rich evidence earns more charts, a short
   input earns fewer; two charts saying the same thing collapse into one.

## Repository map

```
SKILL.md          this file — entry point
scripts/          build.py (multi-file → single HTML), validate.py (self-check),
                  serve.py (LAN sharing of a built page)
references/       knowledge base: tokens, narrative, interactions, charts/
workflows/        per-input-type processing flows (accumulate over time)
runtime/          run archive: input / output / notes per run (local only)
examples/         curated exemplars promoted from runtime (local only)
```

`runtime/` and `examples/` are excluded from the public repo — they exist
to evolve the skill: workflows grow from runtime notes, exemplars become
regression baselines when tokens or glyphs change.

## References

- `references/tokens.md` — day/night theme tokens (the only color source)
- `references/narrative.md` — explainer structure and writing rules
- `references/interactions.md` — hover-to-read and theme toggle patterns
- `references/charts/` — glyph library: line, bars, dots, ring, timeline
- `references/decisions.md` — why the design is what it is

## Workflows

- `workflows/article.md` — article / long-read → page
- `workflows/paper.md` — academic paper → page
- `workflows/data.md` — dataset / CSV → page
- `workflows/news.md` — news digest → page
- `workflows/transcript.md` — video transcript → page
