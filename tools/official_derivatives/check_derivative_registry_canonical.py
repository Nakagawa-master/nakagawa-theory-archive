#!/usr/bin/env python3
import csv
from pathlib import Path

MANIFEST = Path('tools/official_derivatives/origin_manifest.tsv')
REGISTRY = Path('tools/official_derivatives/derivative_registry_candidate_05_09.tsv')
SUFFIX = {
    'hub': '',
    'human_summary': 'ja/human-summary/',
    'faq': 'ja/faq/',
    'ja_ai_index': 'ja/ai-index/',
    'en_ai_index': 'en/ai-index/',
    'zh_ai_index': 'zh/ai-index/',
}


def read(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def main():
    manifest = {r['folder_id']: r for r in read(MANIFEST) if r.get('export_status') == 'staged'}
    errors = []
    rows = read(REGISTRY)
    for r in rows:
        folder = r.get('folder_id','')
        role = r.get('page_role','')
        m = manifest.get(folder)
        if not m:
            errors.append('unknown_folder=' + folder)
            continue
        if role not in SUFFIX:
            errors.append('unknown_role=' + role)
            continue
        base = m['canonical_url'].rstrip('/') + '/'
        expected = base if role == 'hub' else base + SUFFIX[role]
        if r.get('canonical_url') != expected:
            errors.append('canonical_mismatch=' + folder + ':' + role)
        if not r.get('parent_url','').startswith('https://master.ricette.jp/'):
            errors.append('bad_parent_url=' + folder + ':' + role)
        if not r.get('canonical_url','').startswith('https://master.ricette.jp/derivatives/' + folder + '/'):
            errors.append('bad_canonical_prefix=' + folder + ':' + role)
    print('check_set=derivative_registry_canonical_v1')
    print('registry_rows=' + str(len(rows)))
    if errors:
        print('\n'.join(errors[:20]))
        print('derivative_registry_canonical_pass=false')
        return 1
    print('derivative_registry_canonical_pass=true')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
