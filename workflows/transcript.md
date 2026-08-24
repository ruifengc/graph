# Workflow · Transcript

Inherits: base (read `base.md` first — only the differences below).

## When to use

A video / talk / podcast transcript (plain text or subtitle export).

## Special processing steps

1. **Transcribe-first reality:** spoken content is redundant; the
   extraction step is heavier — find the argument buried in
   digressions, repetition, fillers. The page is the talk's skeleton,
   not its transcript.
2. **Strip SRT timestamps before composing** (index lines + `-->`
   ranges) into plain text — one line per subtitle block, keep order.
3. **ASR / hearing-error handling** (validated in practice):
   - Fix obvious hearing errors by context, and say so in the footer;
     the page uses the corrected form, the footer admits the
     correction.
   - Never guess an entity you can't resolve — drop it, no
     placeholders.
   - Numbers are quoted as spoken, sanity-checked against context;
     flag assumptions in the figcaption.
   - **Internal contradictions** (the same talk says "三年半来首次
     加息" and "2024年1月以来首次加息"): use the verifiable statement,
     drop the other, record the drop in scope + notes. Never pick
     arbitrarily.
   - **Unrecoverable segments are dropped whole** — when an entire
     dialogue block is garbled past recovery, drop the WHOLE segment,
     declare it in the page footnote, never reprint the fragments.
   - Unverifiable quotes are not printed verbatim — keep the concept,
     drop the wording.

## Special glyph tendencies

- **Quotes are the evidence** — key numbers keep their quote or slide
  reference (tooltip carries the original wording).
- Timeline glyph fits well (the talk's own structure can become the
  page's sections).

## Special honesty discipline

- Tone is preserved, volume is not: the page keeps the speaker's voice
  in titles/takeaways, not every aside.
- The source line names the talk (title, speaker, channel, date, URL).

## Recorded gaps

See runtime notes of transcript runs (ASR noise patterns, drama
recaps, talk analyses).
