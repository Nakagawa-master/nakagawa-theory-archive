#!/usr/bin/env python3
import csv
from pathlib import Path

BASE = Path('tools/official_derivatives')
SUMMARY = BASE / 'pr35_candidate_scope_summary.tsv'
CANDIDATES = BASE / 'candidate_activation_list_pr35.tsv'
CHOICE_NOTE = BASE / 'pr35_scope_choice_note.tsv'
EXPECTED_OPTIONS = {'all_13', 'candidate_05_09_only', 'candidate_10_17_only'}
EXPECTED_CHOICE = {
    'all_13': ('full', 'high', 'ready_for_choice'),
    'candidate_05_09_only': ('initial', 'low', 'ready_for_choice'),
    'candidate_10_17_only': ('followup', 'medium', 'hold'),
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    return list(csv.DictReader(path.open(encoding='utf-8'), delimiter='\t'))


def main() -> int:
    errors: list[str] = []
    summary_rows = read_tsv(SUMMARY)
    candidate_rows = read_tsv(CANDIDATES)
    choice_rows = read_tsv(CHOICE_NOTE)
    by_option = {row['scope_option']: row for row in summary_rows}
    choice_by_option = {row['scope_option']: row for row in choice_rows}

    if set(by_option) != EXPECTED_OPTIONS:
        errors.append('scope_option_set_mismatch')
    if set(choice_by_option) != EXPECTED_OPTIONS:
        errors.append('choice_option_set_mismatch')

    candidate_folder_count = len(candidate_rows)
    candidate_page_total = sum(int(row['page_count']) for row in candidate_rows)
    candidate_unit_total = sum(int(row['materialized_effect_units']) for row in candidate_rows)

    all_13 = by_option.get('all_13')
    if all_13:
        if int(all_13['folder_count']) != candidate_folder_count:
            errors.append('all_13_folder_count_mismatch')
        if int(all_13['page_count']) != candidate_page_total:
            errors.append('all_13_page_count_mismatch')
        if int(all_13['materialized_effect_units']) != candidate_unit_total:
            errors.append('all_13_unit_count_mismatch')

    expected_numbers = {
        'all_13': ('13', '78', '429', '5', '8'),
        'candidate_05_09_only': ('5', '30', '165', '5', '0'),
        'candidate_10_17_only': ('8', '48', '264', '0', '8'),
    }
    number_keys = ['folder_count', 'page_count', 'materialized_effect_units', 'candidate_05_09_folders', 'candidate_10_17_folders']
    shared_keys = ['folder_count', 'page_count', 'materialized_effect_units']
    for option, values in expected_numbers.items():
        row = by_option.get(option)
        choice_row = choice_by_option.get(option)
        if not row:
            continue
        for key, expected in zip(number_keys, values):
            if row[key] != expected:
                errors.append(f'bad_{key}:{option}:{row[key]} expected={expected}')
        if row['pre_boundary_change'] != 'false':
            errors.append(f'bad_pre_boundary_change:{option}:{row["pre_boundary_change"]}')
        if choice_row:
            for key in shared_keys:
                if choice_row[key] != row[key]:
                    errors.append(f'choice_mismatch_{key}:{option}')
            for key, expected in zip(['coverage_level', 'review_load', 'choice_state'], EXPECTED_CHOICE[option]):
                if choice_row[key] != expected:
                    errors.append(f'bad_choice_{key}:{option}:{choice_row[key]} expected={expected}')
            if choice_row['change_now'] != 'false':
                errors.append(f'bad_choice_change_now:{option}:{choice_row["change_now"]}')
    if by_option.get('candidate_10_17_only', {}).get('decision_state') != 'blocked_until_boundary':
        errors.append('candidate_10_17_only_state_mismatch')

    print('check_set=pr35_candidate_scope_summary_v2')
    print(f'scope_options={len(summary_rows)}')
    print(f'choice_options={len(choice_rows)}')
    if errors:
        for error in errors:
            print(error)
        print('pr35_candidate_scope_summary_pass=false')
        return 1
    print('pr35_candidate_scope_summary_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
