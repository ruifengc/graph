#!/usr/bin/env python3
"""graph build — inline local CSS/JS into a single HTML artifact.

Usage:
    python3 scripts/build.py <input.html> [output.html]

Input HTML may reference local stylesheets and scripts via
<link rel="stylesheet" href="..."> and <script src="..."></script>.
Local files are inlined; remote URLs are kept as-is (declared external
resources are allowed per SKILL.md rule 3). Data files are inlined the
same way (<script src="data.js">).

Run validate.py on the output afterwards.
"""
import re
import sys
from pathlib import Path

EXTERNAL = re.compile(r"^(https?:|//|data:|#|mailto:)")


def inline_link(m: re.Match, base: Path) -> str:
    href = m.group(1)
    if EXTERNAL.match(href):
        return m.group(0)
    p = (base / href).resolve()
    if not p.exists():
        print(f"  WARN  missing css: {href}")
        return m.group(0)
    return f"<style>\n{p.read_text(encoding='utf-8')}\n</style>"


def inline_script(m: re.Match, base: Path) -> str:
    src = m.group(1)
    if EXTERNAL.match(src):
        return m.group(0)
    p = (base / src).resolve()
    if not p.exists():
        print(f"  WARN  missing js: {src}")
        return m.group(0)
    return f"<script>\n{p.read_text(encoding='utf-8')}\n</script>"


def build(input_html: str, output_html: str | None = None) -> Path:
    src = Path(input_html)
    base = src.parent
    html = src.read_text(encoding="utf-8")

    before = len(html)
    html = re.sub(
        r'<link[^>]*rel=["\']stylesheet["\'][^>]*href=["\']([^"\']+)["\'][^>]*>',
        lambda m: inline_link(m, base), html,
    )
    html = re.sub(
        r'<script[^>]*src=["\']([^"\']+)["\'][^>]*>\s*</script>',
        lambda m: inline_script(m, base), html,
    )

    out = Path(output_html) if output_html else src.with_name(src.stem + ".built.html")
    out.write_text(html, encoding="utf-8")
    print(f"built {out}  ({len(html)/1024:.1f} KB, was {before/1024:.1f} KB)")
    return out


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    build(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
