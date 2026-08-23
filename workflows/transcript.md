# Workflow · Transcript

Input: a video/talk/podcast transcript (plain text or subtitle export).

Same eight-step pipeline as `article.md` — the differences:

1. **Transcribe-first reality:** spoken content is redundant. The
   extraction step is heavier: find the argument buried in digressions,
   repetition, and fillers. The page is the talk's *skeleton*, not its
   transcript.
2. **Quotes are the evidence.** Direct quotes carry the talk's authority;
   each key number keeps its quote or slide reference.
3. **Timeline glyph fits well** — the talk's own structure (chapters,
   examples) can become the page's sections.
4. **Tone is preserved, volume is not.** The page keeps the speaker's
   voice in titles/takeaways; it does not keep every aside.
5. **The source line names the talk** (title, speaker, channel, date,
   URL) — not just "video transcript".

## ASR / hearing-error handling (validated in investment run, 2026-08)

Auto-transcripts are noisy. Rules that held in practice:

- **Fix obvious hearing errors by context**, and say so in the footer
  (e.g. a mis-transcribed proper noun corrected to its canonical form).
  The page uses the corrected form; the footer admits the correction
  happened.
- **Never guess an entity you can't resolve.** If a spoken name can't
  be mapped to anything confirmable, drop it — don't put a placeholder
  name on the page.
- **Numbers are quoted as spoken**, but sanity-check them against
  context; flag assumptions in the figcaption ("28–29 取 28").
- Spoken redundancy (fillers, restarts, repetitions) is removed in
  extraction — the page is the talk's skeleton, not its transcript.

Framework status: validated by one real run (investment share video);
record new noise patterns in runtime notes.

Framework status: first version. Will be enriched by real transcript
runs — record gaps in runtime notes.
