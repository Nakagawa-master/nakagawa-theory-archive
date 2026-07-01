#!/usr/bin/env python3
import csv
from pathlib import Path

REGISTRY = Path('tools/official_derivatives/staged_official_derivative_registry.tsv')
BASE = Path('deploy/lolipop/master-ricette/derivatives')


def rows():
    with REGISTRY.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def main():
    errors = []
    data = rows()
    if len(data) != 78:
        errors.append('registry_rows_expected=78')
    for r in data:
        folder = r.get('folder_id','')
        rel = r.get('relative_path','')
        path = BASE / folder / rel
        label = folder + ':' + r.get('page_role','')
        if not path.exists():
            errors.append('missing_page=' + label)
            continue
        html = path.read_text(encoding='utf-8')
        if r.get('canonical_url','') not in html:
            errors.append('canonical_not_in_page=' + label)
        if r.get('parent_url','') not in html:
            errors.append('parent_url_not_in_page=' + label)
        if r.get('parent_ncl_id','') not in html:
            errors.append('parent_ncl_not_in_page=' + label)
        if r.get('parent_diff_id','') not in html:
            errors.append('parent_diff_not_in_page=' + label)
        if 'Nakagawa Master' not in html:
            errors.append('origin_not_in_page=' + label)
        if r.get('export_status') == 'staged':
            if 'noindex,nofollow' not in html:
                errors.append('staged_robots_missing=' + label)
            if 'official_derivative_staged_nonindexable' not in html:
                errors.append('staged_status_missing=' + label)
    print('check_set=derivative_registry_page_parity_v2')
    print('registry_rows=' + str(len(data)))
    if errors:
        print('\n'.join(errors[:30]))
        print('derivative_registry_page_parity_pass=false')
        return 1
    print('derivative_registry_page_parity_pass=true')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
