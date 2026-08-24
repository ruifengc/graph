# Workflow · Paper

Inherits: base (read `base.md` first — only the differences below).

## When to use

An academic paper / arXiv PDF / lecture notes.

## Special processing steps

1. **Read abstract + figures first.** Papers are dense: abstract, skim
   figures/captions, then method/results. The page's job is *why the
   paper matters and what it found*, not a literature review.
2. **Extract differently:**
   - Core claim = the paper's contribution (what it shows that wasn't
     known).
   - Evidence = headline results (numbers from tables/figures) + the
     method in one line (so the reader can gauge trust).
   - Data shapes: results tables → bars/line/dots; method → timeline
     or flow if it tells the story; before/after benchmarks → bars.
3. **Every result number keeps its source** — which table/figure in
   the paper, or the arXiv ID.

## Special glyph tendencies

- Two-model / two-generation row-by-row comparisons → spec-table
  variant (`charts/contrast.md`).
- Evaluation sections with qualitative verdicts and no scores →
  qualitative scoreboard (`charts/scoreboard.md`) — never a fake bar
  chart from words.
- Architecture / data-flow when the method IS the story (relations.md
  conventions; `charts/README.md` geometry hygiene).

## Special honesty discipline

- Equations go in the caption as plain text ("log-scale loss, lower is
  better"), not LaTeX — the page reads for a non-specialist friend,
  not a reviewer.
- Formulas that the source cleaned up (e.g. an attention-affinity
  function reduced to prose) are summarized in words, never
  reconstructed; state that in the scope block.

## Recorded gaps

See runtime notes of paper runs (spec tables, qualitative evals).
