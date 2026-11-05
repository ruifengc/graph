"""Regressions for artifact checks and the limits of literal review."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


validator = load('validate')
review = load('deep_check')


def document(body, head='<title>Example</title>'):
    return f'<!doctype html><html lang="en"><head>{head}</head><body>{body}</body></html>'


class StaticChecks(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'page.html'

    def check(self, html, standalone=False):
        self.path.write_text(html)
        return validator.check(self.path, standalone)

    def test_static_explainer_needs_no_theme_hover_or_motion(self):
        failures, _ = self.check(document('<h1>Mechanism</h1><p>A readable explanation.</p>'))
        self.assertEqual(failures, [])

    def test_multi_file_delivery_accepts_existing_assets(self):
        (self.path.parent / 'style.css').write_text('body { color: black; }')
        failures, _ = self.check(document('<p>Text</p>',
                                         "<title>Page</title><link href='style.css' rel='stylesheet'>"))
        self.assertEqual(failures, [])

    def test_missing_resource_detected_with_single_quotes(self):
        failures, _ = self.check(document("<script src='missing.js'></script>"))
        self.assertTrue(any('missing local asset' in f for f in failures))

    def test_standalone_allows_source_links_and_data_images(self):
        failures, _ = self.check(document(
            '<a href="https://example.org/paper#table-2">Source</a>'
            '<img src="data:image/svg+xml;base64,PHN2Zy8+" alt="Diagram">'), True)
        self.assertEqual(failures, [])

    def test_standalone_rejects_external_and_local_assets(self):
        for src in ('https://example.org/library.js', 'local.js'):
            with self.subTest(src=src):
                failures, _ = self.check(document(f'<script src="{src}"></script>'), True)
                self.assertTrue(any('non-inlined asset' in f for f in failures))

    def test_duplicate_ids_and_attributes_detected(self):
        failures, _ = self.check(document("<p id='x' class='a' class='b'>A</p><p id='x'>B</p>"))
        self.assertTrue(any('duplicate id' in f for f in failures))
        self.assertTrue(any('duplicate' in f and 'attribute' in f for f in failures))

    def test_anchors_and_aria_references_resolve(self):
        body = '<a href="#t%3A30">00:30</a><p id="t:30">Demonstration</p>'
        body += '<svg aria-labelledby="fig-title"><title id="fig-title">Method</title></svg>'
        failures, _ = self.check(document(body))
        self.assertEqual(failures, [])

    def test_broken_fragment_and_aria_detected(self):
        failures, _ = self.check(document('<a href="#missing">Go</a><svg aria-labelledby="lost"></svg>'))
        self.assertTrue(any('fragment' in f for f in failures))
        self.assertTrue(any('ARIA' in f for f in failures))

    def test_svg_title_does_not_replace_document_title(self):
        failures, _ = self.check(document('<svg><title>Only figure title</title></svg>', head=''))
        self.assertTrue(any('title' in f for f in failures))


class LiteralReview(unittest.TestCase):
    def test_svg_and_small_integers_are_included(self):
        report = review.scan('<p>共99个样本</p><svg><text>9999万元</text></svg>', '共12个样本，收入1200万元')
        self.assertEqual({n['number'] for n in report['numbers']}, {'99', '9999'})
        self.assertTrue(all(n['literal_match'] == 'none' for n in report['numbers']))

    def test_numeric_tokens_do_not_match_substrings(self):
        report = review.scan('<p>200</p>', '收入1200万元')
        self.assertEqual(report['numbers'][0]['literal_match'], 'none')

    def test_matching_number_cannot_establish_attribution(self):
        report = review.scan('<p>B收入1200万元</p>', 'A收入1200万元，B收入300万元')
        self.assertEqual(report['numbers'][0]['literal_match'], 'input')
        self.assertIn('do not verify attribution', report['limitation'])
        self.assertNotIn('pass', report)

    def test_formatting_and_signs(self):
        report = review.scan('<p>1,200 −4.5 0.10</p>', '1200 -4.5 0.1')
        self.assertTrue(all(n['literal_match'] == 'input' for n in report['numbers']))

    def test_css_js_and_geometry_are_not_read_as_claims(self):
        report = review.scan('<style>p {width:777px}</style><script>const x=888;</script>'
                             '<svg width="999"><text>12</text></svg>', '12')
        self.assertEqual([n['number'] for n in report['numbers']], ['12'])

    def test_supplements_remain_distinct(self):
        report = review.scan('<p>12 34</p>', '12', '34')
        self.assertEqual([n['literal_match'] for n in report['numbers']], ['input', 'supplement'])

    def test_quotes_are_review_hints(self):
        report = review.scan('<blockquote>A translated quotation.</blockquote>', '另一种语言的引语')
        self.assertEqual(report['quotes_to_review'], ['A translated quotation.'])

    def test_count_up_values_are_reviewed_without_requiring_animation(self):
        report = review.scan('<b data-count="99">0</b>', '12')
        self.assertIn('99', {n['number'] for n in report['numbers']})


class CommandBehavior(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.page = self.directory / 'page.html'
        self.source = self.directory / 'input.md'
        self.source.write_text('A收入1200万元。')

    def run_script(self, name, *args):
        return subprocess.run([sys.executable, str(ROOT / 'scripts' / name), *map(str, args)],
                              capture_output=True, text=True)

    def test_correct_conversion_is_not_a_factual_failure(self):
        self.page.write_text(document('<p>A收入0.12亿元。</p>'))
        result = self.run_script('deep_check.py', self.page, self.source)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('0.12', result.stdout)
        self.assertNotIn('PASS', result.stdout)

    def test_explicit_phrase_contract_can_fail(self):
        self.page.write_text(document('<p>Selected findings.</p>'))
        result = self.run_script('deep_check.py', self.page, self.source, '--phrases', 'limitations', '--json')
        self.assertEqual(result.returncode, 1)
        self.assertEqual(json.loads(result.stdout)['missing_phrases'], ['limitations'])

    def test_missing_input_is_an_io_error(self):
        result = self.run_script('deep_check.py', self.page, self.source)
        self.assertEqual(result.returncode, 2)
        self.assertNotIn('Traceback', result.stderr)

    def test_source_supplement_and_url_ids(self):
        self.page.write_text(document('<p>34 9999</p>'))
        (self.directory / 'sources.md').write_text('34 units: https://example.org/9999')
        result = self.run_script('deep_check.py', self.page, self.source, '--json')
        report = json.loads(result.stdout)
        self.assertEqual([n['literal_match'] for n in report['numbers']], ['supplement', 'none'])

    def test_ordinary_static_delivery_passes_cli(self):
        self.page.write_text(document('<h1>Question</h1><p>Explanation</p>'))
        result = self.run_script('validate.py', self.page, '--standalone')
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)

    def test_explicit_missing_supplement_is_not_ignored(self):
        self.page.write_text(document('<p>Text</p>'))
        result = self.run_script('deep_check.py', self.page, self.source,
                                 '--sources', self.directory / 'absent.md')
        self.assertEqual(result.returncode, 2)


if __name__ == '__main__':
    unittest.main()
