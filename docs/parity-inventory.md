# Codex parity inventory

Each package is pinned to the published source revision recorded in the design
and implementation plan. Every tracked source artifact is classified as one of
the following: **copied runtime** (skills, engines, scripts, templates, themes,
licenses, and hook code); **copied verification** (tests, fixtures, scenarios);
**translated manifest** (Codex metadata and skill routing); **consolidated CI**
(the root workflow); or **source-repository-only documentation/release
packaging** (readmes, changelogs, showcase assets, release installers, and
source-maintenance automation).

| Package | Copied/translated runtime coverage | Host adapter |
| --- | --- | --- |
| Three Axes | framework skill, nine command artifacts, profiles, tests, MIT license | Canonical `hooks/hooks.json` runs the native `SessionStart` wrapper for startup, resume, clear, and compact; prompt/tool hooks enforce guided persistent-profile setup. |
| Sage | instructor, 20 command artifacts, curricula, profile/schema checks, fixtures, ten scenarios, MIT license | Codex routes and structured prompts; bundled Three Axes contract works with or without that installed package. |
| Whiting | four skills, all scripts/hooks/templates (agent rule files, work log, merge and manifest-version helpers), release workflow, tests, MIT license | Skill routes replace command discovery; operational scripts are unchanged beyond reading `.codex-plugin/plugin.json` for the manifest-version check; the release-time plugin check uses this repo's `validate_plugin.py` rather than the Claude CLI. |
| Lux Swiss | skill, exact theme, component catalogue, house mark, dual licenses | Invocation only; visual material is host-independent. |
| Hannah | full Python package, pyproject, CLI, strategy material, smoke tests, README, MIT license | Local `run-hannah` invokes the package without third-party dependencies. |
| Tri-Swiss | skill, exact theme, component catalogue, house mark, dual licenses | Invocation only; visual material is host-independent. |
| Lux Visual Systems | native Codex skill, canonical master, 13 supporting visual boards, format rules, reference governance, dual licenses | Direct image generation; subject references and current-turn corrections take priority over the packaged visual system. |

The only package-system translation is Sage's Claude marketplace dependency:
Codex manifests have no package-dependency field, so Sage carries the complete
calibration contract and uses Three Axes state when available. No learner,
profile, project, or session state is stored inside an installed package.
