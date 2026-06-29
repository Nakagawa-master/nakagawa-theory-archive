#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

text = Path('tools/official_derivatives/official_derivative_effect_readiness_report.md').read_text(encoding='utf-8')
required = ['current_readiness_percent: 40','estimated_operational_multiplier_range: 300-700','target_operational_multiplier: 10000','candidate_05_09_registry_rows: 30','effect_surface_rows: 6','production_deploy: false','sitemap_update: false','search_console_action: false']
missing = [x for x in required if x not in text]
print('check_set=effect_readiness_v2')
if missing:
    print('\n'.join('missing=' + x for x in missing))
    print('effect_readiness_pass=false')
    raise SystemExit(1)
activation = Path('tools/official_derivatives/check_activation.py')
if activation.exists():
    result = subprocess.run([sys.executable, str(activation)])
    if result.returncode != 0:
        print('effect_readiness_pass=false')
        raise SystemExit(result.returncode)
print('effect_readiness_pass=true')
