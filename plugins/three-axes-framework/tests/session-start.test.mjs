import assert from 'node:assert/strict';
import { existsSync, mkdtempSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { spawnSync } from 'node:child_process';
import test from 'node:test';

const ROOT = resolve(import.meta.dirname, '..');
const HOOK = join(ROOT, 'hooks', 'inject-framework-codex.mjs');

function invoke(event) {
  const codexHome = mkdtempSync(join(tmpdir(), 'three-axes-codex-home-'));
  const sessionPath = join(codexHome, 'three-axes-session.json');
  writeFileSync(sessionPath, JSON.stringify({ mastery: 'high' }), 'utf8');
  const result = spawnSync(process.execPath, [HOOK], {
    cwd: ROOT,
    env: { ...process.env, CODEX_HOME: codexHome, PLUGIN_ROOT: ROOT },
    input: JSON.stringify({ session_event: event }),
    encoding: 'utf8',
  });

  assert.equal(result.status, 0, result.stderr);
  return { output: JSON.parse(result.stdout), sessionPath };
}

test('emits a native SessionStart payload with the framework context', () => {
  const { output } = invoke('resume');

  assert.equal(output.suppressOutput, true);
  assert.equal(output.hookSpecificOutput.hookEventName, 'SessionStart');
  assert.match(output.hookSpecificOutput.additionalContext, /Three Axes/);
  assert.match(output.hookSpecificOutput.additionalContext, /mastery: high \(session\)/);
});

test('clears the session profile only on startup', () => {
  const startup = invoke('startup');
  assert.equal(existsSync(startup.sessionPath), false);

  for (const event of ['resume', 'clear', 'compact']) {
    const result = invoke(event);
    assert.equal(existsSync(result.sessionPath), true, event);
  }
});
