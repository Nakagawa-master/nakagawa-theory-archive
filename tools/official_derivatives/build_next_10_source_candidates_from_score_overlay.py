#!/usr/bin/env python3
import csv
from pathlib import Path

CATALOG = Path('tools/official_derivatives/next_10_origin_catalog_candidate_10_19.tsv')
DISCOVERY = Path('tools/official_derivatives/next_10_public_origin_discovery_input.tsv')
SCORE_OVERLAY = Path('tools/official_derivatives/next_10_source_score_overlay_20260630.tsv')
OUT = Path('tools/official_derivatives/next_10_source_candidates_candidate_10_19.tsv')

HEADER = [
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


def key(row):
    return (row.get('parent_url',''), row.get('parent_ncl_id',''), row.get('parent_diff_id',''))


def main():
    catalog_by_id = {row.get('origin_catalog_id',''): row for row in read_rows(CATALOG)}
    discovery_by_key = {key(row): row for row in read_rows(DISCOVERY)}
    overlay_rows = read_rows(SCORE_OVERLAY)
    out_rows = []
    for overlay in overlay_rows:
        if overlay.get('recommendation') != 'ready_for_candidate':
            continue
        catalog = catalog_by_id.get(overlay.get('origin_catalog_id',''))
        if not catalog:
            raise SystemExit('missing catalog row: ' + overlay.get('origin_catalog_id',''))
        discovery = discovery_by_key.get(key(catalog))
        if not discovery:
            raise SystemExit('missing discovery row for catalog: ' + overlay.get('origin_catalog_id',''))
        index = len(out_rows) + 1
        row = {
            'batch_id': 'candidate-10-19',
            'source_candidate_id': f'SC-{index:04d}',
            'source_status': 'recommended',
            'source_category': catalog.get('source_category',''),
            'parent_url': catalog.get('parent_url',''),
            'parent_title': discovery.get('parent_title',''),
            'parent_ncl_id': catalog.get('parent_ncl_id',''),
            'parent_diff_id': catalog.get('parent_diff_id',''),
            'folder_id': catalog.get('folder_id',''),
            'canonical_url': catalog.get('canonical_url',''),
            'public_safe_status': 'pass',
            'recommendation': 'ready_for_queue',
            'reason_for_inclusion': discovery.get('reason_for_inclusion',''),
            'risk_note': discovery.get('risk_note',''),
            'review_notes': 'generated_from_score_overlay; queue_not_updated; page_generation_false',
        }
        for field in SCORE_FIELDS:
            row[field] = overlay.get(field,'')
        row['total_score'] = overlay.get('total_score','')
        out_rows.append(row)
    with OUT.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=HEADER, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(out_rows)
    print('wrote=' + str(OUT))
    print('source_candidate_rows=' + str(len(out_rows)))
    print('ready_for_queue_candidates=' + str(len(out_rows)))
    print('queue_update=false')
    print('page_generation=false')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
