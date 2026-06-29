#!/usr/bin/env python3
from pathlib import Path

text = Path('tools/official_derivatives/all_origin_effect_scale_model.md').read_text(encoding='utf-8')
keys = ['280_plus','320_to_330','400_500_1000_plus','10000','1000000','100000000','1000000000','no_manual_page_by_page_operation: true','automation_default: near_full_or_full']
missing = [k for k in keys if k not in text]
print('check_set=scale_keys_v1')
if missing:
    print('scale_keys_pass=false')
    raise SystemExit(1)
print('scale_keys_pass=true')
