#!/usr/bin/env python3
import csv
from pathlib import Path

BASE = Path('tools/official_derivatives')
NOTE = BASE / 'pr35_scope_choice_note.tsv'
SUMMARY = BASE / 'pr35_candidate_scope_summary.tsv'
EXPECTED = {
    'all_13': ('13', '78', '429', 'full', 'high', 'ready_for_choice'),
    'candidate_05_09_only': ('5', '30', '165', 'initial', 'low', 'ready_for_choice'),
    'candidate_10_17_only': ('8', '48', '264', 'followup', 'medium', 'hold'),
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    return list(csv.DictReader(path.open(encoding='utf-8'), delimiter='\t'))


def main() -> int:
    errors: list[str] = []
    rows = read_tsv(NOTE)
    summary_rows = read_tsv(SUMMARY)
    by_option = {row['scope_option']: row for row in rows}
    summary_by_option = {row['scope_option']: row for row in summary_rows}

    if set(by_option) != set(EXPECTED):
        errors.append('scope_option_set_mismatch')
    if set(by_option) != set(summary_by_option):
        errors.append('summary_option_set_mismatch')

    keys = ['folder_count', 'page_count', 'materialized_effect_units']
    for option, expected_values in EXPECTED.items():
        row = by_option.get(option)
        if not row:
            continue
        expected_numbers = expected_values[:3]
        expected_labels = expected_values[3:]
        for key, expected in zip(keys, expected_numbers):
            if row[key] != expected:
                errors.append(f'bad_{key}:{option}:{row[key]} expected={expected}')
            if summary_by_option.get(option, {}).get(key) != row[key]:
                errors.append(f'summary_mismatch_{key}:{option}')
        for key, expected in zip(['coverage_level', 'review_load', 'choice_state'], expected_labels):
            if row[key] != expected:
                errors.append(f'bad_{key}:{option}:{row[key]} expected={expected}')
        if row['source_pr'] != '35':
            errors.append(f'bad_source_pr:{option}:{row["source_pr"]}')
        if row['change_now'] != 'false':
            errors.append(f'bad_change_now:{option}:{row["change_now"]}')

    print('check_set=pr35_scope_choice_note_v1')
    print(f'choice_rows={len(rows)}')
    if errors:
        for error in errors:
            print(error)
        print('pr35_scope_choice_note_pass=false')
        return 1
    print('pr35_scope_choice_note_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
