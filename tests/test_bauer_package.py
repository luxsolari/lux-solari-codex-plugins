"""Offline Bauer package parity and installed-path contract checks."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'plugins/bauer'
SKILL = PACKAGE / 'skills/bauer'
PIN = '69c870e3bc5cfedc204899c9ad08feaef8f7e5d8'


class BauerPackageTests(unittest.TestCase):
    def test_package_matches_pinned_source_bytes(self):
        path = ROOT / 'docs/bauer-source-parity.json'
        self.assertTrue(path.is_file(), 'pinned source parity inventory missing')
        inventory = json.loads(path.read_text())
        self.assertEqual(inventory['revision'], PIN)
        self.assertEqual(inventory['version'], '0.2.0')
        self.assertEqual(len(inventory['files']), 26)
        readme = (PACKAGE / 'README.md').read_text()
        for expected in ('For persistent terminal setup', '~/.zshrc', '~/.bashrc',
                         'shell_environment_policy', '### Secret-manager example: 1Password',
                         "TYPESAFE_API_KEY='op://Private/TypeSafe/api_key' op run -- claude",
                         'claude-jev()', 'Bauer does not resolve secret-manager references',
                         'no live vault retrieval was exercised',
                         'A configured key does not grant that approval'):
            with self.subTest(documented_setup=expected):
                self.assertIn(expected, readme)
        self.assertNotIn('read -r -s TYPESAFE_API_KEY', readme)
        for host in ('claude', 'codex'):
            manifest = json.loads((PACKAGE / ('.' + host + '-plugin/plugin.json')).read_text())
            self.assertEqual(manifest['version'], inventory['version'])
            self.assertEqual(manifest['description'],
                             'Evidence-backed security audits with optional Jev review.')
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
        required = {'scripts/dependencies.py', 'scripts/jev.py', 'scripts/report.py', 'scripts/sources.py', 'scripts/selection.py', 'scripts/completion.py',
                    'references/advisories.md', 'references/jev.md', 'references/report.md',
                    'references/security-sources.json', 'references/supply-chain.md'}
        self.assertTrue((required - {'scripts/completion.py'}).issubset(references), required - references)
        self.assertTrue((SKILL / 'scripts/completion.py').is_file())
        self.assertIn('completion_checks', (SKILL / 'references/report.md').read_text())
        self.assertIn('completion_scope', (SKILL / 'references/report.md').read_text())
        for relative in references:
            self.assertTrue((SKILL / relative).is_file(), relative)

    def test_helpers_run_from_outside_the_package_without_network(self):
        for name in ('dependencies', 'jev', 'report', 'sources', 'selection'):
            with self.subTest(helper=name):
                run = subprocess.run([sys.executable, str(SKILL / 'scripts' / (name + '.py')), '--help'],
                                     cwd=ROOT.parent, capture_output=True, text=True, timeout=10)
                self.assertEqual(run.returncode, 0, run.stderr)
                self.assertEqual(run.stderr, '')
                self.assertIn('usage:', run.stdout)

        fixture = dict(scope='synthetic package contract', sources=[], coverage=[],
                       limitations=['Synthetic only; no queries'], findings=[])
        with tempfile.TemporaryDirectory() as folder:
            evidence = Path(folder) / 'evidence.json'
            evidence.write_text(json.dumps(fixture))
            for fmt in ('json', 'markdown'):
                run = subprocess.run([sys.executable, str(SKILL / 'scripts/report.py'), str(evidence), '--format', fmt],
                                     capture_output=True, text=True, timeout=10)
                self.assertEqual(run.returncode, 0, run.stderr)
                if fmt == 'json':
                    gate = json.loads(run.stdout)['completion_gate']
                    self.assertEqual(gate['status'], 'partial')
                    self.assertEqual(len(gate['obligations']), 15)
                    self.assertTrue(all(row['status'] == 'unattempted' for row in gate['obligations']))
                else:
                    self.assertIn('Overall: partial', run.stdout)
                    self.assertIn('dependency&#95;coverage', run.stdout)


    def test_ci_exercises_packaged_bauer_tests_and_parity(self):
        workflow = (ROOT / '.github/workflows/ci.yml').read_text()
        self.assertIn('tests/test_bauer_package.py', workflow)
        self.assertIn('python3 -m unittest discover -s plugins/bauer/tests -v', workflow)


if __name__ == '__main__':
    unittest.main()
