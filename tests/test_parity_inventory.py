"""High-level assertions for the published-plugin parity inventory."""

from __future__ import annotations

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ParityInventoryTests(unittest.TestCase):
    def manifest(self, name: str) -> dict:
        return json.loads((ROOT / "plugins" / name / ".codex-plugin/plugin.json").read_text())

    def test_versions_and_licenses_match_the_published_catalog(self) -> None:
        expected = {
            "three-axes-framework": ("1.3.0", "MIT"),
            "sage-instructor": ("1.7.2", "MIT"),
            "whiting": ("0.5.0", "MIT"),
            "lux-swiss": ("2.3.0", "CC-BY-SA-4.0"),
            "hannah": ("0.10.6", "MIT"),
            "tri-swiss": ("1.1.0", "CC-BY-SA-4.0"),
        }
        for name, (version, license_name) in expected.items():
            manifest = self.manifest(name)
            self.assertEqual(manifest["version"], version)
            self.assertEqual(manifest["license"], license_name)

    def test_host_adapters_and_runtime_artifacts_are_present(self) -> None:
        required = [
            "plugins/three-axes-framework/hooks/hooks.json",
            "plugins/three-axes-framework/hooks/inject-framework-codex.mjs",
            "plugins/sage-instructor/skills/sage-instructor/references/three-axes-contract.md",
            "plugins/whiting/scripts/run_tests.sh",
            "plugins/lux-swiss/skills/lux-swiss/references/HOUSE-MARK.md",
            "plugins/hannah/scripts/run-hannah",
            "plugins/tri-swiss/skills/tri-swiss/references/HOUSE-MARK.md",
            "docs/parity-inventory.md",
        ]
        for path in required:
            self.assertTrue((ROOT / path).is_file(), path)
        self.assertNotIn("hooks", self.manifest("three-axes-framework"))

    def test_file_level_upstream_ledger_is_checked_in(self) -> None:
        ledger = ROOT / "docs/parity-ledger.md"
        text = ledger.read_text(encoding="utf-8")
        for source in ("three-axes-framework", "sage-instructor", "whiting", "lux-swiss", "hannah", "tri-swiss"):
            self.assertIn(f"## {source}", text)
        self.assertIn("| Source file | Classification |", text)


if __name__ == "__main__":
    unittest.main()
