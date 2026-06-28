#!/usr/bin/env python3
from pathlib import Path
import csv
import subprocess
import sys

HERE = Path(__file__).resolve().parent
TARGETS = HERE / 'targets.tsv'
PREFIX = 'deploy/lolipop/master-ricette/derivatives/'


def run(*args):
    return subprocess.run(['git', *args], text=True, capture_output=True)


def folders():
    with TARGETS.open(encoding='utf-8', newline='') as f:
        return {row['folder_id'] for row in csv.DictReader(f, delimiter='\t')}


def files():
    subprocess.run(['git', 'fetch', 'origin', 'main', '--depth=1'], text=True)
    result = run('diff', '--name-only', 'origin/main...HEAD')
    if result.returncode == 0 and result.stdout.strip():
        return [x.strip() for x in result.stdout.splitlines() if x.strip()]
    return []


def main():
    allowed = folders()
    errors = []
    checked = 0
    for path in files():
        if not path.startswith(PREFIX):
            continue
        checked += 1
        rest = path[len(PREFIX):]
        folder = rest.split('/', 1)[0]
        if folder not in allowed or '/' not in rest:
            errors.append(path)
    print('check_set=target_folder_scope_v1')
    print('checked_derivative_files=' + str(checked))
    if errors:
        print('\n'.join('unexpected_derivative_path=' + x for x in errors))
        print('target_folder_scope_pass=false')
        return 1
    print('target_folder_scope_pass=true')
    return 0


if __name__ == '__main__':
    sys.exit(main())
