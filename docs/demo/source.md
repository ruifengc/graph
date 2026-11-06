# Inside Graph: source and teaching model

This is an original teaching example created for Graph. The place, routes, schedules and journey times below are fictional. They are not travel advice or measured results.

## What the page explains

The design principles come from the repository's `SKILL.md`:

- Understand the content, genre and audience before choosing a structure.
- Explain important relationships through text, graphics and useful operations.
- When differences between conditions matter, compare around a shared reference and keep graphics, values and explanations consistent.
- Do not add controls when a static comparison is sufficient.
- Distinguish source claims, explanations and teaching assumptions.
- Automated checks assist review; they do not establish factual accuracy or interaction correctness.

Source: https://github.com/ruifengc/graph/blob/81cc96f392087231e7a26016ad1703248f0c660b/SKILL.md

The summary, comparison and exploration views are examples chosen for this page, not a prescribed Graph layout or mandatory workflow. This page is an authored demonstration, not an unedited generation or an evaluation of model performance.

## Fictional source note

You need to cross a river. All routes begin at the same origin and finish at the same destination.

- Ferry: leaves at 08:00 and every 20 minutes thereafter. The crossing takes 8 minutes.
- Footbridge: a 16-minute walk. You can start immediately.
- Tram: leaves at 08:00 and every 10 minutes thereafter. The ride and final walk take 10 minutes in total (6 minutes riding, then 4 minutes walking).

## Teaching assumptions

- Arrival time at the origin is varied from 08:00 to 08:19 in whole minutes.
- You can board at the exact departure minute. There is no boarding cutoff.
- All quoted durations are exact and fixed, all routes are available, and capacity is unlimited.
- Waiting, travelling and walking are sequential. Weather, fares, accessibility and personal preferences are outside this model.

## Calculation

For a departure period `p` and arrival minute `m` after 08:00:

`wait = (p - (m % p)) % p`

Ferry total = wait(20, m) + 8.
Footbridge total = 16.
Tram total = wait(10, m) + 6 + 4.

The recommendation selects the smallest total. Equal totals are displayed as a tie. Timeline bars have one fixed scale from 0 to 30 minutes.

The static comparison uses 08:03 throughout. The exploration view starts there and allows the reader to change arrival time. The summary lists the source facts but makes no route recommendation.
