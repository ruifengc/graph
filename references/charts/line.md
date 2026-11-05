# Lines

Useful for measured change along an ordered, often temporal, axis.

- Equal temporal distance represents equal elapsed time. Map full dates
  rather than integer years when several samples occur in a year.
- Declare sampling, aggregation, and log scales. Choose scale for the
  comparison; a particular max/min ratio does not automatically require log.
- Distinguish observations from fitted or interpolated values. Do not
  smooth a path in a way that implies unobserved peaks or measurements.
- Anchor annotations to actual observations. If sampling omits a pivotal
  extreme, include or separately identify the real point instead of
  attaching its value to a nearby sample.
- Keep annotations within the viewBox and away from neighboring points.
  Mid-year series endings can put centered year ticks beyond the plot;
  align ticks to actual dates and check the final label.
- If offering inspection, map the pointer into data/SVG coordinates before
  nearest-point lookup. Show the actual observation and date; identify
  interpolation explicitly. Provide readable labels or another accessible
  route to essential values. Hover is optional.
