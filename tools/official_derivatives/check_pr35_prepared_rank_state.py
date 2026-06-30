#!/usr/bin/env python3
import csv
from pathlib import Path

BASE = Path('tools/official_derivatives')
PATH = BASE / 'pr35_prepared_rank_state.tsv'
EXPECTED = {
    'all_13': ('1', '13', '78', '429', 'prepared'),
    'candidate_05_09_only': ('2', '5', '30', '165', 'fallback'),
    'candidate_10_17_only': ('3', '8', '48', '264', 'later'),
}


def main() -> int:
    rows = list(csv.DictReader(PATH.open(encoding='utf-8'), delimiter='\t'))
    errors: list[str] = []
    by_key = {row['option_key']: row for row in rows}
    if set(by_key) != set(EXPECTED):
        errors.append('option_set_mismatch')
    for key, expected in EXPECTED.items():
        row = by_key.get(key)
        if not row:
            continue
        for field, value in zip(['rank', 'folder_count', 'page_count', 'materialized_effect_units', 'state'], expected):
            if row[field] != value:
                errors.append(f'bad_{field}:{key}:{row[field]} expected={value}')
        if row['source_pr'] != '35':
            errors.append(f'bad_source_pr:{key}:{row["source_pr"]}')
        if row['change_now'] != 'false':
            errors.append(f'bad_change_now:{key}:{row["change_now"]}')

    print('check_set=pr35_prepared_rank_state_v1')
    print(f'rows={len(rows)}')
    if errors:
        for error in errors:
            print(error)
        print('pr35_prepared_rank_state_pass=false')
        return 1
    print('pr35_prepared_rank_state_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
