# Lux Solari Codex Plugins

Codex-native packages for Lux Solari's published Claude Code plugins.

## Catalog

- **Three Axes Framework** — calibrates assistance by mastery, consequence, and intent, including session lifecycle context.
- **Sage Instructor** — adaptive, discovery-first programming instruction with persistent progress.
- **Whiting** — repository release discipline, Conventional Commit enforcement, and release tooling.
- **Lux Swiss** — a governed Swiss visual system and Tailwind theme.
- **Hannah** — a local LLM strategy engine that analyses a repository and host hardware.
- **Tri-Swiss** — a red/turquoise Swiss visual system and Tailwind theme.

## Install locally

From this repository root:

```sh
codex plugin marketplace add .
```

The marketplace preserves the source package versions and all runtime behavior.
Claude-branded commands are exposed as Codex skill routes; Three Axes uses a
Codex `SessionStart` hook. Sage includes its complete Three Axes calibration
contract, and cooperates with Three Axes when it is also installed.

## Source ledger

| Package | Source version |
| --- | --- |
| Three Axes Framework | 1.2.1 |
| Sage Instructor | 1.7.2 |
| Whiting | 0.2.0 |
| Lux Swiss | 2.3.0 |
| Hannah | 0.10.6 |
| Tri-Swiss | 1.1.0 |

See `docs/parity-inventory.md` for the completed source-to-target inventory.
