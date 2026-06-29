#!/usr/bin/env python3
from pathlib import Path
text = Path('tools/official_derivatives/activation_flow_contract.md').read_text(encoding='utf-8')
keys = ['origin_intake','origin_identity_check','derivative_generation','quality_gate_check','activation_ready_check','owner_boundary_action','no_quality_gate_skip','no_publication_before_ready']
missing = [k for k in keys if k not in text]
print('check_set=flow_v1')
if missing:
    print('flow_pass=false')
    raise SystemExit(1)
print('flow_pass=true')
