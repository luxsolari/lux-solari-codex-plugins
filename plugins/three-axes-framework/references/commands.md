# Three Axes Codex routes

The full published command wording is preserved under `source-commands/` as an
upstream audit record only; do not execute its Claude-specific instructions.
Use these Codex routes in place of Claude slash commands, applying the same
validation, confirmation, merge-before-write, and one-question-at-a-time
requirements from the corresponding source file.

| Source command | Codex route | Persistent state substitution |
| --- | --- | --- |
| `/three-axes` and `/three-axes-framework` | `three-axes-framework` | Show status then the command and signal reference. |
| `/three-axes-setup` | `three-axes setup` | Ask the same three choices sequentially; write `~/.codex/three-axes-profile.json`. |
| `/three-axes-status` | `three-axes status` | Resolve defaults → global → project → session, reporting every source label. |
| `/three-axes-mode <preset>` | `three-axes mode <preset>` | Replace `~/.codex/three-axes-session.json` with the selected full preset. |
| `/three-axes-set <axis>=<value> [--project|--global]` | `three-axes set <axis>=<value> [--project|--global]` | Use `.three-axes.json`, `~/.codex/three-axes-profile.json`, or `~/.codex/three-axes-session.json`. |
| `/three-axes-audit [what went wrong]` | `three-axes audit [what went wrong]` | No persistent state. Emit no new code and no apology loop; name the violated Integrity Rule by ID with the offending output quoted, give a mechanical cause, propose a correction, rate the session CLEAN/DEGRADED/COMPROMISED, then stop. |
| `/three-axes-handoff [output-path]` | `three-axes handoff [output-path]` | Write to the given path, or print the document when no path is supplied. Never write to an unrequested location. |
| `/three-axes-log [note]` | `three-axes log [note]` | Append to `BITACORA.md` at the repository root, newest first; compact past ~40 entries without dropping a decision or a recorded failure. |

The thirteen Integrity Rules (IR-01 … IR-13) in the skill apply to every route and
are cited by ID; the `three-axes audit` route is their recovery path.

Presets remain `learning`, `output`, `production`, `explore`, and `balanced`.
The task-scoped signals remain “walk me through this,” “let me try this,”
“just do it,” and “what are the tradeoffs?” Their source-defined durations and
behavioral effects remain unchanged.
