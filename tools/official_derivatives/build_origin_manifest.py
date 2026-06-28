#!/usr/bin/env python3
from pathlib import Path
import csv
import html
import re
import sys

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1] / 'deploy/lolipop/master-ricette/derivatives'
TARGETS = HERE / 'targets.tsv'
MANIFEST = HERE / 'origin_manifest.tsv'
FIELDS = ['folder_id','export_status','pilot_id','parent_url','parent_ncl_id','parent_diff_id','canonical_url','hub_title']


def read_targets():
    with TARGETS.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def meta(text, name):
    m = re.search(r'<meta\s+name=["\']' + re.escape(name) + r'["\']\s+content=["\'](.*?)["\']', text, re.S | re.I)
    return html.unescape(m.group(1)) if m else ''


def canonical(text):
    m = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', text, re.S | re.I)
    return html.unescape(m.group(1)) if m else ''


def title(text):
    m = re.search(r'<title>(.*?)</title>', text, re.S | re.I)
    return html.unescape(m.group(1)) if m else ''


def build_rows():
    rows=[]
    for target in read_targets():
        folder=target['folder_id']
        hub=BASE / folder / 'index.html'
        if not hub.exists():
            raise SystemExit('missing hub index.html: ' + folder)
        text=hub.read_text(encoding='utf-8')
        rows.append({
            'folder_id': folder,
            'export_status': target['export_status'],
            'pilot_id': meta(text, 'pilot-id'),
            'parent_url': meta(text, 'parent-url'),
            'parent_ncl_id': meta(text, 'parent-ncl-id'),
            'parent_diff_id': meta(text, 'parent-diff-id'),
            'canonical_url': canonical(text),
            'hub_title': title(text),
        })
    return rows


def write_rows(rows):
    with MANIFEST.open('w', encoding='utf-8', newline='') as f:
        writer=csv.DictWriter(f, fieldnames=FIELDS, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def main():
    rows=build_rows()
    write_rows(rows)
    print('manifest_rows=' + str(len(rows)))
    print('origin_manifest_built=true')
    return 0


if __name__ == '__main__':
    sys.exit(main())
