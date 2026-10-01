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
| Three Axes | framework skill, nine command artifacts, profiles, tests, MIT license | Canonical `hooks/hooks.json` runs the native `SessionStart` wrapper for startup, resume, clear, and compact; the prompt hook reports configured state, while the tool hook starts guided setup only at the first local workspace action. |
| Sage | instructor, 20 command artifacts, curricula, profile/schema checks, fixtures, ten scenarios, MIT license | Codex routes and structured prompts; bundled Three Axes contract works with or without that installed package. |
| Whiting | four skills, all scripts/hooks/templates (agent rule files, work log, merge and manifest-version helpers), release workflow, tests, MIT license | Skill routes replace command discovery; operational scripts are unchanged beyond reading `.codex-plugin/plugin.json` for the manifest-version check; the release-time plugin check uses this repo's `validate_plugin.py` rather than the Claude CLI. |
| Lux Swiss | skill, exact theme, component catalogue, house mark, dual licenses | Invocation only; visual material is host-independent. |
| Hannah | full Python package, pyproject, CLI, strategy material, smoke tests, README, MIT license | Local `run-hannah` invokes the package without third-party dependencies. |
| Tri-Swiss | skill, exact theme, component catalogue, house mark, dual licenses | Invocation only; visual material is host-independent. |
| Lux Visual Systems | native Codex skill, canonical master, 13 supporting visual boards, format rules, reference governance, dual licenses | Direct image generation; subject references and current-turn corrections take priority over the packaged visual system. |
| Anime Identity Designer | recovered GPT prompt/configuration, compact skill, 13 original PNG references, tests, dual licenses | GPT capabilities become an explicit Codex skill that calls image generation directly and separates subject identity from the packaged style system. |
| Machine Pilgrim | recovered GPT prompt/configuration, original source text, compact canon, 18 original PNG references, tests, dual licenses | GPT capabilities become an explicit Codex skill that calls image generation directly and preserves scene, canon, and conversation continuity. |
| Bauer 0.1.1 | exact portable skill, four Python helpers, five reference files, six upstream test modules, both manifests, README, changelog, MIT license and third-party notice | No runtime translation; resolve helper paths from the installed skill. Claude manifest is verification-only for the unchanged upstream cross-host contract. |

Bauer is pinned to `b66402ad3cb194cce684602a2728414c5d583d8f` from
`luxsolari/bauer`: the post-tag metadata fix for version 0.1.1, not the immutable
`v0.1.1` tag at `9870701ce5fa73cecc71a9ed2e1935eeebb8e943`. Both source
manifests carry the corrected description, "Evidence-backed security audits with
optional Jev review." [bauer-source-parity.json](bauer-source-parity.json) records
SHA-256 for every copied file, including documentation and verification. The
package parity test checks the exact file inventory and helper/reference paths
without needing the source checkout or network. The pinned upstream manifest
includes the required Codex interface metadata, and the changelog contains a
dated 0.1.1 entry. All 22 files are copied unchanged, including the refreshed
README, manifest/skill versions and upstream version assertion. This is a
documentation-and-version refresh: the four helper implementations and reference
files are unchanged. Host dogfood evidence in the README is bounded: Claude
session-local execution and Codex local-skill execution did not exercise activated
marketplace plugins or demonstrate a new vulnerability. Known discovery, secret-
filter and OSV timestamp limitations remain documented, not remediated. See
`JOURNAL.md` for local verification and publication boundaries.

The only package-system translation is Sage's Claude marketplace dependency:
Codex manifests have no package-dependency field, so Sage carries the complete
calibration contract and uses Three Axes state when available. No learner,
profile, project, or session state is stored inside an installed package.
