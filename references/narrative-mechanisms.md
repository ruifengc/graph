# Optional scroll and state sequences

Use a sequence when order helps explain the subject. A normal flowing page
is a complete solution; a long input does not require motion or changing scenes.

A sticky figure with adjacent steps, an inline sequence, tabs, or a control
can each work. Choose for the material and viewport. There is no fixed
section height, column count, travel distance, or required number of states.

For a sequence that does help:

- Tie each state to its explanation. Preserve orientation and make earlier
  states revisitable; do not require guessing how to reach a key finding.
- Keep native scrolling, keyboard navigation, browser find, and anchor links
  usable. Avoid capturing wheel/touch input to manufacture navigation.
- For sticky layouts, check the container's travel and the actual drawing
  position. States should not change after the relevant figure has left view.
- Avoid empty travel created only to trigger an effect. On narrow or short
  viewports, let content flow when the staged layout stops working.
- Offer a static or stepped alternative to scroll-driven animation under
  reduced motion, retaining all significant information and useful controls.
- Keep decorative layers subordinate to content and distinct from data
  encodings. Avoid needless work while off-screen or in a hidden tab.

Review the rendered sequence across its states. An observer or scroll
handler being present does not establish that the sequence works.
