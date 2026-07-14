#!/usr/bin/env python3
"""Generate the checked-in, file-level ledger for pinned Claude sources."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


RUNTIME_PREFIXES = (
    ".claude-plugin/", "commands/", "hooks/", "skills/", "templates/",
    "hannah/", "pyproject.toml", "LICENSE", "LICENSE-DESIGN", "README.md",
    "scripts/", "tests/",
)


def classify(repository: str, path: str) -> str:
    if path.startswith(".github/"):
        return "consolidated CI or source release packaging"
    if path.startswith(("docs/", "assets/")) or path in {"AGENTS.md", "CLAUDE.md", "CHANGELOG.md", "CONTRIBUTING.md", "ROADMAP.md", ".gitignore"}:
        return "source-repository-only documentation/release packaging"
    if path.startswith("tests/"):
        return "copied verification"
    if path.startswith(".claude-plugin/") or path.startswith("commands/"):
        return "translated manifest or Codex route"
    if path.startswith(("skills/", "hooks/", "templates/", "hannah/", "pyproject.toml", "LICENSE", "LICENSE-DESIGN")):
        return "copied runtime"
    if repository == "sage-instructor" and path.startswith("scripts/"):
        return "copied runtime"
    if repository == "whiting" and path.startswith("scripts/"):
        return "copied runtime"
    if repository == "hannah" and path == "README.md":
        return "copied runtime"
    return "source-repository-only documentation/release packaging"


def source_files(repo: Path) -> list[str]:
    result = subprocess.run(["git", "-C", str(repo), "ls-files"], check=True, text=True, capture_output=True)
    return [line for line in result.stdout.splitlines() if line]


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: generate_parity_ledger.py SOURCE_ROOT OUTPUT")
    source_root, output = map(Path, sys.argv[1:])
    repositories = ["three-axes-framework", "sage-instructor", "whiting", "lux-swiss", "hannah", "tri-swiss"]
    lines = ["# File-level upstream parity ledger", "", "Generated from the pinned source checkouts with `scripts/generate_parity_ledger.py`. Every tracked upstream file has exactly one classification.", ""]
    for name in repositories:
        lines.extend([f"## {name}", "", "| Source file | Classification |", "| --- | --- |"])
        for path in source_files(source_root / name):
            lines.append(f"| `{path}` | {classify(name, path)} |")
        lines.append("")
    output.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
