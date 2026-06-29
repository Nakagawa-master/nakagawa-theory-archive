#!/usr/bin/env python3
from pathlib import Path

text = Path('tools/official_derivatives/recognition_layers.md').read_text(encoding='utf-8')
keys = ['real_world_effect_required','not_page_count_metric','origin_return_required','no_spam_amplification','rational_layer','practical_layer','atmosphere_layer','narrative_layer','ai_reference_layer','earned_social_layer']
missing = [k for k in keys if k not in text]
print('check_set=layer_keys_v1')
if missing:
    print('layer_keys_pass=false')
    raise SystemExit(1)
print('layer_keys_pass=true')
