import assert from 'node:assert/strict';
import { mkdtempSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import test from 'node:test';

import {
  DEFAULTS,
  resolveProfile,
  validateProfile,
} from '../hooks/lib/profile.mjs';

function tempDirectory() {
  return mkdtempSync(join(tmpdir(), 'three-axes-profile-'));
}

function profile(directory, name, contents) {
  const path = join(directory, name);
  writeFileSync(path, JSON.stringify(contents), 'utf8');
  return path;
}

test('uses documented defaults when all profiles are absent', () => {
  const directory = tempDirectory();
  const resolved = resolveProfile(
    join(directory, 'global.json'),
    join(directory, 'project.json'),
    join(directory, 'session.json'),
  );

  assert.deepEqual(resolved.values, DEFAULTS);
  assert.deepEqual(resolved.sources, {
    mastery: 'default',
    consequence: 'default',
    intent: 'default',
  });
});

test('resolves each axis through the global project session cascade', () => {
  const directory = tempDirectory();
  const resolved = resolveProfile(
    profile(directory, 'global.json', { mastery: 'low', consequence: 'high' }),
    profile(directory, 'project.json', { mastery: 'high', intent: 'growth' }),
    profile(directory, 'session.json', { mastery: 'medium' }),
  );

  assert.deepEqual(resolved.values, {
    mastery: 'medium',
    consequence: 'high',
    intent: 'growth',
  });
  assert.deepEqual(resolved.sources, {
    mastery: 'session',
    consequence: 'global',
    intent: 'project',
  });
});

test('ignores malformed profile JSON and reports invalid writes', () => {
  const directory = tempDirectory();
  const malformed = join(directory, 'malformed.json');
  writeFileSync(malformed, '{not json', 'utf8');
  const resolved = resolveProfile(malformed, join(directory, 'missing.json'), join(directory, 'also-missing.json'));

  assert.deepEqual(resolved.values, DEFAULTS);
  assert.deepEqual(validateProfile({ surprise: 'high', mastery: 'expert' }), [
    'Unknown axis: "surprise". Valid axes: mastery, consequence, intent',
    'Invalid value for mastery: "expert". Valid values: low, medium, high',
  ]);
});
