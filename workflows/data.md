# Workflow · Data

Inherits: base (read `base.md` first — only the differences below).

## When to use

A dataset / CSV / JSON / table with a story to tell (no prose), and
official-statistics release pages (prose + data tables + footnotes).

## Special processing steps

1. **Profile the data first.** Rows? columns? ranges? missing values?
   units? period? The story is in the shapes, not in a text claim.
2. **Find the claim in the data.** A dataset is not an argument; the
   claim is whatever the data most strongly shows (trend, gap, outlier,
   before/after). If nothing stands out, say so in the notes instead
   of forcing a page.
3. **Official statistics — caliber notes are part of the data.** 现价
   vs 不变价, base-period rotation, seasonal adjustment, rounding
   disclaimers (总量≠分项之和), and the definition of EVERY
   growth-rate column (单季同比 / 累计同比 / 环比) go into the page
   footer scope section AND are restated in each chart caption /
   tooltip — never mixed, never dropped.
4. **Derived claims are verified point-by-point before printing.**
   "lowest since 2023" / "only negative in the series" — check against
   every data point; don't attach a cause the source doesn't state.
5. **Cross-check inlined numbers against the source before
   archiving** — validate.py checks structure, not numbers; run the
   recipe in `references/data-cross-check.md`.
6. **Person / entity profiles** (timeline + composition + classification
   + counts mixed): list identity facts first → timeline finds the
   watershed → composition finds the generation shift → classification
   finds the obsession. Sections follow the shapes, not the source's
   order; unverifiable attributions are stated as unverified or
   dropped.

## Special glyph tendencies

- Signed 涨跌 data → zero-line charts (`charts/README.md` signed-value
  section, `charts/scatter.md` zero-line dot plot).
- Many entities × two metrics → quadrant scatter.

## Special honesty discipline

- The source line carries the dataset's origin (file name, collector,
  date, license if any) — or the release page URL and publish time.
- Sampling is declared in the caption ("每 3 个月一个点").

## Recorded gaps

See runtime notes of data runs (official statistics with caliber
discipline, person profiles, agent-trace datasets).
