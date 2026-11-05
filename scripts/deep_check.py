#!/usr/bin/env python3
"""Literal number/quotation review hints, NOT semantic or provenance validation.

Usage: python3 scripts/deep_check.py page.html input.md [--sources FILE]
       [--phrases comma,separated] [--ignore REGEX] [--json]
Matching cannot verify a number's subject, unit, period, or derivation.
Includes static SVG text and data-count values; excludes scripts/styles.
Exit 0: scan completed (hints may remain); 1: explicit --phrases missing;
2: input/usage error. No exit code certifies factual accuracy.
"""
import argparse
from collections import Counter
from decimal import Decimal
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import unicodedata

# Group thousands without treating a comma-separated list as one number.
NUMBER = re.compile(r'(?<![\d.])[+−-]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?![\d.])')


class Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.counts = []
        self.quotes = []
        self.skip = 0
        self.quote_stack = []

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style', 'template', 'head'):
            self.skip += 1
        if self.skip:
            return
        a = dict(attrs)
        if a.get('data-count'):
            self.counts.append(a['data-count'])
        if tag in ('q', 'blockquote'):
            self.quote_stack.append([])

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'template', 'head'):
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            return
        if tag in ('q', 'blockquote') and self.quote_stack:
            self.quotes.append(' '.join(self.quote_stack.pop()).strip())
        if tag in ('p', 'div', 'li', 'text', 'td', 'th', 'figcaption', 'br'):
            self.parts.append('\n')

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)
            for quote in self.quote_stack:
                quote.append(data)


def numeric_tokens(text):
    return [format(Decimal(m.group().replace(',', '').replace('−', '-')).normalize(), 'f')
            for m in NUMBER.finditer(unicodedata.normalize('NFKC', text))]


def normalize(text):
    return re.sub(r'\s+', '', unicodedata.normalize('NFKC', text)).casefold()


def scan(output, source, supplement='', ignore=''):
    page = Text()
    page.feed(output)
    page.close()
    text = ''.join(page.parts)
    original, added = set(numeric_tokens(source)), set(numeric_tokens(supplement))
    ignore_re = re.compile(ignore) if ignore else None
    numbers = []
    for token, count in Counter(numeric_tokens(text + ' ' + ' '.join(page.counts))).items():
        if ignore_re and ignore_re.fullmatch(token):
            continue
        match = 'input' if token in original else 'supplement' if token in added else 'none'
        numbers.append({'number': token, 'occurrences': count, 'literal_match': match})
    return {
        'numbers': numbers,
        'quotes_to_review': [q for q in page.quotes if normalize(q) and
                             normalize(q) not in normalize(source + '\n' + supplement)],
        'text': text,
        'limitation': 'Literal matches do not verify attribution, units, conditions, or truth. '
                      'Nonmatches may be valid calculations, axis ticks, or translations. '
                      'Dynamic JS/canvas text and Chinese number words are not audited.',
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('output', type=Path)
    ap.add_argument('input', type=Path)
    ap.add_argument('--sources', type=Path)
    ap.add_argument('--phrases', default='')
    ap.add_argument('--ignore', default='', help='regex on normalized numeric tokens')
    ap.add_argument('--json', action='store_true')
    args = ap.parse_args()
    try:
        source_path = args.sources or args.input.parent / 'sources.md'
        supplement = source_path.read_text(encoding='utf-8') if source_path.is_file() else ''
        if args.sources and not source_path.is_file():
            raise FileNotFoundError(source_path)
        # URL ids are not candidate numeric evidence.
        supplement = re.sub(r'https?://\S+', ' ', supplement)
        report = scan(args.output.read_text(encoding='utf-8'),
                      args.input.read_text(encoding='utf-8'), supplement, args.ignore)
    except (OSError, UnicodeError, ValueError, re.error) as exc:
        ap.exit(2, f'deep_check: {exc}\n')
    report['missing_phrases'] = [p.strip() for p in args.phrases.split(',')
                                 if p.strip() and normalize(p.strip()) not in normalize(report['text'])]
    del report['text']
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print('Literal review scan — no factual or semantic verdict')
        for item in report['numbers']:
            print(f"  {item['number']}: literal match={item['literal_match']} "
                  f"({item['occurrences']} occurrence(s))")
        for quote in report['quotes_to_review']:
            print(f'  REVIEW quote wording/translation: {quote[:160]}')
        for phrase in report['missing_phrases']:
            print(f'  FAIL explicit phrase missing: {phrase}')
        print(report['limitation'])
    return 1 if report['missing_phrases'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
