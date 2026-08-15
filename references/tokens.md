# Design Tokens

The single source of truth for graph's visual language. Values below are
fixed by the style lab iteration (2026-08); do not invent new colors,
fonts, or motion parameters. Every page is assembled from these tokens.

## Theme system

Every output page ships **day and night themes** (toggle in the corner).
The two themes differ only in the color tokens; type, spacing, and motion
are shared.

### Day · Paper (`data-theme="day"`)

Warm paper ground, ink text, orange-red accent. Editorial, quiet.

| Token | Value | Use |
|---|---|---|
| `--bg` | `#F4F3EE` | page background (warm paper) |
| `--ink` | `#1C1C1A` | primary text (near-black, warm) |
| `--muted` | `#8B8A83` | secondary text, captions, labels |
| `--faint` | `#C9C8C0` | tertiary text, source line, axis labels |
| `--grid` | `#E4E3DB` | hairline dividers, gridlines |
| `--accent` | `#C2502C` | the single emphasis color (vermillion orange) |

### Night · Ink (`data-theme="night"`)

Near-black ground, cream text, gold accent. Still, theatrical.

| Token | Value | Use |
|---|---|---|
| `--bg` | `#151515` | page background |
| `--ink` | `#EDEDEA` | primary text (warm cream) |
| `--muted` | `#8E8E8A` | secondary text, captions, labels |
| `--faint` | `#4A4A47` | tertiary text, source line, axis labels |
| `--grid` | `#262626` | hairline dividers, gridlines |
| `--accent` | `#D9A05B` | the single emphasis color (gold) |

### Accent rules

- **One accent per theme.** It marks: the chart line/stroke, the most
  important key number, the takeaway border, the hover dot. Nothing else.
- The author picks the accent for the content *at build time* (day and
  night may keep their own defaults above); it is **never exposed as a
  user-facing control** in the page.
- All other elements stay on the gray ladder — no second color, no
  gradients, no shadows. Contrast and whitespace do the work.

## Type

System font stacks only (no webfont by default; a webfont may be added
only when declared and justified, per SKILL.md rule 3).

```
--serif: Georgia, "Times New Roman", "Songti SC", "SimSun", serif
--sans:  system-ui, -apple-system, "Segoe UI", "PingFang SC",
         "Microsoft YaHei", sans-serif
```

| Role | Stack | Size / weight | Notes |
|---|---|---|---|
| Kicker | sans, 600 | 11px · ls +0.14em | uppercase, muted |
| Section eyebrow | sans, 600 | 11px · ls +0.14em | uppercase, muted; top-left of each section (same voice as kicker) |
| Title | serif, 600 | 44px · ls -0.01em | conclusion, not topic |
| Sub-line | sans, 400 | 15px · lh 1.8 | muted, max-width 560px |
| Key number | serif, 600 | 40px · ls -0.02em | tabular figures |
| Chart title | sans, 700 | 14px | conclusion sentence |
| Chart caption | sans, 400 | 11.5px | muted: unit · scale · period |
| Takeaway | serif, 400 | 17px · lh 1.8 | left border 2px accent |
| Source line | sans, 500 | 10px · ls +0.1em | uppercase, faint |
| Hover tooltip | sans, 700 | 11.5px | tabular figures |

Sizes are minimums for readability; never shrink to fit — restructure.

## Spacing & layout

| Token | Value | Use |
|---|---|---|
| Page width | 880px max | centered, `padding: 0 20px 120px` |
| Section rhythm | 44–64px | between kicker/title/stats/chart blocks |
| Block separator | 1px `--grid` hairline | above stats, above chart block |
| Key-number row | 3-col grid, 28px gap | 2–4 numbers |
| Chart block gap | 32px top padding | after hairline |

No cards, no borders around content, no shadows — whitespace and hairlines
separate. One visual motif per page.

## Motion

| Effect | Params | When |
|---|---|---|
| Draw-in (line/path) | 2.4s · `cubic-bezier(.4,0,.15,1)` · once | chart enters viewport |
| Count-up (numbers) | 900ms · cubic-out (1−(1−p)³) | key numbers enter viewport |
| Theme switch | 0.35s ease (bg/color) | toggle clicked |
| Tooltip | 0.15s ease, 3px rise | hover |

Rules: effects play once, on enter-viewport (IntersectionObserver),
never loop, never decorate. `prefers-reduced-motion` disables draw-in and
count-up entirely (CSS `@media` + JS check).

## Shapes

| Element | Shape |
|---|---|
| Theme toggle | pill, 999px radius, 1px grid border; active = `--ink` bg, `--bg` text |
| Hover dot | r 3.5, `--accent` fill, `--bg` stroke 1.5 |
| Annotation dot | r 3.2, `--bg` fill, `--accent` stroke 1.4 |
| Chart gridlines | 1px `--grid`, hairline only (max 3–4 per chart) |
| Tooltip | 5px radius, `--ink` bg, `--bg` text, 5×10px padding |

## Reference CSS skeleton

```css
body[data-theme="day"]{ --bg:#F4F3EE; --ink:#1C1C1A; --muted:#8B8A83;
  --faint:#C9C8C0; --grid:#E4E3DB; --accent:#C2502C; }
body[data-theme="night"]{ --bg:#151515; --ink:#EDEDEA; --muted:#8E8E8A;
  --faint:#4A4A47; --grid:#262626; --accent:#D9A05B; }
body{ background:var(--bg); color:var(--ink);
  font-family:var(--sans); transition:background-color .35s,color .35s; }
```

## Do / Don't

- Do keep every color on the ladder or the accent.
- Do use the hairline separator instead of borders/shadows.
- Don't add a second accent, a gradient, a glow, or a card wall.
- Don't change a token's value in a page — change it here first, then
  regenerate (and re-check `examples/`).
