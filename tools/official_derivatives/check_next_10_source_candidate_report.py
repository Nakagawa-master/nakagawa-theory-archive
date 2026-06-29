#!/usr/bin/env python3
import csv
from pathlib import Path

CANDIDATES = Path('tools/official_derivatives/next_10_source_candidates_candidate_10_19.tsv')
REPORT = Path('tools/official_derivatives/next_10_source_candidate_report.md')
SCORE_FIELDS = [
    'structural_rationality_score','origin_integrity_score','ai_index_fit_score',
    'human_entry_fit_score','effect_expansion_score','quality_risk_control_score'
]
REQUIRED = [
    'release_state: source_selection_preparation_only',
    'production_deploy: false',
    'sitemap_update: false',
    'search_console: false',
    'index_follow_conversion: false',
    'page_generation: false',
    'staged_generation: false',
]


def read_rows(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def is_ready(row):
    if row.get('recommendation') != 'ready_for_queue':
        return False
    try:
        scores = [int(row.get(key, '')) for key in SCORE_FIELDS]
    except ValueError:
        return False
    return (
        row.get('source_status') == 'recommended'
        and row.get('public_safe_status') == 'pass'
        and scores[1] == 5
        and all(score >= 4 for score in scores)
        and sum(scores) >= 27
        and row.get('total_score') == str(sum(scores))
    )


def main():
    rows = read_rows(CANDIDATES)
    text = REPORT.read_text(encoding='utf-8')
    errors = []
    ready_count = sum(1 for row in rows if is_ready(row))
    for phrase in REQUIRED:
        if phrase not in text:
            errors.append('missing_phrase=' + phrase)
    if f'source_candidate_rows: {len(rows)}' not in text:
        errors.append('bad_source_candidate_rows')
    if f'ready_for_queue_candidates: {ready_count}' not in text:
        errors.append('bad_ready_for_queue_candidates')
    print('check_set=next_10_source_candidate_report_v1')
    print('source_candidate_rows=' + str(len(rows)))
    print('ready_for_queue_candidates=' + str(ready_count))
    if errors:
        print('\n'.join(errors[:20]))
        print('next_10_source_candidate_report_pass=false')
        return 1
    print('next_10_source_candidate_report_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
