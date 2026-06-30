#!/usr/bin/env python3
import csv
from pathlib import Path

DISCOVERY = Path('tools/official_derivatives/next_10_public_origin_discovery_input.tsv')
HEADER = ['batch_id','discovery_id','discovery_status','source_category','parent_url','parent_title','parent_ncl_id','parent_diff_id','folder_id','canonical_url','already_in_origin_manifest','public_safe_status','exclusion_status','exclusion_reason','reason_for_inclusion','risk_note','review_notes']
STATUS = {'unreviewed','reviewed','blocked','ready_for_catalog'}
SAFE = {'pending','pass','block'}
EXCL = {'available','excluded','review_required'}
CAT = {'theory','society','future','structural-reading','other'}


def rows():
    with DISCOVERY.open(encoding='utf-8', newline='') as f:
        r = csv.DictReader(f, delimiter='\t')
        return r.fieldnames or [], list(r)


def main():
    header, data = rows()
    errors = []
    seen = set()
    ready = 0
    if header != HEADER:
        errors.append('bad_header')
    for row in data:
        did = row.get('discovery_id','')
        key = (row.get('parent_url',''), row.get('parent_ncl_id',''), row.get('parent_diff_id',''))
        if key in seen:
            errors.append('duplicate=' + did)
        seen.add(key)
        if row.get('batch_id') != 'candidate-10-19': errors.append('bad_batch=' + did)
        if row.get('discovery_status') not in STATUS: errors.append('bad_status=' + did)
        if row.get('source_category') not in CAT: errors.append('bad_category=' + did)
        if row.get('public_safe_status') not in SAFE: errors.append('bad_safe=' + did)
        if row.get('exclusion_status') not in EXCL: errors.append('bad_exclusion=' + did)
        if row.get('already_in_origin_manifest') not in {'true','false'}: errors.append('bad_manifest_flag=' + did)
        if row.get('discovery_status') == 'ready_for_catalog':
            ready += 1
            for k in ['parent_url','parent_title','parent_ncl_id','parent_diff_id','folder_id','canonical_url','reason_for_inclusion','risk_note']:
                if not row.get(k,'').strip(): errors.append('missing=' + did + ':' + k)
    print('check_set=next_10_public_origin_discovery_v2')
    print('discovery_rows=' + str(len(data)))
    print('ready_for_catalog_rows=' + str(ready))
    if errors:
        print('\n'.join(errors[:50]))
        print('next_10_public_origin_discovery_pass=false')
        return 1
    print('next_10_public_origin_discovery_pass=true')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
