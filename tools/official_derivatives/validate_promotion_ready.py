#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent

def run(script, *args):
    cmd = [sys.executable, str(HERE / script)] + list(args)
    print('run=' + ' '.join(cmd))
    result = subprocess.run(cmd)
    if result.returncode != 0:
        return result.returncode
    return 0

def main():
    print('check_set=promotion_readiness_v2')
    checks = [
        ('validate_origin_manifest.py',),
        ('validate_template_parity.py', '--status=staged'),
        ('render_heads.py', '--status=staged'),
        ('validate_staged_boundary.py',),
        ('validate_release_boundary.py',),
    ]
    for check in checks:
        code = run(*check)
        if code != 0:
            print('promotion_ready=false')
            return code
    print('promotion_ready=true')
    return 0

if __name__ == '__main__':
    sys.exit(main())
