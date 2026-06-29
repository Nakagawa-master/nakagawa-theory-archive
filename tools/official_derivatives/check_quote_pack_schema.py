#!/usr/bin/env python3
import csv
from pathlib import Path
schema = list(csv.DictReader(Path('tools/official_derivatives/quote_pack_schema.tsv').open(encoding='utf-8'), delimiter='\t'))
plan = list(csv.DictReader(Path('tools/official_derivatives/priority_artifact_plan.tsv').open(encoding='utf-8'), delimiter='\t'))
fields = [r.get('field','') for r in schema]
quote_plan = [r for r in plan if r.get('artifact') == 'quote_pack']
print('check_set=quote_pack_schema_v1')
if len(quote_plan) != 1:
    print('quote_pack_schema_pass=false')
    raise SystemExit(1)
required = set(quote_plan[0].get('required_fields','').split(','))
if not required.issubset(set(fields)):
    print('quote_pack_schema_pass=false')
    raise SystemExit(1)
for key in ['quote_id','quality_floor','quality_status','release_state']:
    if key not in fields:
        print('quote_pack_schema_pass=false')
        raise SystemExit(1)
required_rows = [r for r in schema if r.get('required') == 'yes']
if len(required_rows) != len(schema):
    print('quote_pack_schema_pass=false')
    raise SystemExit(1)
print('quote_pack_schema_pass=true')
