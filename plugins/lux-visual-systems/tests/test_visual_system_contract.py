from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import struct
import unittest
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "lux-visual-systems"


class VisualSystemContractTests(unittest.TestCase):
    def test_canonical_master_and_all_reference_assets_are_present(self) -> None:
        assets = SKILL / "assets"
        expected = {
            "00_VISUAL_SYSTEM_MASTER.png",
            "10_REFERENCE_STICKER_SYSTEM_EDITORIAL.png",
            "11_REFERENCE_STICKER_SYSTEM_TECH.png",
            "12_REFERENCE_CHARACTER_EDITORIAL_A.png",
            "13_REFERENCE_CHARACTER_EDITORIAL_B.png",
            "14_REFERENCE_CHARACTER_STICKERS_A.png",
            "15_REFERENCE_CHARACTER_STICKERS_B.png",
            "16_REFERENCE_PHOTOGRAPHY_EDITORIAL.png",
            "17_REFERENCE_TECH_EDITORIAL.png",
            "20_REFERENCE_WEBSITE_COMMIT_PAGE.png",
            "21_REFERENCE_WEBSITE_HOME_LIGHT.png",
            "22_REFERENCE_WEBSITE_HOME_DARK.png",
            "23_REFERENCE_WEBSITE_BLOG.png",
            "24_REFERENCE_WEBSITE_PHOTO_INDEX.png",
            "25_REFERENCE_WEBSITE_HOME_DARK.png",
            "26_REFERENCE_WEBSITE_BLOG_DARK.png",
            "27_REFERENCE_WEBSITE_PHOTO_INDEX_DARK.png",
            "28_REFERENCE_WEBSITE_PHOTO_DIARY_DARK.png",
            "30_REFERENCE_ILLUSTRATION_LIGHT_WIDE.png",
            "31_REFERENCE_ILLUSTRATION_DARK_WIDE.png",
            "32_REFERENCE_ILLUSTRATION_DARK_ARCHITECTURE.png",
            "33_REFERENCE_ILLUSTRATION_LIGHT_PORTRAIT.png",
        }
        self.assertEqual({path.name for path in assets.glob("*.png")}, expected)

    def test_skill_preserves_reference_priority_and_subject_system_split(self) -> None:
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        priority_section = text.split("## Reference priority", 1)[1].split(
            "## Create the image", 1
        )[0]
        expected_priority = """1. Explicit user corrections
2. User-selected rendering language and color mode
3. Current-turn references
4. Subject references
5. `00_VISUAL_SYSTEM_MASTER.png`
6. Project references
7. General Lux Solari references
8. Model knowledge"""
        self.assertIn(expected_priority, priority_section)
        self.assertIn("Subject references control", text)
        self.assertIn("rendering language controls medium and rendering technique", text)
        self.assertIn("The Lux Solari system controls", text)

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
            text.index("## Start every request"), text.index("## Load the system")
        )
        self.assertIn("## Conversation starters", help_text)
        self.assertIn("Create a Lux Solari sticker sheet", help_text)

        agent = (SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn('default_prompt: "Use $lux-visual-systems."', agent)
        manifest = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text())
        self.assertEqual(
            manifest["interface"]["defaultPrompt"],
            [
                "Create a Lux Solari sticker sheet around this subject.",
                "Turn this reference into a production-ready character sheet.",
                "Create a full illustration for this piece of writing.",
                "Design four disciplined visual experiments for this idea.",
            ],
        )

    def test_reference_files_exist(self) -> None:
        for name in (
            "help.md",
            "visual-system.md",
            "formats.md",
            "reference-assets.md",
            "craft-stickers.md",
            "craft-stickers.json",
        ):
            self.assertTrue((SKILL / "references" / name).is_file(), name)

    def test_craft_collection_preserves_every_source_image(self) -> None:
        inventory = json.loads((SKILL / "references/craft-stickers.json").read_text())
        entries = inventory["entries"]
        self.assertEqual(inventory["schema_version"], 1)
        self.assertEqual(inventory["source_image_count"], 57)
        self.assertEqual(len(entries), 57)
        self.assertEqual(len({entry["source_name"] for entry in entries}), 57)
        self.assertEqual(inventory["unique_image_count"], 56)
        self.assertEqual(len({entry["sha256"] for entry in entries}), 56)
        new_paths = set()
        for entry in entries:
            with self.subTest(source=entry["source_name"]):
                path = SKILL / entry["asset"]
                self.assertTrue(path.resolve().is_relative_to(SKILL.resolve()))
                data = path.read_bytes()
                self.assertEqual(hashlib.sha256(data).hexdigest(), entry["sha256"])
                self.assertEqual(len(data), entry["bytes"])
                self.assertEqual(data[:8], b"\x89PNG\r\n\x1a\n")
                self.assertEqual(data[12:16], b"IHDR")
                self.assertEqual(
                    struct.unpack(">II", data[16:24]),
                    (entry["width"], entry["height"]),
                )
                if path.parent.name == "craft-stickers":
                    self.assertEqual(path.name, entry["source_name"])
                    new_paths.add(path)
        self.assertEqual(inventory["added_image_count"], 44)
        self.assertEqual(len(new_paths), 44)
        self.assertEqual(new_paths, set((SKILL / "assets/craft-stickers").glob("*.png")))

    def test_craft_catalogue_links_every_original_for_portable_selection(self) -> None:
        references = SKILL / "references"
        inventory = json.loads((references / "craft-stickers.json").read_text())
        catalogue = (references / "craft-stickers.md").read_text()
        rows = re.findall(r"\| \[([^\]]+)\]\(([^)]+)\) \|", catalogue)
        self.assertEqual(len(rows), 57)
        linked = {name: (references / unquote(link)).resolve() for name, link in rows}
        for entry in inventory["entries"]:
            with self.subTest(source=entry["source_name"]):
                self.assertEqual(
                    linked[entry["source_name"]], (SKILL / entry["asset"]).resolve()
                )
                self.assertIn(entry["description"], catalogue)
                self.assertIn(entry["reference_mode"], {"light", "dark", "multicolor"})
        self.assertEqual(
            {entry["category"] for entry in inventory["entries"]},
            {"canonical", "mixed-craft", "character", "illustration", "photography",
             "photography-card", "film-label", "gaming"},
        )
        skill = (SKILL / "SKILL.md").read_text()
        self.assertIn("references/craft-stickers.md", skill)
        self.assertIn("visually inspect", skill)
        self.assertNotIn("/Users/", skill + catalogue + json.dumps(inventory))


if __name__ == "__main__":
    unittest.main()
