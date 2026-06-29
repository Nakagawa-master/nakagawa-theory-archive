#!/usr/bin/env python3
from pathlib import Path

text = Path('tools/official_derivatives/activation_readiness_gate.md').read_text(encoding='utf-8')
keys = ['pre_activation_draft','activation_requires_owner_boundary','no_production_deploy_without_owner','no_sitemap_update_without_owner','no_search_console_action_without_owner','quality_gate_required']
missing = [k for k in keys if k not in text]
print('check_set=activation_v1')
if missing:
    print('activation_pass=false')
    raise SystemExit(1)
print('activation_pass=true')
