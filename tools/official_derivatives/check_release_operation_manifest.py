#!/usr/bin/env python3
import csv
from pathlib import Path

PATH = Path('tools/official_derivatives/release_operation_manifest_pr35.tsv')
REQUIRED = {
    'manifest_version': 'v0.1',
    'source_pr': '35',
    'operation_state': 'draft_only',
    'owner_boundary_required': 'true',
    'production_deploy': 'false',
    'ftp_action': 'false',
    'sitemap_update': 'false',
    'search_console_action': 'false',
    'index_follow_conversion': 'false',
    'public_activation': 'false',
    'staged_origins': '13',
    'staged_pages': '78',
    'staged_registry_rows': '78',
    'materialized_effect_units': '429',
    'required_preflight': 'public_export_preflight',
    'required_entry_check': 'entry_signal_check',
    'required_boundary_check': 'candidate_boundary_doc_check',
}

def main() -> int:
    if not PATH.exists():
        print('release_operation_manifest_exists=false')
        return 1
    rows = list(csv.DictReader(PATH.open(encoding='utf-8'), delimiter='\t'))
    data = {row['field']: row['value'] for row in rows}
    missing = []
    for key, expected in REQUIRED.items():
        actual = data.get(key)
        if actual != expected:
            missing.append(f'{key}:expected={expected}:actual={actual}')
    print('check_set=release_operation_manifest_v1')
    if missing:
        for item in missing:
            print(f'manifest_mismatch={item}')
        print('release_operation_manifest_pass=false')
        return 1
    print('release_operation_manifest_pass=true')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
