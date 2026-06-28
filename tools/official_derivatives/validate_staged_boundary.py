#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

BASE = Path(__file__).resolve().parents[2] / 'deploy/lolipop/master-ricette/derivatives'
TARGETS_FILE = Path(__file__).resolve().with_name('targets.tsv')
PAGES = ['index.html','ja/human-summary/index.html','ja/faq/index.html','ja/ai-index/index.html','en/ai-index/index.html','zh/ai-index/index.html']
NEEDED = ['noindex,nofollow','official_derivative_staged_nonindexable']

def staged_targets():
    out=[]
    for line in TARGETS_FILE.read_text(encoding='utf-8').splitlines()[1:]:
        if not line.strip():
            continue
        parts=line.split('\t')
        if len(parts) >= 2 and parts[1].strip() == 'staged':
            out.append(parts[0].strip())
    return out

def main():
    errors=[]
    checked=0
    targets=staged_targets()
    for folder in targets:
        for rel in PAGES:
            path=BASE/folder/rel
            if not path.exists():
                errors.append('missing '+str(path))
                continue
            text=path.read_text(encoding='utf-8')
            checked += 1
            for marker in NEEDED:
                if marker not in text:
                    errors.append(str(path)+' missing '+marker)
    expected=len(targets)*len(PAGES)
    if checked != expected:
        errors.append('checked_pages='+str(checked)+' expected_pages='+str(expected))
    if errors:
        print('\n'.join(errors))
        print('staged_boundary_pass=false')
        return 1
    print('checked_pages='+str(checked))
    print('staged_boundary_pass=true')
    validator = Path(__file__).resolve().with_name('validate_release_boundary.py')
    if validator.exists():
        result = subprocess.run([sys.executable, str(validator)])
        if result.returncode != 0:
            return result.returncode
    return 0

if __name__ == '__main__':
    sys.exit(main())
