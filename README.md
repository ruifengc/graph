# graph

**English** · [中文](README.zh-CN.md)

Turn one piece of content — an article, a research report, a paper, a
news digest, a video transcript, or a dataset — into a single-file
interactive HTML page that *explains it visually*.

The page is a tour guide, not a document: hand-written SVG charts carry
the argument, short lines of text add the punchlines, and interaction
(hover-to-read, day/night themes) serves readers who want to dig in.

## What you get

- **One self-contained HTML file** — all CSS, JS, SVG, and data
  inlined. Double-click to open, send it to a friend, drop it on a USB
  stick. No framework, no CDN, no build step for the reader.
- **Day/night themes** — Paper (warm gray + vermillion) and Ink
  (near-black + gold), toggle in the corner.
- **Hand-written SVG charts** — no chart library. The visual language
  is defined by the skill's design tokens, not by ECharts or d3.
- **Two interactions only** — hover-to-read (exact value at the nearest
  data point) and theme toggle. Restraint is the aesthetic.
- **Honest by construction** — every number traces to the input or a
  cited source; log axes, sampling, rounding, and assumptions are
  declared in the captions; the source line is mandatory.

## Usage

graph is an Agent Skills style skill — `SKILL.md` is the entry point.
Install it into your agent's skill directory (Claude Code, Codex,
Hermes, or any skill-aware agent), then ask it to visualize a piece of
content:

```
Turn this article into a page: <paste article>
Visualize this data: <dataset>
Explain this paper as an HTML page: <arxiv link or PDF text>
```

The agent reads `SKILL.md` and follows the eight-step pipeline:
understand → extract → narrative → glyph selection → assembly →
build+validate → archive → optional LAN sharing.

## Repository layout

```
SKILL.md          entry point: pipeline, rules, division of labor
scripts/          build.py (multi-file → single HTML), validate.py (self-check),
                  serve.py (LAN sharing of a built page)
references/       design tokens, narrative structure, interactions, glyph library
workflows/        per-input-type processing flows (article / paper / data / news / transcript)
```

## Design philosophy

**Style is law, execution is free.** The skill fixes the style system
(colors, type, spacing, motion, honesty rules, technical pitfalls) and
the information (what the input means, what must not happen) — but
never the specific drawing. The composing agent has full creative
freedom within those bounds, which is what keeps every page alive
instead of templated.

The skill evolves from real runs: feedback from actual pages flows back
into the references, so the knowledge grows with use.

## License

MIT © 2026 ruifengchen
