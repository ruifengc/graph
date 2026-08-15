# Workflow · Paper

Input: an academic paper / arXiv PDF / lecture notes.

Same seven-step pipeline as `article.md` — the differences:

1. **Read with the abstract + figures first.** Papers are dense; read
   abstract, skim figures/captions, then the method/results sections.
   The page's job is *why the paper matters and what it found*, not a
   literature review.
2. **Extract differently:**
   - Core claim = the paper's contribution (what it shows that wasn't
     known).
   - Evidence = the headline results (numbers from tables/figures) +
     the method in one line (so the reader can gauge trust).
   - Data shapes: results tables → bars/line/dots; method → timeline or
     flow if it tells the story; the "before/after" of a benchmark →
     bars.
3. **Honesty notes are mandatory.** Equations go in the caption as plain
   text ("log-scale loss, lower is better"), not LaTeX — the page is
   readable by a non-specialist friend, not a reviewer.
4. **Every result number keeps its source** (which table/figure in the
   paper, or the arXiv ID).

Framework status: first version. Will be enriched by real paper runs —
record gaps in runtime notes.
