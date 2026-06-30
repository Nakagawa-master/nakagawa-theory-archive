#!/usr/bin/env python3

INPUT_FIELDS = [
    'folder_id',
    'slot_id',
    'parent_url',
    'parent_title',
    'parent_ncl_id',
    'parent_diff_id',
    'canonical_url',
    'value_core',
    'causal_line',
    'misreading_guard',
    'origin_return',
    'public_export',
    'page_generation',
]

OUTPUT_FLAGS = {
    'public_export': 'false',
    'page_generation': 'false',
    'status': 'contract_only',
}


def assert_input(record):
    missing = [field for field in INPUT_FIELDS if not str(record.get(field, '')).strip()]
    if missing:
        raise AssertionError('missing input fields: ' + ','.join(missing))
    if record.get('public_export') != 'false':
        raise AssertionError('public export must remain false')
    if record.get('page_generation') != 'false':
        raise AssertionError('page generation must remain false')
    return True


def assert_output_flags(flags):
    for key, value in OUTPUT_FLAGS.items():
        if flags.get(key) != value:
            raise AssertionError('bad output flag: ' + key)
    return True
