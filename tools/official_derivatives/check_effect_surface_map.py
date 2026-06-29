#!/usr/bin/env python3
import csv
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAP = HERE / 'official_derivative_effect_surface.tsv'
REGISTRY = HERE / 'derivative_registry_candidate_05_09.tsv'
REQUIRED = {'hub','human_summary','faq','ja_ai_index','en_ai_index','zh_ai_index'}


def read(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def main():
    surface_rows = read(MAP)
    registry_rows = read(REGISTRY)
    errors = []
    surface = {(r['page_role'], r['language']): r for r in surface_rows}
    if {r['page_role'] for r in surface_rows} != REQUIRED:
        errors.append('surface_roles_mismatch')
    for row in surface_rows:
        label = row.get('page_role','')
        for key in ['surface_layer','primary_audience','effect_goal']:
            if not row.get(key,'').strip():
                errors.append('missing_surface_' + key + '=' + label)
        if row.get('origin_preservation_required') != 'yes':
            errors.append('origin_not_required=' + label)
    roles_by_folder = defaultdict(set)
    for row in registry_rows:
        role = row.get('page_role','')
        language = row.get('language','')
        folder = row.get('folder_id','')
        roles_by_folder[folder].add(role)
        if (role, language) not in surface:
            errors.append('registry_role_without_surface=' + folder + ':' + role + ':' + language)
    for folder, roles in roles_by_folder.items():
        if roles != REQUIRED:
            errors.append('folder_surface_role_mismatch=' + folder)
    print('check_set=effect_surface_map_v1')
    print('surface_rows=' + str(len(surface_rows)))
    print('registry_folders=' + str(len(roles_by_folder)))
    if errors:
        print('\n'.join(errors[:60]))
        print('effect_surface_map_pass=false')
        return 1
    print('effect_surface_map_pass=true')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
