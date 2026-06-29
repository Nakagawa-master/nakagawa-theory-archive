#!/usr/bin/env python3
import csv
from pathlib import Path

io_rows = list(csv.DictReader(Path('tools/official_derivatives/stage_io.tsv').open(encoding='utf-8'), delimiter='\t'))
condition_rows = list(csv.DictReader(Path('tools/official_derivatives/stage_conditions.tsv').open(encoding='utf-8'), delimiter='\t'))
io_stages = [r.get('stage','') for r in io_rows]
condition_stages = [r.get('stage','') for r in condition_rows]
print('check_set=stage_conditions_v1')
if condition_stages != io_stages:
    print('stage_conditions_pass=false')
    raise SystemExit(1)
for row in condition_rows:
    if not row.get('artifact') or not row.get('ok_key') or not row.get('stop_key'):
        print('stage_conditions_pass=false')
        raise SystemExit(1)
print('stage_conditions_pass=true')
