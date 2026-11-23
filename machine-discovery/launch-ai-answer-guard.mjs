#!/usr/bin/env node
/**
 * Minimal, dependency-free Qwen Code extension launcher for the SAME local
 * read-only Python MCP. Qwen itself requires Node; Python 3 may be registered
 * as 'py -3' on Windows rather than as 'python3'.
 *
 * No model invocation, package installation, network access, or auto-execution
 * except the one MCP server explicitly selected by the installed extension.
 * Never log to stdout: that channel belongs exclusively to MCP JSON-RPC.
 */
import { spawn, spawnSync } from 'node:child_process';
import { realpathSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

export function pythonCandidates(platform = process.platform) {
  return platform === 'win32'
    ? [
        { command: 'py', prefix: ['-3'] },
        { command: 'python3', prefix: [] },
        { command: 'python', prefix: [] },
      ]
    : [
        { command: 'python3', prefix: [] },
        { command: 'python', prefix: [] },
      ];
}

function choosePython(platform = process.platform) {
  for (const candidate of pythonCandidates(platform)) {
    const probe = spawnSync(candidate.command, [...candidate.prefix, '--version'], {
      encoding: 'utf8',
      timeout: 3000,
      windowsHide: true,
      shell: false,
    });
    const version = (probe.stdout || '') + '\n' + (probe.stderr || '');
    if (probe.status === 0 && /(?:^|\n)Python 3\.\d+(?:\.\d+)?(?:\s|$)/.test(version)) {
      return candidate;
    }
  }
  return null;
}

function main() {
  const candidate = choosePython();
  if (!candidate) {
    console.error(
      'AI Answer Guard requires Python 3. Install Python 3 and ensure python3, ' +
      'python, or (on Windows) py -3 works in your terminal.',
    );
    process.exitCode = 2;
    return;
  }
  const here = dirname(fileURLToPath(import.meta.url));
  const script = join(here, 'nakagawa-theory-mcp.py');
  const child = spawn(candidate.command, [...candidate.prefix, script], {
    cwd: dirname(here),
    env: { ...process.env, PYTHONIOENCODING: 'utf-8' },
    stdio: 'inherit',
    windowsHide: true,
    shell: false,
  });
  child.on('error', (error) => {
    console.error('AI Answer Guard Python MCP could not start:', error.message);
    process.exitCode = 1;
  });
  child.on('close', (code) => {
    if (process.exitCode !== 1) process.exitCode = code ?? 1;
  });
  for (const signal of ['SIGINT', 'SIGTERM']) {
    process.on(signal, () => child.kill(signal));
  }
}

// npm creates a node_modules/.bin symlink; compare the real target, not the shim path.
if (process.argv[1] && realpathSync(resolve(process.argv[1])) === fileURLToPath(import.meta.url)) {
  main();
}
