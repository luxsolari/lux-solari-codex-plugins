# Codex Plugin Parity Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a standalone Codex marketplace whose six packages preserve every runtime capability of Lux Solari's published Claude Code plugins.

**Architecture:** Each plugin is a self-contained Codex package under `plugins/` with a validated manifest and native skills. Host-specific entry points are translated, not discarded: Three Axes uses a Codex `SessionStart` hook; Sage exposes its full command vocabulary as skill routes; Whiting ships its scripts/templates; Hannah ships its Python engine; and the Swiss systems ship their exact themes and component references.

**Tech Stack:** Codex marketplace/plugin manifests, Markdown skills and references, Node.js 20+ for Three Axes hooks, Python 3.11+ standard library for Hannah and Whiting utilities, POSIX shell, GitHub Actions templates, Tailwind CSS 4 theme files.

## Global Constraints

- Port against the source revisions recorded below; do not summarize, selectively recreate, or silently omit a source runtime file.
- Preserve published plugin names and source versions: Three Axes `1.2.1`, Sage `1.7.2`, Whiting `0.2.0`, Lux Swiss `2.3.0`, Hannah `0.10.6`, Tri-Swiss `1.1.0`.
- Preserve upstream licenses: MIT for Three Axes, Sage, Whiting, and Hannah; dual MIT/X11 (`LICENSE`) plus CC-BY-SA-4.0 (`LICENSE-DESIGN`) for Lux Swiss and Tri-Swiss, with the design-system material under CC-BY-SA-4.0.
- Keep all packages offline-capable except Hannah's explicitly optional live benchmark/library enrichment and Sage's explicitly conditional current-docs research.
- Keep Three Axes lifecycle parity: inject on `startup`, `resume`, `clear`, and `compact`; clear only the session override on `startup`.
- Preserve all learner data and Three Axes project files as user/project state, never inside an installed plugin directory.
- Never replace an existing project file, hook path, release workflow, GitHub setting, or learner profile without the confirmation rules already defined by the source skills.
- Every manifest, declared skill path, hook path, script path, and marketplace path must exist and pass validation before handoff. Validate manifest shape with `validate_plugin.py`; validate hook discovery and execution with a real disposable Codex profile, because generic manifest validation intentionally does not model hook configuration.
- Treat the following as explicit host translations, not omissions: Claude command files become documented Codex skill routes; Claude hook-manifest pointers become Codex's canonical auto-discovered `hooks/hooks.json`; and Sage's Claude package dependency becomes a self-contained instructional contract plus optional cooperation with an installed Three Axes package (Codex's verified plugin manifest contract has no package-dependency field).

## Source-of-Truth Ledger

| Plugin | Source revision | Runtime material to preserve |
| --- | --- | --- |
| Three Axes | `04346e064ffac6a3026002601571185603fc651c` | framework skill; six commands; profile library/tests; session injector/hook |
| Sage | `fe94cc3a38a733aa80bf4c92aa616a199429a3d0` | instructor skill; 20 command routes; curricula/template/references; schema validator and ten scenarios |
| Whiting | `31c545d117f99908a2256c5b0f79d64b1fe038c8` | four skills; auditor; release/version/template utilities; hooks; release workflow template; tests |
| Lux Swiss | `c255468eec1e8a81ae4cd00d74fec2a26d4293c1` | complete skill; exact Tailwind theme; component catalogue; house-mark rules |
| Hannah | `21c19d03cb6611f9d36e678e37a28817df3fe49c` | full `hannah` Python package; CLI; strategy skill; tests |
| Tri-Swiss | `51ce460204a0c7f26cc46ce966c580a1d16dce81` | complete skill; exact Tailwind theme; component catalogue; house-mark rules |

## Target File Structure

```text
.agents/plugins/marketplace.json
.github/workflows/ci.yml
plugins/
  three-axes-framework/
    .codex-plugin/plugin.json
    LICENSE
    skills/three-axes-framework/SKILL.md
    references/commands.md
    hooks/hooks.json
    hooks/inject-framework-codex.mjs
    hooks/lib/profile.mjs
    tests/profile.test.mjs
    tests/session-start.test.mjs
  sage-instructor/
    .codex-plugin/plugin.json
    LICENSE
    skills/sage-instructor/SKILL.md
    skills/sage-instructor/curricula/{TEMPLATE,python-basics,rust-cli}.md
    skills/sage-instructor/references/{philosophy,learner-profile-template,commands,three-axes-contract}.md
    skills/sage-instructor/references/.three-axes-upstream-snapshot.md
    scripts/check_framework_drift.py
    tests/{check_progress_schema.py,fixtures,scenarios,run_scenario_prompt.md,test_check_progress_schema.py}
  whiting/
    .codex-plugin/plugin.json
    LICENSE
    skills/{repo-init,commit-conventions,inspect,semver-release}/SKILL.md
    scripts/{inspect_repo.sh,extract_changelog.py,render_template.py,shields_escape.py,suggest_version_bump.py,run_tests.sh}
    scripts/hooks/{commit-msg,pre-push}
    templates/{AGENTS.md.tmpl,CHANGELOG.md.tmpl,CLAUDE.md.tmpl,LICENSE-MIT.tmpl,README.md.tmpl,release.yml}
    tests/
  lux-swiss/
    .codex-plugin/plugin.json
    skills/lux-swiss/{SKILL.md,assets/theme.css,references/components.md,references/HOUSE-MARK.md}
    {LICENSE,LICENSE-DESIGN}
  hannah/
    .codex-plugin/plugin.json
    LICENSE
    README.md
    skills/hannah/{SKILL.md,references/strategy.md}
    hannah/{__init__,__main__,cli}.py and analyzer/catalog/hardware/models/reporter modules
    pyproject.toml
    scripts/run-hannah
    tests/test_smoke.py
  tri-swiss/
    .codex-plugin/plugin.json
    skills/tri-swiss/{SKILL.md,assets/theme.css,references/components.md,references/HOUSE-MARK.md}
    {LICENSE,LICENSE-DESIGN}
README.md
LICENSE
tests/test_marketplace.py
```

## Capability Matrix

| Package | Must work after port |
| --- | --- |
| Three Axes | six behavioral principles; three-layer profile cascade; defaults/source labels; five presets; granular set; setup/status/overview routes; four conversational signals; all four session events; profile validation and malformed-file resilience |
| Sage | onboarding; profile/track persistence; three-axis calibration; two bundled curricula; custom curriculum generation with conditional current-docs research; all 20 navigation/progress/mode/interaction/track/meta routes; seven-step lesson; verification gate; hint escalation/streaks; confidence/review queue; track completion/switch/reset; schema and scenario coverage |
| Whiting | repo bootstrap; conventional-commit and no-direct-push hooks; AGENTS/CLAUDE rules; read-only compliance audit; changelog release workflow; release backfill; semver classification; all templates/utilities/tests |
| Lux Swiss | all house-mark rules, exact tokens/fonts/Tailwind mappings, component catalogue, interaction/hover rules, chart policy, image/icon rules, implementation checklist |
| Hannah | positional path plus `--json`, `--track`, `--gpu`, `--ram`, `--no-color`, and `--version` CLI options; repository scan/complexity/framework detection; hardware detection and overrides; Ollama pulled-model/library scan; benchmark enrichment/cache; ranked candidates; console/JSON reports; platform race notes; strategy report/pull commands |
| Tri-Swiss | all house-mark rules, exact tokens/fonts/Tailwind mappings, component catalogue, red/turquoise governance, structural blocks, interaction/hover rules, chart policy, image/icon rules, implementation checklist |

---

### Task 1: Establish the marketplace and parity test harness

**Files:**
- Create: `.agents/plugins/marketplace.json`
- Create: `.github/workflows/ci.yml`
- Create: `tests/test_marketplace.py`
- Create: `README.md`
- Create: `LICENSE`
- Create: `.gitignore`

**Interfaces:**
- Produces: marketplace entries named exactly `three-axes-framework`, `sage-instructor`, `whiting`, `lux-swiss`, `hannah`, and `tri-swiss`.
- Produces: `tests/test_marketplace.py`, which later tasks extend with their package-specific assertions.

- [ ] **Step 1: Write the failing marketplace test**

```python
def test_marketplace_has_the_complete_published_catalog():
    names = [entry["name"] for entry in load_marketplace()["plugins"]]
    assert names == [
        "three-axes-framework", "sage-instructor", "whiting",
        "lux-swiss", "hannah", "tri-swiss",
    ]

def test_every_entry_resolves_to_a_manifest():
    for entry in load_marketplace()["plugins"]:
        plugin = REPO / entry["source"]["path"] / ".codex-plugin/plugin.json"
        assert plugin.is_file()
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `python3 -m unittest tests/test_marketplace.py -v`

Expected: FAIL because `.agents/plugins/marketplace.json` and package manifests do not yet exist.

- [ ] **Step 3: Create the catalog and root documentation**

Create the ordered local marketplace entries with `AVAILABLE` / `ON_INSTALL` policy and categories `Productivity` (Three Axes, Sage, Whiting, Hannah) and `Design` (Lux Swiss, Tri-Swiss). Write the README with the six package descriptions, local marketplace installation, the source ledger, and an explicit compatibility statement: every listed runtime capability is ported; only Claude-branded invocation wording is translated to Codex skill routing. Add one CI workflow that runs the complete validation matrix defined in Task 8 on Ubuntu with Node 20 and Python 3.11.

- [ ] **Step 4: Run the test to verify it passes**

Run: `python3 -m unittest tests/test_marketplace.py -v`

Expected: the catalog-order assertion passes; the manifest assertion will remain failing until Task 8.

- [ ] **Step 5: Commit**

```bash
git add .agents/plugins/marketplace.json .github/workflows/ci.yml tests/test_marketplace.py README.md LICENSE .gitignore
git commit -m "feat: add Codex marketplace foundation"
```

### Task 2: Port Three Axes completely, including lifecycle injection

**Files:**
- Create: `plugins/three-axes-framework/.codex-plugin/plugin.json`
- Create: `plugins/three-axes-framework/LICENSE`
- Create: `plugins/three-axes-framework/skills/three-axes-framework/SKILL.md`
- Create: `plugins/three-axes-framework/references/commands.md`
- Create: `plugins/three-axes-framework/hooks/hooks.json`
- Create: `plugins/three-axes-framework/hooks/inject-framework-codex.mjs`
- Create: `plugins/three-axes-framework/hooks/lib/profile.mjs`
- Create: `plugins/three-axes-framework/tests/profile.test.mjs`
- Create: `plugins/three-axes-framework/tests/session-start.test.mjs`

**Interfaces:**
- Consumes: Codex plugin root variable `${PLUGIN_ROOT}` and `SessionStart` hook output contract.
- Produces: `resolveProfile(globalPath, projectPath, sessionPath) -> { values, sources }`.
- Produces: Four user routes: `three-axes setup`, `three-axes status`, `three-axes mode <preset>`, and `three-axes set <axis>=<value> [--project|--global]`; their `three-axes-framework` overview alias; and four conversational mode signals.

- [ ] **Step 1: Write failing profile and hook tests**

```js
assert.deepEqual(resolveProfile(missing, missing, missing).values,
  { mastery: 'medium', consequence: 'medium', intent: 'balanced' });
assert.equal(resolveProfile(global, project, session).sources.mastery, 'session');
assert.match(runHook('resume'), /"hookEventName":"SessionStart"/);
assert.doesNotThrow(() => runHookWithMalformedProfile());
```

Include fixture cases for defaults, per-axis precedence, unknown-axis validation, malformed JSON, startup-only deletion of the session profile, and retention of that session profile on `resume`, `clear`, and `compact`.

- [ ] **Step 2: Run the tests to verify they fail**

Run: `node --test plugins/three-axes-framework/tests/*.test.mjs`

Expected: FAIL because the profile library and Codex hook are absent.

- [ ] **Step 3: Transfer the framework material and make only host-specific substitutions**

Copy the published framework body, all six principles, axis tables, presets, command rules, and MIT `LICENSE` verbatim into the package. Port the profile helper and preserve `.three-axes.json` as the project file. Use `~/.codex/three-axes-profile.json` and `~/.codex/three-axes-session.json` as Codex-owned global/session paths; when the Codex global file is absent, read the legacy `~/.claude/three-axes-profile.json` once as a migration fallback.

Create the canonical auto-discovered `hooks/hooks.json` with all four matchers; deliberately omit a `hooks` key from `plugin.json`. This is the Codex-compatible form that both activates hooks and keeps the generic package validator authoritative for the supported manifest schema. The wrapper must derive its root from its own path, clear the session file only for `startup`, read the full skill body, resolve the cascade, and write the Codex `hookSpecificOutput.additionalContext` JSON. Keep `suppressOutput: true` so normal sessions are not polluted.

Map every original slash command to explicit skill-route phrases and default prompts; retain usage errors, all five preset values, merge-before-write behavior, source labels, profile setup questions, and the four conversational signal durations.

- [ ] **Step 4: Run the tests to verify they pass**

Run: `node --test plugins/three-axes-framework/tests/*.test.mjs`

Expected: PASS with lifecycle and cascade tests proving profile parity.

- [ ] **Step 5: Validate the package, hook discovery, and commit**

```bash
python3 /Users/luxsolari/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/three-axes-framework
# In a disposable CODEX_HOME: add the local marketplace, install Three Axes,
# and invoke each SessionStart matcher. Assert its additionalContext is present
# and that only startup removes the session override.
git add plugins/three-axes-framework tests/test_marketplace.py
git commit -m "feat: port Three Axes framework lifecycle"
```

### Task 3: Port Sage's full instructor state machine and curricula

**Files:**
- Create: `plugins/sage-instructor/.codex-plugin/plugin.json`
- Create: `plugins/sage-instructor/LICENSE`
- Create: `plugins/sage-instructor/skills/sage-instructor/SKILL.md`
- Create: `plugins/sage-instructor/skills/sage-instructor/curricula/TEMPLATE.md`
- Create: `plugins/sage-instructor/skills/sage-instructor/curricula/python-basics.md`
- Create: `plugins/sage-instructor/skills/sage-instructor/curricula/rust-cli.md`
- Create: `plugins/sage-instructor/skills/sage-instructor/references/{philosophy.md,learner-profile-template.md,commands.md,three-axes-contract.md}`
- Create: `plugins/sage-instructor/skills/sage-instructor/references/.three-axes-upstream-snapshot.md`
- Create: `plugins/sage-instructor/scripts/{check_framework_drift.py,check_progress_schema.py}`
- Create: `plugins/sage-instructor/tests/fixtures/`, `plugins/sage-instructor/tests/scenarios/`, `plugins/sage-instructor/tests/test_check_progress_schema.py`

**Interfaces:**
- Consumes: project-root `.sage-profile.md`, `.sage-progress.json`, and curricula files.
- Produces: the documented progress schema with `active_track`, independent `tracks`, confidence/review/streak fields, and all source-compatible defaults for omitted legacy fields.
- Produces: all 20 Sage routes: start, next, lesson, challenge, checkpoint, progress, drill, review, hint, explain, stuck, recap, status, help, reset, phase, tracks, switch, new-track, and exercise.
- Produces: equivalent three-axis calibration whether or not the separately installed `three-axes-framework` package is present; when it is present, Sage explicitly cooperates with its active profile rather than creating conflicting state.

- [ ] **Step 1: Write failing schema and route-coverage tests**

```python
def test_valid_progress_fixture_passes_schema_check():
    assert check_progress(FIXTURES / "valid/.sage-progress.json") == []

def test_invalid_review_queue_is_rejected():
    errors = check_progress(FIXTURES / "invalid-review-due-dangling/.sage-progress.json")
    assert any("review_due" in error for error in errors)

def test_command_reference_contains_all_twenty_routes():
    assert set(ROUTES) == {"start", "next", "lesson", "challenge", "checkpoint", "progress", "drill", "review", "hint", "explain", "stuck", "recap", "status", "help", "reset", "phase", "tracks", "switch", "new-track", "exercise"}
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python3 -m unittest plugins/sage-instructor/tests/test_check_progress_schema.py -v`

Expected: FAIL because the validator, fixtures, and command reference are absent.

- [ ] **Step 3: Transfer all instructional behavior**

Copy the source skill, curricula, profile template, philosophy, `.three-axes-upstream-snapshot.md`, `scripts/check_framework_drift.py`, `tests/check_progress_schema.py`, valid/invalid fixtures, scenario runner prompt, all ten scenario documents, and MIT `LICENSE`. Retain the source snapshot path relationship so `check_framework_drift.py` can detect source-framework drift and update the snapshot only after an explicit reconciliation. Translate Claude's `AskUserQuestion` calls to Codex/ChatGPT structured user-input prompts while retaining every choice, confirmation point, and one-question-at-a-time rule.

Create `references/commands.md` from every source command file and make the skill route both the original slash-like forms and plain-language equivalents. Create `references/three-axes-contract.md`: it must carry the complete calibration semantics Sage needs, locate and respect the Three Axes project/global/session state when that package is installed, and perform the same calibration locally when it is not. This replaces only the upstream marketplace auto-install mechanism; no instructional or state-machine behavior may depend on an undeclared host capability. Preserve the seven-step lesson flow, verifying exercises by their curriculum `verify` command, toolchain-vs-learner failure distinction, progressive hints, confidence/review updates, axis recalibration, multi-track state isolation, full and active-only reset confirmations, custom-track grounding research, source recording, and all track-completion behavior.

- [ ] **Step 4: Run the tests to verify they pass**

Run: `python3 -m unittest plugins/sage-instructor/tests/test_check_progress_schema.py -v`

Expected: PASS for both valid fixtures and every invalid-schema rejection. Manually review each of the ten scenario documents against the Codex route instructions and record no unsupported branch.

- [ ] **Step 5: Validate the package and commit**

```bash
python3 /Users/luxsolari/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/sage-instructor
git add plugins/sage-instructor tests/test_marketplace.py
git commit -m "feat: port Sage instructor workflows"
```

### Task 4: Port Whiting's reusable release-discipline toolkit

**Files:**
- Create: `plugins/whiting/.codex-plugin/plugin.json`
- Create: `plugins/whiting/LICENSE`
- Create: `plugins/whiting/skills/{repo-init,commit-conventions,inspect,semver-release}/SKILL.md`
- Create: `plugins/whiting/scripts/{inspect_repo.sh,extract_changelog.py,render_template.py,shields_escape.py,suggest_version_bump.py,run_tests.sh}`
- Create: `plugins/whiting/scripts/hooks/{commit-msg,pre-push}`
- Create: `plugins/whiting/templates/{AGENTS.md.tmpl,CHANGELOG.md.tmpl,CLAUDE.md.tmpl,LICENSE-MIT.tmpl,README.md.tmpl,release.yml}`
- Create: `plugins/whiting/tests/` copied from the source test suite

**Interfaces:**
- Produces: a read-only `inspect_repo.sh` audit; Conventional Commit and protected-branch hooks; `extract(version)`, `render(template, mapping)`, and `classify_bump(subjects, bodies)` Python interfaces.
- Produces: four independently invocable Codex skills matching the source skills.

- [ ] **Step 1: Copy the source tests before implementation**

Copy `test_commit_msg_hook.sh`, `test_inspect_repo.sh`, `test_pre_push_hook.sh`, `test_render_template.py`, `test_shields_escape.py`, `test_suggest_version_bump.py`, `test_suggest_version_bump_cli.py`, and `test_templates_render.py` unchanged into the package test directory.

- [ ] **Step 2: Run the tests to verify they fail**

Run: `sh plugins/whiting/scripts/run_tests.sh`

Expected: FAIL because the scripts, templates, and hooks are absent.

- [ ] **Step 3: Transfer every operational artifact and route**

Copy the four skills, six utility scripts, two executable hooks, five templates, release workflow, and MIT `LICENSE` verbatim. Store the workflow as `templates/release.yml` and have the release skill install it at `.github/workflows/release.yml` exactly as the source does.

Keep every safety check: read-only inspect behavior; existing-file confirmation; existing hook-path confirmation; existing release-workflow stop; explicit confirmation before tags/pushes; tag-scheme consistency; best-effort GitHub metadata/branch-protection checks; branch-and-PR discipline. Preserve the source test commands and executable modes.

- [ ] **Step 4: Run the tests to verify they pass**

Run: `sh plugins/whiting/scripts/run_tests.sh`

Expected: PASS, including semver bump classification, template placeholder failures, commit rejection, protected-branch rejection, and no-write inspect audit.

- [ ] **Step 5: Validate the package and commit**

```bash
python3 /Users/luxsolari/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/whiting
git add plugins/whiting tests/test_marketplace.py
git commit -m "feat: port Whiting release discipline"
```

### Task 5: Port Lux Swiss without weakening its design governance

**Files:**
- Create: `plugins/lux-swiss/.codex-plugin/plugin.json`
- Create: `plugins/lux-swiss/skills/lux-swiss/SKILL.md`
- Create: `plugins/lux-swiss/skills/lux-swiss/assets/theme.css`
- Create: `plugins/lux-swiss/skills/lux-swiss/references/{components.md,HOUSE-MARK.md}`
- Create: `plugins/lux-swiss/LICENSE`
- Create: `plugins/lux-swiss/LICENSE-DESIGN`
- Create: `plugins/lux-swiss/tests/test_theme_contract.py`

**Interfaces:**
- Produces: exact CSS custom-property and Tailwind token contract from the published `theme.css`.
- Produces: all visual, component, chart, typography, hover, image, icon, and implementation-checklist rules from the published skill and house mark.

- [ ] **Step 1: Write the failing theme contract test**

```python
def test_lux_swiss_theme_has_required_tokens():
    css = THEME.read_text()
    for token in ("--background", "--foreground", "--primary", "--font-mono", "--font-sans"):
        assert token in css
    assert "box-shadow" not in css
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `python3 -m unittest plugins/lux-swiss/tests/test_theme_contract.py -v`

Expected: FAIL because the exact theme is absent.

- [ ] **Step 3: Transfer the complete design-system runtime**

Copy the published `SKILL.md`, `assets/theme.css`, `references/components.md`, `HOUSE-MARK.md`, `LICENSE`, and `LICENSE-DESIGN` byte-for-byte. Use `CC-BY-SA-4.0` in the manifest for the installed design-system content and retain the separate MIT/X11 code/tooling license file. Retain Space Mono/Space Grotesk and governed Geist/Jost variants, hard borders, no shadows, two-color-plus-red governance, hand-rolled SVG default, Observable Plot exception, component patterns, image treatment, and every implementation checklist rule.

- [ ] **Step 4: Run the test to verify it passes**

Run: `python3 -m unittest plugins/lux-swiss/tests/test_theme_contract.py -v`

Expected: PASS, confirming the copied token contract and shadow prohibition.

- [ ] **Step 5: Validate the package and commit**

```bash
python3 /Users/luxsolari/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/lux-swiss
git add plugins/lux-swiss tests/test_marketplace.py
git commit -m "feat: port Lux Swiss design system"
```

### Task 6: Port Tri-Swiss without weakening its accent governance

**Files:**
- Create: `plugins/tri-swiss/.codex-plugin/plugin.json`
- Create: `plugins/tri-swiss/skills/tri-swiss/SKILL.md`
- Create: `plugins/tri-swiss/skills/tri-swiss/assets/theme.css`
- Create: `plugins/tri-swiss/skills/tri-swiss/references/{components.md,HOUSE-MARK.md}`
- Create: `plugins/tri-swiss/LICENSE`
- Create: `plugins/tri-swiss/LICENSE-DESIGN`
- Create: `plugins/tri-swiss/tests/test_theme_contract.py`

**Interfaces:**
- Produces: exact CSS/Tailwind tokens, including `--highlight` and its foreground token.
- Produces: all red/turquoise governance, structural blocks, chart, icon, typography, component, and hover rules.

- [ ] **Step 1: Write the failing accent-governance test**

```python
def test_tri_swiss_has_governed_highlight_tokens():
    css = THEME.read_text()
    assert "--highlight" in css
    assert "--highlight-foreground" in css
    assert "box-shadow" not in css

def test_component_reference_documents_the_red_turquoise_exception():
    assert "Tri-part segment stripe" in COMPONENTS.read_text()
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `python3 -m unittest plugins/tri-swiss/tests/test_theme_contract.py -v`

Expected: FAIL because the theme and component catalogue are absent.

- [ ] **Step 3: Transfer the complete design-system runtime**

Copy the published `SKILL.md`, `assets/theme.css`, `references/components.md`, `HOUSE-MARK.md`, `LICENSE`, and `LICENSE-DESIGN` byte-for-byte. Preserve the dual-license scope and all baseline Swiss rules and the Tri-Swiss-only red/turquoise restrictions, tri-part stripe exception, turquoise second-series/chart guidance, sidebar/hero/closing-band options, Geist/Jost governance, and hover hierarchy.

- [ ] **Step 4: Run the test to verify it passes**

Run: `python3 -m unittest plugins/tri-swiss/tests/test_theme_contract.py -v`

Expected: PASS, proving the full highlight token and structural exception material is available.

- [ ] **Step 5: Validate the package and commit**

```bash
python3 /Users/luxsolari/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/tri-swiss
git add plugins/tri-swiss tests/test_marketplace.py
git commit -m "feat: port Tri-Swiss design system"
```

### Task 7: Ship Hannah's complete recommendation engine

**Files:**
- Create: `plugins/hannah/.codex-plugin/plugin.json`
- Create: `plugins/hannah/LICENSE`
- Create: `plugins/hannah/README.md`
- Create: `plugins/hannah/skills/hannah/SKILL.md`
- Create: `plugins/hannah/skills/hannah/references/strategy.md`
- Create: `plugins/hannah/pyproject.toml`
- Create: `plugins/hannah/scripts/run-hannah`
- Create: `plugins/hannah/hannah/` copied from the source package
- Create: `plugins/hannah/tests/test_smoke.py`

**Interfaces:**
- Produces: `python3 -m hannah [path]` with exact `--json`, `--track`, `--gpu`, `--ram`, `--no-color`, and `--version` parity.
- Produces: ranked `recommendations`, detected `discoveries`, repository profile, hardware spec, and race notes in console and JSON forms.

- [ ] **Step 1: Copy the smoke test and add CLI-contract assertions**

```python
def test_json_report_contains_full_strategy_contract():
    report = run_hannah(str(FIXTURE_REPO), "--json")
    assert {"repo", "hardware", "recommendations", "discoveries", "race_notes"} <= report.keys()

def test_hardware_overrides_are_respected():
    report = run_hannah(str(FIXTURE_REPO), "--json", "--gpu", "vram=16gb", "--ram", "32gb")
    assert report["hardware"]["gpu_vram_gb"] == 16

def test_no_color_and_version_contracts_are_available():
    assert "\x1b" not in run_hannah("--no-color")
    assert run_hannah("--version").startswith("hannah ")
```

Add an isolated-install assertion that `python3 -m pip install --no-deps .` exposes the published `hannah` console-script entry point and that `hannah --version` matches the module invocation.

- [ ] **Step 2: Run the tests to verify they fail**

Run: `cd plugins/hannah && python3 -m unittest discover -s tests -v`

Expected: FAIL because the Python package and CLI are absent.

- [ ] **Step 3: Transfer the engine, not a simplified prompt**

Copy `pyproject.toml`, `README.md`, MIT `LICENSE`, `hannah/__init__.py`, `__main__.py`, `cli.py`, every analyzer/catalog/hardware/models/reporters module, the strategy skill, command rendering rules, and the source smoke test. Keep the README next to `pyproject.toml`, as its published build metadata declares it as the project readme. Add an executable `scripts/run-hannah` that derives the package root and invokes `PYTHONPATH=<plugin-root> python3 -m hannah "$@"`, so the installed skill has the same self-contained engine discovery as the published command. Retain zero runtime dependencies and Python 3.11 floor.

Preserve repository language/framework/entry-point/token/complexity analysis; macOS/Linux/Windows/WSL hardware detection; hardware overrides; the candidate registry/scoring and benchmark weights; pulled Ollama model detection through REST and CLI; optional Ollama library discovery; optional benchmark cache/enrichment; console and JSON output; platform-specific Ollama race notes; and exact P1/P2/P3 pull/strategy guidance. The skill invokes this local engine and renders its complete output rather than replacing it with model-memory recommendations.

- [ ] **Step 4: Run the tests to verify they pass**

Run: `cd plugins/hannah && python3 -m unittest discover -s tests -v`

Expected: PASS without installing third-party runtime dependencies.

- [ ] **Step 5: Validate the package and commit**

```bash
python3 /Users/luxsolari/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/hannah
git add plugins/hannah tests/test_marketplace.py
git commit -m "feat: port Hannah strategy engine"
```

### Task 8: Finish package metadata, parity assertions, and local installation verification

**Files:**
- Modify: all six `.codex-plugin/plugin.json` files
- Modify: `tests/test_marketplace.py`
- Modify: `README.md`
- Create: `tests/test_parity_inventory.py`
- Create: `docs/parity-inventory.md`

**Interfaces:**
- Consumes: all package directories created in Tasks 2–7.
- Produces: a machine-checked source-to-target runtime inventory and a validated installable marketplace.

- [ ] **Step 1: Write the failing inventory test**

```python
REQUIRED = {
    "three-axes-framework": ["LICENSE", "skills/three-axes-framework/SKILL.md", "references/commands.md", "hooks/hooks.json", "hooks/inject-framework-codex.mjs", "hooks/lib/profile.mjs"],
    "sage-instructor": ["LICENSE", "skills/sage-instructor/SKILL.md", "skills/sage-instructor/curricula/TEMPLATE.md", "skills/sage-instructor/curricula/python-basics.md", "skills/sage-instructor/curricula/rust-cli.md", "skills/sage-instructor/references/.three-axes-upstream-snapshot.md", "skills/sage-instructor/references/three-axes-contract.md", "scripts/check_framework_drift.py", "tests/check_progress_schema.py", "tests/run_scenario_prompt.md"],
    "whiting": ["LICENSE", "scripts/inspect_repo.sh", "scripts/extract_changelog.py", "scripts/suggest_version_bump.py", "scripts/render_template.py", "scripts/shields_escape.py", "scripts/hooks/commit-msg", "scripts/hooks/pre-push", "templates/release.yml"],
    "lux-swiss": ["skills/lux-swiss/SKILL.md", "skills/lux-swiss/assets/theme.css", "skills/lux-swiss/references/components.md", "skills/lux-swiss/references/HOUSE-MARK.md", "LICENSE", "LICENSE-DESIGN"],
    "hannah": ["LICENSE", "README.md", "pyproject.toml", "scripts/run-hannah", "hannah/cli.py", "hannah/analyzers/repo.py", "hannah/catalog/benchmarks.py", "hannah/catalog/ollama.py", "hannah/hardware/detect.py", "hannah/models/registry.py", "hannah/reporters/console.py", "hannah/reporters/json.py", "hannah/reporters/notes.py"],
    "tri-swiss": ["skills/tri-swiss/SKILL.md", "skills/tri-swiss/assets/theme.css", "skills/tri-swiss/references/components.md", "skills/tri-swiss/references/HOUSE-MARK.md", "LICENSE", "LICENSE-DESIGN"],
}

def test_every_source_runtime_artifact_has_a_target():
    for plugin, paths in REQUIRED.items():
        for path in paths:
            assert_target(plugin, path)

def test_manifests_preserve_source_versions_and_licenses():
    assert manifest("hannah")["version"] == "0.10.6"
    assert manifest("lux-swiss")["license"] == "CC-BY-SA-4.0"
```

Add explicit host-adapter assertions: Three Axes has `hooks/hooks.json` and no unsupported manifest `hooks` key; every Codex route is mapped from its source command; Sage has all 20 routes and a complete `three-axes-contract.md`; and the Hannah package's console-script metadata names `hannah.cli:main`.

- [ ] **Step 2: Run the test to verify it fails**

Run: `python3 -m unittest tests/test_parity_inventory.py -v`

Expected: FAIL until each manifest and source artifact has been completed.

- [ ] **Step 3: Populate all manifests and documentation**

Set each manifest name/version/description/author/source links/license/keywords/skills/interface fields from its published source. Keep the target repository as the Codex package repository and list the originating Claude repository and source revision in `docs/parity-inventory.md`. That inventory must map every item in `REQUIRED`, every Three Axes command/preset/signal, every one of Sage's 20 routes, Whiting's four skills, and Hannah's six CLI switches to its Codex target. It must include a host-adapter table accounting for the three explicit translations in the Global Constraints, including the test that proves each substitute preserves behavior. It must also classify each remaining tracked source artifact as one of: translated manifest, copied runtime, copied verification, consolidated CI, or source-repository-only documentation/release packaging; no tracked source file may remain unclassified. Declare Three Axes' hook configuration only through its canonical `hooks/hooks.json`; keep all plugin manifests free of unsupported `hooks` or package-`dependencies` keys.

Update the README with per-plugin capability lists and exact local validation commands. It must state the Three Axes Codex state paths and legacy-read migration, Sage's persistent project files, Whiting's confirmation boundaries, Hannah's optional network modes, and the CC-BY-SA terms for the Swiss packages.

- [ ] **Step 4: Run the complete verification suite**

Run:

```bash
python3 -m unittest tests/test_marketplace.py tests/test_parity_inventory.py -v
node --test plugins/three-axes-framework/tests/*.test.mjs
python3 -m unittest plugins/sage-instructor/tests/test_check_progress_schema.py -v
sh plugins/whiting/scripts/run_tests.sh
python3 -m unittest plugins/lux-swiss/tests/test_theme_contract.py -v
cd plugins/hannah && python3 -m unittest discover -s tests -v && cd ../..
python3 -m unittest plugins/tri-swiss/tests/test_theme_contract.py -v
```

Expected: every command exits `0`.

- [ ] **Step 5: Validate every package and the marketplace**

Run:

```bash
for plugin in plugins/*; do
  python3 /Users/luxsolari/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py "$plugin"
done
python3 -m json.tool .agents/plugins/marketplace.json >/dev/null
git diff --check
```

Expected: six successful plugin validations, valid JSON, and no whitespace errors.

- [ ] **Step 6: Commit and perform a fresh-install smoke test**

```bash
git add .
git commit -m "feat: complete Codex plugin parity marketplace"
codex plugin marketplace add .
```

Expected: Codex recognizes the marketplace and exposes all six packages in catalog order. In a disposable test profile, install Three Axes and verify all four `SessionStart` invocations emit the framework and resolved profile, with startup as the only event that removes the session override. Install Sage both with and without Three Axes and verify the complete instructor calibration contract works in both states, then install Hannah with `pip --no-deps` and verify both its console-script and module CLIs before declaring the migration complete.
