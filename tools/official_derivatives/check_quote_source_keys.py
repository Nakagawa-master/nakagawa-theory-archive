#!/usr/bin/env python3
from pathlib import Path
text = Path('tools/official_derivatives/quote_pack_source_matrix.tsv').read_text(encoding='utf-8')
keys = ['origin_article','primary','human_summary','faq','ja_ai_index','en_ai_index','zh_ai_index','support','memory_only','unlinked_text','low_basis_text','parent_url']
print('check_set=quote_source_keys_v1')
if any(k not in text for k in keys):
    print('quote_source_keys_pass=false')
    raise SystemExit(1)
print('quote_source_keys_pass=true')
