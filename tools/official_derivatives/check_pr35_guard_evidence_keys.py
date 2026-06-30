#!/usr/bin/env python3
import csv
from pathlib import Path

PATH = Path('tools/official_derivatives/pr35_guard_evidence_keys.tsv')
EXPECTED = {
    'origin_traceability': ('candidate_list_check', 'green'),
    'quality_checks': ('preflight_check', 'green'),
    'ai_index_integrity': ('entry_signal_check', 'green'),
    'human_entry_surface': ('option_brief', 'present'),
    'batch_validation': ('scope_summary_check', 'green'),
    'manual_review_need': ('guard_table_check', 'false'),
}


def main() -> int:
    rows = list(csv.DictReader(PATH.open(encoding='utf-8'), delimiter='\t'))
    errors: list[str] = []
    by_area = {row['guard_area']: row for row in rows}
    if set(by_area) != set(EXPECTED):
        errors.append('guard_area_set_mismatch')
    if len(rows) != 6:
        errors.append(f'row_count={len(rows)} expected=6')
    for area, expected in EXPECTED.items():
        row = by_area.get(area)
        if not row:
            continue
        expected_key, expected_state = expected
        if row['source_pr'] != '35':
            errors.append(f'bad_source_pr:{area}')
        if row['evidence_key'] != expected_key:
            errors.append(f'bad_evidence_key:{area}:{row["evidence_key"]}')
        if row['expected_state'] != expected_state:
            errors.append(f'bad_expected_state:{area}:{row["expected_state"]}')
        if row['change_now'] != 'false':
            errors.append(f'bad_change_now:{area}')
    print('check_set=pr35_guard_evidence_keys_v1')
    print(f'rows={len(rows)}')
    if errors:
        for error in errors:
            print(error)
        print('pr35_guard_evidence_keys_pass=false')
        return 1
    print('pr35_guard_evidence_keys_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
