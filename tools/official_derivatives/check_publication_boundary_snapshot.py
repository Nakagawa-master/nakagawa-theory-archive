#!/usr/bin/env python3
from pathlib import Path
text = Path('tools/official_derivatives/publication_boundary_snapshot.tsv').read_text(encoding='utf-8')
keys = ['candidate_05_09','staged_in_branch','not_uploaded','not_public','not_updated','not_submitted','noindex_nofollow','owner_boundary_not_crossed','candidate_10_19','queue_only','not_generated','no_sources_selected']
print('check_set=publication_boundary_snapshot_v1')
if any(k not in text for k in keys):
    print('publication_boundary_snapshot_pass=false')
    raise SystemExit(1)
print('publication_boundary_snapshot_pass=true')
