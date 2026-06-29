#!/usr/bin/env python3
import csv
from pathlib import Path
launch_rows = list(csv.DictReader(Path('tools/official_derivatives/launch_surface_map.tsv').open(encoding='utf-8'), delimiter='\t'))
impact_rows = list(csv.DictReader(Path('tools/official_derivatives/impact_execution_map.tsv').open(encoding='utf-8'), delimiter='\t'))
launch = {r.get('surface','') for r in launch_rows if r.get('surface') != 'official_pages'}
impact = {r.get('surface','') for r in impact_rows}
print('check_set=impact_execution_map_v1')
if launch != impact:
    print('impact_execution_map_pass=false')
    raise SystemExit(1)
for row in impact_rows:
    if not row.get('required_artifact') or not row.get('impact_route') or not row.get('owner_boundary'):
        print('impact_execution_map_pass=false')
        raise SystemExit(1)
print('impact_execution_map_pass=true')
