# Changelog

All notable changes to `three-axes-framework` are documented in this file.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Releases are tagged `three-axes-framework-v<version>`; each plugin in this repository
versions and releases independently.

---

## [Unreleased]

## [1.6.0] - 2026-09-23

### Added
- Defined the ownership standard for generated code: it should be code the
  developer could responsibly have authored, rather than code they can
  reproduce line-by-line or recite framework/API trivia for.
- Added the explicit human ownership loop: `intent → generation → comprehension
  → challenge → evidence → ownership`.
- Made the practical comprehension gate explicit: the developer should be able
  to explain the important decisions and mechanisms tomorrow without the agent
  present.

### Changed
- Review behavior now identifies the smallest missing concept, explains it
  against the actual implementation, challenges architectural and behavioral
  assumptions, and returns ownership to the developer instead of silently
  repairing one agent's output with another.

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
