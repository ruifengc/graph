# Workflow · Article

Input: an article / long-read / analysis piece (text, or transcript of a
written piece). The most common input type — this workflow is the
reference shape for the others.

## Steps

### 1. Read the whole input

No skimming. Read the full text before extracting anything.

### 2. Extract the structure

Write down (in your working notes, not yet on the page):

- **Core claim** — the article's one-sentence argument. If you can't say
  it in one sentence, you haven't understood the article yet.
- **Evidence** — the 2–6 facts/numbers/events that actually support the
  claim. Rank them by weight.
- **Data shapes** — for each piece of evidence: is it a series over time?
  a ranking? a share? an event sequence? a relation? (map to
  `references/charts/README.md`)
- **Sources** — every number's origin, with date. The page's source line
  comes from here.

### 3. Decide the narrative (references/narrative.md)

- Kicker: domain · scope · as-of date.
- Title: the core claim as a judgment ("Shipping is not one cycle").
- Sub-line: the tension — why this claim is surprising or worth reading.
- Key numbers: 2–4 strongest numbers from Evidence, each with label +
  note.
- Chart blocks: one per independent conclusion. Count follows the
  content — a long article with rich evidence earns more charts; two
  charts making the same point collapse into one.

### 4. Select glyphs

For each chart block, match its data shape to a glyph
(`references/charts/`). No fit → closest glyph + note the gap for
runtime notes.

### 5. Assemble the page

Build per tokens (`references/tokens.md`) and the narrative spec. The
chart is the argument; text is the punchline. Write figcaptions with the
honesty load (unit · scale · period · sampling).

### 6. Build & validate

`python3 scripts/build.py page-src.html` → single file, then
`python3 scripts/validate.py out.html` — fix every finding. Then open
the file and actually look: labels clipped? annotations overlapping?
hover working on every chart? both themes readable? Report
`visual_review: passed` only after looking.

### 7. Archive to runtime

`runtime/YYYY-MM-DD-<topic>/`:
- `input.md` — the article (or its URL + full text), who wrote it, when.
- `output.html` — the built artifact.
- `notes.md` — which workflow steps held, which didn't, what was
  improvised, any new shape/glyph/workflow insight.

No archive, no completion (SKILL.md rule).

## Example (worked, abbreviated)

Input: the shipping analysis used for the style lab (global freight,
three sub-sectors, orderbook divergence).

- Core claim: shipping is not one cycle — same price shock, three
  different orderbook positions.
- Evidence ranked: orderbook shares 38.7% / 7% / 14.7%; BDI 10843 →
  307; SCFI event peaks.
- Shapes: 3 key numbers; one series (BDI, log); one comparison
  (orderbook shares).
- Narrative: kicker "GLOBAL SHIPPING · DATA AS OF 2026-07-10"; title
  "Shipping is not one cycle"; sub-line the tension; numbers with
  source notes; one line chart + takeaway; source line.
- Glyphs: line (log, annotated peak/trough) + key-number row.
- Pitfalls hit (all now in `references/charts/line.md`): integer-year x
  tridents, clipped top annotation, hover px/year mixup, peak missing
  from sampled data.
