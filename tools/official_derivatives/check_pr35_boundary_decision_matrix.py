#!/usr/bin/env python3
import csv
from pathlib import Path

PATH = Path('tools/official_derivatives/pr35_boundary_decision_matrix.tsv')
EXPECTED_AREAS = {
    'candidate_folder_scope',
    'staged_page_visibility_state',
    'public_listing_scope',
    'external_service_timing',
    'transfer_method',
    'public_flag_timing',
}
EXPECTED_STATES = {'decision_pending', 'blocked_until_boundary'}


def main() -> int:
    rows = list(csv.DictReader(PATH.open(encoding='utf-8'), delimiter='\t'))
    errors: list[str] = []
    areas = {row['decision_area'] for row in rows}
    if len(rows) != 6:
        errors.append(f'row_count={len(rows)} expected=6')
    if areas != EXPECTED_AREAS:
        errors.append('decision_area_set_mismatch')
    for row in rows:
        area = row['decision_area']
        if row['source_pr'] != '35':
            errors.append(f'bad_source_pr:{area}:{row["source_pr"]}')
        if row['state'] not in EXPECTED_STATES:
            errors.append(f'bad_state:{area}:{row["state"]}')
        if row['pre_boundary_change'] != 'false':
            errors.append(f'bad_pre_boundary_change:{area}:{row["pre_boundary_change"]}')
        if row['pre_boundary_work'] != 'safe_to_prepare':
            errors.append(f'bad_pre_boundary_work:{area}:{row["pre_boundary_work"]}')
        if not row['basis_file'].endswith('.tsv'):
            errors.append(f'bad_basis_file:{area}:{row["basis_file"]}')
    pending = [row for row in rows if row['state'] == 'decision_pending']
    if len(pending) != 1 or pending[0]['decision_area'] != 'candidate_folder_scope':
        errors.append('decision_pending_scope_mismatch')

    print('check_set=pr35_boundary_decision_matrix_v1')
    print(f'decision_rows={len(rows)}')
    if errors:
        for error in errors:
            print(error)
        print('pr35_boundary_decision_matrix_pass=false')
        return 1
    print('pr35_boundary_decision_matrix_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
