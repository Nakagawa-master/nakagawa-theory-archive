#!/usr/bin/env python3
import csv
import sys
from pathlib import Path

P = Path('tools/official_derivatives/next_batch_intake_schema.tsv')
NEEDED = ['batch_id','slot_id','parent_url','parent_ncl_id','parent_diff_id','folder_id','canonical_url','quality_gate_status','export_status']


def main():
    with P.open(encoding='utf-8', newline='') as f:
        r = csv.DictReader(f, delimiter='\t')
        rows = list(r)
    fields = [x.get('field','') for x in rows]
    bad = [x for x in NEEDED if x not in fields]
    print('check_set=next_batch_schema_v1')
    if bad:
        print('\n'.join('missing=' + x for x in bad))
        print('next_batch_schema_pass=false')
        return 1
    print('schema_fields=' + str(len(fields)))
    print('next_batch_schema_pass=true')
    return 0


if __name__ == '__main__':
    sys.exit(main())
