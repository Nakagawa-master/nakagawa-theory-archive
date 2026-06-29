#!/usr/bin/env python3
import csv
from pathlib import Path

CATALOG = Path('tools/official_derivatives/next_10_origin_catalog_candidate_10_19.tsv')
OVERLAY = Path('tools/official_derivatives/next_10_source_score_overlay_20260630.tsv')
HEADER = [
    'origin_catalog_id','score_status','structural_rationality_score','origin_integrity_score',
    'ai_index_fit_score','human_entry_fit_score','effect_expansion_score','quality_risk_control_score',
    'total_score','recommendation','note'
]
SCORE_FIELDS = [
    'structural_rationality_score','origin_integrity_score','ai_index_fit_score',
    'human_entry_fit_score','effect_expansion_score','quality_risk_control_score'
]


def read_rows(path):
    with path.open(encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        return reader.fieldnames or [], list(reader)


def as_int(value):
    try:
        number = int(value)
    except ValueError:
        return None
    if number < 0 or number > 5:
        return None
    return number


def main():
    _, catalog_rows = read_rows(CATALOG)
    header, rows = read_rows(OVERLAY)
    catalog_ids = {row.get('origin_catalog_id','') for row in catalog_rows}
    errors = []
    ready_count = 0
    defer_count = 0
    if header != HEADER:
        errors.append('bad_source_score_overlay_header')
    seen = set()
    for row in rows:
        rid = row.get('origin_catalog_id','')
        if rid in seen:
            errors.append('duplicate_origin_catalog_id=' + rid)
        seen.add(rid)
        if rid not in catalog_ids:
            errors.append('overlay_id_not_in_catalog=' + rid)
        scores = [as_int(row.get(key,'')) for key in SCORE_FIELDS]
        if any(value is None for value in scores):
            errors.append('bad_score=' + rid)
            continue
        total = sum(scores)
        if row.get('total_score') != str(total):
            errors.append('score_total_mismatch=' + rid)
        recommendation = row.get('recommendation','')
        if recommendation == 'ready_for_candidate':
            ready_count += 1
            if scores[1] != 5 or any(value < 4 for value in scores) or total < 27:
                errors.append('ready_score_below_gate=' + rid)
        elif recommendation == 'defer':
            defer_count += 1
            if total >= 27 and all(value >= 4 for value in scores) and scores[1] == 5:
                errors.append('deferred_score_meets_ready_gate=' + rid)
        else:
            errors.append('bad_recommendation=' + rid)
        if not row.get('note','').strip():
            errors.append('missing_note=' + rid)
    if len(rows) != 9:
        errors.append('score_overlay_rows=' + str(len(rows)) + ':expected=9')
    if ready_count != 8:
        errors.append('ready_for_candidate_overlay_rows=' + str(ready_count) + ':expected=8')
    if defer_count != 1:
        errors.append('defer_overlay_rows=' + str(defer_count) + ':expected=1')
    print('check_set=next_10_source_score_overlay_v1')
    print('score_overlay_rows=' + str(len(rows)))
    print('ready_for_candidate_overlay_rows=' + str(ready_count))
    print('defer_overlay_rows=' + str(defer_count))
    print('source_selection=false')
    print('page_generation=false')
    if errors:
        print('\n'.join(errors[:50]))
        print('next_10_source_score_overlay_pass=false')
        return 1
    print('next_10_source_score_overlay_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
