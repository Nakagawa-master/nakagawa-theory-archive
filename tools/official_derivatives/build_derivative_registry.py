#!/usr/bin/env python3
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / 'origin_manifest.tsv'
OUT = HERE / 'derivative_registry_candidate_05_09.tsv'
PAGES = [
    ('hub','und','index.html'),
    ('human_summary','ja','ja/human-summary/index.html'),
    ('faq','ja','ja/faq/index.html'),
    ('ja_ai_index','ja','ja/ai-index/index.html'),
    ('en_ai_index','en','en/ai-index/index.html'),
    ('zh_ai_index','zh','zh/ai-index/index.html'),
]
FIELDS = ['registry_version','batch_id','origin_slot_id','derivative_id','page_role','language','export_status','parent_url','parent_title','parent_ncl_id','parent_diff_id','folder_id','relative_path','canonical_url','origin_author','source_archive','quality_gate_status','render_status','created_from_manifest','notes']


def slug(role):
    return role.replace('_','-')


def main():
    rows = []
    with MANIFEST.open(encoding='utf-8', newline='') as f:
        for m in csv.DictReader(f, delimiter='\t'):
            if m.get('export_status') != 'staged':
                continue
            folder = m['folder_id']
            title = m.get('hub_title','')
            for role, lang, rel in PAGES:
                canonical = m['canonical_url'] if rel == 'index.html' else m['canonical_url'].rstrip('/') + '/' + rel.rsplit('index.html',1)[0]
                rows.append({
                    'registry_version':'v0.1',
                    'batch_id':'candidate-05-09',
                    'origin_slot_id':m['pilot_id'],
                    'derivative_id':folder + '--' + slug(role),
                    'page_role':role,
                    'language':lang,
                    'export_status':m['export_status'],
                    'parent_url':m['parent_url'],
                    'parent_title':title,
                    'parent_ncl_id':m['parent_ncl_id'],
                    'parent_diff_id':m['parent_diff_id'],
                    'folder_id':folder,
                    'relative_path':rel,
                    'canonical_url':canonical,
                    'origin_author':'Nakagawa Master',
                    'source_archive':'master.ricette.jp',
                    'quality_gate_status':'pending',
                    'render_status':'staged_nonindexable',
                    'created_from_manifest':'true',
                    'notes':'public-safe staged registry row',
                })
    with OUT.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, delimiter='\t')
        w.writeheader()
        w.writerows(rows)
    print('registry_rows=' + str(len(rows)))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
