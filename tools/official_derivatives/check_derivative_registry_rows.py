#!/usr/bin/env python3
import csv
from pathlib import Path

MANIFEST = Path('tools/official_derivatives/origin_manifest.tsv')
REGISTRY = Path('tools/official_derivatives/derivative_registry_candidate_05_09.tsv')
PAGES = {'hub','human_summary','faq','ja_ai_index','en_ai_index','zh_ai_index'}
NEEDED = ['derivative_id','page_role','language','export_status','parent_url','parent_ncl_id','parent_diff_id','folder_id','relative_path','canonical_url','quality_gate_status','render_status']


def read_rows(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def main():
    manifest = {r['folder_id']: r for r in read_rows(MANIFEST) if r.get('export_status') == 'staged'}
    rows = read_rows(REGISTRY)
    errors = []
    if len(rows) != len(manifest) * 6:
        errors.append('registry_row_count=' + str(len(rows)))
    for row in rows:
        for key in NEEDED:
            if not row.get(key):
                errors.append('missing_' + key)
        m = manifest.get(row.get('folder_id',''))
        if not m:
            errors.append('unknown_folder=' + row.get('folder_id',''))
            continue
        if row.get('page_role') not in PAGES:
            errors.append('bad_page_role=' + row.get('page_role',''))
        if row.get('parent_ncl_id') != m.get('parent_ncl_id'):
            errors.append('ncl_mismatch=' + row.get('folder_id',''))
        if row.get('parent_diff_id') != m.get('parent_diff_id'):
            errors.append('diff_mismatch=' + row.get('folder_id',''))
    print('check_set=derivative_registry_rows_v1')
    print('registry_rows=' + str(len(rows)))
    if errors:
        print('\n'.join(errors[:20]))
        print('derivative_registry_rows_pass=false')
        return 1
    print('derivative_registry_rows_pass=true')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
