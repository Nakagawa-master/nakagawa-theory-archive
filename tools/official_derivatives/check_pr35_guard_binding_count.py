#!/usr/bin/env python3
import csv
from pathlib import Path

BINDINGS = Path('tools/official_derivatives/pr35_guard_check_bindings.tsv')
EVIDENCE = Path('tools/official_derivatives/pr35_guard_evidence_keys.tsv')
FILE_INDEX = Path('tools/official_derivatives/pr35_file_index.tsv')
EXPECTED_KEYS = {
    'candidate_list_check',
    'preflight_check',
    'entry_signal_check',
    'option_brief',
    'scope_summary_check',
    'guard_table_check',
}
ALLOWED_SUFFIXES = {'.py', '.tsv'}
ROOT = 'tools/official_derivatives/'


def read_rows(path: Path) -> list[dict[str, str]]:
    return list(csv.DictReader(path.open(encoding='utf-8'), delimiter='\t'))


def main() -> int:
    rows = read_rows(BINDINGS)
    evidence_rows = read_rows(EVIDENCE)
    index_rows = read_rows(FILE_INDEX)
    errors: list[str] = []
    keys = [row['evidence_key'] for row in rows]
    evidence_keys = {row['evidence_key'] for row in evidence_rows}
    if len(rows) != 6:
        errors.append(f'row_count={len(rows)} expected=6')
    if len(set(keys)) != len(keys):
        errors.append('duplicate_key')
    if set(keys) != EXPECTED_KEYS:
        errors.append('binding_key_set_mismatch')
    if evidence_keys != EXPECTED_KEYS:
        errors.append('evidence_key_set_mismatch')
    if set(keys) != evidence_keys:
        errors.append('binding_evidence_key_mismatch')
    for row in rows:
        key = row['evidence_key']
        check_path = row['check_path']
        path = Path(check_path)
        if row['binding_state'] != 'bound':
            errors.append(f'bad_binding_state:{key}')
        if row['change_now'] != 'false':
            errors.append(f'bad_change_now:{key}')
        if not check_path.startswith(ROOT):
            errors.append(f'bad_path_root:{key}')
        if path.suffix not in ALLOWED_SUFFIXES:
            errors.append(f'bad_path_suffix:{key}')
        if not path.is_file():
            errors.append(f'missing_path:{key}')
    index_keys = [row['item_key'] for row in index_rows]
    if len(index_rows) != 8:
        errors.append(f'index_row_count={len(index_rows)} expected=8')
    if len(set(index_keys)) != len(index_keys):
        errors.append('duplicate_index_key')
    for row in index_rows:
        key = row['item_key']
        file_path = row['file_path']
        path = Path(file_path)
        if row['source_pr'] != '35':
            errors.append(f'bad_index_source_pr:{key}')
        if row['state'] != 'present':
            errors.append(f'bad_index_state:{key}')
        if row['change_now'] != 'false':
            errors.append(f'bad_index_change_now:{key}')
        if not file_path.startswith(ROOT):
            errors.append(f'bad_index_path_root:{key}')
        if path.suffix not in ALLOWED_SUFFIXES:
            errors.append(f'bad_index_path_suffix:{key}')
        if not path.is_file():
            errors.append(f'missing_index_path:{key}')
    print('check_set=pr35_guard_binding_count_v5')
    print(f'rows={len(rows)}')
    print(f'evidence_rows={len(evidence_rows)}')
    print(f'index_rows={len(index_rows)}')
    if errors:
        for error in errors:
            print(error)
        print('pr35_guard_binding_count_pass=false')
        return 1
    print('pr35_guard_binding_count_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
