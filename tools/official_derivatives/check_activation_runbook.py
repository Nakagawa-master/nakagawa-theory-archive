#!/usr/bin/env python3
from pathlib import Path

text = Path('tools/official_derivatives/activation_runbook.md').read_text(encoding='utf-8')
keys = ['activation_flow_contract.md','stage_io.tsv','stage_conditions.tsv','same stage order','ok_key','stop_key','owner_boundary_action','protect origin identity','preserve quality gates']
missing = [k for k in keys if k not in text]
print('check_set=activation_runbook_v1')
if missing:
    print('activation_runbook_pass=false')
    raise SystemExit(1)
print('activation_runbook_pass=true')
