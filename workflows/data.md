# Workflow · Data

Input: a dataset / CSV / JSON / table with a story to tell (no prose).

Same eight-step pipeline as `article.md` — the differences:

1. **Profile the data first.** Rows? columns? ranges? missing values?
   units? period covered? This is the extraction step — the story is in
   the shapes, not in a text claim.
2. **Find the claim in the data.** A dataset is not an argument. The
   claim is whatever the data most strongly shows (the trend, the gap,
   the outlier, the before/after). If nothing stands out, say so in the
   notes instead of forcing a page.
3. **Data shapes are the map:** columns of numbers over time → line;
   category totals → bars; shares → ring/dots; dates → timeline.
4. **Numbers stay traceable.** The page carries the dataset's origin
   (file name, collector, date, license if any) in the source line.
5. **Sampling is declared.** If a 30-year daily series is downsampled to
   monthly for the chart, the caption says so ("每 3 个月一个点").

Framework status: first version. Will be enriched by real data runs —
record gaps in runtime notes.
