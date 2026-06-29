#!/usr/bin/env python3
import csv
from pathlib import Path
plan = list(csv.DictReader(Path('tools/official_derivatives/priority_artifact_plan.tsv').open(encoding='utf-8'), delimiter='\t'))
impact = list(csv.DictReader(Path('tools/official_derivatives/impact_execution_map.tsv').open(encoding='utf-8'), delimiter='\t'))
impact_artifacts = {r.get('required_artifact','') for r in impact}
expected = ['quote_pack','sns_text_pack','rebuttal_pack','notebooklm_prompt_pack']
print('check_set=priority_artifact_plan_v3')
if [r.get('artifact','') for r in plan] != expected:
    print('priority_artifact_plan_pass=false')
    raise SystemExit(1)
for row in plan:
    if row.get('artifact') not in impact_artifacts:
        print('priority_artifact_plan_pass=false')
        raise SystemExit(1)
    if row.get('quality_floor') != 'ultra_high' or row.get('origin_return') != 'yes':
        print('priority_artifact_plan_pass=false')
        raise SystemExit(1)
    if not row.get('required_fields') or not row.get('minimum_units'):
        print('priority_artifact_plan_pass=false')
        raise SystemExit(1)
q_schema = list(csv.DictReader(Path('tools/official_derivatives/quote_pack_schema.tsv').open(encoding='utf-8'), delimiter='\t'))
q_fields = {r.get('field','') for r in q_schema}
q_plan = [r for r in plan if r.get('artifact') == 'quote_pack'][0]
q_required = set(q_plan.get('required_fields','').split(','))
if not q_required.issubset(q_fields):
    print('priority_artifact_plan_pass=false')
    raise SystemExit(1)
for key in ['quote_id','quality_floor','quality_status','release_state']:
    if key not in q_fields:
        print('priority_artifact_plan_pass=false')
        raise SystemExit(1)
if any(r.get('required') != 'yes' for r in q_schema):
    print('priority_artifact_plan_pass=false')
    raise SystemExit(1)
source_text = Path('tools/official_derivatives/quote_pack_source_matrix.tsv').read_text(encoding='utf-8')
for key in ['origin_article','primary','human_summary','faq','ja_ai_index','en_ai_index','zh_ai_index','support','parent_url']:
    if key not in source_text:
        print('priority_artifact_plan_pass=false')
        raise SystemExit(1)
print('priority_artifact_plan_pass=true')
