# Data cross-check before archiving

Why: validate.py checks structure (themes, toggle, hover, motion, no
hardcoded colors) — NOT the numbers. Hand-transcribing data into the
page's JS is where pages lie. A real run
wrote "4 misses" when the source had 3: a related-tool call had been
miscounted into the wrong bucket. Only a
source-comparison script caught it.

## The standing script: `scripts/deep_check.py`

The recurring checks are consolidated — run this before archiving:

```bash
python3 scripts/deep_check.py output.html input.md [--phrases "短语1,短语2"] [--ignore REGEX]
```

It asserts, over the built page:

1. **Number provenance** — every 3+ digit integer in the visible body
   text appears literally in input.md (SVG internals are excluded: axis
   ticks and geometry numbers there come from the same gen.py function
   as the data; the slip-prone surface is body text, captions, key
   numbers).
2. **Count-up provenance** — every `data-count="N"` appears literally in
   input.md, OR its `<figure>` caption declares the derivation (推算).
   Derived values are honest only when declared; an undeclared
   derivation reads as fabrication.
3. **Quote fidelity** — every `<blockquote>`/`<q>` appears verbatim in
   input.md, whitespace-stripped and case-insensitive on both sides
   (input may be sentence-case where the page capitalizes). The
   attribution inside the block (`<span class="src">` / `<cite>` /
   `<footer>`) is editorial and excluded from the compare.
4. **Required phrases** (`--phrases`) — quantity-bearing strings the
   argument hinges on ("时隔九年", "四次") actually made it onto the page.

Known edge cases a PASS can legitimately paper over (decide manually
when they apply): derived arithmetic in body text (a spread computed
from two input numbers — verify the math yourself), CJK numerals the
page rendered as digits (一百一十七 → 117), decimal shares the source
prints only in a table cell with different rounding. When a category
recurs for your run, pass `--ignore` or assert it in a throwaway
addendum instead of loosening the script.

## Beyond the standing script (per-run assertions)

deep_check.py covers what recurs on every run. Run-specific data
deserves run-specific assertions — a throwaway script (~5 min):

1. **Read the source dataset programmatically** — SQLite/CSV/原文, never
   eyeball the source. For agent trace data:
   SQLite: query the source tables directly.
2. **Extract the numbers embedded in input.html** (not output.html):
   - JS arrays: `const HOPS = [...]`, `const PROMPT = [...]`,
     `const rows = [...]` — regex the source text.
   - key numbers: `data-v="55.8"`, `data-suffix="×"`.
   - figtitle digits: "九次取文，三次空手" (6+3, not 4).
3. **Assert every figure against the source**:
   - per-point series values, not just totals
   - bar totals AND the ok/miss split segments (the real error was in a
     split bucket)
   - key numbers and derived claims ("last hop = half the total" →
     compare last-dur / total-dur)
   - hop count, tool count, tool-type counts
4. **Also verify output.html == build(input.html)** so the archived
   artifact matches the reviewed source.

## Pitfall: JS object literals are NOT JSON

`const HOPS = [{n:1, dur:7560, final:false}, ...]` — unquoted keys and
lowercase `true`/`false` make `json.loads` throw "Expecting property name
enclosed in double quotes". Two options:

- regex-extract fields: `re.finditer(r"\{n:(\d+),\s*dur:(\d+),\s*ptok:(\d+),\s*ctok:(\d+),\s*final:(true|false)", ...)`
- or quote keys + uppercase booleans, then json.loads

Pure number arrays (`const PROMPT = [1279,5904,...]`) ARE valid JSON
and parse fine — only object literals need the regex treatment.

Archive a copy of the script (or its assertions in notes.md) with the
run so repeat-topic runs re-run it before archiving.

## Pitfall: verify-script bugs produce false FAILs — suspect the script first

A throwaway key regex (`c\d\d:`) missed suffixed keys (`c01a:`) and
reported 11 false FAILs while the page was empirically fine. When an
ad-hoc check fails, cross-check with a browser probe before touching
the page — and prefer extending the standing script (it is
fixture-tested) over one-off regexes.
