#!/usr/bin/env python3
from universal_renderer_contract import INPUT_FIELDS, OUTPUT_FLAGS, assert_output_flags

if len(INPUT_FIELDS) < 10:
    raise SystemExit(1)
assert_output_flags(OUTPUT_FLAGS)
print('check_set=universal_renderer_contract_v1')
print('input_fields=' + str(len(INPUT_FIELDS)))
print('universal_renderer_contract_pass=true')
