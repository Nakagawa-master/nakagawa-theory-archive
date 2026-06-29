#!/usr/bin/env python3
import csv
from pathlib import Path

P = Path('tools/official_derivatives/derivative_registry_candidate_05_09.tsv')
ROLES = {'hub','human_summary','faq','ja_ai_index','en_ai_index','zh_ai_index'}
LANG = {'hub':'und','human_summary':'ja','faq':'ja','ja_ai_index':'ja','en_ai_index':'en','zh_ai_index':'zh'}
PATHS = {'hub':'index.html','human_summary':'ja/human-summary/index.html','faq':'ja/faq/index.html','ja_ai_index':'ja/ai-index/index.html','en_ai_index':'en/ai-index/index.html','zh_ai_index':'zh/ai-index/index.html'}


def rows():
    with P.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def main():
    data = rows()
    ids = set()
    roles = {}
    errors = []
    for r in data:
        folder = r.get('folder_id','')
        role = r.get('page_role','')
        expected_id = folder + '--' + role.replace('_','-')
        roles.setdefault(folder,set()).add(role)
        if r.get('derivative_id') in ids:
            errors.append('duplicate_id=' + r.get('derivative_id',''))
        ids.add(r.get('derivative_id',''))
        if role not in ROLES:
            errors.append('bad_role=' + role)
        if r.get('derivative_id') != expected_id:
            errors.append('bad_id=' + folder + ':' + role)
        if r.get('language') != LANG.get(role):
            errors.append('bad_language=' + folder + ':' + role)
        if r.get('relative_path') != PATHS.get(role):
            errors.append('bad_path=' + folder + ':' + role)
        if r.get('origin_author') != 'Nakagawa Master':
            errors.append('bad_origin_author=' + folder + ':' + role)
    for folder, found in roles.items():
        if found != ROLES:
            errors.append('bad_role_set=' + folder)
    print('check_set=derivative_registry_identity_v1')
    print('registry_rows=' + str(len(data)))
    if errors:
        print('\n'.join(errors[:20]))
        print('derivative_registry_identity_pass=false')
        return 1
    print('derivative_registry_identity_pass=true')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
