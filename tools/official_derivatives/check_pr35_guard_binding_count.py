#!/usr/bin/env python3
import csv
from pathlib import Path

PATH = Path('tools/official_derivatives/pr35_guard_check_bindings.tsv')


def main() -> int:
    rows = list(csv.DictReader(PATH.open(encoding='utf-8'), delimiter='\t'))
    errors: list[str] = []
    keys = [row['evidence_key'] for row in rows]
    if len(rows) != 6:
        errors.append(f'row_count={len(rows)} expected=6')
    if len(set(keys)) != len(keys):
        errors.append('duplicate_key')
    for row in rows:
        key = row['evidence_key']
        if row['binding_state'] != 'bound':
            errors.append(f'bad_binding_state:{key}')
        if row['change_now'] != 'false':
            errors.append(f'bad_change_now:{key}')
    print('check_set=pr35_guard_binding_count_v1')
    print(f'rows={len(rows)}')
    if errors:
        for error in errors:
            print(error)
        print('pr35_guard_binding_count_pass=false')
        return 1
    print('pr35_guard_binding_count_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
