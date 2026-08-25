# Narrative Structure

The page is a **tour guide, not a document**. It replaces line-by-line
reading: charts carry the argument, text adds punchlines, interaction
serves readers who want to dig in. Every element below has a job; if an
element cannot state its job, cut it.

All concrete style values (sizes, weights, spacing, colors) live in
`references/tokens.md` — this file states WHAT each element is for and
HOW to write it, never its pixels.

## Page anatomy (top to bottom)

```
kicker            provenance + scope, one line
title             the conclusion, in one sentence
sub-line          the tension / question behind the conclusion
key numbers       2–4 numbers that make the case by themselves
chart blocks      one per independent conclusion (title + caption + SVG + takeaway)
source line       where everything came from
```

### 1. Kicker

Provenance and scope, not decoration: what domain, what period, as of
when. No verbs. (Style: tokens.md Type table — Kicker.)

> SECTOR REPORT · DATA AS OF 2026-07-10

### 2. Title — the conclusion, not the topic

A judgment, in one sentence, in the author's voice. If the title could
also headline a Wikipedia article, it is a topic — rewrite it as a claim.

- Topic: "Quarterly Earnings" ✗
- Claim: "Earnings turned, and nobody priced it" ✓

Chinese titles may use the same rule: 结论，不是话题。

### 3. Sub-line — the tension

One or two sentences that state *why the conclusion is worth reading*:
the contradiction, the surprise, the question it answers. (Style:
tokens.md Type table — Sub-line.)

> The headline number rose, but the split tells the real story: the
> growth is not where the market is looking.

### 4. Key numbers

2–4 numbers that carry the argument alone. Each gets a label (what it
measures) and a one-line note (source/period). Numbers animate with
count-up on scroll. The most important number is the accent one.
(Style: tokens.md Type table — Key number.)

**No numbers in the input? Omit the row.** Do not force pseudo-numbers
for the sake of the anatomy (a drama analysis has no numbers — the row
simply disappears, and the page goes straight from sub-line to
sections).

## Page structure (D12 — structure is part of the style)

The page must read as a **structured composition**, not a stack of
blocks. When assembling:

- **Vertical rhythm**: kicker → title → sub → key numbers → sections →
  source. Each step is a clear level; spacing encodes the hierarchy
  (values in tokens.md Spacing).
- **Aligned hierarchy**: section titles at one level, chart captions
  one step below, takeaway one step below that. Related elements share
  an alignment edge; nothing floats arbitrarily.
- **Section eyebrows**: each section carries a small marker in its
  top-left corner — a sequence number and/or a one-word label, in the
  kicker's voice (style: tokens.md Type table — Section eyebrow), e.g.
  `01 · 时间线` or `二 · 关系`. The eyebrow makes the section hierarchy
  readable at a glance; a hairline alone does not separate sections
  (user feedback).

### Charts per section — angles, not counts

A section may carry **several chart blocks**. The constraint is not
how many charts a section holds — it is whether each chart adds a
DIFFERENT angle:

- **Allowed**: the same data viewed from different angles, each with
  its own independent conclusion (a spectrum AND the curve behind it;
  a hierarchy AND the contrast that explains it; a series AND its
  composition). Each block still gets its own figtitle / figcaption /
  takeaway.
- **Forbidden**: the same angle drawn twice — two charts saying the
  same thing collapse into one (SKILL.md rule 6).
- **Multi-chart is permission, not a goal.** If one chart carries the
  angle fully, one chart is the answer. Decide each angle's claim
  first, then let the chart count fall out of it — a thin angle that
  yields only a line and a few labels should merge into a richer
  chart, not spawn one of its own.
- When a section holds multiple blocks, keep the hierarchy readable:
  number them (`01a / 01b`), share a sub-eyebrow, or let the figtitles
  carry the angle distinction. Split the section only when the charts
  belong to different arguments.

### Long-page enhancements (optional, pages with >6 sections)

Short pages need none of this. Long pages (a deep dive, a full
chronicle) earn three structural aids:

- **Sticky section titles**: the current section's title stays pinned
  to the top of the viewport while its charts scroll past — the reader
  always knows which chapter they are inside. Pure CSS (`position:
  sticky`).
- **Section navigation**: a slim fixed rail on the side listing the
  sections; the active one is highlighted as you scroll (scrollspy via
  IntersectionObserver). For pages long enough that jumping matters.
- **Big-information components**: a horizontal chronicle rail (see
  `charts/timeline.md` chronicle mode) or a full comparison matrix
  belong to long pages — they exist because the content is big, not
  for their own sake.
- **Charts are compositions**: axis, labels, annotations, and caption
  form one readable object. A chart whose elements read as scattered
  fragments (e.g. dots pinned to a baseline) is not finished — see
  `charts/timeline.md` constraints.
- **Fit over variety, but notice repetition.** Choose each chart for
  what fits its conclusion — there is no quota of skeleton types per
  page. But when two adjacent sections end up on the same skeleton
  (node+arrow maps, stacked bars, columns...), stop and ask: does this
  section *really* need this skeleton, or was it the path of least
  resistance? If a different shape fits equally well (a lane diagram
  instead of a branch tree, a mirror instead of arrows), use it —
  variety is the byproduct of honest fit, not a target.

### 5. Chart blocks

Each chart block = one independent conclusion:

```
figtitle    conclusion sentence (not "Line chart of X")
figcaption  unit · scale · period · sample rate · any data honesty notes
SVG         the chart itself
takeaway    the reading: what the eye should take from this chart
```

- **figtitle is a claim** like the page title. "From 10843 to 307" beats
  "monthly average". (Style: tokens.md Type table — Chart title.)
- **figcaption carries the honesty load**: unit, log scale if used,
  sampling, missing data, rounding ("rounding ate 2 people"). If a chart
  needs no honesty notes, it still gets unit + period. (Style: tokens.md
  Type table — Chart caption.)
- **takeaway is the one-liner reading** (style: tokens.md Type table —
  Takeaway): what this chart changes about the reader's picture.

Chart count follows the content: a long, evidence-rich input earns more
charts; two charts making the same point collapse into one (rule 6).

### 6. Source line

Every chart's provenance, and the page's aggregate source. Each source
is name + date + (URL if public). No source line = unfinished page
(SKILL.md rule 1). (Style: tokens.md Type table — Source line.)

## Voice rules

- **Say it like a person.** No "it can be observed that". The title,
  takeaway, and notes read like a smart friend explaining.
- **Numbers are the evidence, not the subject.** Sentences lead with the
  judgment; numbers support it.
- **Never fill space.** A paragraph that does not change the reader's
  understanding is deleted.
- **Chinese or English** follows the input language, never mixed in one
  page.

## Anti-patterns

| Instead of | Do |
|---|---|
| Topic title ("Revenue by plan") | Claim title ("Where we gained, where we bled") |
| Chart with no caption | Caption with unit + period + honesty notes |
| A chart that repeats the previous one | Keep one, cut the other |
| Two charts, same angle | Two angles, or one chart |
| Decorative animation | No animation, or a once-only draw-in |
| "Data visualization" as the goal | "This conclusion, proven by data" |
