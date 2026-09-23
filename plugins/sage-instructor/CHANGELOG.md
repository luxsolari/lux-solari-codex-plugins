# Changelog

All notable changes to `sage-instructor` are documented in this file.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Releases are tagged `sage-instructor-v<version>`; each plugin in this repository
versions and releases independently.

---

## [Unreleased]

## [1.8.0] - 2026-09-23

### Added
- Added a generated-code ownership review that keeps the learner in the loop:
  `intent → generation → comprehension → challenge → evidence → ownership`.
- Defined the ownership gate as the ability to explain the important decisions
  and mechanisms tomorrow without the agent present; framework/API trivia and
  line-by-line recall are deliberately outside that gate.

### Changed
- Sage reviews now identify the smallest missing concept, explain it against
  the implementation at hand, challenge architecture, control flow, invariants,
  failure paths, and tests, then return control instead of silently repairing
  one agent's output with another.

## [1.7.2] — 2026-09-07

- The changelog starts here. Everything up to and including 1.7.2 predates it;
  read the git history for that. Entries from the next release onward record
  what changed, so this file is a record rather than a reconstruction.
