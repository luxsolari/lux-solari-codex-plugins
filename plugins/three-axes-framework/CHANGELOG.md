# Changelog

All notable changes to `three-axes-framework` are documented in this file.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Releases are tagged `three-axes-framework-v<version>`; each plugin in this repository
versions and releases independently.

---

## [Unreleased]

## [1.5.1] - 2026-09-23

### Fixed
- Made first-run blocking copy identify the Three Axes Framework plugin and the
  absent persistent profile as the cause.
- Skip profile enforcement for hook events without a workspace `cwd`, allowing
  projectless prompts to continue without onboarding.
- Require an exposed Codex Desktop native question picker to be called directly
  and reserve the unavailable fallback for turns where the host omits it.

## [1.5.0] — 2026-09-07

- The changelog starts here. Everything up to and including 1.5.0 predates it;
  read the git history for that. Entries from the next release onward record
  what changed, so this file is a record rather than a reconstruction.
