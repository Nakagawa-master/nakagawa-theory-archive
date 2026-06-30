#!/usr/bin/env python3
import csv
from pathlib import Path

BASE = Path('tools/official_derivatives')
REGISTRY = BASE / 'staged_official_derivative_registry.tsv'
LIST = BASE / 'candidate_activation_list_pr35.tsv'

EXPECTED_ROWS = 13
EXPECTED_PAGES = 78
EXPECTED_UNITS = 429


def read_tsv(path: Path) -> list[dict[str, str]]:
    return list(csv.DictReader(path.open(encoding='utf-8'), delimiter='\t'))


def main() -> int:
    errors: list[str] = []
    registry_rows = read_tsv(REGISTRY)
    list_rows = read_tsv(LIST)

    registry_folders = sorted({row['folder_id'] for row in registry_rows})
    list_folders = sorted({row['folder_id'] for row in list_rows})

    if len(list_rows) != EXPECTED_ROWS:
        errors.append(f'candidate_rows={len(list_rows)} expected={EXPECTED_ROWS}')
    if registry_folders != list_folders:
        errors.append('folder_set_mismatch')
    page_total = sum(int(row['page_count']) for row in list_rows)
    unit_total = sum(int(row['materialized_effect_units']) for row in list_rows)
    if page_total != EXPECTED_PAGES:
        errors.append(f'page_total={page_total} expected={EXPECTED_PAGES}')
    if unit_total != EXPECTED_UNITS:
        errors.append(f'unit_total={unit_total} expected={EXPECTED_UNITS}')
    for row in list_rows:
        if row['operation_state'] != 'draft_only':
            errors.append(f"bad_operation_state:{row['folder_id']}:{row['operation_state']}")
        if row['owner_boundary_required'] != 'true':
            errors.append(f"bad_boundary:{row['folder_id']}:{row['owner_boundary_required']}")
        if row['candidate_status'] != 'pending_boundary':
            errors.append(f"bad_candidate_status:{row['folder_id']}:{row['candidate_status']}")

    print('check_set=candidate_activation_list_v1')
    print(f'candidate_rows={len(list_rows)}')
    print(f'page_total={page_total}')
    print(f'unit_total={unit_total}')
    if errors:
        for error in errors:
            print(error)
        print('candidate_activation_list_pass=false')
        return 1
    print('candidate_activation_list_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
