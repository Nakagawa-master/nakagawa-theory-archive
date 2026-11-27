#!/usr/bin/env python3
"""Real Git recovery control; uses only disposable repositories, never your checkout.
Run as an ordinary POSIX user with Python 3 and Git. No network or dependencies.
"""
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile


def main():
    if os.name != 'posix' or os.geteuid() == 0:
        raise SystemExit('Run as an unprivileged POSIX user; root can bypass the permission control.')
    git = shutil.which('git')
    if not git:
        raise SystemExit('Git is required.')
    with tempfile.TemporaryDirectory(prefix='git-restore-probe-') as temp:
        root = Path(temp)
        home = root / 'home'
        home.mkdir()
        repo = root / 'repo'
        repo.mkdir()
        env = {'PATH': os.defpath, 'HOME': str(home), 'GIT_CONFIG_NOSYSTEM': '1',
               'GIT_CONFIG_GLOBAL': '/dev/null', 'LC_ALL': 'C', 'GIT_TERMINAL_PROMPT': '0'}

        def run(*args, required=True):
            result = subprocess.run([git, *args], cwd=repo, env=env,
                                    capture_output=True, text=True, timeout=30)
            if required and result.returncode:
                raise RuntimeError(result.stderr)
            return result

        run('init', '-q')
        run('config', 'user.name', 'Local Probe')
        run('config', 'user.email', 'probe@example.invalid')
        tracked = repo / 'tracked.txt'
        tracked.write_text('checkpoint\n')
        run('add', 'tracked.txt')
        run('commit', '-qm', 'checkpoint')
        checkpoint = run('rev-parse', 'HEAD').stdout.strip()
        tracked.write_text('current\n')
        leftover = repo / 'leftover'
        leftover.mkdir()
        marker = leftover / 'file.txt'
        marker.write_text('untracked\n')
        rows = []

        def observe(name, restore, clean):
            rows.append({'case': name, 'restore_exit': restore.returncode,
                         'clean_exit': None if clean is None else clean.returncode,
                         'tracked': tracked.read_text().strip(), 'untracked_exists': marker.exists()})

        invalid = run('restore', '--source', 'no-such-probe-checkpoint', '.', required=False)
        observe('missing_checkpoint', invalid, None)
        leftover.chmod(0o500)
        try:
            restored = run('restore', '--source', checkpoint, '.')
            cleaned = run('clean', '-f', '-d', required=False)
            observe('cleanup_refused', restored, cleaned)
        finally:
            leftover.chmod(0o700)
        tracked.write_text('current\n')
        restored = run('restore', '--source', checkpoint, '.')
        cleaned = run('clean', '-f', '-d')
        observe('complete', restored, cleaned)
        print(json.dumps({'git': run('--version').stdout.strip(), 'results': rows}, indent=2))
        a, b, c = rows
        ok = (a['restore_exit'] != 0 and a['clean_exit'] is None and a['tracked'] == 'current' and a['untracked_exists']
              and b['restore_exit'] == 0 and b['clean_exit'] != 0 and b['tracked'] == 'checkpoint' and b['untracked_exists']
              and c['restore_exit'] == c['clean_exit'] == 0 and c['tracked'] == 'checkpoint' and not c['untracked_exists'])
        if not ok:
            raise SystemExit('Control mismatch; do not infer partial recovery on this filesystem.')


if __name__ == '__main__':
    main()
