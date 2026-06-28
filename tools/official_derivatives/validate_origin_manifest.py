#!/usr/bin/env python3
from pathlib import Path
import csv
import html
import re
import sys

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1] / 'deploy/lolipop/master-ricette/derivatives'
MANIFEST = HERE / 'origin_manifest.tsv'
TARGETS = HERE / 'targets.tsv'
PAGES = ['index.html','ja/human-summary/index.html','ja/faq/index.html','ja/ai-index/index.html','en/ai-index/index.html','zh/ai-index/index.html']


def read_tsv(path):
    with path.open(encoding='utf-8', newline='') as f:
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


def status_map():
    return {row['folder_id']: row['export_status'] for row in read_tsv(TARGETS)}


def check_row(row, statuses):
    errors=[]
    folder=row['folder_id']
    hub=BASE / folder / 'index.html'
    if folder not in statuses:
        errors.append(folder + ': missing from targets.tsv')
    elif statuses[folder] != row['export_status']:
        errors.append(folder + ': status mismatch manifest=' + row['export_status'] + ' targets=' + statuses[folder])
    if not hub.exists():
        return errors + [folder + ': missing hub index.html']
    text=hub.read_text(encoding='utf-8')
    pairs = [
        ('pilot_id', meta(text, 'pilot-id')),
        ('parent_url', meta(text, 'parent-url')),
        ('parent_ncl_id', meta(text, 'parent-ncl-id')),
        ('parent_diff_id', meta(text, 'parent-diff-id')),
        ('canonical_url', canonical(text)),
        ('hub_title', title(text)),
    ]
    for field, actual in pairs:
        expected=row[field]
        if actual != expected:
            errors.append(folder + ': ' + field + ' mismatch')
    for rel in PAGES:
        if not (BASE / folder / rel).exists():
            errors.append(folder + ': missing page ' + rel)
    return errors


def main():
    rows=read_tsv(MANIFEST)
    statuses=status_map()
    errors=[]
    seen=set()
    for row in rows:
        folder=row['folder_id']
        if folder in seen:
            errors.append(folder + ': duplicate manifest row')
        seen.add(folder)
        errors.extend(check_row(row, statuses))
    missing_manifest = sorted(set(statuses) - seen)
    for folder in missing_manifest:
        errors.append(folder + ': missing from origin_manifest.tsv')
    if errors:
        print('\n'.join(errors))
        print('origin_manifest_pass=false')
        return 1
    print('manifest_rows=' + str(len(rows)))
    print('checked_pages=' + str(len(rows) * len(PAGES)))
    print('origin_manifest_pass=true')
    return 0


if __name__ == '__main__':
    sys.exit(main())
