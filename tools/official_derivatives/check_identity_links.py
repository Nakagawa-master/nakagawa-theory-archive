#!/usr/bin/env python3
import csv
from pathlib import Path
from derive_official_derivative_identity import row_identity_errors

HERE = Path(__file__).resolve().parent
FILES = ['origin_manifest.tsv','next_10_public_origin_discovery_input.tsv','next_10_origin_catalog_candidate_10_19.tsv','next_10_source_candidates_candidate_10_19.tsv','next_10_queue_candidate_10_19.tsv','next_batch_intake_candidate_10_19.tsv']


def rows(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def main():
    errors = []
    checked = 0
    for name in FILES:
        path = HERE / name
        if not path.exists():
            continue
        for line_no, row in enumerate(rows(path), start=2):
            if row.get('parent_ncl_id','').strip():
                checked += 1
            errors += row_identity_errors(row, name + ':' + str(line_no))
    print('check_set=identity_links_v1')
    print('checked_rows=' + str(checked))
    if errors:
        print('\n'.join(errors[:60]))
        print('identity_links_pass=false')
        return 1
    print('identity_links_pass=true')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
