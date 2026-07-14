"""Marketplace-level contract tests."""

from __future__ import annotations

import json
from pathlib import Path
import unittest


REPO = Path(__file__).resolve().parents[1]
MARKETPLACE = REPO / ".agents/plugins/marketplace.json"


def load_marketplace() -> dict:
    return json.loads(MARKETPLACE.read_text(encoding="utf-8"))


class MarketplaceTests(unittest.TestCase):
    def test_marketplace_has_complete_published_catalog(self) -> None:
        names = [entry["name"] for entry in load_marketplace()["plugins"]]
        self.assertEqual(
            names,
            [
                "three-axes-framework",
                "sage-instructor",
                "whiting",
                "lux-swiss",
                "hannah",
                "tri-swiss",
            ],
        )

    def test_every_entry_resolves_to_a_manifest(self) -> None:
        for entry in load_marketplace()["plugins"]:
            manifest = REPO / entry["source"]["path"] / ".codex-plugin/plugin.json"
            self.assertTrue(manifest.is_file(), manifest)


if __name__ == "__main__":
    unittest.main()
