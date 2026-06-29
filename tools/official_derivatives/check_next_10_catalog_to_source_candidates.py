#!/usr/bin/env python3
import csv
from pathlib import Path

CATALOG = Path('tools/official_derivatives/next_10_origin_catalog_candidate_10_19.tsv')
CANDIDATES = Path('tools/official_derivatives/next_10_source_candidates_candidate_10_19.tsv')
SCORE_FIELDS = [
    'structural_rationality_score','origin_integrity_score','ai_index_fit_score',
    'human_entry_fit_score','effect_expansion_score','quality_risk_control_score'
]


def read_rows(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def ready_catalog(row):
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


def key(row):
    return (row.get('parent_url',''), row.get('parent_ncl_id',''), row.get('parent_diff_id',''))


def main():
    catalog_rows = read_rows(CATALOG)
    candidate_rows = read_rows(CANDIDATES)
    ready_keys = {key(row): row for row in catalog_rows if ready_catalog(row)}
    errors = []
    for row in candidate_rows:
        rid = row.get('source_candidate_id','')
        catalog = ready_keys.get(key(row))
        if not catalog:
            errors.append('candidate_without_ready_catalog=' + rid)
            continue
        for field in ['source_category','parent_url','parent_title','parent_ncl_id','parent_diff_id','folder_id','canonical_url'] + SCORE_FIELDS + ['total_score','reason_for_inclusion','risk_note']:
            catalog_field = 'source_category' if field == 'source_category' else field
            if row.get(field,'') != catalog.get(catalog_field,''):
                errors.append('candidate_catalog_mismatch=' + rid + ':' + field)
        if row.get('source_status') != 'recommended':
            errors.append('candidate_not_recommended=' + rid)
        if row.get('public_safe_status') != 'pass':
            errors.append('candidate_public_safe_not_pass=' + rid)
        if row.get('recommendation') != 'ready_for_queue':
            errors.append('candidate_not_ready_for_queue=' + rid)
    print('check_set=next_10_catalog_to_source_candidates_v1')
    print('ready_catalog_rows=' + str(len(ready_keys)))
    print('source_candidate_rows=' + str(len(candidate_rows)))
    if errors:
        print('\n'.join(errors[:50]))
        print('next_10_catalog_to_source_candidates_pass=false')
        return 1
    print('next_10_catalog_to_source_candidates_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
