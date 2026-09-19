# Narrative Mechanisms (page-level devices)

Page-level devices that pace a long-form explainer. They sit above the
glyph library: glyphs carry a claim inside one viewBox, these carry the
argument across the page. Every device is hand-written (no external
libraries — IntersectionObserver + CSS are sufficient), token-faithful,
and held to the same honesty contract as every chart.

## 1. Hero argument-visual

The cover earns ONE visual that states the page's central tension —
usually the input's own opening juxtaposition (a weight against a
weight, a before against an after, two scales that refuse to match).

- Forms that work: shared-scale rulers (two values, one scale — length
  IS the argument), isotype contrast (unit counts against a declared
  baseline), a single structural diagram of the system the page will
  dissect.
- It encodes the core claim; it does not decorate. Quantities carried
  by length/count follow the full chart contract (baseline declared,
  caption carries the honesty note, hover applies).
- Static by default: it sits above the fold and never loops. Count-up
  on its labels still applies.
- If the input's opening is not visual, ship no hero visual — a forced
  one reads as a poster, not an argument.

## 2. Sticky chronicle cards

Chronicle form for text-heavy entries: each entry is a two-cell row —
the left cell STICKS (date/place + one-word tag + small marker) while
the right cell's story text scrolls past.

- When: entries carry paragraphs, not one-liners. (The step timeline
  and the horizontal rail carry one-liners; this form carries prose.)
- The sticky cell stays minimal: date, tag, marker. The story lives
  right; quotes and figures inside it follow the normal rules.
- Entries without dates use position labels (01, 02 …) — the sticky
  cell still anchors the reader.
- Scroll alignment: the sticky cell releases as its entry's text ends
  (`align-self: start` inside the row) — never a viewport lock.

## 3. Scrollytelling steps

One sticky figure + N text steps beside it: crossing each step changes
the figure's state — highlight a segment, fill the next unit, reveal
an annotation, advance a counter.

- IO-driven, no libraries: each step div observed (threshold ~0.5);
  entering a step applies that step's state class to the figure;
  scrolling back restores the previous state.
- Every step's state change traces to that step's own text beside it —
  the reader reads a sentence and sees exactly that sentence's geometry.
- The figure must stay readable at EVERY state: no blank figures, no
  state that asserts more than its step text says.
- Reduced motion: collapse to a static stack — the figure shows the
  final state and the steps render as a normal list (annotations from
  all states only where they coexist honestly).
- Native scroll only; never hijack or snap the wheel.

## 4. Click-through detail

Hover surfaces the value; CLICK surfaces the argument — a row, node,
or dot expands inline (or opens a modal) carrying the source sentence /
extra fields that would crowd the chart.

- The trigger is the same element that carries `data-tip`: one target,
  two depths. Prefer inline expansion (keeps reading position); use a
  modal only when the detail is long.
- Expanded content is honest: verbatim source lines, declared derived
  values, nothing padded to make panels even.
- Touch devices have no hover — wherever detail exists, the click layer
  is mandatory.
- `aria-expanded` on the trigger; second click or Escape closes.

## Contract checklist

- [ ] Every device encodes the argument it claims to encode
- [ ] No loops; native scroll; a reduced-motion collapse defined per device
- [ ] All geometry/quantities inside devices follow the chart contract
- [ ] Zero external libraries — IO + CSS only
