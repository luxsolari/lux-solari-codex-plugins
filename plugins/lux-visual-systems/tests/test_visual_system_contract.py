from __future__ import annotations

from pathlib import Path
import unittest


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
        }
        self.assertEqual({path.name for path in assets.glob("*.png")}, expected)

    def test_skill_preserves_reference_priority_and_subject_system_split(self) -> None:
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        priority_section = text.split("## Reference priority", 1)[1].split(
            "## Create the image", 1
        )[0]
        expected_priority = """1. Current-turn references
2. Explicit user corrections
3. Subject references
4. `00_VISUAL_SYSTEM_MASTER.png`
5. Project references
6. General Lux Solari references
7. Model knowledge"""
        self.assertIn(expected_priority, priority_section)
        self.assertIn("Subject references control", text)
        self.assertIn("The Lux Solari system controls", text)

    def test_reference_files_exist(self) -> None:
        for name in ("visual-system.md", "formats.md", "reference-assets.md"):
            self.assertTrue((SKILL / "references" / name).is_file(), name)


if __name__ == "__main__":
    unittest.main()
