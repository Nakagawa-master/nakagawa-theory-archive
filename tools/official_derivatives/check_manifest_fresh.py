#!/usr/bin/env python3
import subprocess
import sys


def main():
    print('check_set=manifest_freshness_v1')
    a = subprocess.call([sys.executable, 'tools/official_derivatives/build_origin_manifest.py'])
    if a != 0:
        return a
    b = subprocess.call(['git', 'diff', '--quiet', '--', 'tools/official_derivatives/origin_manifest.tsv'])
    if b != 0:
        print('manifest_fresh=false')
        return b
    print('manifest_fresh=true')
    return 0


if __name__ == '__main__':
    sys.exit(main())
