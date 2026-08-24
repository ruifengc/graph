# Data cross-check before archiving

Why: validate.py checks structure (themes, toggle, hover, motion, no
hardcoded colors) — NOT the numbers. Hand-transcribing data into the
page's JS is where pages lie. A real run
wrote "4 misses" when the source had 3: a related-tool call had been
miscounted into the wrong bucket. Only a
source-comparison script caught it.

## Recipe (throwaway script, ~5 min)

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
lowercase `true`/`false` make `json.loads` throw "Expecting property
name enclosed in double quotes". Two options:

- regex-extract fields: `re.finditer(r"\{n:(\d+),\s*dur:(\d+),\s*ptok:(\d+),\s*ctok:(\d+),\s*final:(true|false)", ...)`
- or quote keys + uppercase booleans, then json.loads

Pure number arrays (`const PROMPT = [1279,5904,...]`) ARE valid JSON
and parse fine — only object literals need the regex treatment.

Archive a copy of the script (or its assertions in notes.md) with the
run so repeat-topic runs re-run it before archiving.
