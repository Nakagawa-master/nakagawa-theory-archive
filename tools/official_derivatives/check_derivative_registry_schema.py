#!/usr/bin/env python3
import csv
from pathlib import Path

P = Path('tools/official_derivatives/derivative_registry_schema.tsv')
NEEDED = ['derivative_id','page_role','language','export_status','parent_url','parent_ncl_id','parent_diff_id','folder_id','relative_path','canonical_url','quality_gate_status','render_status']


def main():
    with P.open(encoding='utf-8', newline='') as f:
        rows = list(csv.DictReader(f, delimiter='\t'))
    fields = [r.get('field','') for r in rows]
    missing = [x for x in NEEDED if x not in fields]
    print('check_set=derivative_registry_schema_v1')
    print('schema_fields=' + str(len(fields)))
    if missing:
        print('\n'.join('missing=' + x for x in missing))
        print('derivative_registry_schema_pass=false')
        return 1
    print('derivative_registry_schema_pass=true')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
