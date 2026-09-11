from __future__ import annotations

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "anime-identity-designer"


class AnimeIdentityContractTests(unittest.TestCase):
    def test_all_original_visual_references_are_present(self) -> None:
        expected = {
            "ChatGPT Image Jun 13, 2026, 01_00_07 AM.png",
            "ChatGPT Image Jun 13, 2026, 01_00_28 AM.png",
            "ChatGPT Image Jun 13, 2026, 01_02_31 AM.png",
            "ChatGPT Image Jun 13, 2026, 01_05_54 AM.png",
            "ChatGPT Image Jun 13, 2026, 01_07_28 AM.png",
            "ChatGPT Image Jun 13, 2026, 01_10_51 AM.png",
            "ChatGPT Image Jun 13, 2026, 01_12_23 AM.png",
            "ChatGPT Image Jun 13, 2026, 01_13_19 AM.png",
            "ChatGPT Image Jun 13, 2026, 01_18_56 AM.png",
            "ChatGPT Image Jun 13, 2026, 01_20_22 AM.png",
            "ChatGPT Image Jun 13, 2026, 01_24_25 AM.png",
            "ChatGPT Image Jun 13, 2026, 01_26_17 AM.png",
            "ChatGPT Image Jun 13, 2026, 01_31_40 AM.png",
        }
        self.assertEqual({path.name for path in (SKILL / "assets").glob("*.png")}, expected)

    def test_operational_contract_preserves_core_behavior(self) -> None:
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        for phrase in (
            "Subject versus style system",
            "call image generation directly",
            "EXPERIMENT 01",
            "Branding is optional",
            "Refine without drift",
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

    def test_source_configuration_is_preserved(self) -> None:
        references = SKILL / "references"
        for name in (
            "help.md",
            "original-master-prompt.md",
            "original-gpt-config.md",
            "reference-assets.md",
            "visual-system.md",
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
            text.index("## Start every request"), text.index("## Load the grounding")
        )
        self.assertIn("## Conversation starters", help_text)
        self.assertIn("Turn this photo into an anime branding board", help_text)

        agent = (SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn('default_prompt: "Use $anime-identity-designer."', agent)
        manifest = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text())
        self.assertEqual(
            manifest["interface"]["defaultPrompt"],
            [
                "Turn this photo into an anime branding board",
                "Design logos and emblems for this character",
                "Make expression sheets from this portrait",
                "Turn this photo into an anime portrait for sharing. No Text",
            ],
        )


if __name__ == "__main__":
    unittest.main()
