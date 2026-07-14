# Lux Solari Codex Plugins — Design

## Purpose

Create `lux-solari-codex-plugins`, a standalone marketplace for Codex-native
versions of Lux Solari's published Claude Code plugins. The marketplace must
preserve each plugin's purpose while using supported Codex plugin structures
and making deliberate, documented adaptations where the two hosts differ.

## Scope

The first release ports the six plugins published by the Claude marketplace,
in this stable order:

1. `three-axes-framework`
2. `sage-instructor`
3. `whiting`
4. `lux-swiss`
5. `hannah`
6. `tri-swiss`

This work creates the new repository, a marketplace catalog, one installable
Codex package per plugin, documentation, and local validation. It does not
alter the existing `lux-solari-plugins` Claude marketplace or publish a remote
GitHub repository.

## Repository architecture

```text
lux-solari-codex-plugins/
├── .agents/plugins/marketplace.json
├── plugins/
│   └── <plugin-name>/
│       ├── .codex-plugin/plugin.json
│       ├── skills/
│       ├── hooks/                   # only when lifecycle behavior is required
│       ├── references/
│       ├── scripts/                 # only when required
│       └── assets/                  # only when required
├── docs/superpowers/specs/
├── README.md
├── LICENSE
└── .gitignore
```

The marketplace catalog is the single discovery and installation-policy
source. Each local marketplace entry uses `./plugins/<plugin-name>` and
includes the required `AVAILABLE` installation policy, `ON_INSTALL`
authentication policy, and a category.

Each plugin's `.codex-plugin/plugin.json` is the package source of truth for
name, semantic version, publisher metadata, source links, license, keywords,
skills location, and user-facing interface metadata. Plugin names, folder
names, and marketplace entry names are identical.

## Porting model

The porting standard is behaviorally faithful rather than mechanically
identical. Claude-only commands, hooks, and interaction primitives will not
be copied into a Codex package or presented as supported. Equivalent Codex
skills, references, and portable scripts will carry the product behavior.

| Plugin | Codex package behavior | Intentional adaptation |
| --- | --- | --- |
| `three-axes-framework` | Applies Mastery, Consequence, and Intent calibration; supports project/global profile guidance and mode signals. | Port its lifecycle injection through a Codex-native `SessionStart` hook and a Codex-specific wrapper. It will target `startup`, `resume`, `clear`, and `compact`, matching the published framework; only `startup` clears the ephemeral session profile. |
| `sage-instructor` | Delivers discovery-first programming instruction, curricula, milestones, and progress guidance. | Claude `AskUserQuestion` interactions become normal Codex conversational prompts; its complete Three Axes calibration contract is bundled so it works both alongside and without a separately installed Three Axes package. |
| `whiting` | Provides distinct release-discipline initialization and repository-inspection workflows, with portable release guidance/scripts where applicable. | Claude command routing becomes skills and starter prompts. |
| `lux-swiss` | Supplies the Lux Swiss visual rules, Tailwind theme, and component/chart guidance. | The styling guidance is host-independent; only invocation changes. |
| `hannah` | Analyzes the repository and local machine context to recommend local LLM models and runtimes. | Codex-native read-only inspection replaces Claude-specific invocation. |
| `tri-swiss` | Supplies the Tri-Swiss visual rules, Tailwind theme, and component guidance. | The styling guidance is host-independent; only invocation changes. |

## Package contents

Each package has a focused `SKILL.md` that identifies when Codex should use it,
the user-visible workflow, safeguards, and links to only the references it
needs. Larger reusable material is kept in `references/` rather than
duplicated in manifests.

`three-axes-framework` includes the canonical auto-discovered
`hooks/hooks.json` and a portable `session-start-codex` wrapper. Its manifest
does not include a `hooks` field: Codex discovers the canonical file while the
supported manifest validator remains authoritative. The wrapper derives its
own plugin root, resolves the appropriate Three Axes profile layer, and emits
Codex's `SessionStart` additional-context payload for all four lifecycle
matchers. Fixture and disposable-install tests verify the emitted JSON,
injection content, and startup-only session clearing.

`whiting` and `hannah` may contain scripts only when a direct shell operation
is a necessary part of their documented behavior. Such scripts must be
portable, narrowly scoped, and documented. Design-system packages retain
their reusable theme artifacts as plain reference assets.

## Metadata and user experience

All manifests use Lux Solari as publisher, retain their upstream license scope
(MIT for four packages and dual MIT/X11 plus CC-BY-SA-4.0 for the Swiss design
systems), source/homepage links, and concise Codex-specific starter prompts.
Categories are `Productivity` for the framework, instruction, release, and
local-model packages; `Design` for the two Swiss systems. Marketplace order
matches the existing Claude catalog.

The README explains installation through a Codex marketplace, lists the six
packages, calls out the Three Axes activation difference, and provides local
validation instructions. It maps every Claude command to an available Codex
skill route and names each host adapter rather than claiming unsupported host
features.

## Validation and acceptance criteria

Before handoff:

1. Validate every plugin with Codex's plugin validator.
2. Parse and inspect the marketplace JSON and every plugin manifest.
3. Exercise the Three Axes SessionStart hook against profile fixtures and
   verify its Codex additional-context payload.
4. Confirm each marketplace entry resolves to an existing local package.
5. Confirm every declared skills, hook, or asset path exists.
6. Confirm the README represents all six packages and all documented
   compatibility differences accurately.
7. Verify the complete source-to-target inventory, including legal artifacts,
   command routes, and source-repository-only release material classification.
8. Perform disposable-install smoke tests for Three Axes lifecycle injection,
   Sage with and without Three Axes, and Hannah's module and console CLIs.
9. Review the worktree to ensure the existing Claude marketplace remains
   untouched.

Success means a user can add the new repository as a Codex marketplace, see
all six packages in their intended order, and install packages whose manifests
and skills accurately communicate supported Codex behavior.

## Risks and decisions

The primary risk is overstating platform parity. The Three Axes hook is a
supported Codex-native port, but its command, matcher, and JSON output contract
must be Codex-specific; copying the Claude hook verbatim would use the wrong
plugin-root variable and lifecycle behavior. Other host-specific interaction
controls will remain explicitly documented. The secondary risk is drift from
the upstream Claude plugins; their public source repositories remain the
behavioral reference during the initial port, while this marketplace
independently owns Codex packaging and release versions.
