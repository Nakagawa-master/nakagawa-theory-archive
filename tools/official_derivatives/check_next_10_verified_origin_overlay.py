#!/usr/bin/env python3
import csv
from pathlib import Path

DISCOVERY = Path('tools/official_derivatives/next_10_public_origin_discovery_input.tsv')
OVERLAY = Path('tools/official_derivatives/next_10_verified_origin_overlay_20260629.tsv')
EXPECTED_HEADER = ['discovery_id','verification_status','parent_ncl_id','parent_diff_id','folder_id','canonical_url']


def read_rows(path):
    with path.open(encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        return reader.fieldnames, list(reader)


def main():
    discovery_header, discovery_rows = read_rows(DISCOVERY)
    header, rows = read_rows(OVERLAY)
    errors = []
    if header != EXPECTED_HEADER:
        errors.append('bad_verified_overlay_header')
    discovery_ids = {row.get('discovery_id','') for row in discovery_rows}
    seen = set()
    for row in rows:
        rid = row.get('discovery_id','')
        if rid in seen:
            errors.append('duplicate_verified_overlay_id=' + rid)
        seen.add(rid)
        if rid not in discovery_ids:
            errors.append('overlay_id_not_in_discovery=' + rid)
        if row.get('verification_status') != 'verified':
            errors.append('bad_verification_status=' + rid)
        if not row.get('parent_ncl_id','').startswith('NCL-'):
            errors.append('bad_parent_ncl_id=' + rid)
        if not row.get('parent_diff_id','').startswith('DIFF-'):
            errors.append('bad_parent_diff_id=' + rid)
        if not row.get('folder_id','').startswith('ncl-alpha-'):
            errors.append('bad_folder_id=' + rid)
        if not row.get('canonical_url','').startswith('https://master.ricette.jp/derivatives/'):
            errors.append('bad_canonical_url=' + rid)
    if 'DISC-010' in seen:
        errors.append('mota_unverified_row_must_not_be_overlay_verified')
    if len(rows) != 9:
        errors.append('verified_overlay_rows=' + str(len(rows)) + ':expected=9')
    print('check_set=next_10_verified_origin_overlay_v1')
    print('verified_overlay_rows=' + str(len(rows)))
    print('page_generation=false')
    if errors:
        print('\n'.join(errors[:50]))
        print('next_10_verified_origin_overlay_pass=false')
        return 1
    print('next_10_verified_origin_overlay_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
