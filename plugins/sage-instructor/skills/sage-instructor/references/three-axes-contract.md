# Three Axes calibration contract

Sage preserves the Three Axes teaching calibration independently of marketplace
installation order. Resolve behavioral context as **defaults → global → project → session**: defaults are `mastery=medium`, `consequence=medium`, and
`intent=balanced`; global and session files live under `~/.codex`, while the
project override is `.three-axes.json` at the repository root.

When Three Axes is installed, respect its resolved profile and never create
conflicting duplicate state. When it is absent, apply the same axes to lesson
depth, verification strictness, hint escalation, and the balance between
discovery and direct implementation. Sage's own `.sage-profile.md` and
`.sage-progress.json` remain the source of learner and track state.
