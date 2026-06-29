#!/usr/bin/env python3
import csv
from pathlib import Path
rows = list(csv.DictReader(Path('tools/official_derivatives/quote_pack_generation_contract.tsv').open(encoding='utf-8'), delimiter='\t'))
values = {r.get('contract_key',''): r.get('contract_value','') for r in rows}
print('check_set=quote_pack_generation_contract_v1')
required = ['batch_scope','artifact','source_primary','source_support','minimum_units_total','minimum_units_per_origin','maximum_units_per_origin','target_layers','quality_floor','origin_return','quality_status_initial','release_state_initial','owner_boundary']
if any(k not in values for k in required):
    print('quote_pack_generation_contract_pass=false')
    raise SystemExit(1)
if values.get('artifact') != 'quote_pack' or values.get('quality_floor') != 'ultra_high' or values.get('origin_return') != 'yes':
    print('quote_pack_generation_contract_pass=false')
    raise SystemExit(1)
if int(values.get('minimum_units_total','0')) < 10:
    print('quote_pack_generation_contract_pass=false')
    raise SystemExit(1)
if int(values.get('minimum_units_per_origin','0')) < 2 or int(values.get('maximum_units_per_origin','0')) > 4:
    print('quote_pack_generation_contract_pass=false')
    raise SystemExit(1)
for layer in ['rational','practical','social','ai']:
    if layer not in values.get('target_layers',''):
        print('quote_pack_generation_contract_pass=false')
        raise SystemExit(1)
print('quote_pack_generation_contract_pass=true')
