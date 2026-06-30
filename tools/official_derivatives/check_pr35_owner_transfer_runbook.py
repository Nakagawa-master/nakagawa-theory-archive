#!/usr/bin/env python3
from pathlib import Path

text = Path('tools/official_derivatives/pr35_owner_transfer_runbook.md').read_text(encoding='utf-8')
keys = ['folders: 13','pages: 78','source path root','target path root','pr35_transfer_manifest.tsv','Do not add folders','Do not remove existing production files','No sitemap','No Search Console','noindex/nofollow']
missing = [key for key in keys if key not in text]
print('check_set=pr35_owner_transfer_runbook_v1')
if missing:
    print('\n'.join('missing=' + key for key in missing))
    print('pr35_owner_transfer_runbook_pass=false')
    raise SystemExit(1)
print('pr35_owner_transfer_runbook_pass=true')
