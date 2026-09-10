from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class HostPortabilityTests(unittest.TestCase):
    def test_ci_uses_repository_local_plugin_validator(self) -> None:
        workflow = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
        self.assertIn("scripts/validate_plugin.py", workflow)
        self.assertNotIn("/Users/", workflow)

    def test_active_skills_use_codex_paths_not_claude_plugin_variables(self) -> None:
        active_files = [
            ROOT / "plugins/hannah/skills/hannah/SKILL.md",
            ROOT / "plugins/hannah/skills/hannah/references/strategy.md",
            ROOT / "plugins/whiting/skills/repo-init/SKILL.md",
            ROOT / "plugins/whiting/skills/commit-conventions/SKILL.md",
            ROOT / "plugins/whiting/skills/inspect/SKILL.md",
            ROOT / "plugins/whiting/skills/semver-release/SKILL.md",
            ROOT / "plugins/three-axes-framework/references/commands.md",
            ROOT / "plugins/sage-instructor/skills/sage-instructor/SKILL.md",
            ROOT / "plugins/lux-visual-systems/skills/lux-visual-systems/SKILL.md",
        ]
        for path in active_files:
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("CLAUDE_PLUGIN_ROOT", text, path)
            self.assertNotIn("${PLUGIN_ROOT}", text, path)
            self.assertNotIn("AskUserQuestion", text, path)
        self.assertNotIn("~/.claude/three-axes-session.json", active_files[-2].read_text(encoding="utf-8"))

    def test_skill_source_tables_point_at_files_the_plugin_ships(self) -> None:
        """A `Source (<plugin root>/...)` column must name a file that exists.

        The destination column is a path in the *target* repo, so only the
        first column is checked.
        """
        for skill in sorted((ROOT / "plugins/whiting/skills").glob("*/SKILL.md")):
            in_source_table = False
            for line in skill.read_text(encoding="utf-8").splitlines():
                if line.startswith("|"):
                    first = line.split("|")[1].strip()
                    if "Source" in first and "<plugin root>" in first:
                        in_source_table = True
                        continue
                    if in_source_table and first.startswith("`"):
                        source = first.strip("`")
                        self.assertTrue(
                            (ROOT / "plugins/whiting" / source).is_file(),
                            f"{skill}: source `{source}` is not shipped by the plugin",
                        )
                elif in_source_table:
                    in_source_table = False


if __name__ == "__main__":
    unittest.main()
