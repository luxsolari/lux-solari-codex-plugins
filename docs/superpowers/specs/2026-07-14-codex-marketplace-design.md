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
| `three-axes-framework` | Applies Mastery, Consequence, and Intent calibration; supports project/global profile guidance and mode signals. | Claude's `SessionStart` hook is not represented. The framework uses an explicit Codex skill and must not claim invisible always-on activation. |
| `sage-instructor` | Delivers discovery-first programming instruction, curricula, milestones, and progress guidance. | Claude `AskUserQuestion` interactions become normal Codex conversational prompts. |
| `whiting` | Provides distinct release-discipline initialization and repository-inspection workflows, with portable release guidance/scripts where applicable. | Claude command routing becomes skills and starter prompts. |
| `lux-swiss` | Supplies the Lux Swiss visual rules, Tailwind theme, and component/chart guidance. | The styling guidance is host-independent; only invocation changes. |
| `hannah` | Analyzes the repository and local machine context to recommend local LLM models and runtimes. | Codex-native read-only inspection replaces Claude-specific invocation. |
| `tri-swiss` | Supplies the Tri-Swiss visual rules, Tailwind theme, and component guidance. | The styling guidance is host-independent; only invocation changes. |

## Package contents

Each package has a focused `SKILL.md` that identifies when Codex should use it,
the user-visible workflow, safeguards, and links to only the references it
needs. Larger reusable material is kept in `references/` rather than
duplicated in manifests.

`whiting` and `hannah` may contain scripts only when a direct shell operation
is a necessary part of their documented behavior. Such scripts must be
portable, narrowly scoped, and documented. Design-system packages retain
their reusable theme artifacts as plain reference assets.

## Metadata and user experience

All manifests use Lux Solari as publisher, retain MIT licensing and upstream
source/homepage links, and expose concise Codex-specific starter prompts.
Categories are `Productivity` for the framework, instruction, release, and
local-model packages; `Design` for the two Swiss systems. Marketplace order
matches the existing Claude catalog.

The README explains installation through a Codex marketplace, lists the six
packages, calls out the Three Axes activation difference, and provides local
validation instructions. It avoids claiming that unimplemented hooks or
Claude slash commands work in Codex.

## Validation and acceptance criteria

Before handoff:

1. Validate every plugin with Codex's plugin validator.
2. Parse and inspect the marketplace JSON and every plugin manifest.
3. Confirm each marketplace entry resolves to an existing local package.
4. Confirm every declared skills or asset path exists.
5. Confirm the README represents all six packages and all documented
   compatibility differences accurately.
6. Review the worktree to ensure the existing Claude marketplace remains
   untouched.

Success means a user can add the new repository as a Codex marketplace, see
all six packages in their intended order, and install packages whose manifests
and skills accurately communicate supported Codex behavior.

## Risks and decisions

The primary risk is overstating platform parity. The packages will state
capability differences explicitly, particularly for automatic session hooks
and host-specific interaction controls. The secondary risk is drift from the
upstream Claude plugins; their public source repositories remain the behavioral
reference during the initial port, while this marketplace independently owns
Codex packaging and release versions.
