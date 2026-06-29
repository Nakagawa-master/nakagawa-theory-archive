#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent

ALLOWED_PREFIXES = (
    '.github/workflows/official-derivative-generation-check.yml',
    'tools/official_derivatives/',
    'deploy/lolipop/master-ricette/derivatives/',
)

DISALLOWED_PARTS = (
    'sitemap',
    'search-console',
    'search_console',
)

EXTRA_CHECKS = (
    'check_target_folder_scope.py',
    'check_next_batch_schema.py',
    'check_workflow_artifact_scope.py',
    'check_derivative_content_strength.py',
)


def git(*args):
    return subprocess.run(['git', *args], text=True, capture_output=True)


def changed_files():
    base = 'origin/main'
    subprocess.run(['git', 'fetch', 'origin', 'main', '--depth=1'], text=True)
    result = git('diff', '--name-only', base + '...HEAD')
    if result.returncode == 0 and result.stdout.strip():
        return [line.strip() for line in result.stdout.splitlines() if line.strip()]
    result = git('diff', '--name-only', 'HEAD~1..HEAD')
    if result.returncode == 0:
        return [line.strip() for line in result.stdout.splitlines() if line.strip()]
    return []


def allowed(path):
    if path in ALLOWED_PREFIXES:
        return True
    return any(path.startswith(prefix) for prefix in ALLOWED_PREFIXES if prefix.endswith('/'))


def run_extra_checks():
    for name in EXTRA_CHECKS:
        script = HERE / name
        if not script.exists():
            continue
        result = subprocess.run([sys.executable, str(script)])
        if result.returncode != 0:
            return result.returncode
    return 0


def main():
    files = changed_files()
    errors = []
    for path in files:
        low = path.lower()
        if not allowed(path):
            errors.append('outside_allowed_scope=' + path)
        if any(part in low for part in DISALLOWED_PARTS):
            errors.append('disallowed_path_part=' + path)
    print('check_set=official_derivative_change_scope_v5')
    print('changed_files=' + str(len(files)))
    if errors:
        print('\n'.join(errors))
        print('change_scope_pass=false')
        return 1
    extra_code = run_extra_checks()
    if extra_code != 0:
        print('change_scope_pass=false')
        return extra_code
    print('change_scope_pass=true')
    return 0


if __name__ == '__main__':
    sys.exit(main())
