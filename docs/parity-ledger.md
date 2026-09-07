# File-level upstream parity ledger

Generated from the pinned source checkouts with `scripts/generate_parity_ledger.py`. Every tracked upstream file has exactly one classification.

## three-axes-framework

| Source file | Classification |
| --- | --- |
| `.claude-plugin/plugin.json` | translated manifest or Codex route |
| `.github/workflows/ci.yml` | consolidated CI or source release packaging |
| `.gitignore` | source-repository-only documentation/release packaging |
| `CHANGELOG.md` | source-repository-only documentation/release packaging |
| `CONTRIBUTING.md` | source-repository-only documentation/release packaging |
| `LICENSE` | copied runtime |
| `README.md` | source-repository-only documentation/release packaging |
| `commands/three-axes-audit.md` | translated manifest or Codex route |
| `commands/three-axes-framework.md` | translated manifest or Codex route |
| `commands/three-axes-handoff.md` | translated manifest or Codex route |
| `commands/three-axes-log.md` | translated manifest or Codex route |
| `commands/three-axes-mode.md` | translated manifest or Codex route |
| `commands/three-axes-set.md` | translated manifest or Codex route |
| `commands/three-axes-setup.md` | translated manifest or Codex route |
| `commands/three-axes-status.md` | translated manifest or Codex route |
| `commands/three-axes.md` | translated manifest or Codex route |
| `docs/superpowers/plans/2026-03-19-three-axes-v1.1.0.md` | source-repository-only documentation/release packaging |
| `docs/superpowers/specs/2026-03-19-three-axes-commands-design.md` | source-repository-only documentation/release packaging |
| `hooks/configure-profile.mjs` | copied runtime |
| `hooks/hooks.json` | copied runtime |
| `hooks/inject-framework.mjs` | copied runtime |
| `hooks/lib/__tests__/profile.test.mjs` | copied runtime |
| `hooks/lib/profile.mjs` | copied runtime |
| `hooks/lib/setup.mjs` | copied runtime |
| `hooks/require-profile.mjs` | copied runtime |
| `skills/three-axes-framework/SKILL.md` | copied runtime |
| `tests/plugin-structure.test.mjs` | copied verification |
| `tests/setup-gate.test.mjs` | copied verification |

## sage-instructor

| Source file | Classification |
| --- | --- |
| `.claude-plugin/plugin.json` | translated manifest or Codex route |
| `.github/workflows/tier1-checks.yml` | consolidated CI or source release packaging |
| `.gitignore` | source-repository-only documentation/release packaging |
| `CHANGELOG.md` | source-repository-only documentation/release packaging |
| `CONTRIBUTING.md` | source-repository-only documentation/release packaging |
| `LICENSE` | copied runtime |
| `README.md` | source-repository-only documentation/release packaging |
| `commands/sage-challenge.md` | translated manifest or Codex route |
| `commands/sage-checkpoint.md` | translated manifest or Codex route |
| `commands/sage-drill.md` | translated manifest or Codex route |
| `commands/sage-exercise.md` | translated manifest or Codex route |
| `commands/sage-explain.md` | translated manifest or Codex route |
| `commands/sage-help.md` | translated manifest or Codex route |
| `commands/sage-hint.md` | translated manifest or Codex route |
| `commands/sage-lesson.md` | translated manifest or Codex route |
| `commands/sage-new-track.md` | translated manifest or Codex route |
| `commands/sage-next.md` | translated manifest or Codex route |
| `commands/sage-phase.md` | translated manifest or Codex route |
| `commands/sage-progress.md` | translated manifest or Codex route |
| `commands/sage-recap.md` | translated manifest or Codex route |
| `commands/sage-reset.md` | translated manifest or Codex route |
| `commands/sage-review.md` | translated manifest or Codex route |
| `commands/sage-start.md` | translated manifest or Codex route |
| `commands/sage-status.md` | translated manifest or Codex route |
| `commands/sage-stuck.md` | translated manifest or Codex route |
| `commands/sage-switch.md` | translated manifest or Codex route |
| `commands/sage-tracks.md` | translated manifest or Codex route |
| `scripts/check_framework_drift.py` | copied runtime |
| `skills/sage-instructor/SKILL.md` | copied runtime |
| `skills/sage-instructor/curricula/TEMPLATE.md` | copied runtime |
| `skills/sage-instructor/curricula/python-basics.md` | copied runtime |
| `skills/sage-instructor/curricula/rust-cli.md` | copied runtime |
| `skills/sage-instructor/references/.three-axes-upstream-snapshot.md` | copied runtime |
| `skills/sage-instructor/references/learner-profile-template.md` | copied runtime |
| `skills/sage-instructor/references/philosophy.md` | copied runtime |
| `tests/README.md` | copied verification |
| `tests/check_progress_schema.py` | copied verification |
| `tests/fixtures/invalid-bad-json/.sage-progress.json` | copied verification |
| `tests/fixtures/invalid-missing-profile/.sage-progress.json` | copied verification |
| `tests/fixtures/invalid-review-due-dangling/.sage-progress.json` | copied verification |
| `tests/fixtures/invalid-streak-overlap/.sage-progress.json` | copied verification |
| `tests/fixtures/invalid-topic-key/.sage-progress.json` | copied verification |
| `tests/fixtures/valid-track-complete/.sage-profile.md` | copied verification |
| `tests/fixtures/valid-track-complete/.sage-progress.json` | copied verification |
| `tests/fixtures/valid/.sage-profile.md` | copied verification |
| `tests/fixtures/valid/.sage-progress.json` | copied verification |
| `tests/run_scenario_prompt.md` | copied verification |
| `tests/scenarios/01-onboarding-and-profile-location.md` | copied verification |
| `tests/scenarios/02-topic-key-consistency.md` | copied verification |
| `tests/scenarios/03-toolchain-vs-learner-bug.md` | copied verification |
| `tests/scenarios/04-hint-streak-scoping-and-decline.md` | copied verification |
| `tests/scenarios/05-track-completion-handling.md` | copied verification |
| `tests/scenarios/06-custom-track-creation.md` | copied verification |
| `tests/scenarios/07-axis-recalibration-accept.md` | copied verification |
| `tests/scenarios/08-multi-track-switching.md` | copied verification |
| `tests/scenarios/09-grounding-research-trigger.md` | copied verification |
| `tests/scenarios/10-track-setup-topic-shortcut.md` | copied verification |
| `tests/test_check_progress_schema.py` | copied verification |

## whiting

| Source file | Classification |
| --- | --- |
| `.claude-plugin/plugin.json` | translated manifest or Codex route |
| `.github/workflows/release.yml` | consolidated CI or source release packaging |
| `.gitignore` | source-repository-only documentation/release packaging |
| `AGENTS.md` | source-repository-only documentation/release packaging |
| `JOURNAL.md` | source-repository-only documentation/release packaging |
| `CHANGELOG.md` | source-repository-only documentation/release packaging |
| `CLAUDE.md` | source-repository-only documentation/release packaging |
| `LICENSE` | copied runtime |
| `README.md` | source-repository-only documentation/release packaging |
| `docs/superpowers/plans/2026-07-04-whiting-badges-metadata.md` | source-repository-only documentation/release packaging |
| `docs/superpowers/plans/2026-07-04-whiting-plugin.md` | source-repository-only documentation/release packaging |
| `docs/superpowers/specs/2026-07-04-whiting-badges-metadata-design.md` | source-repository-only documentation/release packaging |
| `docs/superpowers/specs/2026-07-04-whiting-plugin-design.md` | source-repository-only documentation/release packaging |
| `scripts/extract_changelog.py` | copied runtime |
| `scripts/hooks/commit-msg` | copied runtime |
| `scripts/hooks/pre-push` | copied runtime |
| `scripts/inspect_repo.sh` | copied runtime |
| `scripts/manifest_version.py` | copied runtime |
| `scripts/merge_agents_md.py` | copied runtime |
| `scripts/render_template.py` | copied runtime |
| `scripts/run_tests.sh` | copied runtime |
| `scripts/shields_escape.py` | copied runtime |
| `scripts/suggest_version_bump.py` | copied runtime |
| `skills/commit-conventions/SKILL.md` | copied runtime |
| `skills/inspect/SKILL.md` | copied runtime |
| `skills/repo-init/SKILL.md` | copied runtime |
| `skills/semver-release/SKILL.md` | copied runtime |
| `templates/AGENTS.md.tmpl` | copied runtime |
| `templates/JOURNAL.md.tmpl` | copied runtime |
| `templates/CHANGELOG.md.tmpl` | copied runtime |
| `templates/CLAUDE.md.tmpl` | copied runtime |
| `templates/LICENSE-MIT.tmpl` | copied runtime |
| `templates/README.md.tmpl` | copied runtime |
| `tests/test_commit_msg_hook.sh` | copied verification |
| `tests/test_inspect_repo.sh` | copied verification |
| `tests/test_pre_push_hook.sh` | copied verification |
| `tests/test_render_template.py` | copied verification |
| `tests/test_shields_escape.py` | copied verification |
| `tests/test_suggest_version_bump.py` | copied verification |
| `tests/test_suggest_version_bump_cli.py` | copied verification |
| `tests/test_templates_render.py` | copied verification |

## lux-swiss

| Source file | Classification |
| --- | --- |
| `.claude-plugin/plugin.json` | translated manifest or Codex route |
| `.github/workflows/release.yml` | consolidated CI or source release packaging |
| `.gitignore` | source-repository-only documentation/release packaging |
| `AGENTS.md` | source-repository-only documentation/release packaging |
| `CHANGELOG.md` | source-repository-only documentation/release packaging |
| `CLAUDE.md` | source-repository-only documentation/release packaging |
| `CONTRIBUTING.md` | source-repository-only documentation/release packaging |
| `HOUSE-MARK.md` | source-repository-only documentation/release packaging |
| `LICENSE` | copied runtime |
| `LICENSE-DESIGN` | copied runtime |
| `README.md` | source-repository-only documentation/release packaging |
| `docs/PROMOTION.md` | source-repository-only documentation/release packaging |
| `docs/assets/charts.png` | source-repository-only documentation/release packaging |
| `docs/assets/components.png` | source-repository-only documentation/release packaging |
| `docs/assets/hero-dark.png` | source-repository-only documentation/release packaging |
| `docs/assets/hero-light.png` | source-repository-only documentation/release packaging |
| `docs/assets/images.png` | source-repository-only documentation/release packaging |
| `docs/assets/palette.png` | source-repository-only documentation/release packaging |
| `docs/assets/social-card.png` | source-repository-only documentation/release packaging |
| `docs/assets/text-length.png` | source-repository-only documentation/release packaging |
| `docs/assets/type-registers.png` | source-repository-only documentation/release packaging |
| `docs/index.html` | source-repository-only documentation/release packaging |
| `docs/superpowers/plans/2026-07-05-showcase-landing-page.md` | source-repository-only documentation/release packaging |
| `docs/superpowers/plans/2026-07-06-rebrand-lux-swiss.md` | source-repository-only documentation/release packaging |
| `docs/superpowers/plans/2026-07-06-structural-block-lux-swiss.md` | source-repository-only documentation/release packaging |
| `docs/superpowers/plans/2026-07-07-accent-buttons-and-cards.md` | source-repository-only documentation/release packaging |
| `docs/superpowers/plans/2026-07-07-showcase-content-expansion.md` | source-repository-only documentation/release packaging |
| `docs/superpowers/plans/2026-07-07-stripe-reuse-and-hover-hierarchy.md` | source-repository-only documentation/release packaging |
| `docs/superpowers/specs/2026-07-05-showcase-landing-page-design.md` | source-repository-only documentation/release packaging |
| `docs/superpowers/specs/2026-07-06-structural-block-and-duotone-weight-highlight-design.md` | source-repository-only documentation/release packaging |
| `docs/superpowers/specs/2026-07-07-accent-buttons-and-cards-design.md` | source-repository-only documentation/release packaging |
| `docs/superpowers/specs/2026-07-07-showcase-content-expansion-design.md` | source-repository-only documentation/release packaging |
| `docs/superpowers/specs/2026-07-07-stripe-reuse-and-hover-hierarchy-design.md` | source-repository-only documentation/release packaging |
| `scripts/capture/.gitignore` | source-repository-only documentation/release packaging |
| `scripts/capture/capture.mjs` | source-repository-only documentation/release packaging |
| `scripts/capture/package-lock.json` | source-repository-only documentation/release packaging |
| `scripts/capture/package.json` | source-repository-only documentation/release packaging |
| `scripts/capture/verify-philosophy.mjs` | source-repository-only documentation/release packaging |
| `scripts/extract_changelog.py` | source-repository-only documentation/release packaging |
| `scripts/hooks/commit-msg` | source-repository-only documentation/release packaging |
| `scripts/hooks/pre-push` | source-repository-only documentation/release packaging |
| `scripts/suggest_version_bump.py` | source-repository-only documentation/release packaging |
| `skills/lux-swiss/SKILL.md` | copied runtime |
| `skills/lux-swiss/assets/theme.css` | copied runtime |
| `skills/lux-swiss/references/components.md` | copied runtime |

## hannah

| Source file | Classification |
| --- | --- |
| `.claude-plugin/plugin.json` | translated manifest or Codex route |
| `.github/workflows/ci.yml` | consolidated CI or source release packaging |
| `.github/workflows/installers.yml` | consolidated CI or source release packaging |
| `.github/workflows/release.yml` | consolidated CI or source release packaging |
| `.gitignore` | source-repository-only documentation/release packaging |
| `AGENTS.md` | source-repository-only documentation/release packaging |
| `CHANGELOG.md` | source-repository-only documentation/release packaging |
| `CLAUDE.md` | source-repository-only documentation/release packaging |
| `LICENSE` | copied runtime |
| `README.md` | copied runtime |
| `ROADMAP.md` | source-repository-only documentation/release packaging |
| `assets/.gitkeep` | source-repository-only documentation/release packaging |
| `assets/logo-badge.png` | source-repository-only documentation/release packaging |
| `assets/logo-vector.png` | source-repository-only documentation/release packaging |
| `commands/strategy.md` | translated manifest or Codex route |
| `hannah/__init__.py` | copied runtime |
| `hannah/__main__.py` | copied runtime |
| `hannah/analyzers/__init__.py` | copied runtime |
| `hannah/analyzers/repo.py` | copied runtime |
| `hannah/catalog/__init__.py` | copied runtime |
| `hannah/catalog/benchmarks.py` | copied runtime |
| `hannah/catalog/ollama.py` | copied runtime |
| `hannah/cli.py` | copied runtime |
| `hannah/hardware/__init__.py` | copied runtime |
| `hannah/hardware/detect.py` | copied runtime |
| `hannah/models/__init__.py` | copied runtime |
| `hannah/models/registry.py` | copied runtime |
| `hannah/reporters/__init__.py` | copied runtime |
| `hannah/reporters/console.py` | copied runtime |
| `hannah/reporters/json.py` | copied runtime |
| `hannah/reporters/notes.py` | copied runtime |
| `pyproject.toml` | copied runtime |
| `scripts/build/pyinstaller_entry.py` | source-repository-only documentation/release packaging |
| `scripts/build/windows/hannah.wxs` | source-repository-only documentation/release packaging |
| `scripts/bump_version.py` | source-repository-only documentation/release packaging |
| `scripts/commit_msg_version_bump.py` | source-repository-only documentation/release packaging |
| `scripts/extract_changelog.py` | source-repository-only documentation/release packaging |
| `scripts/hooks/commit-msg` | source-repository-only documentation/release packaging |
| `scripts/hooks/post-commit` | source-repository-only documentation/release packaging |
| `scripts/hooks/pre-push` | source-repository-only documentation/release packaging |
| `scripts/post_commit_version_bump.py` | source-repository-only documentation/release packaging |
| `scripts/pre_commit_version_bump.py` | source-repository-only documentation/release packaging |
| `scripts/suggest_version_bump.py` | source-repository-only documentation/release packaging |
| `skills/hannah/SKILL.md` | copied runtime |
| `tests/test_smoke.py` | copied verification |

## tri-swiss

| Source file | Classification |
| --- | --- |
| `.claude-plugin/plugin.json` | translated manifest or Codex route |
| `.github/workflows/release.yml` | consolidated CI or source release packaging |
| `.gitignore` | source-repository-only documentation/release packaging |
| `AGENTS.md` | source-repository-only documentation/release packaging |
| `CHANGELOG.md` | source-repository-only documentation/release packaging |
| `CLAUDE.md` | source-repository-only documentation/release packaging |
| `CONTRIBUTING.md` | source-repository-only documentation/release packaging |
| `HOUSE-MARK.md` | source-repository-only documentation/release packaging |
| `LICENSE` | copied runtime |
| `LICENSE-DESIGN` | copied runtime |
| `README.md` | source-repository-only documentation/release packaging |
| `docs/assets/charts.png` | source-repository-only documentation/release packaging |
| `docs/assets/closing-band.png` | source-repository-only documentation/release packaging |
| `docs/assets/components.png` | source-repository-only documentation/release packaging |
| `docs/assets/hero-dark.png` | source-repository-only documentation/release packaging |
| `docs/assets/hero-light.png` | source-repository-only documentation/release packaging |
| `docs/assets/images.png` | source-repository-only documentation/release packaging |
| `docs/assets/palette.png` | source-repository-only documentation/release packaging |
| `docs/assets/social-card.png` | source-repository-only documentation/release packaging |
| `docs/assets/text-length.png` | source-repository-only documentation/release packaging |
| `docs/assets/turquoise-moment.png` | source-repository-only documentation/release packaging |
| `docs/assets/type-registers.png` | source-repository-only documentation/release packaging |
| `docs/index.html` | source-repository-only documentation/release packaging |
| `docs/superpowers/plans/2026-07-06-colorful-accents-drop-jost.md` | source-repository-only documentation/release packaging |
| `docs/superpowers/plans/2026-07-06-rebrand-tri-swiss.md` | source-repository-only documentation/release packaging |
| `docs/superpowers/plans/2026-07-06-structural-block-tri-swiss.md` | source-repository-only documentation/release packaging |
| `docs/superpowers/plans/2026-07-06-tri-swiss-implementation.md` | source-repository-only documentation/release packaging |
| `docs/superpowers/plans/2026-07-07-accent-buttons-cards-and-hero-turquoise.md` | source-repository-only documentation/release packaging |
| `docs/superpowers/plans/2026-07-07-showcase-content-expansion.md` | source-repository-only documentation/release packaging |
| `docs/superpowers/plans/2026-07-07-turquoise-structural-block-and-hovers.md` | source-repository-only documentation/release packaging |
| `docs/superpowers/specs/2026-07-06-colorful-accents-drop-jost-design.md` | source-repository-only documentation/release packaging |
| `docs/superpowers/specs/2026-07-06-rebrand-lux-swiss-and-house-mark-design.md` | source-repository-only documentation/release packaging |
| `docs/superpowers/specs/2026-07-06-structural-block-and-duotone-weight-highlight-design.md` | source-repository-only documentation/release packaging |
| `docs/superpowers/specs/2026-07-06-tri-swiss-design.md` | source-repository-only documentation/release packaging |
| `docs/superpowers/specs/2026-07-07-accent-buttons-cards-and-hero-turquoise-design.md` | source-repository-only documentation/release packaging |
| `docs/superpowers/specs/2026-07-07-showcase-content-expansion-design.md` | source-repository-only documentation/release packaging |
| `docs/superpowers/specs/2026-07-07-turquoise-structural-block-and-hover-hierarchy-design.md` | source-repository-only documentation/release packaging |
| `scripts/capture/.gitignore` | source-repository-only documentation/release packaging |
| `scripts/capture/capture.mjs` | source-repository-only documentation/release packaging |
| `scripts/capture/package-lock.json` | source-repository-only documentation/release packaging |
| `scripts/capture/package.json` | source-repository-only documentation/release packaging |
| `scripts/capture/verify-philosophy.mjs` | source-repository-only documentation/release packaging |
| `scripts/extract_changelog.py` | source-repository-only documentation/release packaging |
| `scripts/hooks/commit-msg` | source-repository-only documentation/release packaging |
| `scripts/hooks/pre-push` | source-repository-only documentation/release packaging |
| `scripts/suggest_version_bump.py` | source-repository-only documentation/release packaging |
| `skills/tri-swiss/SKILL.md` | copied runtime |
| `skills/tri-swiss/assets/theme.css` | copied runtime |
| `skills/tri-swiss/references/components.md` | copied runtime |
