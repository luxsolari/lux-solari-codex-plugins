# Journal

## 2026-09-23 - Generated-code ownership packages

- Updated the Codex Three Axes and Sage Instructor packages with the shared
  responsible-authorship standard, ownership loop, comprehension gate, and
  review behavior.
- Set local package metadata to Three Axes `1.6.0` and Sage Instructor `1.8.0`;
  aligned the marketplace parity-inventory test with those versions.
- Verified with the marketplace Python suite (12 tests), Sage schema tests
  (7 tests), both plugin validators, and `git diff --check`.
- Published: commit `794edb6`, tags `three-axes-framework-v1.6.0` and
  `sage-instructor-v1.8.0`, and their GitHub Releases are live. All three
  validation runs and both release workflows completed successfully.
- Relevant files: `plugins/three-axes-framework/`,
  `plugins/sage-instructor/`, and `tests/test_parity_inventory.py`.

## 2026-09-23 - Three Axes profile-gate UX 1.5.1

- Updated the packaged Three Axes Framework profile gate to explain its own
  block, skip projectless hook events, and use exposed native question pickers
  directly.
- Verified with the packaged Node test suite and source-package tests.
- Open: release commit, tag, push, and marketplace CI status remain pending.
- Relevant files: `plugins/three-axes-framework/hooks/`,
  `plugins/three-axes-framework/tests/setup-gate.test.mjs`, and the manifest.

## 2026-09-11 - Visual Systems light/dark palettes 1.2.0

- Added interactive light/dark selection alongside rendering language, with explicit-choice reuse and refinement continuity.
- Aligned palette roles with Tri-Swiss and added eight user-supplied website/illustration references.
- Updated the plugin manifest, changelog, asset inventory, and parity version checks.
- Verified: 16 targeted plugin/marketplace tests, plugin and skill validation, and diff whitespace checks passed. Live generation with the new mode gate remains unverified.

## 2026-09-11 - Visual plugin interaction release 1.1.0

- Promoted the shared rendering-language and bare-invocation help behavior to
  version 1.1.0 for Anime Identity Designer, Lux Solari Visual Systems Director,
  and Machine Pilgrim.
- The marketplace catalog is path-based and carries no separate version field;
  each catalog entry resolves the version from its plugin manifest.
- An independent adversarial review found and prompted fixes for three issues:
  refinements could re-trigger the rendering question, help-only output conflicted
  with host-required skill commentary, and packaged styles could override the
  selected rendering language. The prompt contracts and precedence rules now
  resolve all three.
- The complete local CI-equivalent suite passes, including all nine plugin
  validators, all visual contracts, repository parity/version checks, Whiting's
  test suite with signing disabled only inside its temporary test repositories,
  release-note extraction, JSON/YAML parsing, and `git diff --check`.
- Release delivery uses `feat/visual-plugin-interaction-gates` and a pull request
  against `main`; remote and hosted-CI results are reported in the task handoff.
- Relevant files: the three `.codex-plugin/plugin.json` manifests, their
  `CHANGELOG.md` files, and `.agents/plugins/marketplace.json`.

## 2026-09-11 - Shared visual-plugin invocation gates

- Replaced the uncommitted anime-default direction with an explicit rendering-
  language gate across Anime Identity Designer, Lux Solari Visual Systems
  Director, and Machine Pilgrim.
- A substantive brief without a user-stated rendering language now asks one
  focused question and waits; plugin names, house styles, and packaged references
  do not silently satisfy the choice.
- A bare invocation now returns only a plugin-specific help document containing
  its conversation starters and practical usage guidance. Launcher prompts were
  reduced to bare skill invocations so they reliably enter this help path.
- Added contract coverage for the gates, help documents, and launcher prompts.
  All 12 visual-plugin contract tests, all 12 repository metadata tests, Python
  compilation, YAML parsing for all three launcher files, and `git diff --check`
  pass. The full plugin validator remains unavailable because the system Python
  lacks PyYAML; that environment error occurs before validation begins.
- Recorded the new Lux Visual Systems help document in the parity ledger. The
  Anime Identity Designer and Machine Pilgrim ledgers already classify all
  shipped reference Markdown through their existing wildcard entries.
- The earlier anime-default entry below records the superseded direction; none
  of that default remains in the active prompt or changelog.
- Relevant files: the three visual `SKILL.md` files, their `references/help.md`
  documents, launcher metadata, contract tests, changelogs, and
  `docs/parity-ledger.md`.

## 2026-09-11 - Anime-default visual direction

- Made anime the automatic rendering language for every illustrated Lux Solari
  Visual Systems output, without requiring the user to request it repeatedly.
- Required image-generation prompts to carry the anime direction explicitly and
  limited override behavior to an explicit user request for another rendering
  language; photographic and film work remains photographic by default.
- Added a contract test covering the default, generation-prompt propagation,
  and override rule. The four-test visual-system contract, the 12-test repository
  metadata suite, Python compilation, and `git diff --check` all pass.
- The standalone plugin validator remains unrun because the available system
  Python does not provide PyYAML; its failure occurred before plugin validation.
- Relevant files: `plugins/lux-visual-systems/skills/lux-visual-systems/SKILL.md`,
  `plugins/lux-visual-systems/tests/test_visual_system_contract.py`, and
  `plugins/lux-visual-systems/CHANGELOG.md`.

## 2026-09-10 - Signed PR history

- Re-signed every commit in PR #5 with the configured SSH signing key after
  finding two earlier unsigned commits in the branch history.
- Confirmed the global Git default already enforces `commit.gpgsign=true` with
  SSH signing, so future commits across repositories are signed by default.
- Re-ran the repository suite after the history rewrite and verified every PR
  commit locally before updating the remote branch with lease protection.

## 2026-09-10 - Custom GPT visual plugin migration

- Added independent 1.0.0 plugins for `anime-identity-designer` and
  `machine-pilgrim` to the existing `feat/lux-visual-systems` PR branch so the
  three migrations land together without competing marketplace edits.
- Preserved the original GPT instructions and configuration records, all 13
  Anime Identity Designer PNG references, all 18 Machine Pilgrim PNG
  references, and the original Machine Pilgrim source document.
- Verified all 31 PNGs and the source document byte-for-byte against the
  downloaded GPT knowledge bundles. Both new skills, `lux-visual-systems`, all
  nine marketplace plugins, all three visual contract suites, and the 12-test
  repository suite pass locally; `git diff --check` is clean.
- Added explicit subject-or-scene versus visual-system precedence, direct image
  generation behavior, asset inventories, redistribution notices, continuous
  integration coverage, and marketplace parity records.
- The earlier redistribution hold is resolved by the owner's explicit direction
  to preserve and publish these owned GPT knowledge bundles. The notices still
  make clear that depicted third-party marks, characters, and likenesses are not
  relicensed by the plugin packages.
- Relevant files: `plugins/anime-identity-designer/`,
  `plugins/machine-pilgrim/`, `.agents/plugins/marketplace.json`,
  `.github/workflows/ci.yml`, `README.md`, and `docs/parity-ledger.md`.

## 2026-09-10 - Lux Solari Visual Systems Director 1.0.0

- Added the native `lux-visual-systems` Codex plugin and marketplace entry.
- Packaged the canonical master and 13 supporting boards with explicit
  subject-versus-system precedence and direct image-generation behavior.
- Added contract, catalog, portability, inventory, and continuous-integration
  coverage. The skill and every marketplace plugin validate; the full local
  suite passes when user-level Git signing is disabled for temporary test repos.
- Installed and enabled 1.0.0 through the separate local marketplace
  `lux-solari-codex-local`; the existing published marketplace was not replaced.
- Public upload remains open because the packaged boards include third-party
  characters and marks whose redistribution rights are not established.
- Published branch `feat/lux-visual-systems` and opened PR #5 against `main`;
  both GitHub validation runs passed.
- Kept `lux-swiss` and `tri-swiss` separate because they govern interface
  systems, while this package governs image art direction.
- Relevant files: `plugins/lux-visual-systems/`,
  `.agents/plugins/marketplace.json`, `README.md`, and `docs/parity-inventory.md`.
