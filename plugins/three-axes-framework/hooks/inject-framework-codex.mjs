#!/usr/bin/env node

import { existsSync, readFileSync, unlinkSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  globalProfilePath,
  legacyGlobalProfilePath,
  projectProfilePath,
  resolveProfile,
  sessionProfilePath,
} from './lib/profile.mjs';

const pluginRoot = dirname(dirname(fileURLToPath(import.meta.url)));

async function readEvent() {
  try {
    const chunks = [];
    for await (const chunk of process.stdin) chunks.push(chunk);
    const payload = JSON.parse(Buffer.concat(chunks).toString('utf8'));
    return payload.session_event ?? payload.trigger ?? payload.event ?? 'startup';
  } catch {
    return 'startup';
  }
}

const event = await readEvent();
const sessionPath = sessionProfilePath();
if (event === 'startup' && existsSync(sessionPath)) {
  try { unlinkSync(sessionPath); } catch { /* a stale profile must not block startup */ }
}

let frameworkBody;
try {
  frameworkBody = readFileSync(join(pluginRoot, 'skills', 'three-axes-framework', 'SKILL.md'), 'utf8')
    .replace(/^---[\s\S]*?---\n/, '')
    .trim();
} catch {
  process.exit(0);
}

const codexGlobalPath = globalProfilePath();
const globalPath = existsSync(codexGlobalPath) ? codexGlobalPath : legacyGlobalProfilePath();
const { values, sources } = resolveProfile(globalPath, projectProfilePath(), sessionPath);
const axisContext = Object.entries(values)
  .map(([axis, value]) => `  ${axis}: ${value} (${sources[axis]})`)
  .join('\n');
const additionalContext = `${frameworkBody}\n\n## Active Profile\n\n${axisContext}`;

process.stdout.write(`${JSON.stringify({
  suppressOutput: true,
  hookSpecificOutput: {
    hookEventName: 'SessionStart',
    additionalContext,
  },
})}\n`);
