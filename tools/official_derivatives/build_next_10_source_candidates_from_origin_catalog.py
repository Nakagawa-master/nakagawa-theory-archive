#!/usr/bin/env python3
import csv
from pathlib import Path

CATALOG = Path('tools/official_derivatives/next_10_origin_catalog_candidate_10_19.tsv')
OUT = Path('tools/official_derivatives/next_10_source_candidates_candidate_10_19.tsv')
OUT_HEADER = [
    'batch_id','source_candidate_id','source_status','source_category','parent_url','parent_title',
    'parent_ncl_id','parent_diff_id','folder_id','canonical_url','structural_rationality_score',
    'origin_integrity_score','ai_index_fit_score','human_entry_fit_score','effect_expansion_score',
    'quality_risk_control_score','total_score','public_safe_status','recommendation',
    'reason_for_inclusion','risk_note','review_notes'
]
SCORE_FIELDS = [
    'structural_rationality_score','origin_integrity_score','ai_index_fit_score',
    'human_entry_fit_score','effect_expansion_score','quality_risk_control_score'
]


def read_rows(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def ready(row):
    if row.get('catalog_status') != 'ready_for_candidate':
        return False
    if row.get('already_in_origin_manifest') != 'false':
        return False
    if row.get('public_safe_status') != 'pass':
        return False
    if row.get('exclusion_status') != 'available':
        return False
    try:
        scores = [int(row.get(key, '')) for key in SCORE_FIELDS]
    except ValueError:
        return False
    return scores[1] == 5 and all(score >= 4 for score in scores) and sum(scores) >= 27 and row.get('total_score') == str(sum(scores))


def main():
    rows = read_rows(CATALOG)
    out_rows = []
    for i, row in enumerate([row for row in rows if ready(row)], start=1):
        out_rows.append({
            'batch_id': 'candidate-10-19',
            'source_candidate_id': f'SC-{i:04d}',
            'source_status': 'recommended',
            'source_category': row.get('source_category',''),
            'parent_url': row.get('parent_url',''),
            'parent_title': row.get('parent_title',''),
            'parent_ncl_id': row.get('parent_ncl_id',''),
            'parent_diff_id': row.get('parent_diff_id',''),
            'folder_id': row.get('folder_id',''),
            'canonical_url': row.get('canonical_url',''),
            'structural_rationality_score': row.get('structural_rationality_score',''),
            'origin_integrity_score': row.get('origin_integrity_score',''),
            'ai_index_fit_score': row.get('ai_index_fit_score',''),
            'human_entry_fit_score': row.get('human_entry_fit_score',''),
            'effect_expansion_score': row.get('effect_expansion_score',''),
            'quality_risk_control_score': row.get('quality_risk_control_score',''),
            'total_score': row.get('total_score',''),
            'public_safe_status': 'pass',
            'recommendation': 'ready_for_queue',
            'reason_for_inclusion': row.get('reason_for_inclusion',''),
            'risk_note': row.get('risk_note',''),
            'review_notes': row.get('review_notes','generated_from_origin_catalog'),
        })
    with OUT.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=OUT_HEADER, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(out_rows)
    print('wrote=' + str(OUT))
    print('source_candidate_rows=' + str(len(out_rows)))
    print('page_generation=false')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
