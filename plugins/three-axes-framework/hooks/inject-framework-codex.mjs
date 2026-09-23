#!/usr/bin/env node

import { existsSync, readFileSync, unlinkSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  globalProfilePath,
  hasPersistentProfile,
  legacyGlobalProfilePath,
  projectProfilePath,
  resolveProfile,
  sessionProfilePath,
} from './lib/profile.mjs';
import { setupContext } from './lib/setup.mjs';

const pluginRoot = dirname(dirname(fileURLToPath(import.meta.url)));

let cwd = process.cwd();
let hasWorkspace = false;

async function readEvent() {
  try {
    const chunks = [];
    for await (const chunk of process.stdin) chunks.push(chunk);
    const payload = JSON.parse(Buffer.concat(chunks).toString('utf8'));
    hasWorkspace = typeof payload.cwd === 'string' && payload.cwd.length > 0;
    cwd = payload.cwd || cwd;
    return payload.source ?? payload.session_event ?? payload.trigger ?? payload.event ?? 'startup';
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
const { values, sources } = resolveProfile(globalPath, projectProfilePath(cwd), sessionPath);
const axisContext = Object.entries(values)
  .map(([axis, value]) => `  ${axis}: ${value} (${sources[axis]})`)
  .join('\n');
const configured = hasWorkspace && hasPersistentProfile(cwd);
const additionalContext = `${frameworkBody}\n\n## Active Profile\n\n${axisContext}${hasWorkspace && !configured ? `\n\n${setupContext(cwd)}` : ''}`;

process.stdout.write(`${JSON.stringify({
  suppressOutput: true,
  ...(hasWorkspace && !configured && { systemMessage: 'Three Axes Framework profile required for project work.' }),
  hookSpecificOutput: {
    hookEventName: 'SessionStart',
    additionalContext,
  },
})}\n`);
