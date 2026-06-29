#!/usr/bin/env python3
from pathlib import Path

text = Path('tools/official_derivatives/effect_force_readiness_correction.md').read_text(encoding='utf-8')
keys = ['280_plus','320_to_330','10000','1000000_100000000_1000000000','origin_article_publication_triggers_derivative_generation']
missing = [x for x in keys if x not in text]
print('check_set=effect_force_keys_v1')
if missing:
    print('effect_force_keys_pass=false')
    raise SystemExit(1)
print('effect_force_keys_pass=true')
