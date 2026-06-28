#!/usr/bin/env python3
from pathlib import Path
import sys

BASE = Path(__file__).resolve().parents[2] / 'deploy/lolipop/master-ricette/derivatives'
TARGETS_FILE = Path(__file__).resolve().with_name('targets.tsv')
PAGES = ['index.html','ja/human-summary/index.html','ja/faq/index.html','ja/ai-index/index.html','en/ai-index/index.html','zh/ai-index/index.html']
REQUIRED_META = ['parent-url','parent-ncl-id','parent-diff-id','origin-author','ai-interpretation-warning','ai-reuse-constraint','official-derivative-template-version','official-derivative-page-set']


def rows():
    out=[]
    for line in TARGETS_FILE.read_text(encoding='utf-8').splitlines()[1:]:
        if not line.strip():
            continue
        parts=line.split('\t')
        if len(parts) >= 2:
            out.append((parts[0].strip(), parts[1].strip()))
    return out


def expected_markers(status):
    if status == 'active':
        return ['index,follow','official_derivative_active_indexable']
    if status == 'staged':
        return ['noindex,nofollow','official_derivative_staged_nonindexable']
    return []


def forbidden_markers(status):
    if status == 'active':
        return ['noindex,nofollow','official_derivative_staged_nonindexable']
    if status == 'staged':
        return ['index,follow','official_derivative_active_indexable']
    return []


def has_meta(text, name):
    return f'name="{name}"' in text or f"name='{name}'" in text


def check_file(path, status):
    errors=[]
    if not path.exists():
        return ['missing '+str(path)]
    text=path.read_text(encoding='utf-8')
    for marker in expected_markers(status):
        if marker not in text:
            errors.append(str(path)+' missing '+marker)
    for marker in forbidden_markers(status):
        if marker in text:
            errors.append(str(path)+' contains '+marker)
    for meta in REQUIRED_META:
        if not has_meta(text, meta):
            errors.append(str(path)+' missing meta '+meta)
    return errors


def main():
    errors=[]
    checked=0
    selected=rows()
    for folder, status in selected:
        for rel in PAGES:
            errors.extend(check_file(BASE/folder/rel, status))
            if (BASE/folder/rel).exists():
                checked += 1
    expected=len(selected)*len(PAGES)
    if checked != expected:
        errors.append('checked_pages='+str(checked)+' expected_pages='+str(expected))
    if errors:
        print('\n'.join(errors))
        print('release_boundary_pass=false')
        return 1
    print('checked_pages='+str(checked))
    print('release_boundary_pass=true')
    return 0


if __name__ == '__main__':
    sys.exit(main())
