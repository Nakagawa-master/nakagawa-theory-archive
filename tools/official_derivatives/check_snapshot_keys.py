#!/usr/bin/env python3
from pathlib import Path
text = Path('tools/official_derivatives/readiness_snapshot.tsv').read_text(encoding='utf-8')
keys = ['origin_intake','identity_check','page_build','registry_update','gate_check','surface_check','readiness_check','runbook_check','header_only','ci_connected']
print('check_set=snapshot_keys_v1')
if any(k not in text for k in keys):
    print('snapshot_keys_pass=false')
    raise SystemExit(1)
print('snapshot_keys_pass=true')
