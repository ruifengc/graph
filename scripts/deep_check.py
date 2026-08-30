#!/usr/bin/env python3
"""Semantic deep-check for a built page against its input source.

validate.py is the availability floor (structure, themes, hover, motion,
geometry). It cannot see TRANSCRIPTION SLIPS: a number or quote that made
it into the page but not the source. This script is the semantic layer:

  1. NUMBER PROVENANCE — every number in the page's visible text (3+ digit
     integers, and any decimal) must appear literally in input.md.
  2. COUNT-UP PROVENANCE — every `data-count="N"` must appear literally in
     input.md, OR the enclosing <figure> must declare the derivation
     (推算) in its caption. An undeclared derivation reads as fabrication.
  3. QUOTE FIDELITY — every <blockquote>/<q> must appear verbatim in
     input.md (whitespace-stripped, case-insensitive compare on both
     sides; input may be sentence-case where the page capitalizes).

Usage:
    python3 scripts/deep_check.py output.html input.md [--phrases a,b]
                                             [--ignore REGEX]

Exit code 0 = PASS, 1 = FAIL (each failure printed as `FAIL: ...`).
Throwaway per-run verify scripts remain welcome for run-specific
assertions (per-point series values, bar totals); this script covers the
checks that recur on EVERY run.
"""

import argparse
import html
import re
import sys
from pathlib import Path


def visible_text(src: str, keep_svg: bool = True) -> str:
    """Strip style/script/comments/tags — leave only rendered text.

    keep_svg=False additionally drops SVG internals: axis ticks, scale
    labels, and geometry numbers there come from the same gen.py
    function as the data (drift impossible; validate.py checks their
    bounds). The slips this script hunts live in body text, captions,
    key numbers, and tooltips rendered outside <svg>.
    """
    if not keep_svg:
        src = re.sub(r"<svg\b.*?</svg>", " ", src, flags=re.S | re.I)
    src = re.sub(r"<style\b.*?</style>", " ", src, flags=re.S | re.I)
    src = re.sub(r"<script\b.*?</script>", " ", src, flags=re.S | re.I)
    src = re.sub(r"<!--.*?-->", " ", src, flags=re.S)
    src = re.sub(r"<[^>]+>", " ", src)
    return html.unescape(src)


def norm(s: str) -> str:
    """Whitespace-stripped, comma-stripped, lowercased for trace checks.

    CJK text contains no spaces, so whitespace-stripping alone cannot
    bridge a source line broken mid-sentence vs the page's reflow —
    punctuation-only differences remain visible in the mismatch print
    for manual judgment; everything else must match.
    """
    return re.sub(r"[\s,]", "", html.unescape(s)).lower()


def numbers_in(text: str):
    """3+ digit integers and any decimal number (the slip-prone classes)."""
    out = set()
    for m in re.finditer(r"\d+(?:\.\d+)?", text):
        raw = m.group(0)
        if "." in raw or len(raw.replace(".", "")) >= 3:
            out.add(raw)
    return sorted(out, key=lambda x: (len(x), x))


def figures(src: str):
    """(start, end, block) for each <figure>...</figure>."""
    return [(m.start(), m.end(), m.group(0))
            for m in re.finditer(r"<figure\b.*?</figure>", src, flags=re.S | re.I)]


def quoted_blocks(src: str):
    """Visible text of every <blockquote>/<q>, excluding attribution.

    The attribution (editor-added source note) lives inside the element
    as `<span class="src">` / `<cite>` / `<footer>`; it is editorial, not
    quoted material, so it is dropped before the fidelity compare.
    """
    out = []
    for m in re.finditer(r"<(blockquote|q)\b[^>]*>(.*?)</\1>", src, flags=re.S | re.I):
        inner = re.sub(
            r"<span\b[^>]*class=[\"']src[\"'][^>]*>.*?</span>", " ", m.group(2),
            flags=re.S | re.I,
        )
        inner = re.sub(
            r"<(cite|footer)\b[^>]*>.*?</\1>", " ", inner, flags=re.S | re.I,
        )
        out.append(visible_text(inner))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("output", help="built output.html")
    ap.add_argument("input", help="input.md — the source of truth")
    ap.add_argument("--phrases", default="",
                    help="comma-separated quantity-bearing phrases that must "
                         "appear in the page (each must trace to input too)")
    ap.add_argument("--ignore", default="",
                    help="regex of numbers to skip (e.g. a known derived form)")
    args = ap.parse_args()

    out_src = Path(args.output).read_text(encoding="utf-8")
    in_norm = norm(Path(args.input).read_text(encoding="utf-8"))
    vis = visible_text(out_src, keep_svg=False)
    vis_svg = visible_text(out_src)

    fails = []

    figs = figures(out_src)
    # Figures whose caption declares a derivation (推算): their numbers
    # are honest-by-declaration (the documented fix for a derived value
    # is a caption footnote, not silence) — exempt from number
    # provenance, same escape hatch the count-up check uses.
    declared_nums = set()
    for _, _, block in figs:
        if "推算" in visible_text(block):
            declared_nums.update(numbers_in(visible_text(block, keep_svg=False)))

    # --- 1. number provenance -------------------------------------------
    ignore_re = re.compile(args.ignore) if args.ignore else None
    for num in numbers_in(vis):
        if ignore_re and ignore_re.fullmatch(num):
            continue
        if num in declared_nums:
            continue
        if norm(num) not in in_norm:
            fails.append(f"number not in input: {num!r}")

    # --- 2. count-up provenance -----------------------------------------
    for m in re.finditer(r'data-count="([^"]+)"', out_src):
        val = m.group(1)
        if norm(val) in in_norm:
            continue
        declared = any(
            val in block and "推算" in visible_text(block) for _, _, block in figs
        )
        if not declared:
            fails.append(
                f"count-up value {val!r} not in input and no 推算 declaration "
                f"in its <figure> caption"
            )

    # --- 3. quote fidelity ----------------------------------------------
    for q in quoted_blocks(out_src):
        nq = norm(q)
        if nq and nq not in in_norm:
            fails.append(f"quote not verbatim in input: {q[:80]!r}")

    # --- 4. required phrases --------------------------------------------
    for phrase in [p for p in args.phrases.split(",") if p.strip()]:
        if norm(phrase) not in norm(vis_svg):
            fails.append(f"required phrase missing from page: {phrase.strip()!r}")

    if fails:
        for f in fails:
            print(f"FAIL: {f}")
        print(f"deep_check: {len(fails)} failure(s) — fix, rebuild, re-check")
        return 1
    print("deep_check: PASS — numbers, count-ups, and quotes all trace to input")
    return 0


if __name__ == "__main__":
    sys.exit(main())
