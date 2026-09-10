# Journal

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
