#!/usr/bin/env python3
import csv
from pathlib import Path

PATH = Path('tools/official_derivatives/activation_diff_plan_pr35.tsv')
EXPECTED_AREAS = {
    'robots_directives',
    'sitemap_entries',
    'search_console_submission',
    'index_follow_state',
    'ftp_or_deploy_method',
    'public_activation_flag',
    'canonical_url_publication',
    'candidate_folder_scope',
}


def main() -> int:
    errors: list[str] = []
    rows = list(csv.DictReader(PATH.open(encoding='utf-8'), delimiter='\t'))
    areas = {row['change_area'] for row in rows}
    if areas != EXPECTED_AREAS:
        errors.append('change_area_set_mismatch')
    for row in rows:
        if row['source_pr'] != '35':
            errors.append(f"bad_source_pr:{row['change_area']}:{row['source_pr']}")
        if row['allowed_now'] != 'false':
            errors.append(f"bad_allowed_now:{row['change_area']}:{row['allowed_now']}")
        if row['owner_boundary_required'] != 'true':
            errors.append(f"bad_boundary:{row['change_area']}:{row['owner_boundary_required']}")
        if row['required_current_state'] not in {'no_change', 'listed_only'}:
            errors.append(f"bad_required_state:{row['change_area']}:{row['required_current_state']}")
    print('check_set=activation_diff_plan_v1')
    print(f'change_areas={len(areas)}')
    if errors:
        for error in errors:
            print(error)
        print('activation_diff_plan_pass=false')
        return 1
    print('activation_diff_plan_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
