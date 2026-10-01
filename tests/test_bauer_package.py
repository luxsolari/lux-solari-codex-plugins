"""Offline Bauer package parity and installed-path contract checks."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'plugins/bauer'
SKILL = PACKAGE / 'skills/bauer'
PIN = '213f085dcd316923aab78324c8ea6a3e58713c34'


class BauerPackageTests(unittest.TestCase):
    def test_package_matches_pinned_source_bytes(self):
        path = ROOT / 'docs/bauer-source-parity.json'
        self.assertTrue(path.is_file(), 'pinned source parity inventory missing')
        inventory = json.loads(path.read_text())
        self.assertEqual(inventory['revision'], PIN)
        self.assertEqual(inventory['version'], '0.1.0')
        files = inventory['files']
        self.assertTrue(files)
        actual = {p.relative_to(PACKAGE).as_posix() for p in PACKAGE.rglob('*') if p.is_file()}
        self.assertEqual(actual, set(files))
        for relative, expected in files.items():
            with self.subTest(path=relative):
                self.assertEqual(hashlib.sha256((PACKAGE / relative).read_bytes()).hexdigest(), expected)

    def test_all_documented_helper_and_reference_paths_are_shipped(self):
        documents = list(SKILL.rglob('*.md'))
        self.assertTrue(documents)
        references = set()
        for document in documents:
            text = document.read_text()
            references.update(re.findall(r'(?:scripts|references)/[A-Za-z0-9_.-]+\.(?:py|md|json)', text))
            self.assertNotIn('CLAUDE_PLUGIN_ROOT', text)
            self.assertNotIn('${PLUGIN_ROOT}', text)
        required = {'scripts/dependencies.py', 'scripts/jev.py', 'scripts/report.py', 'scripts/sources.py',
                    'references/advisories.md', 'references/jev.md', 'references/report.md',
                    'references/security-sources.json', 'references/supply-chain.md'}
        self.assertTrue(required.issubset(references), required - references)
        for relative in references:
            self.assertTrue((SKILL / relative).is_file(), relative)

    def test_helpers_run_from_outside_the_package_without_network(self):
        for name in ('dependencies', 'jev', 'report', 'sources'):
            with self.subTest(helper=name):
                run = subprocess.run([sys.executable, str(SKILL / 'scripts' / (name + '.py')), '--help'],
                                     cwd=ROOT.parent, capture_output=True, text=True, timeout=10)
                self.assertEqual(run.returncode, 0, run.stderr)
                self.assertEqual(run.stderr, '')
                self.assertIn('usage:', run.stdout)

    def test_ci_exercises_packaged_bauer_tests_and_parity(self):
        workflow = (ROOT / '.github/workflows/ci.yml').read_text()
        self.assertIn('tests/test_bauer_package.py', workflow)
        self.assertIn('python3 -m unittest discover -s plugins/bauer/tests -v', workflow)


if __name__ == '__main__':
    unittest.main()
