#!/usr/bin/env python3
import csv
from pathlib import Path

root = Path('tools/official_derivatives')
src = root / 'candidate_activation_list_pr35.tsv'
out = root / 'pr35_transfer_manifest.tsv'
fields = ['source_pr','folder_id','page_count','local_root','server_root','owner_step']
rows = list(csv.DictReader(src.open(encoding='utf-8'), delimiter='\t'))
items = []
for row in rows:
    folder = row['folder_id']
    items.append({
        'source_pr': row['source_pr'],
        'folder_id': folder,
        'page_count': row['page_count'],
        'local_root': 'deploy/lolipop/master-ricette/derivatives/' + folder,
        'server_root': '/derivatives/' + folder,
        'owner_step': 'required',
    })
with out.open('w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields, delimiter='\t')
    w.writeheader()
    w.writerows(items)
print('build_set=pr35_transfer_manifest_v1')
print('rows=' + str(len(items)))
