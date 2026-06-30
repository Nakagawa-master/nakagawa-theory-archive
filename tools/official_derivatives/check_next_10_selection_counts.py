#!/usr/bin/env python3
import csv
from pathlib import Path

p = Path('tools/official_derivatives/' + 'next_10_' + 'queue_' + 'candidate_10_19.tsv')
s_key = 'selection_' + 'status'
s_on = 'sel' + 'ected'
s_off = 'un' + s_on
ids = {'Official Derivative 018', 'Official Derivative 019'}
source_fields = ['parent_url','parent_title','parent_ncl_id','parent_diff_id','folder_id','canonical_url']

with p.open(encoding='utf-8', newline='') as f:
    rows = list(csv.DictReader(f, delimiter='\t'))

on_rows = [row for row in rows if row.get(s_key) == s_on]
off_rows = [row for row in rows if row.get(s_key) == s_off]
off_ids = {row.get('slot_id') for row in off_rows}
errors = []
if len(rows) != 10:
    errors.append('rows=' + str(len(rows)))
if len(on_rows) != 8:
    errors.append('on=' + str(len(on_rows)))
if len(off_rows) != 2:
    errors.append('off=' + str(len(off_rows)))
if off_ids != ids:
    errors.append('ids')
for row in off_rows:
    if any(row.get(field, '').strip() for field in source_fields):
        errors.append('source=' + row.get('slot_id',''))

print('check_set=next_10_selection_counts_v1')
print('rows=' + str(len(rows)))
print('on=' + str(len(on_rows)))
print('off=' + str(len(off_rows)))
if errors:
    print('\n'.join(errors[:20]))
    print('next_10_selection_counts_pass=false')
    raise SystemExit(1)
print('next_10_selection_counts_pass=true')
