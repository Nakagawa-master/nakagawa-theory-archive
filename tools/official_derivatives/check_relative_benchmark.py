#!/usr/bin/env python3
from pathlib import Path

text = Path('tools/official_derivatives/relative_strength_benchmark.md').read_text(encoding='utf-8')
keys = ['20_to_50','5_to_20','10_to_30','2_to_10','1_to_3','500_to_2000','100_to_500','300_to_1000','10_to_100','not an empirical public-impact claim']
missing = [k for k in keys if k not in text]
print('check_set=relative_benchmark_v1')
if missing:
    print('relative_benchmark_pass=false')
    raise SystemExit(1)
print('relative_benchmark_pass=true')
