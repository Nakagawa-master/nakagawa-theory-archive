#!/usr/bin/env python3
import csv
import subprocess
import sys
from pathlib import Path

SCHEMA = Path('tools/official_derivatives/derivative_registry_schema.tsv')
REGISTRY = Path('tools/official_derivatives/derivative_registry_candidate_05_09.tsv')
NEEDED = ['derivative_id','page_role','language','export_status','parent_url','parent_ncl_id','parent_diff_id','folder_id','relative_path','canonical_url','quality_gate_status','render_status']


def fields(path):
    with path.open(encoding='utf-8', newline='') as f:
        return [r.get('field','') for r in csv.DictReader(f, delimiter='\t')]


def row_count(path):
    with path.open(encoding='utf-8', newline='') as f:
        return len(list(csv.DictReader(f, delimiter='\t')))


def main():
    print('check_set=derivative_registry_schema_v2')
    result = subprocess.run([sys.executable, 'tools/official_derivatives/build_derivative_registry.py'])
    if result.returncode != 0:
        print('derivative_registry_schema_pass=false')
        return result.returncode
    found = fields(SCHEMA)
    missing = [x for x in NEEDED if x not in found]
    print('schema_fields=' + str(len(found)))
    rows = row_count(REGISTRY) if REGISTRY.exists() else 0
    print('registry_rows=' + str(rows))
    if missing or rows != 30:
        for x in missing:
            print('missing=' + x)
        print('derivative_registry_schema_pass=false')
        return 1
    print('derivative_registry_schema_pass=true')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
