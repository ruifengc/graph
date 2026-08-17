# Design Decisions

Why graph is what it is. Read this before changing anything — if a
decision's reason no longer holds, change the decision here first, then
the code. Every entry: decision, reason, date, status.

## 2026-08 · Foundation

### D1. One page, one argument; chart count follows content
The page serves a single core claim. Charts carry independent
conclusions; a long input earns more charts, two charts saying the same
thing collapse into one. *Reason:* the page replaces reading — its job is
to make one case stick, not to exhibit every datapoint. *Status:* in use.

### D2. Day/night dual theme (Paper + vermillion / Ink + gold)
Every page ships both themes, toggle in the corner. *Reason:* users read
in different environments; the two themes are the product's signature and
cost nothing per-page (tokens only). Accent colors chosen by the author
per content, never exposed to readers. *Status:* in use.

### D3. Hand-written SVG, no chart library
Glyphs are authored by hand following `charts/`, no ECharts/Chart.js/d3.
*Reason:* full control of the visual language (the library look would
leak through), zero dependency weight, and the skill's own glyphs become
the brand. *Status:* in use.

### D4. System font stacks by default
Serif (Georgia / Songti) for titles, system sans for body. *Reason:*
readable everywhere, zero licensing risk for an open-source repo, no
network needed. Webfonts allowed only when declared and justified
(SKILL.md rule 3). *Status:* in use.

### D5. Self-contained single file (our assets inlined)
CSS, JS, SVG, and data all inline into one HTML via `scripts/build.py`.
*Reason:* the artifact is shareable as one file (WeChat, email, USB);
our own assets are fully under our control so inlining costs nothing.
External resources allowed if declared. *Status:* in use.

### D6. Interactions and motion carry information (revised 2026-08)
Hover-to-read and theme toggle; draw-in and count-up; plus
reader-operable experiments when the content invites them. The
original decision capped interaction COUNT as part of the visual
identity; the user corrected this — the constraint is INFORMATION, not
quantity. What is forbidden: show-off interactions and effects that
exist only to impress (a particle field, a title that scatters into
particles) — they carry no data and interrupt reading. What is
encouraged: any interaction that surfaces data, changes the reading
context, or re-judges the state. Motion that needs new layout to exist
doesn't deserve to exist. *Status:* in use (as revised).

### D7. Log scale only when the range demands it, declared in caption
A series spanning 307 → 10843 (35×) cannot be read linearly; log scale
flattens the noise of the boom and reveals the long low plateau. Any
log axis is stated in the figcaption. *Reason:* honest encoding — the
reader must know the scale they are reading. *Status:* in use.

### D8. Workflows grow from runtime gaps, glyphs grow the same way
New input types and new shapes are handled by the closest existing
workflow/glyph, and the gap is recorded in runtime notes. The notes are
the raw material for the next workflow/glyph. *Reason:* the skill
evolves from real use, not from speculation (SKILL.md pipeline 2/4).
*Status:* in use.

### D9. Accent color is an author decision, not a user control
The page never offers color controls to the reader; the author picks the
accent per content at build time. *Reason:* one accent is part of the
composition; exposing it turns the page into a tool. *Status:* in use.

### D10. runtime/ and examples/ stay out of the public repo
`runtime/` (every run's input/output/notes) and `examples/` (promoted
exemplars) are gitignored; they exist to evolve the skill. *Reason:*
inputs may be private; and the public repo stays lean. *Status:* in use.

### D11. Style is law, execution is free (2026-08, after transcript run 1)
The skill determines style (tokens, narrative structure, honesty rules,
interactions, pitfalls) and provides information + constraints — it never
prescribes the specific drawing. The LLM author has full creative
freedom within those bounds; hand-written SVG is the medium, composition
is the author's. *Reason:* run 1 showed hand-written charts (relation
map, contrast columns) outperform template-copied ones; as LLMs grow
stronger, the skill's value is the style system + constraints, not a
cookbook of drawings. *Status:* in use.

### D12. Page structure is part of the style (2026-08, user review of run 1)
The page must read as a structured composition: clear vertical rhythm
(kicker → title → sub → key numbers → sections → source), aligned
block hierarchy, one level of visual nesting per idea. Flat "row of
dots pinned to the bottom" layouts are rejected. *Reason:* run 1's
timeline read as a string of dots stuck to the baseline — structure is
a style property, not an afterthought. *Status:* in use.

### D13. Section eyebrows mark the hierarchy (2026-08, user review of run 2)
Every section carries a small top-left marker (sequence number and/or
one-word label, kicker style) so the reader always knows where they are.
A hairline alone does not separate sections. *Reason:* run 2's sections
were separated only by a faint line and read as ambiguous blocks.
*Status:* in use.

### D14. Review is light: console + theme toggle (2026-08, user decision, revised)
The review gate is minimal: `validate.py` PASS + browser console clean +
theme toggle flips both themes. Explicitly no screenshots, no OCR, no
pixel statistics, no scroll-through verification, no per-element
confirmation. *Reason:* three consecutive subagent runs completed the
artifact then burned their timeout on ever-finer review (pixel review →
screenshots+OCR → scroll-through draw-in checks); the artifact is the
deliverable, and the human does the final look. *Status:* in use.

### D15. Validated expressions are documented, not prescribed (2026-08)
Run 1's relation map and contrast columns were judged good by the user;
they are now documented in `charts/relations.md` and `charts/contrast.md`
as *proven forms* — available information for the author, not mandatory
drawings (D11 still governs). *Reason:* the skill's value grows by
accumulating what worked, while leaving execution free. *Status:* in
use.

### D16. `--faint` is never a data color (2026-08)
A 4.5% ring segment rendered in `--faint` was invisible against the
paper ground (contrast ≈1.4:1). Data series colors come from
`--accent`/`--ink`/`--muted` only; small segments get MORE ink, not
less; a fourth series color requires a new token. *Reason:* faint
exists for the text hierarchy, not for carrying data; visibility is a
hard requirement. *Status:* in use (tokens.md Color roles + ring.md
Rules).
