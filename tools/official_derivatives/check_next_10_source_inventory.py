#!/usr/bin/env python3
import csv
from pathlib import Path

ORIGIN = Path('tools/official_derivatives/origin_manifest.tsv')
INVENTORY = Path('tools/official_derivatives/next_10_source_inventory_candidate_10_19.tsv')
EXPECTED_HEADER = [
    'batch_id','source_inventory_id','source_scope','origin_manifest_status','selection_eligibility',
    'parent_url','parent_title','parent_ncl_id','parent_diff_id','folder_id','canonical_url',
    'exclusion_reason','public_safe_status','notes'
]


def read_rows(path):
    with path.open(encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        return reader.fieldnames, list(reader)


def main():
    origin_header, origin_rows = read_rows(ORIGIN)
    header, rows = read_rows(INVENTORY)
    errors = []
    if header != EXPECTED_HEADER:
        errors.append('bad_inventory_header')
    if len(rows) != len(origin_rows):
        errors.append(f'inventory_origin_row_count_mismatch={len(rows)}:{len(origin_rows)}')

    origin_by_url = {row.get('parent_url',''): row for row in origin_rows}
    seen_ids = set()
    selected_like = []
    for row in rows:
        sid = row.get('source_inventory_id','')
        if sid in seen_ids:
            errors.append('duplicate_source_inventory_id=' + sid)
        seen_ids.add(sid)
        if row.get('batch_id') != 'candidate-10-19':
            errors.append('bad_batch_id=' + sid)
        if row.get('source_scope') != 'origin_manifest_current_rows_only':
            errors.append('bad_source_scope=' + sid)
        if row.get('public_safe_status') != 'pass':
            errors.append('bad_public_safe_status=' + sid)
        if row.get('notes') != 'inventory_only_not_a_source_selection':
            errors.append('bad_notes=' + sid)
        if row.get('selection_eligibility') != 'excluded':
            selected_like.append(sid)
        if row.get('exclusion_reason') != 'already_active_or_staged_official_derivative':
            errors.append('bad_exclusion_reason=' + sid)
        origin = origin_by_url.get(row.get('parent_url',''))
        if not origin:
            errors.append('inventory_url_not_in_origin_manifest=' + sid)
            continue
        for key in ['parent_ncl_id','parent_diff_id','folder_id','canonical_url']:
            if row.get(key,'') != origin.get(key,''):
                errors.append('origin_identity_mismatch=' + sid + ':' + key)
        if row.get('origin_manifest_status','') != origin.get('export_status',''):
            errors.append('origin_status_mismatch=' + sid)
        if origin.get('export_status','') not in {'active','staged'}:
            errors.append('unexpected_origin_status=' + sid)
    if selected_like:
        errors.append('inventory_must_not_select_sources=' + ','.join(selected_like[:20]))

    print('check_set=next_10_source_inventory_v1')
    print('origin_rows=' + str(len(origin_rows)))
    print('inventory_rows=' + str(len(rows)))
    print('selected_sources=0')
    if errors:
        print('\n'.join(errors[:50]))
        print('next_10_source_inventory_pass=false')
        return 1
    print('next_10_source_inventory_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
