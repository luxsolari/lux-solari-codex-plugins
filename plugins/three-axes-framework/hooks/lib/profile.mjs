import { existsSync, readFileSync, writeFileSync } from 'node:fs';
import { execSync } from 'node:child_process';
import { homedir } from 'node:os';
import { resolve } from 'node:path';

export const VALID_AXES = {
  mastery: ['low', 'medium', 'high'],
  consequence: ['low', 'medium', 'high'],
  intent: ['growth', 'balanced', 'output'],
};

export const DEFAULTS = { mastery: 'medium', consequence: 'medium', intent: 'balanced' };

function codexHome() {
  return process.env.CODEX_HOME || resolve(homedir(), '.codex');
}

export function globalProfilePath() {
  return resolve(codexHome(), 'three-axes-profile.json');
}

export function legacyGlobalProfilePath() {
  return resolve(homedir(), '.claude', 'three-axes-profile.json');
}

export function sessionProfilePath() {
  return resolve(codexHome(), 'three-axes-session.json');
}

export function projectProfilePath() {
  try {
    return resolve(execSync('git rev-parse --show-toplevel', {
      encoding: 'utf8',
      stdio: ['pipe', 'pipe', 'pipe'],
    }).trim(), '.three-axes.json');
  } catch {
    return resolve(process.cwd(), '.three-axes.json');
  }
}

export function readProfile(filePath) {
  try {
    return JSON.parse(readFileSync(filePath, 'utf8'));
  } catch {
    return {};
  }
}

export function resolveProfile(globalPath, projectPath, sessionPath) {
  const globalData = readProfile(globalPath);
  const projectData = readProfile(projectPath);
  const sessionData = readProfile(sessionPath);
  const values = { ...DEFAULTS, ...globalData, ...projectData, ...sessionData };
  const sources = {};

  for (const axis of Object.keys(VALID_AXES)) {
    sources[axis] = sessionData[axis] !== undefined ? 'session'
      : projectData[axis] !== undefined ? 'project'
        : globalData[axis] !== undefined ? 'global'
          : 'default';
  }
  return { values, sources };
}

export function writeProfile(filePath, data) {
  writeFileSync(filePath, `${JSON.stringify(data, null, 2)}\n`, 'utf8');
}

export function validateProfile(data) {
  const errors = [];
  for (const [axis, value] of Object.entries(data)) {
    if (!VALID_AXES[axis]) {
      errors.push(`Unknown axis: "${axis}". Valid axes: ${Object.keys(VALID_AXES).join(', ')}`);
    } else if (!VALID_AXES[axis].includes(value)) {
      errors.push(`Invalid value for ${axis}: "${value}". Valid values: ${VALID_AXES[axis].join(', ')}`);
    }
  }
  return errors;
}

export function isFirstRun(globalPath, projectPath) {
  return !existsSync(globalPath) && !existsSync(projectPath);
}
