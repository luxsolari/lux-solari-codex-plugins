"""Every plugin must carry a changelog whose newest entry is its current version.

Without this, a tag can be pushed for a version that has no changelog section.
The release workflow then fails at tag time -- after the tag is already public,
which is the expensive moment to find out.
"""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from extract_changelog import extract, split_tag  # noqa: E402


def plugins() -> list[Path]:
    return sorted(p for p in (ROOT / "plugins").iterdir() if p.is_dir())


class PluginChangelogTests(unittest.TestCase):
    def test_every_plugin_has_a_changelog(self) -> None:
        for plugin in plugins():
            with self.subTest(plugin=plugin.name):
                self.assertTrue((plugin / "CHANGELOG.md").is_file())

    def test_newest_entry_matches_the_manifest_version(self) -> None:
        for plugin in plugins():
            with self.subTest(plugin=plugin.name):
                version = json.loads(
                    (plugin / ".codex-plugin/plugin.json").read_text()
                )["version"]
                text = (plugin / "CHANGELOG.md").read_text(encoding="utf-8")
                newest = re.search(r"^## \[(\d+\.\d+\.\d+)\]", text, re.MULTILINE)
                self.assertIsNotNone(newest, "no released version heading")
                self.assertEqual(newest.group(1), version)

    def test_release_notes_can_be_extracted_for_the_current_version(self) -> None:
        for plugin in plugins():
            with self.subTest(plugin=plugin.name):
                version = json.loads(
                    (plugin / ".codex-plugin/plugin.json").read_text()
                )["version"]
                text = (plugin / "CHANGELOG.md").read_text(encoding="utf-8")
                self.assertTrue(extract(text, version).strip())

    def test_tags_split_on_the_last_marker_so_hyphenated_names_survive(self) -> None:
        self.assertEqual(split_tag("three-axes-framework-v1.4.0"),
                         ("three-axes-framework", "1.4.0"))
        self.assertEqual(split_tag("whiting-v0.6.0"), ("whiting", "0.6.0"))
        with self.assertRaises(SystemExit):
            split_tag("v1.4.0")


if __name__ == "__main__":
    unittest.main()
