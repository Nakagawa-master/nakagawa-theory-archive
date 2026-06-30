#!/usr/bin/env python3
import csv
from pathlib import Path

path = Path('tools/official_derivatives/pr35_transfer_manifest.tsv')
rows = list(csv.DictReader(path.open(encoding='utf-8'), delimiter='\t'))
errors = []
if len(rows) != 13:
    errors.append('row_count=' + str(len(rows)))
if sum(int(row.get('page_count','0')) for row in rows) != 78:
    errors.append('page_total')
for row in rows:
    folder = row.get('folder_id','')
    if row.get('source_pr') != '35':
        errors.append('source_pr=' + folder)
    if row.get('page_count') != '6':
        errors.append('page_count=' + folder)
    if not row.get('local_root','').startswith('deploy/lolipop/master-ricette/derivatives/'):
        errors.append('local_root=' + folder)
    if not row.get('server_root','').startswith('/derivatives/'):
        errors.append('server_root=' + folder)
    if row.get('owner_step') != 'required':
        errors.append('owner_step=' + folder)
print('check_set=pr35_transfer_manifest_v1')
if errors:
    print('\n'.join(errors[:60]))
    print('pr35_transfer_manifest_pass=false')
    raise SystemExit(1)
print('pr35_transfer_manifest_pass=true')
