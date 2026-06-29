#!/usr/bin/env python3
import csv
from pathlib import Path

CATALOG = Path('tools/official_derivatives/next_10_origin_catalog_candidate_10_19.tsv')
DISCOVERY = Path('tools/official_derivatives/next_10_public_origin_discovery_input.tsv')
SCORE_OVERLAY = Path('tools/official_derivatives/next_10_source_score_overlay_20260630.tsv')
CANDIDATES = Path('tools/official_derivatives/next_10_source_candidates_candidate_10_19.tsv')
SCORE_FIELDS = [
    'structural_rationality_score','origin_integrity_score','ai_index_fit_score',
    'human_entry_fit_score','effect_expansion_score','quality_risk_control_score'
]


def read_rows(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def key(row):
    return (row.get('parent_url',''), row.get('parent_ncl_id',''), row.get('parent_diff_id',''))


def ready_overlay(row):
    if row.get('recommendation') != 'ready_for_candidate':
        return False
    try:
        scores = [int(row.get(field,'')) for field in SCORE_FIELDS]
    except ValueError:
        return False
    return scores[1] == 5 and all(score >= 4 for score in scores) and sum(scores) >= 27 and row.get('total_score') == str(sum(scores))


def main():
    catalog_rows = read_rows(CATALOG)
    discovery_rows = read_rows(DISCOVERY)
    overlay_rows = read_rows(SCORE_OVERLAY)
    candidate_rows = read_rows(CANDIDATES)
    catalog_by_key = {key(row): row for row in catalog_rows}
    discovery_by_key = {key(row): row for row in discovery_rows}
    overlay_by_catalog_id = {row.get('origin_catalog_id',''): row for row in overlay_rows if ready_overlay(row)}
    ready_count = len(overlay_by_catalog_id)
    errors = []
    for row in candidate_rows:
        rid = row.get('source_candidate_id','')
        catalog = catalog_by_key.get(key(row))
        if not catalog:
            errors.append('candidate_without_catalog=' + rid)
            continue
        overlay = overlay_by_catalog_id.get(catalog.get('origin_catalog_id',''))
        if not overlay:
            errors.append('candidate_without_ready_score_overlay=' + rid)
            continue
        discovery = discovery_by_key.get(key(row))
        if not discovery:
            errors.append('candidate_without_discovery=' + rid)
            continue
        for field in ['source_category','parent_url','parent_ncl_id','parent_diff_id','folder_id','canonical_url']:
            if row.get(field,'') != catalog.get(field,''):
                errors.append('candidate_catalog_mismatch=' + rid + ':' + field)
        for field in ['parent_title','reason_for_inclusion','risk_note']:
            if row.get(field,'') != discovery.get(field,''):
                errors.append('candidate_discovery_mismatch=' + rid + ':' + field)
        for field in SCORE_FIELDS + ['total_score']:
            if row.get(field,'') != overlay.get(field,''):
                errors.append('candidate_score_overlay_mismatch=' + rid + ':' + field)
        if row.get('source_status') != 'recommended':
            errors.append('candidate_not_recommended=' + rid)
        if row.get('public_safe_status') != 'pass':
            errors.append('candidate_public_safe_not_pass=' + rid)
        if row.get('recommendation') != 'ready_for_queue':
            errors.append('candidate_not_ready_for_queue=' + rid)
    print('check_set=next_10_catalog_to_source_candidates_v2')
    print('ready_score_overlay_rows=' + str(ready_count))
    print('source_candidate_rows=' + str(len(candidate_rows)))
    if errors:
        print('\n'.join(errors[:50]))
        print('next_10_catalog_to_source_candidates_pass=false')
        return 1
    print('next_10_catalog_to_source_candidates_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
