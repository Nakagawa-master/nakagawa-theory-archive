#!/usr/bin/env python3
import csv
from pathlib import Path

P = Path('tools/official_derivatives/derivative_registry_candidate_05_09.tsv')
BAD = ['private_only','internal_only','qgate_pending']


def rows():
    with P.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def main():
    data = rows()
    errors = []
    for i, row in enumerate(data, start=1):
        text = '\t'.join(row.values()).lower()
        if any(x in text for x in BAD):
            errors.append('bad_marker_row=' + str(i))
        if row.get('origin_author') != 'Nakagawa Master':
            errors.append('bad_origin_author_row=' + str(i))
        if row.get('source_archive') != 'master.ricette.jp':
            errors.append('bad_source_archive_row=' + str(i))
    print('check_set=derivative_registry_boundary_v1')
    print('registry_rows=' + str(len(data)))
    if errors:
        print('\n'.join(errors[:30]))
        print('derivative_registry_boundary_pass=false')
        return 1
    print('derivative_registry_boundary_pass=true')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
