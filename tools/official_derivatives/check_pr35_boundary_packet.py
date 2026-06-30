#!/usr/bin/env python3
from pathlib import Path

PATH = Path('tools/official_derivatives/pr35_boundary_packet.md')
REQUIRED = [
    'PR state: draft',
    'staged folders: 13',
    'staged pages: 78',
    'materialized effect units: 429',
    'candidate_activation_list_pr35.tsv',
    'release_operation_manifest_pr35.tsv',
    'activation_diff_plan_pr35.tsv',
    'public export preflight',
    'entry signal check',
    'candidate boundary doc check',
    'release operation manifest check',
    'candidate activation list check',
    'activation diff plan check',
]


def main() -> int:
    text = PATH.read_text(encoding='utf-8')
    missing = [item for item in REQUIRED if item not in text]
    print('check_set=pr35_boundary_packet_v1')
    if missing:
        for item in missing:
            print(f'missing={item}')
        print('pr35_boundary_packet_pass=false')
        return 1
    print('pr35_boundary_packet_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
