#!/usr/bin/env python3
import csv
from pathlib import Path

ORIGIN = Path('tools/official_derivatives/origin_manifest.tsv')
DISCOVERY = Path('tools/official_derivatives/next_10_public_origin_discovery_input.tsv')
EXPECTED_HEADER = [
    'batch_id','discovery_id','discovery_status','source_category','parent_url','parent_title',
    'parent_ncl_id','parent_diff_id','folder_id','canonical_url','already_in_origin_manifest',
    'public_safe_status','exclusion_status','exclusion_reason','reason_for_inclusion','risk_note','review_notes'
]
CATEGORIES = {'theory','society','future','structural-reading','other'}
STATUSES = {'unreviewed','reviewed','blocked','ready_for_catalog'}
PUBLIC_SAFE = {'pending','pass','block'}
EXCLUSION = {'available','excluded','review_required'}


def read_rows(path):
    with path.open(encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        return reader.fieldnames, list(reader)


def main():
    origin_header, origin_rows = read_rows(ORIGIN)
    header, rows = read_rows(DISCOVERY)
    origin_urls = {row.get('parent_url','') for row in origin_rows}
    errors = []
    if header != EXPECTED_HEADER:
        errors.append('bad_public_origin_discovery_header')
    seen = set()
    ready_count = 0
    for row in rows:
        rid = row.get('discovery_id','')
        key = (row.get('parent_url',''), row.get('parent_ncl_id',''), row.get('parent_diff_id',''))
        if key in seen:
            errors.append('duplicate_origin_identity=' + rid)
        seen.add(key)
        if row.get('batch_id') != 'candidate-10-19':
            errors.append('bad_batch_id=' + rid)
        if not rid.startswith('DISC-'):
            errors.append('bad_discovery_id=' + rid)
        if row.get('discovery_status') not in STATUSES:
            errors.append('bad_discovery_status=' + rid)
        if row.get('source_category') not in CATEGORIES:
            errors.append('bad_source_category=' + rid)
        if row.get('public_safe_status') not in PUBLIC_SAFE:
            errors.append('bad_public_safe_status=' + rid)
        if row.get('exclusion_status') not in EXCLUSION:
            errors.append('bad_exclusion_status=' + rid)
        in_manifest = row.get('parent_url','') in origin_urls
        if row.get('already_in_origin_manifest') not in {'true','false'}:
            errors.append('bad_already_in_origin_manifest=' + rid)
        elif (row.get('already_in_origin_manifest') == 'true') != in_manifest:
            errors.append('origin_manifest_presence_mismatch=' + rid)
        if in_manifest and row.get('exclusion_status') != 'excluded':
            errors.append('used_origin_must_be_excluded=' + rid)
        if row.get('discovery_status') == 'ready_for_catalog':
            ready_count += 1
            if row.get('already_in_origin_manifest') != 'false':
                errors.append('ready_origin_already_used=' + rid)
            if row.get('public_safe_status') != 'pass':
                errors.append('ready_public_safe_not_pass=' + rid)
            if row.get('exclusion_status') != 'available':
                errors.append('ready_not_available=' + rid)
            if not row.get('parent_url','').startswith('https://master.ricette.jp/'):
                errors.append('bad_parent_url=' + rid)
            if not row.get('parent_ncl_id','').startswith('NCL-'):
                errors.append('bad_parent_ncl_id=' + rid)
            if not row.get('parent_diff_id','').startswith('DIFF-'):
                errors.append('bad_parent_diff_id=' + rid)
            if not row.get('canonical_url','').startswith('https://master.ricette.jp/derivatives/'):
                errors.append('bad_canonical_url=' + rid)
    print('check_set=next_10_public_origin_discovery_v1')
    print('discovery_rows=' + str(len(rows)))
    print('ready_for_catalog_rows=' + str(ready_count))
    if errors:
        print('\n'.join(errors[:50]))
        print('next_10_public_origin_discovery_pass=false')
        return 1
    print('next_10_public_origin_discovery_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
