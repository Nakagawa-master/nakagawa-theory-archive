#!/usr/bin/env python3
import csv
from pathlib import Path

p = Path('tools/official_derivatives/pr35_publication_scope_summary.tsv')
rows = list(csv.DictReader(p.open(encoding='utf-8'), delimiter='\t'))
errors = []
if len(rows) != 1:
    errors.append('rows=' + str(len(rows)))
row = rows[0] if rows else {}
for k, v in {'source_pr':'35','folder_count':'13','page_count':'78','registry_rows':'78'}.items():
    if row.get(k) != v:
        errors.append(k + '=' + row.get(k, ''))
print('check_set=pr35_publication_scope_summary_v1')
if errors:
    print('\n'.join(errors))
    print('pr35_publication_scope_summary_pass=false')
    raise SystemExit(1)
print('pr35_publication_scope_summary_pass=true')
