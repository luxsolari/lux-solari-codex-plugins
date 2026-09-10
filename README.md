# Lux Solari Codex Plugins

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A personal Codex plugin marketplace for Lux Solari's published developer,
learning, release-discipline, design-system, and local-model tools.

## Add this marketplace

```sh
codex plugin marketplace add luxsolari/lux-solari-codex-plugins
```

For a local checkout:

```sh
codex plugin marketplace add .
```

## Available plugins

### three-axes-framework

Always-active AI development philosophy calibrated across Mastery, Consequence,
and Intent to prevent comprehension debt. Includes Codex `SessionStart`
lifecycle context and profile state at global, project, and session scope.
If no valid persistent user or project profile exists, it guides setup in chat
and denies project tool calls until the user chooses a scope and axis values and
the profile is saved. Question tools and the dedicated setup writer remain
available. A partial persistent profile is sufficient; an empty, malformed, or
invalid profile and session-only settings are not. Codex paths honor `CODEX_HOME`,
with the existing legacy Claude global fallback when the Codex global is absent.
For the native option picker in Codex CLI Default mode, builds exposing the
`default_mode_request_user_input` feature can enable it at launch with
`codex --enable default_mode_request_user_input`. The plugin cannot enable host
features itself. If the question tool is unavailable, setup asks one question
at a time in chat.
Hooks must be enabled and trusted; tool enforcement covers the paths the host
exposes to `PreToolUse`, not hosted tools outside that hook lifecycle.

```sh
codex plugin add three-axes-framework@lux-solari-codex
```

See [three-axes-framework](https://github.com/luxsolari/three-axes-framework)
for the original framework documentation.

### sage-instructor

Adaptive programming instruction with discovery-first lessons, persistent
multi-track progress, confidence/review queues, exercise verification, and
bundled Python and Rust curricula. It honors Three Axes state when installed
and carries the equivalent calibration contract when it is not.

```sh
codex plugin add sage-instructor@lux-solari-codex
```

See [sage-instructor](https://github.com/luxsolari/sage-instructor) for the
original instructor documentation.

### whiting

Bootstraps repository release discipline end-to-end: initialization,
Conventional Commit enforcement, semver classification, changelog-driven
releases, and a read-only inspection workflow for existing repositories.

```sh
codex plugin add whiting@lux-solari-codex
```

See [whiting](https://github.com/luxsolari/whiting) for full documentation.

### lux-swiss

Lux Solari's strict two-color Swiss design system: visible borders, no shadows,
Space Mono / Space Grotesk typography, governed blood-red accents, hand-rolled
SVG charts, component guidance, and a ready-to-paste Tailwind 4 theme.

```sh
codex plugin add lux-swiss@lux-solari-codex
```

See [lux-swiss](https://github.com/luxsolari/lux-swiss) for full documentation.

### hannah

F1 strategy engineer for your local LLM garage. Hannah analyses a repository
and host hardware, discovers local Ollama context, and ranks the best-fitting
models with console or JSON reports.

```sh
codex plugin add hannah@lux-solari-codex
```

See [hannah](https://github.com/luxsolari/hannah) for full documentation.

### tri-swiss

Tri-Swiss is the red-and-turquoise sibling to Lux Swiss: a governed tri-tone
Swiss system with Geist typography, structural bands, chart guidance, component
catalogue, and an exact Tailwind 4 theme.

```sh
codex plugin add tri-swiss@lux-solari-codex
```

See [tri-swiss](https://github.com/luxsolari/tri-swiss) for full documentation.

### lux-visual-systems

Lux Solari Visual Systems Director governs image-making across Swiss editorial,
anime, analogue, and technical modes. It includes the canonical visual master,
format-specific reference boards, explicit subject-versus-system rules, and
direct image-generation and iteration workflows.

```sh
codex plugin add lux-visual-systems@lux-solari-codex
```

## Codex compatibility

The marketplace preserves the published source versions and runtime behavior
of imported packages and records native Codex packages at their authored version.
Claude command wording is represented by explicit Codex skill routes. Three
Axes uses a native `SessionStart` hook; Sage uses Codex structured prompts and
contains a complete Three Axes calibration contract. The full host-adapter and
source-file records are in [docs/parity-inventory.md](docs/parity-inventory.md)
and [docs/parity-ledger.md](docs/parity-ledger.md).

## Maintaining this marketplace

Plugin versions live in each package's `.codex-plugin/plugin.json`; update that
package when its source changes. Test the catalog and packages locally before
pushing:

```sh
python3 -m unittest tests/test_marketplace.py tests/test_parity_inventory.py tests/test_host_portability.py -v
for plugin in plugins/*; do python3 scripts/validate_plugin.py "$plugin"; done
codex plugin marketplace add .
codex plugin add <name>@lux-solari-codex
```
