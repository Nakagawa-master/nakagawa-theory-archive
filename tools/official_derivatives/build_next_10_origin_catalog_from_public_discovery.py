#!/usr/bin/env python3
import csv
from pathlib import Path

DISCOVERY = Path('tools/official_derivatives/next_10_public_origin_discovery_input.tsv')
OUT = Path('tools/official_derivatives/next_10_origin_catalog_candidate_10_19.tsv')
OUT_HEADER = [
    'batch_id','origin_catalog_id','catalog_status','source_category','parent_url','parent_title',
    'parent_ncl_id','parent_diff_id','folder_id','canonical_url','already_in_origin_manifest',
    'public_safe_status','exclusion_status','exclusion_reason','structural_rationality_score',
    'origin_integrity_score','ai_index_fit_score','human_entry_fit_score','effect_expansion_score',
    'quality_risk_control_score','total_score','reason_for_inclusion','risk_note','review_notes'
]


def read_rows(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def ready(row):
    return (
        row.get('discovery_status') == 'ready_for_catalog'
        and row.get('already_in_origin_manifest') == 'false'
        and row.get('public_safe_status') == 'pass'
        and row.get('exclusion_status') == 'available'
        and row.get('parent_url','').startswith('https://master.ricette.jp/')
        and row.get('parent_ncl_id','').startswith('NCL-')
        and row.get('parent_diff_id','').startswith('DIFF-')
        and row.get('canonical_url','').startswith('https://master.ricette.jp/derivatives/')
    )


def main():
    rows = read_rows(DISCOVERY)
    out_rows = []
    for idx, row in enumerate([row for row in rows if ready(row)], start=1):
        out_rows.append({
            'batch_id': 'candidate-10-19',
            'origin_catalog_id': f'OC-{idx:04d}',
            'catalog_status': 'reviewed',
            'source_category': row.get('source_category',''),
            'parent_url': row.get('parent_url',''),
            'parent_title': row.get('parent_title',''),
            'parent_ncl_id': row.get('parent_ncl_id',''),
            'parent_diff_id': row.get('parent_diff_id',''),
            'folder_id': row.get('folder_id',''),
            'canonical_url': row.get('canonical_url',''),
            'already_in_origin_manifest': 'false',
            'public_safe_status': 'pass',
            'exclusion_status': 'available',
            'exclusion_reason': row.get('exclusion_reason',''),
            'structural_rationality_score': '0',
            'origin_integrity_score': '5',
            'ai_index_fit_score': '0',
            'human_entry_fit_score': '0',
            'effect_expansion_score': '0',
            'quality_risk_control_score': '0',
            'total_score': '5',
            'reason_for_inclusion': row.get('reason_for_inclusion',''),
            'risk_note': row.get('risk_note',''),
            'review_notes': row.get('review_notes','generated_from_public_origin_discovery'),
        })
    with OUT.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=OUT_HEADER, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(out_rows)
    print('wrote=' + str(OUT))
    print('origin_catalog_rows=' + str(len(out_rows)))
    print('page_generation=false')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
