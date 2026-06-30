#!/usr/bin/env python3
import csv
from pathlib import Path

PATH = Path('tools/official_derivatives/pr35_rank1_guard_matrix.tsv')
AREAS = {
    'origin_traceability',
    'quality_checks',
    'ai_index_integrity',
    'human_entry_surface',
    'batch_validation',
    'manual_review_need',
}


def main() -> int:
    rows = list(csv.DictReader(PATH.open(encoding='utf-8'), delimiter='\t'))
    errors: list[str] = []
    areas = {row['guard_area'] for row in rows}
    if len(rows) != 6:
        errors.append(f'row_count={len(rows)} expected=6')
    if areas != AREAS:
        errors.append('area_set_mismatch')
    for row in rows:
        area = row['guard_area']
        if row['rank_option'] != 'all_13':
            errors.append(f'bad_rank_option:{area}')
        if row['source_pr'] != '35':
            errors.append(f'bad_source_pr:{area}')
        if row['fallback_option'] != 'candidate_05_09_only':
            errors.append(f'bad_secondary_option:{area}')
        if row['change_now'] != 'false':
            errors.append(f'bad_change_now:{area}')
    print('check_set=pr35_rank1_guard_table_v1')
    print(f'guard_rows={len(rows)}')
    if errors:
        for error in errors:
            print(error)
        print('pr35_rank1_guard_table_pass=false')
        return 1
    print('pr35_rank1_guard_table_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
