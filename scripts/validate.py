#!/usr/bin/env python3
"""Static HTML checks; no requirements for themes, charts, hover, or motion.

Usage: python3 scripts/validate.py page.html [--standalone]
Only literal HTML references are inspected. CSS/JS-generated dependencies,
rendering, accessibility quality, and factual accuracy require separate review.
Exit 0: no detected structural/resource failures; 1: failures; 2: usage/IO error.
"""
import argparse
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Document(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = Counter()
        self.ids = Counter()
        self.targets = set()
        self.references = []
        self.assets = []
        self.aria = []
        self.title = []
        self.in_title = False
        self.in_head = False
        self.lang = None
        self.base = False
        self.failures = []

    def handle_starttag(self, tag, attrs):
        self.tags[tag] += 1
        names = Counter(k for k, _ in attrs)
        for key, count in names.items():
            if count > 1:
                self.failures.append(f'duplicate {key!r} attribute on <{tag}>')
        a = dict(attrs)
        if a.get('id'):
            self.ids[a['id']] += 1
            self.targets.add(a['id'])
        if tag == 'a' and a.get('name'):
            self.targets.add(a['name'])
        if tag == 'html':
            self.lang = a.get('lang')
        if tag == 'base':
            self.base = True
        if tag == 'head':
            self.in_head = True
        if tag == 'title' and self.in_head:
            self.in_title = True
        for key in ('aria-labelledby', 'aria-describedby'):
            self.aria.extend((a.get(key) or '').split())
        href = a.get('href') or a.get('xlink:href')
        if href and href.startswith('#'):
            self.references.append(unquote(href[1:]))
        if a.get('src'):
            self.assets.append(a['src'])
        if a.get('poster'):
            self.assets.append(a['poster'])
        if tag == 'link' and href and set((a.get('rel') or '').lower().split()) & {
            'stylesheet', 'icon', 'preload', 'modulepreload', 'manifest',
        }:
            self.assets.append(href)
        if tag in ('image', 'use') and href:
            self.assets.append(href)
        if tag == 'object' and a.get('data'):
            self.assets.append(a['data'])

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
        if tag == 'head':
            self.in_head = False

    def handle_data(self, data):
        if self.in_title:
            self.title.append(data)


def check(path: Path, standalone=False):
    doc = Document()
    doc.feed(path.read_text(encoding='utf-8'))
    doc.close()
    failures, warnings = list(doc.failures), []
    for tag in ('html', 'head', 'body'):
        if not doc.tags[tag]:
            failures.append(f'missing explicit <{tag}> element')
    if not ''.join(doc.title).strip():
        failures.append('missing nonempty title')
    if not doc.lang:
        warnings.append('document language is not declared')
    failures.extend(f'duplicate id: {key}' for key, n in doc.ids.items() if n > 1)
    failures.extend(f'missing fragment target: #{key}'
                    for key in sorted(set(doc.references) - doc.targets) if key)
    failures.extend(f'missing ARIA reference: {key}'
                    for key in sorted(set(doc.aria) - set(doc.ids)))
    if doc.base:
        warnings.append('<base> present: resource paths require browser review')
    for ref in sorted(set(doc.assets)):
        parts = urlsplit(ref)
        if ref.startswith('#') or parts.scheme == 'data':
            continue
        if standalone:
            failures.append(f'non-inlined asset: {ref}')
        elif parts.scheme or parts.netloc:
            warnings.append(f'external/runtime asset: {ref}')
        elif not doc.base:
            if parts.path.startswith('/'):
                warnings.append(f'server-root asset requires HTTP review: {ref}')
            elif parts.path and not (path.parent / unquote(parts.path)).is_file():
                failures.append(f'missing local asset: {ref}')
    return failures, warnings


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('page', type=Path)
    ap.add_argument('--standalone', action='store_true',
                    help='reject literal non-inlined HTML asset references (source links allowed)')
    args = ap.parse_args()
    try:
        failures, warnings = check(args.page, args.standalone)
    except (OSError, UnicodeError, ValueError) as exc:
        ap.exit(2, f'validate: {exc}\n')
    print(f'validate {args.page.name}')
    for message in warnings:
        print(f'  WARN  {message}')
    for message in failures:
        print(f'  FAIL  {message}')
    print('static checks: ' + ('FAIL' if failures else 'PASS') +
          ' — rendering, dynamic dependencies, and evidence need separate review')
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
