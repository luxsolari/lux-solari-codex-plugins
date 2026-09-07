#!/usr/bin/env python3
"""Extract one version's section from a plugin's CHANGELOG for release notes.

The extract() function is kept identical to the copy in luxsolari/whiting,
which is where it originated. Fix a parsing bug in one, fix it in the other.
Only the CLI differs: this repo holds several plugins, so a release is named
by a <plugin>-v<version> tag and the changelog lives at
plugins/<plugin>/CHANGELOG.md.
"""
import re
import sys
from pathlib import Path


def extract(changelog_text: str, version: str) -> str:
    pattern = re.compile(
        rf'^## \[{re.escape(version)}\].*?\n(.*?)(?=^## \[|\Z)',
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(changelog_text)
    if not match:
        raise SystemExit(f"No CHANGELOG entry found for version {version}")

    body = match.group(1)
    # Drop the trailing reference-link line and "---" separator.
    lines = [
        line for line in body.split('\n')
        if not line.startswith(f'[{version}]:') and line.strip() != '---'
    ]
    return '\n'.join(lines).strip() + '\n'


def split_tag(tag: str) -> tuple[str, str]:
    """Split a `<plugin>-v<version>` tag into its two halves.

    Split on the LAST `-v`: plugin names contain hyphens (three-axes-framework,
    lux-solari-*), so splitting on the first one would truncate them.
    """
    marker = tag.rfind('-v')
    if marker == -1:
        raise SystemExit(f"Tag {tag!r} is not of the form <plugin>-v<version>")
    return tag[:marker], tag[marker + 2:]


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: extract_changelog.py <plugin>-v<version>", file=sys.stderr)
        return 1

    plugin, version = split_tag(sys.argv[1])
    repo_root = Path(__file__).parent.parent
    changelog = repo_root / "plugins" / plugin / "CHANGELOG.md"
    if not changelog.is_file():
        raise SystemExit(f"No CHANGELOG.md for plugin {plugin!r} at {changelog}")
    print(extract(changelog.read_text(encoding="utf-8"), version), end='')
    return 0


if __name__ == "__main__":
    sys.exit(main())
