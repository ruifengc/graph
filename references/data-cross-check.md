# Review claims against evidence

Static validation checks the artifact, not the truth of its explanation.
Focus review on findings that carry the page and caveats that could change them.

## Review the complete claim

For each important quantitative claim, compare the subject, metric, value,
unit, population, period, and experimental conditions with the cited location.
The same number elsewhere in a source is not evidence for this claim.
Check quotation wording and attribution; distinguish translation and paraphrase.

For derived results, verify the inputs, formula, denominator, units, rounding,
and assumptions. Valid conversions and calculated differences need not appear
literally in the source. For rankings and superlatives, check the relevant
comparison set; for causality, check whether the evidence supports causation.

## Data-heavy pages

Prefer one data representation for marks, labels, summaries, and tooltips.
Compare consequential series and transformations with the source, including
missing values, signs, totals, aggregation, and scale. A short calculation or
page-specific assertion is useful when it tests the actual data relationship.
Do not test only that the generated HTML repeats the same copied value.

## Optional literal scan

`python3 scripts/deep_check.py page.html input.md` lists numeric tokens and
quotes that merit review. It includes SVG text and small integers. A
`sources.md` next to the input, or `--sources FILE`, adds text for comparison.

Matching is literal: it cannot verify attribution, units, assumptions,
causality, source reliability, or dynamic JS/canvas text. Nonmatches may be
valid axis ticks, translations, conversions, or calculations. Matches may be
wrongly attributed. The scan reports hints, never a semantic PASS; its normal
exit code is not a factual verdict. `--phrases` can check explicitly requested
visible phrases, and only that contract can fail on content.

Browser smoke checks likewise do not establish that a model, comparison,
or control is correct. Exercise important page behavior and review evidence
separately. Report the checks actually performed.
