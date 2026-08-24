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

    # 10. data series classes must not use --faint (D16: faint is a text
    #     layer, too low-contrast ≈1.4:1 to carry data)
    faint_data = re.findall(
        r'\.(?:seg|bar|dot|series|chip|ring|arc|point)[^{}]*\{[^}]*var\(--faint\)',
        html,
    )
    if faint_data:
        warns.append(
            f"data series class uses --faint (invisible on paper, use --ink/"
            f"muted/accent): {sorted(set(faint_data))[:4]}"
        )

    # 11. animation trigger mechanics (real bug: .grow/.fade-in present
    #     but no trigger rule → every animated child stays hidden, the
    #     chart renders as labels only). Either element-level .on rules
    #     (.grow.on, .fade-in.on with per-element watch) or a container
    #     propagation rule (.chart.on .grow, .chart.on .fade-in).
    if re.search(r'\.grow\s*\{', html):
        if not re.search(r'\.grow\.on\s*\{', html) and not re.search(r'\.chart\.on\s+\.grow\s*\{', html):
            findings.append(
                ".grow present but no trigger rule (.grow.on or .chart.on .grow) — bars stay at scaleX(.001), invisible"
            )
    if re.search(r'\.fade-in\s*\{', html):
        if not re.search(r'\.fade-in\.on\s*\{', html) and not re.search(r'\.chart\.on\s+\.fade-in\s*\{', html):
            findings.append(
                ".fade-in present but no trigger rule (.fade-in.on or .chart.on .fade-in) — elements stay at opacity 0, invisible"
            )

    # 12. duplicate class attribute on one tag (the second silently wins,
    #     styling/animation of the first is lost; passes all other checks)
    dup_class = re.findall(r'<[^>]*\bclass="[^"]*"[^>]*\bclass="', html)
    if dup_class:
        findings.append(
            f"duplicate class= on one element ({len(dup_class)}×) — second wins, first silently lost; merge the classes"
        )

    # 13. SVG geometry bounds — elements outside their viewBox get
    #     clipped (warn level: heuristic, catches the common overshoots)
    for m in re.finditer(r'<svg[^>]*viewBox="0 0 (\d+) (\d+)"[^>]*>(.*?)</svg>', html, re.S):
        W, H = int(m.group(1)), int(m.group(2))
        body = m.group(3)
        for t in re.finditer(r'<text[^>]*\bx="(-?[\d.]+)"[^>]*\by="(-?[\d.]+)"', body):
            x, y = float(t.group(1)), float(t.group(2))
            if x < -2 or x > W + 2 or y < -2 or y > H + 2:
                warns.append(f"text outside viewBox ({x:.0f},{y:.0f} in 0 0 {W} {H}): {t.group(0)[:56]}")
        for c in re.finditer(r'<circle[^>]*\bcx="(-?[\d.]+)"[^>]*\bcy="(-?[\d.]+)"[^>]*\br="(-?[\d.]+)"', body):
            cx, cy, r = float(c.group(1)), float(c.group(2)), float(c.group(3))
            if cx - r < -2 or cx + r > W + 2 or cy - r < -2 or cy + r > H + 2:
                warns.append(f"circle outside viewBox (cx={cx:.0f} cy={cy:.0f} r={r:.0f} in 0 0 {W} {H})")
        for q in re.finditer(
            r'<rect[^>]*\bx="(-?[\d.]+)"[^>]*\by="(-?[\d.]+)"[^>]*\bwidth="(-?[\d.]+)"[^>]*\bheight="(-?[\d.]+)"',
            body,
        ):
            x, y, w, h = float(q.group(1)), float(q.group(2)), float(q.group(3)), float(q.group(4))
            if x < -2 or y < -2 or x + w > W + 2 or y + h > H + 2:
                warns.append(f"rect outside viewBox (x={x:.0f} y={y:.0f} w={w:.0f} h={h:.0f} in 0 0 {W} {H})")

    # 14. hover wiring per chart — every chart needs a hover layer
    #     (warn level: heuristic count of hover bindings vs chart holders)
    charts = len(re.findall(r'class="chart', html))
    hovers = len(re.findall(r'mousemove|mouseenter|mouseover', html))
    if charts and hovers < charts:
        warns.append(
            f"{charts} chart holder(s) but only {hovers} hover binding(s) — check charts missing a hover layer"
        )

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
