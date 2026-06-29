#!/usr/bin/env python3
import csv
from pathlib import Path

DISCOVERY = Path('tools/official_derivatives/next_10_public_origin_discovery_input.tsv')
OVERLAY = Path('tools/official_derivatives/next_10_verified_origin_overlay_20260629.tsv')
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


def main():
    discovery_rows = {row.get('discovery_id',''): row for row in read_rows(DISCOVERY)}
    overlay_rows = read_rows(OVERLAY)
    out_rows = []
    for index, overlay in enumerate(overlay_rows, start=1):
        discovery_id = overlay.get('discovery_id','')
        source = discovery_rows.get(discovery_id)
        if not source:
            raise SystemExit('overlay source not found: ' + discovery_id)
        out_rows.append({
            'batch_id': 'candidate-10-19',
            'origin_catalog_id': f'OC-{index:04d}',
            'catalog_status': 'reviewed',
            'source_category': source.get('source_category',''),
            'parent_url': source.get('parent_url',''),
            'parent_title': source.get('parent_title',''),
            'parent_ncl_id': overlay.get('parent_ncl_id',''),
            'parent_diff_id': overlay.get('parent_diff_id',''),
            'folder_id': overlay.get('folder_id',''),
            'canonical_url': overlay.get('canonical_url',''),
            'already_in_origin_manifest': 'false',
            'public_safe_status': 'pass',
            'exclusion_status': 'available',
            'exclusion_reason': 'live_ncl_diff_confirmed',
            'structural_rationality_score': '0',
            'origin_integrity_score': '5',
            'ai_index_fit_score': '0',
            'human_entry_fit_score': '0',
            'effect_expansion_score': '0',
            'quality_risk_control_score': '0',
            'total_score': '5',
            'reason_for_inclusion': source.get('reason_for_inclusion',''),
            'risk_note': source.get('risk_note',''),
            'review_notes': 'generated_from_verified_overlay; scoring_pending',
        })
    with OUT.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=OUT_HEADER, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(out_rows)
    print('wrote=' + str(OUT))
    print('origin_catalog_rows=' + str(len(out_rows)))
    print('ready_for_candidate_rows=0')
    print('page_generation=false')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
