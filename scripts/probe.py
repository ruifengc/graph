#!/usr/bin/env python3
"""Optional browser smoke check; no prescribed design, controls, or chart types.

Usage: python3 scripts/probe.py page.html [--json]
Requires Playwright or Patchright plus an installed Chromium. Checks desktop,
mobile, and reduced-motion loading, scrolling, overflow, and runtime errors.
Does not exercise page-specific controls or certify content/accessibility.
Exit 0: no observed smoke failures; 1: failures; 2: unavailable browser/IO error.
"""
import argparse
import importlib
import json
from pathlib import Path


SNAPSHOT = r"""() => {
  const root = document.documentElement;
  return {
    scrollHeight: root.scrollHeight,
    overflow: root.scrollWidth > innerWidth + 2,
    text: (document.body?.innerText || '').trim().length,
    visuals: document.querySelectorAll('svg, canvas, img, video, iframe').length,
    brokenImages: [...document.images].filter(i => i.currentSrc &&
      i.complete && i.naturalWidth === 0).map(i => i.currentSrc)
  };
}"""


def browser_api():
    for name in ('playwright.sync_api', 'patchright.sync_api'):
        try:
            return importlib.import_module(name)
        except ModuleNotFoundError as exc:
            if exc.name not in {name, name.split('.')[0]}:
                raise
    raise RuntimeError('Playwright/Patchright is unavailable; use an existing browser '
                       'tool or install a browser backend in your chosen environment')


def inspect(browser, url, width, height, reduced=False):
    context = browser.new_context(viewport={'width': width, 'height': height},
                                  reduced_motion='reduce' if reduced else 'no-preference')
    page = context.new_page()
    errors, warnings, snapshots = [], [], []
    page.on('pageerror', lambda exc: errors.append(str(exc)))
    page.on('console', lambda msg: errors.append(msg.text) if msg.type == 'error' else None)
    page.on('requestfailed', lambda req: errors.append(f'request failed: {req.url}')
            if req.failure != 'net::ERR_ABORTED' else None)
    page.on('response', lambda response: errors.append(f'HTTP {response.status}: {response.url}')
            if response.status >= 400 else None)
    try:
        # Patchright can leave Runtime disabled, suppressing pageerror/console
        # callbacks. Observe Chromium's runtime directly for this local audit.
        runtime = context.new_cdp_session(page)
        runtime.on('Runtime.exceptionThrown', lambda event: errors.append(
            event['exceptionDetails'].get('exception', {}).get('description')
            or event['exceptionDetails'].get('text', 'Uncaught exception')))
        runtime.on('Runtime.consoleAPICalled', lambda event: errors.append(
            'console.error: ' + ' '.join(str(arg.get('value', arg.get('description', '')))
                                        for arg in event.get('args', [])))
            if event.get('type') == 'error' else None)
        runtime.send('Runtime.enable')
        page.goto(url, wait_until='load', timeout=20000)
        page.wait_for_timeout(250)
        first = page.evaluate(SNAPSHOT)
        # Bounded sampling, including the bottom; tall content is reported, not penalized.
        travel = max(0, first['scrollHeight'] - height)
        for fraction in (0, .2, .4, .6, .8, 1):
            page.evaluate('y => window.scrollTo(0, y)', int(travel * fraction))
            page.wait_for_timeout(100)
            snapshots.append(page.evaluate(SNAPSHOT))
        if any(s['overflow'] for s in snapshots):
            errors.append('document overflows horizontally (check local scrolling/reflow)')
        if not first['text'] and not first['visuals']:
            errors.append('page has no readable text or visual elements')
        images = sorted({src for s in snapshots for src in s['brokenImages']})
        errors.extend(f'broken image: {src}' for src in images)
        warnings.append('controls, hover/focus behavior, and state correctness require page-specific review')
        return {'viewport': [width, height], 'reduced_motion': reduced,
                'failures': sorted(set(errors)), 'warnings': sorted(set(warnings))}
    finally:
        context.close()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('page', help='local HTML file or HTTP(S) preview URL')
    ap.add_argument('--json', action='store_true')
    args = ap.parse_args()
    try:
        if args.page.startswith(('http://', 'https://')):
            url = args.page
        else:
            path = Path(args.page).resolve(strict=True)
            if not path.is_file():
                raise ValueError(f'not a file: {path}')
            url = path.as_uri()
        api = browser_api()
        with api.sync_playwright() as driver:
            browser = driver.chromium.launch()
            try:
                results = [inspect(browser, url, 1440, 900),
                           inspect(browser, url, 390, 844),
                           inspect(browser, url, 390, 844, reduced=True)]
            finally:
                browser.close()
    except Exception as exc:
        ap.exit(2, f'probe unavailable or incomplete: {exc}\n')
    if args.json:
        print(json.dumps({'smoke_checks': results}, ensure_ascii=False, indent=2))
    else:
        for result in results:
            print(f"probe {result['viewport']} reduced-motion={result['reduced_motion']}")
            for message in result['failures']:
                print(f'  FAIL  {message}')
            for message in result['warnings']:
                print(f'  NOTE  {message}')
        print('Browser smoke checks only; no content or interaction verdict')
    return int(any(r['failures'] for r in results))


if __name__ == '__main__':
    raise SystemExit(main())
