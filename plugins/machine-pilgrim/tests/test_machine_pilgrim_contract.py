from __future__ import annotations

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "machine-pilgrim"


class MachinePilgrimContractTests(unittest.TestCase):
    def test_all_original_visual_references_are_present(self) -> None:
        expected = {
            "1-enhanced.png",
            "1.png",
            "2-e.png",
            "2.png",
            "3.png",
            "4.png",
            "4467ad69-c3f1-4341-9259-889d7d83fc42.png",
            "5.png",
            "5f36b0f1-932f-44bd-9a47-7ee483905a8b.png",
            "ChatGPT Image Jun 12, 2026, 07_36_48 PM.png",
            "ChatGPT Image Jun 12, 2026, 07_37_02 PM.png",
            "ChatGPT Image Jun 12, 2026, 07_42_22 PM.png",
            "ChatGPT Image Jun 12, 2026, 07_42_30 PM.png",
            "ChatGPT Image Jun 12, 2026, 07_44_32 PM.png",
            "ChatGPT Image Jun 12, 2026, 07_46_14 PM.png",
            "ChatGPT Image Jun 12, 2026, 07_49_34 PM (1).png",
            "ChatGPT Image Jun 12, 2026, 07_49_35 PM (2).png",
            "ChatGPT Image Jun 13, 2026, 12_09_15 AM.png",
        }
        self.assertEqual({path.name for path in (SKILL / "assets").glob("*.png")}, expected)

    def test_canon_and_original_source_are_present(self) -> None:
        references = SKILL / "references"
        for name in (
            "machine-canon.md",
            "conversations-with-the-machine-01.md",
            "help.md",
            "original-master-prompt.md",
            "original-gpt-config.md",
            "reference-assets.md",
        ):
            self.assertTrue((references / name).is_file(), name)

    def test_invocation_and_rendering_language_gates(self) -> None:
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        help_text = (SKILL / "references" / "help.md").read_text(encoding="utf-8")
        for phrase in (
            "No visual brief",
            "Rendering language missing",
            "Never infer or silently default this choice",
            "final answer must contain only the complete contents",
            "An attachment by itself is not a visual brief",
            "the conversation already has an active selection",
        ):
            self.assertIn(phrase, text)
        self.assertLess(
            text.index("No visual brief"), text.index("Rendering language missing")
        )
        self.assertLess(
            text.index("## Start every request"), text.index("## Load the canon")
        )
        self.assertIn("## Conversation starters", help_text)
        self.assertIn("Create The Seventh Archive", help_text)

        agent = (SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn('default_prompt: "Use $machine-pilgrim."', agent)
        manifest = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text())
        self.assertEqual(
            manifest["interface"]["defaultPrompt"],
            "Use $machine-pilgrim.",
        )

    def test_operational_contract_preserves_core_behavior(self) -> None:
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        for phrase in (
            "Artificial intelligence is never humanoid",
            "call image generation directly",
            "Standalone Artwork",
            "Illustrated Book",
            "Cinematic Sequence",
            "Maintain continuity",
            "roughly 40% luminous atmosphere",
        ):
            self.assertIn(phrase, text)
        self.assertLess(
            text.index("1. Explicit user corrections"),
            text.index("2. User-selected rendering language"),
        )
        self.assertLess(
            text.index("2. User-selected rendering language"),
            text.index("3. Current-turn references"),
        )


if __name__ == "__main__":
    unittest.main()
