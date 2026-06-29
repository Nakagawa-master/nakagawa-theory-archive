#!/usr/bin/env python3
import csv
from pathlib import Path

DISCOVERY = Path('tools/official_derivatives/next_10_public_origin_discovery_input.tsv')
CATALOG = Path('tools/official_derivatives/next_10_origin_catalog_candidate_10_19.tsv')


def read_rows(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def key(row):
    return (row.get('parent_url',''), row.get('parent_ncl_id',''), row.get('parent_diff_id',''))


def ready_discovery(row):
    return (
        row.get('discovery_status') == 'ready_for_catalog'
        and row.get('already_in_origin_manifest') == 'false'
        and row.get('public_safe_status') == 'pass'
        and row.get('exclusion_status') == 'available'
        and row.get('parent_url','').startswith('https://master.ricette.jp/')
        and row.get('parent_ncl_id','').startswith('NCL-')
        and row.get('parent_diff_id','').startswith('DIFF-')
        and row.get('canonical_url','').startswith('https://master.ricette.jp/derivatives/')
    )


def main():
    discovery_rows = read_rows(DISCOVERY)
    catalog_rows = read_rows(CATALOG)
    ready = {key(row): row for row in discovery_rows if ready_discovery(row)}
    errors = []
    for row in catalog_rows:
        rid = row.get('origin_catalog_id','')
        source = ready.get(key(row))
        if not source:
            errors.append('catalog_without_ready_discovery=' + rid)
            continue
        for field in ['source_category','parent_url','parent_title','parent_ncl_id','parent_diff_id','folder_id','canonical_url','exclusion_reason','reason_for_inclusion','risk_note']:
            if row.get(field,'') != source.get(field,''):
                errors.append('catalog_discovery_mismatch=' + rid + ':' + field)
        if row.get('already_in_origin_manifest') != 'false':
            errors.append('catalog_origin_already_used=' + rid)
        if row.get('public_safe_status') != 'pass':
            errors.append('catalog_public_safe_not_pass=' + rid)
        if row.get('exclusion_status') != 'available':
            errors.append('catalog_not_available=' + rid)
    print('check_set=next_10_discovery_to_origin_catalog_v1')
    print('ready_discovery_rows=' + str(len(ready)))
    print('origin_catalog_rows=' + str(len(catalog_rows)))
    if errors:
        print('\n'.join(errors[:50]))
        print('next_10_discovery_to_origin_catalog_pass=false')
        return 1
    print('next_10_discovery_to_origin_catalog_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
