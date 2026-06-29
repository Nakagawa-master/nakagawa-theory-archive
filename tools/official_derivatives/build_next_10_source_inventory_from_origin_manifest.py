#!/usr/bin/env python3
import csv
from pathlib import Path

ORIGIN = Path('tools/official_derivatives/origin_manifest.tsv')
OUT = Path('tools/official_derivatives/next_10_source_inventory_candidate_10_19.tsv')
HEADER = [
    'batch_id','source_inventory_id','source_scope','origin_manifest_status','selection_eligibility',
    'parent_url','parent_title','parent_ncl_id','parent_diff_id','folder_id','canonical_url',
    'exclusion_reason','public_safe_status','notes'
]


def slug_title(row):
    title = row.get('hub_title', '').strip()
    if '｜' in title:
        return title.split('｜', 1)[1].replace('｜公式派生物一覧', '').strip()
    return title


def main():
    with ORIGIN.open(encoding='utf-8', newline='') as f:
        rows = list(csv.DictReader(f, delimiter='\t'))
    out_rows = []
    for i, row in enumerate(rows, start=1):
        status = row.get('export_status', '').strip()
        eligibility = 'excluded'
        exclusion = 'already_active_or_staged_official_derivative'
        if status not in {'active', 'staged'}:
            eligibility = 'review_required'
            exclusion = 'origin_manifest_status_requires_review'
        out_rows.append({
            'batch_id': 'candidate-10-19',
            'source_inventory_id': f'INV-{i:04d}',
            'source_scope': 'origin_manifest_current_rows_only',
            'origin_manifest_status': status,
            'selection_eligibility': eligibility,
            'parent_url': row.get('parent_url', '').strip(),
            'parent_title': slug_title(row),
            'parent_ncl_id': row.get('parent_ncl_id', '').strip(),
            'parent_diff_id': row.get('parent_diff_id', '').strip(),
            'folder_id': row.get('folder_id', '').strip(),
            'canonical_url': row.get('canonical_url', '').strip(),
            'exclusion_reason': exclusion,
            'public_safe_status': 'pass',
            'notes': 'inventory_only_not_a_source_selection',
        })
    with OUT.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=HEADER, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(out_rows)
    print('wrote=' + str(OUT))
    print('inventory_rows=' + str(len(out_rows)))
    print('selected_sources=0')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
