# Interaction and motion

Add interaction when it helps a reader inspect evidence, compare cases,
follow a mechanism, or explore supported conditions. Static explanations,
annotations, and tooltips are all valid. There is no interaction quota or
ranking that every figure must satisfy.

## Useful operations

- Reveal a node's explanation or a point's exact value.
- Isolate a series or compare two conditions while preserving context.
- Step through a process, with the current state clearly explained.
- Vary a parameter when a stated model or dataset supports the response.

Do not imply empirical or causal knowledge that the source does not supply.
Label hypothetical examples and models; state assumptions and valid ranges.
An operation that changes a conclusion must keep the relevant conditions
and caveats visible. Do not add controls merely to make a page interactive.

## Access and fallback

- The initial view establishes the subject and a meaningful starting state.
  Make the route into a staged explanation visible. Important text and
  values are not available only on hover; support focus/tap or provide
  readable labels, a table, or an adjacent explanation as appropriate.
- Use native buttons, inputs, details, and links where suitable. Keep
  accessible names and selected states synchronized. Preserve keyboard
  access and visible focus.
- A tooltip reports the actual inspected point. Distinguish interpolation
  from observation. Keep it within the viewport and avoid parsing source
  strings as HTML; textContent is often sufficient.
- Theme switching is optional. If provided, verify legibility and data
  distinctions in each theme; preserve a usable default.
- Respect prefers-reduced-motion by suppressing transitions, playback, and
  continuous effects. Keep comparison buttons and other useful operations
  working; reduced motion does not mean reduced functionality.
- For animated explanations, provide a static view or step list retaining
  important states. Content must not depend on an entrance animation firing.

## Finish the chosen interaction

Once an operation helps explain the subject, give it a complete reading
experience rather than stopping when a handler fires:

- Make the affordance and current state clear. A reader should know what
  can be changed, what happened, and how to revisit the relevant comparison.
- Keep the same objects recognizable across states. Synchronize the visual,
  values, formula, explanation, and selected control where they apply.
  Preserve spatial context instead of making the reader relocate everything.
- For a staged process, make sequence and progress intelligible. Provide
  appropriate ways to inspect, pause, revisit, or reset; choose controls
  for the process rather than adding a standard playback bar everywhere.
- Keep responses stable: repeated input, reversing direction, resizing,
  or resetting must not leave stale labels, competing animations, or a
  stranded state. Respect valid parameter ranges and explain boundaries.
- Keep tooltips and detail panels legible, reachable, and dismissible.
  Avoid jitter and overlays that obscure the object being explained.

Polish follows the explanation. Extra geometry changes, motion, and controls
do not improve an operation unless the reader can follow their meaning.

## Check what the page actually does

Exercise its important controls using mouse/touch and keyboard as applicable.
Check values, labels, states, and the explanation after the action. A DOM
change alone does not show that an interaction is meaningful or correct.
Check a complete cycle, including relevant endpoints, repeated or reversed
actions, and reset where offered; confirm the reader can tell what changed
and why. A smooth animation with an incoherent explanation is still unfinished.
Use page-specific assertions when a calculation or state transition warrants
it; no universal hover count or selector convention is required.
