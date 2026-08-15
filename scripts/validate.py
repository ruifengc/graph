#!/usr/bin/env python3
"""graph validate — mechanical self-check of a built HTML artifact.

Usage:
    python3 scripts/validate.py <output.html>

Checks the non-negotiable rules that can be verified mechanically:
themes present, toggle exists, hover + tooltip, reduced-motion honored,
draw-in present, no leftover local file references, no hardcoded SVG
colors. Visual review is still the author's job (SKILL.md pipeline 6) —
this script is the floor, not the ceiling.

Exit code 0 = pass, 1 = fail (fix findings before delivery).
"""
import re
import sys
from pathlib import Path

EXTERNAL = re.compile(r"^(https?:|//|data:|#|mailto:)")


def main() -> int:
    path = Path(sys.argv[1])
    html = path.read_text(encoding="utf-8")
    findings: list[str] = []
    warns: list[str] = []

    # 1. no leftover local file references (everything we make must be inlined)
    refs = re.findall(r'(?:href|src)="([^"]+)"', html)
    local = [r for r in refs if not EXTERNAL.match(r)]
    if local:
        findings.append(f"leftover local references (not inlined): {sorted(set(local))[:6]}")

    # 2. both theme token blocks present
    for t in ("day", "night"):
        if f'data-theme="{t}"' not in html:
            findings.append(f'theme block "{t}" missing (body[data-theme="{t}"]{{...}})')

    # 3. theme toggle control
    if not re.search(r'toggle|btnDay|btnNight', html, re.I):
        findings.append("theme toggle control missing")

    # 4. hover-to-read
    if "mousemove" not in html:
        findings.append("hover handler missing (mousemove)")
    if not re.search(r'tip|tooltip', html, re.I):
        findings.append("hover tooltip element missing")

    # 5. reduced-motion honored
    if "prefers-reduced-motion" not in html:
        findings.append("prefers-reduced-motion block missing")

    # 6. draw-in motion (pathLength + dashoffset + keyframes)
    if not re.search(r'stroke-dashoffset', html) or "@keyframes" not in html:
        findings.append("draw-in motion missing (stroke-dashoffset + @keyframes)")

    # 7. count-up
    if "requestAnimationFrame" not in html:
        warns.append("no count-up animation found (ok if page has no key numbers)")

    # 8. no hardcoded colors inside SVG (must use tokens via CSS vars)
    hard = re.findall(r'(?:stroke|fill)="(?:#[0-9a-fA-F]{3,8}|rgb\()', html)
    if hard:
        warns.append(f"hardcoded SVG colors found (should be var(--...)): {sorted(set(hard))[:6]}")

    # 9. tokens referenced (var(--bg) etc.)
    if "var(--bg)" not in html:
        warns.append("token variables not referenced (var(--bg) absent)")

    print(f"validate {path.name}  ({len(html)/1024:.1f} KB)")
    for w in warns:
        print(f"  WARN  {w}")
    if findings:
        for f in findings:
            print(f"  FAIL  {f}")
        print("result: FAIL — fix findings before delivery")
        return 1
    print("result: PASS")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    sys.exit(main())
