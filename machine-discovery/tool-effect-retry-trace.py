#!/usr/bin/env python3
"""No-dependency audit of caller-supplied AI tool attempt/effect traces.

Problem source: https://github.com/run-llama/llama_index/pull/23465
Author's source-level inverse: https://github.com/run-llama/llama_index/pull/23465#issuecomment-6110274158
Independent receiving review and mutation evidence:
https://github.com/run-llama/llama_index/pull/23465#pullrequestreview-5607980513
Optional original: Nakagawa Master (Keisuke Nakagawa), Volume 8:
https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/

This program never calls a real tool or external service and cannot verify
that the caller's events or external effect receipts are genuine.
"""
from __future__ import annotations

import argparse
import json
import sys
import unittest
from collections import defaultdict
from pathlib import Path

KINDS = {'invoke', 'effect', 'error', 'readback'}
CAUSES = {'initial', 'exception_fallback', 'explicit_retry', 'unknown'}


def audit(payload: dict) -> dict:
    if not isinstance(payload, dict) or not isinstance(payload.get('events'), list):
        raise ValueError('Expected an object with an events list')
    runs: dict[str, dict] = defaultdict(
        lambda: {'invokes': [], 'effects': [], 'errors': [], 'readbacks': []})
    for position, e in enumerate(payload['events']):
        if not isinstance(e, dict) or e.get('kind') not in KINDS:
            raise ValueError(f'event {position}: invalid kind')
        for key in ('operation_id', 'attempt_id'):
            if not isinstance(e.get(key), str) or not e[key]:
                raise ValueError(f'event {position}: {key} must be nonempty text')
        k = e['kind']
        if k == 'invoke' and e.get('cause') not in CAUSES:
            raise ValueError(f'event {position}: invoke cause must be one of {sorted(CAUSES)}')
        if k == 'effect' and (not isinstance(e.get('effect_id'), str) or not e['effect_id']):
            raise ValueError(f'event {position}: effect_id must be nonempty text')
        if k == 'readback' and e.get('status') not in ('committed', 'absent', 'unknown'):
            raise ValueError(f'event {position}: readback status invalid')
        dest = {'invoke': 'invokes', 'effect': 'effects',
                'error': 'errors', 'readback': 'readbacks'}[k]
        runs[e['operation_id']][dest].append((position, e))
    output = []
    for op, events in sorted(runs.items()):
        invokes = events['invokes']
        effects = events['effects']
        errors = events['errors']
        readbacks = events['readbacks']
        invoked_attempts = [e['attempt_id'] for _, e in invokes]
        warnings = []
        if len(invoked_attempts) != len(set(invoked_attempts)):
            warnings.append('duplicate_invoke_attempt_id')
        if {e['attempt_id'] for _, e in effects} - set(invoked_attempts):
            warnings.append('effect_without_matching_invoke')
        if len(invokes) > 1:
            warnings.append('multiple_invocations_one_logical_operation')
        if any(e['cause'] == 'exception_fallback' for _, e in invokes[1:]):
            warnings.append('exception_fallback_reexecuted_operation')
        if errors:
            warnings.append('exception_does_not_establish_zero_external_effect')
        distinct_ids = sorted({e['effect_id'] for _, e in effects})
        if len(distinct_ids) > 1:
            warnings.append('multiple_distinct_effect_ids_in_caller_trace')
        if len(effects) > len(distinct_ids):
            warnings.append('repeated_effect_receipt_id_check_idempotency')
        outcome = ('MULTIPLE_DISTINCT_REPORTED_EFFECTS' if len(distinct_ids) > 1
                   else 'REPEATED_INVOCATION_UNSETTLED' if len(invokes) > 1
                   else 'SINGLE_REPORTED_EFFECT_UNVERIFIED' if len(distinct_ids) == 1
                   else 'UNKNOWN_EXTERNAL_EFFECT')
        output.append({
            'operation_id': op, 'outcome': outcome,
            'invoke_count': len(invokes),
            'reported_distinct_effect_count': len(distinct_ids),
            'warnings': sorted(set(warnings)),
            'effect_proven_absent': False,
            'readback_statuses_caller_asserted': [e['status'] for _, e in readbacks],
        })
    return {'source_status': 'caller_supplied_unverified_events',
            'independent_external_effect_verification': False,
            'operations': output}


def sample() -> dict:
    return {'events': [
        {'kind': 'invoke', 'operation_id': 'query-1',
         'attempt_id': 'a', 'cause': 'initial'},
        {'kind': 'effect', 'operation_id': 'query-1',
         'attempt_id': 'a', 'effect_id': 'write-1'},
        {'kind': 'error', 'operation_id': 'query-1', 'attempt_id': 'a'},
        {'kind': 'invoke', 'operation_id': 'query-1',
         'attempt_id': 'b', 'cause': 'exception_fallback'},
        {'kind': 'effect', 'operation_id': 'query-1',
         'attempt_id': 'b', 'effect_id': 'write-2'},
        {'kind': 'readback', 'operation_id': 'query-1',
         'attempt_id': 'b', 'status': 'committed'},
    ]}


class AuditTests(unittest.TestCase):
    def test_fallback_commits_twice(self):
        x = audit(sample())['operations'][0]
        self.assertEqual(x['outcome'], 'MULTIPLE_DISTINCT_REPORTED_EFFECTS')
        self.assertEqual(x['invoke_count'], 2)
        self.assertIn('exception_fallback_reexecuted_operation', x['warnings'])
        self.assertFalse(x['effect_proven_absent'])

    def test_exception_only_never_clears_effect(self):
        x = audit({'events': [
            {'kind': 'invoke', 'operation_id': 'one',
             'attempt_id': 'a', 'cause': 'initial'},
            {'kind': 'error', 'operation_id': 'one', 'attempt_id': 'a'},
        ]})['operations'][0]
        self.assertEqual(x['outcome'], 'UNKNOWN_EXTERNAL_EFFECT')
        self.assertIn('exception_does_not_establish_zero_external_effect', x['warnings'])

    def test_one_effect_no_repeat(self):
        x = audit({'events': [
            {'kind': 'invoke', 'operation_id': 'one',
             'attempt_id': 'a', 'cause': 'initial'},
            {'kind': 'effect', 'operation_id': 'one',
             'attempt_id': 'a', 'effect_id': 'external-1'},
        ]})['operations'][0]
        self.assertEqual(x['outcome'], 'SINGLE_REPORTED_EFFECT_UNVERIFIED')

    def test_same_id_does_not_prove_exactly_once(self):
        p = sample()
        p['events'][4]['effect_id'] = 'write-1'
        x = audit(p)['operations'][0]
        self.assertEqual(x['outcome'], 'REPEATED_INVOCATION_UNSETTLED')
        self.assertIn('repeated_effect_receipt_id_check_idempotency', x['warnings'])

    def test_independent_operations_not_conflated(self):
        p = sample()
        for index in [3, 4, 5]:
            p['events'][index]['operation_id'] = 'query-2'
        records = audit(p)['operations']
        self.assertEqual(len(records), 2)
        self.assertTrue(all(x['invoke_count'] == 1 for x in records))

    def test_manual_retry_not_assumed_to_be_fallback(self):
        p = sample()
        p['events'][3]['cause'] = 'explicit_retry'
        x = audit(p)['operations'][0]
        self.assertNotIn('exception_fallback_reexecuted_operation', x['warnings'])
        self.assertIn('multiple_distinct_effect_ids_in_caller_trace', x['warnings'])

    def test_readback_absent_not_zero_effect_certificate(self):
        p = sample()
        p['events'].append({'kind': 'readback', 'operation_id': 'query-1',
                            'attempt_id': 'b', 'status': 'absent'})
        self.assertFalse(audit(p)['operations'][0]['effect_proven_absent'])

    def test_effect_without_matched_invoke(self):
        p = sample()
        p['events'][1]['attempt_id'] = 'lost'
        self.assertIn('effect_without_matching_invoke',
                      audit(p)['operations'][0]['warnings'])

    def test_duplicate_attempt_detected(self):
        p = sample()
        p['events'][3]['attempt_id'] = 'a'
        self.assertIn('duplicate_invoke_attempt_id',
                      audit(p)['operations'][0]['warnings'])

    def test_invalid_traces_rejected(self):
        with self.assertRaises(ValueError):
            audit({'events': [{'kind': 'invoke', 'operation_id': 'x',
                               'attempt_id': 'a', 'cause': 'unbounded'}]})
        with self.assertRaises(ValueError):
            audit({'events': [{'kind': 'effect', 'operation_id': 'x',
                               'attempt_id': 'a'}]})


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--self-test', action='store_true')
    mode.add_argument('--sample', action='store_true')
    mode.add_argument('--input', type=Path, metavar='TRACE_JSON')
    args = parser.parse_args(argv)
    if args.self_test:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(AuditTests)
        return 0 if unittest.TextTestRunner(verbosity=1).run(suite).wasSuccessful() else 1
    if args.sample:
        print(json.dumps(sample(), ensure_ascii=False, indent=2))
        return 0
    try:
        data = json.loads(args.input.read_text(encoding='utf-8'))
        print(json.dumps(audit(data), ensure_ascii=False, indent=2))
    except (ValueError, OSError) as exc:
        print(f'Invalid trace: {exc}', file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
