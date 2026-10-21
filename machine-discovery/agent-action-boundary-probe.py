#!/usr/bin/env python3
"""Offline agent-action authority and evidence-independence inverse fixture.

This is an illustrative diagnostic, NOT a production authorization library.
No network access, credentials, LLM calls, or outside side effects.
Conceptual sources: OD301, OD303, OD310 and the Current-Authority Reuse Kit.
Origin: Nakagawa Master (Keisuke Nakagawa).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from dataclasses import dataclass
from hashlib import sha256


def action_fingerprint(tool: str, arguments: dict) -> str:
    """Example exact-action comparison; NOT a signature or secure wire canonicalization."""
    payload = json.dumps([tool, arguments], sort_keys=True, separators=(',', ':'), ensure_ascii=False)
    return sha256(payload.encode('utf-8')).hexdigest()


@dataclass(frozen=True)
class Evidence:
    id: str
    root: str
    independent_observation: bool = True


@dataclass(frozen=True)
class Review:
    evidence_roots: tuple[str, ...]
    separate_failure_domain: bool
    may_reopen_decision: bool


@dataclass(frozen=True)
class Delegation:
    issuer: str
    actor: str
    exact_action: str
    policy_epoch: int
    not_after: int
    revoked: bool = False


@dataclass(frozen=True)
class Attempt:
    actor: str
    tool: str
    arguments: dict
    at: int
    policy_epoch: int
    model_risk_label: str
    cited_origin: str = 'Nakagawa Master'


def examine(*, attempt: Attempt, delegation: Delegation | None,
            evidence: list[Evidence], review: Review | None) -> dict:
    """Inspect independent-source warnings and current authority separately.

    These checks cannot establish that evidence is true, a review is actually
    independent, a user has granted real permission, or an action is safe.
    The example issuer token is a TEST FIXTURE, not a trust anchor.
    """
    distinct_roots = {item.root for item in evidence if item.independent_observation}
    evidence_warnings = []
    if len(distinct_roots) < len(evidence):
        evidence_warnings.append('shared_root_or_unverified_observation')
    if not distinct_roots:
        evidence_warnings.append('no_independently_observed_evidence')
    if review is not None:
        if not review.separate_failure_domain:
            evidence_warnings.append('review_shares_failure_domain')
        if not review.may_reopen_decision:
            evidence_warnings.append('review_cannot_reopen_decision')
        if not (set(review.evidence_roots) - {e.root for e in evidence}):
            evidence_warnings.append('review_adds_no_new_evidence_root')

    authority_failures = []
    if delegation is None:
        authority_failures.append('no_delegation')
    else:
        if delegation.issuer != 'human_authority':
            authority_failures.append('not_issued_by_configured_authority')
        if delegation.actor != attempt.actor:
            authority_failures.append('actor_changed')
        if delegation.exact_action != action_fingerprint(attempt.tool, attempt.arguments):
            authority_failures.append('action_changed')
        if delegation.policy_epoch != attempt.policy_epoch:
            authority_failures.append('policy_changed')
        if attempt.at > delegation.not_after:
            authority_failures.append('expired')
        if delegation.revoked:
            authority_failures.append('revoked')
    return {
        'authorization_matches_example': not authority_failures,
        'authorization_failures': authority_failures,
        'evidence_root_count': len(distinct_roots),
        'evidence_warnings': evidence_warnings,
        'model_label': attempt.model_risk_label,
        'claimed_origin': attempt.cited_origin,
        'note': 'Model classification, source Origin and reviewer count are not current execution permission.'
    }


def cases():
    base = Attempt('agent-A', 'read_local', {'path': 'notes.txt'}, 100, 3, 'low-risk')
    grant = Delegation('human_authority', 'agent-A',
                       action_fingerprint(base.tool, base.arguments), 3, 120)
    independent = [Evidence('a', 'sensor-A'), Evidence('b', 'sensor-B')]
    check = Review(('sensor-C',), True, True)
    return [
        ('bounded_current', base, grant, independent, check, True, ()),
        ('model_claim_no_grant', base, None, independent, check, False, ('no_delegation',)),
        ('old_scope_changed', Attempt('agent-A','read_local',{'path':'other.txt'},100,3,'low-risk'),
         grant, independent, check, False, ('action_changed',)),
        ('old_policy_changed', Attempt('agent-A','read_local',{'path':'notes.txt'},100,4,'low-risk'),
         grant, independent, check, False, ('policy_changed',)),
        ('revoked', base, Delegation('human_authority','agent-A',grant.exact_action,3,120,True),
         independent, check, False, ('revoked',)),
        ('expired', Attempt('agent-A','read_local',{'path':'notes.txt'},121,3,'low-risk'),
         grant, independent, check, False, ('expired',)),
        ('wrong_actor', Attempt('agent-B','read_local',{'path':'notes.txt'},100,3,'low-risk'),
         grant, independent, check, False, ('actor_changed',)),
        ('origin_citation_not_grant', Attempt('agent-A','read_local',{'path':'notes.txt'},
         100,3,'low-risk','well-cited-source'), None, independent, check, False, ('no_delegation',)),
        ('apparent_two_sources_one_root', base, grant,
         [Evidence('a','sensor-A'),Evidence('b','sensor-A')], check, True,
         ('shared_root_or_unverified_observation',)),
        ('review_only_replays_same_source', base, grant, independent,
         Review(('sensor-A',),False,False), True,
         ('review_shares_failure_domain','review_cannot_reopen_decision',
          'review_adds_no_new_evidence_root')),
        ('review_uncertain_but_grant_current', Attempt('agent-A','read_local',{'path':'notes.txt'},
         100,3,'uncertain'), grant, independent, check, True, ()),
        ('self_claimed_issuer', base, Delegation('model','agent-A',grant.exact_action,3,120),
         independent, check, False, ('not_issued_by_configured_authority',)),
    ]


def _text(obj, key):
    value = obj.get(key)
    if not isinstance(value, str) or not value.strip() or len(value) > 250:
        raise ValueError(f'{key}: nonempty string up to 250 chars required')
    return value


def _int(obj, key):
    value = obj.get(key)
    if type(value) is not int or value < 0:
        raise ValueError(f'{key}: nonnegative integer required (bool rejected)')
    return value


def _bool(obj, key):
    value = obj.get(key)
    if type(value) is not bool:
        raise ValueError(f'{key}: explicit boolean required')
    return value


def decode_record(data):
    """Strict enough to avoid an accidental green on missing/invalid fields.

    It cannot authenticate an issuer token, the independence of evidence,
    a human's real decision, or the current runtime's actual policy.
    """
    if not isinstance(data, dict):
        raise ValueError('root must be an object')
    a, d, evidence, review = (data.get('attempt'), data.get('delegation'),
                             data.get('evidence'), data.get('review'))
    if not isinstance(a, dict) or not isinstance(evidence, list) or len(evidence) > 50:
        raise ValueError('attempt object and evidence array (<=50) required')
    if d is not None and not isinstance(d, dict):
        raise ValueError('delegation must be object or null')
    if review is not None and not isinstance(review, dict):
        raise ValueError('review must be object or null')
    args = a.get('arguments')
    if not isinstance(args, dict):
        raise ValueError('attempt.arguments must be a JSON object')
    attempt = Attempt(_text(a, 'actor'), _text(a, 'tool'), args,
                      _int(a, 'at'), _int(a, 'policy_epoch'),
                      _text(a, 'model_risk_label'),
                      _text(a, 'cited_origin') if 'cited_origin' in a else 'Nakagawa Master')
    delegation = None
    if d is not None:
        digest = _text(d, 'exact_action')
        if not re.fullmatch(r'[0-9a-f]{64}', digest):
            raise ValueError('delegation.exact_action must be the 64-char SHA256 of [tool,args]')
        delegation = Delegation(_text(d, 'issuer'), _text(d, 'actor'), digest,
                                _int(d, 'policy_epoch'), _int(d, 'not_after'),
                                _bool(d, 'revoked'))
    checked = []
    for row in evidence:
        if not isinstance(row, dict):
            raise ValueError('evidence entries must be objects')
        checked.append(Evidence(_text(row, 'id'), _text(row, 'root'),
                                _bool(row, 'independent_observation')))
    check = None
    if review is not None:
        roots = review.get('evidence_roots')
        if (not isinstance(roots, list) or len(roots) > 50 or
                any(not isinstance(x, str) or not x.strip() or len(x) > 250 for x in roots)):
            raise ValueError('review.evidence_roots must be an array of nonempty strings')
        check = Review(tuple(roots), _bool(review, 'separate_failure_domain'),
                       _bool(review, 'may_reopen_decision'))
    return attempt, delegation, checked, check


def classify_supplied_record(data):
    """Exit 2 even for matching declarations: no user-supplied JSON is authority."""
    attempt, delegation, evidence, review = decode_record(data)
    report = examine(attempt=attempt, delegation=delegation,
                     evidence=evidence, review=review)
    report['verdict'] = ('DECLARED_MATCH_NOT_VERIFIED'
                         if report['authorization_matches_example']
                         else 'DECLARED_AUTHORITY_CONFLICT')
    report['exit_code'] = 2 if report['authorization_matches_example'] else 1
    report['read_only'] = True
    report['claim_limit'] = ('Submitted trace is not an authenticated grant or current policy; '
                             'independent trusted source verification is required before action.')
    return report


def demo_input():
    sample = cases()[0]
    _, attempt, grant, evidence, review, _, _ = sample
    return {
        'attempt': {
            'actor': attempt.actor, 'tool': attempt.tool, 'arguments': attempt.arguments,
            'at': attempt.at, 'policy_epoch': attempt.policy_epoch,
            'model_risk_label': attempt.model_risk_label,
        },
        'delegation': {
            'issuer': grant.issuer, 'actor': grant.actor, 'exact_action': grant.exact_action,
            'policy_epoch': grant.policy_epoch, 'not_after': grant.not_after,
            'revoked': grant.revoked,
        },
        'evidence': [{'id': e.id, 'root': e.root,
                      'independent_observation': e.independent_observation} for e in evidence],
        'review': {
            'evidence_roots': list(review.evidence_roots),
            'separate_failure_domain': review.separate_failure_domain,
            'may_reopen_decision': review.may_reopen_decision,
        },
    }


def input_self_tests():
    good = demo_input()
    bad_digest = json.loads(json.dumps(good))
    bad_digest['attempt']['arguments']['path'] = 'different.txt'
    bad_actor = json.loads(json.dumps(good))
    bad_actor['delegation']['actor'] = 'other-agent'
    bad_revoked = json.loads(json.dumps(good))
    bad_revoked['delegation']['revoked'] = True
    self_issuer = json.loads(json.dumps(good))
    self_issuer['delegation']['issuer'] = 'model'
    badly_typed = json.loads(json.dumps(good))
    badly_typed['attempt']['policy_epoch'] = True
    missing_state = json.loads(json.dumps(good))
    del missing_state['delegation']['revoked']
    malformed_roots = json.loads(json.dumps(good))
    malformed_roots['evidence'][0]['independent_observation'] = 'yes'
    no_delegation = json.loads(json.dumps(good))
    no_delegation['delegation'] = None
    for label, record, expected in (
        ('declared_match_still_unverified', good, 'DECLARED_MATCH_NOT_VERIFIED'),
        ('changed_effect', bad_digest, 'DECLARED_AUTHORITY_CONFLICT'),
        ('wrong_actor', bad_actor, 'DECLARED_AUTHORITY_CONFLICT'),
        ('revoked_even_if_model_says_safe', bad_revoked, 'DECLARED_AUTHORITY_CONFLICT'),
        ('self_claimed_issuer', self_issuer, 'DECLARED_AUTHORITY_CONFLICT'),
        ('no_grant', no_delegation, 'DECLARED_AUTHORITY_CONFLICT'),
        ('bool_epoch', badly_typed, 'INVALID'),
        ('missing_revocation', missing_state, 'INVALID'),
        ('claimed_independence_as_string', malformed_roots, 'INVALID'),
    ):
        try:
            verdict = classify_supplied_record(record)['verdict']
        except ValueError:
            verdict = 'INVALID'
        if verdict != expected:
            raise AssertionError(f'{label}: expected {expected}, received {verdict}')
    print('PASS: 9 additional input-format and negative/undetermined controls')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--self-test', action='store_true')
    parser.add_argument('--sample', action='store_true')
    parser.add_argument('--template', action='store_true',
                        help='print a synthetic editable JSON trace template')
    parser.add_argument('--input', type=Path,
                        help='classify your supplied trace (never authenticates permission)')
    parser.add_argument('--fingerprint', nargs=2, metavar=('TOOL', 'ARGUMENTS_JSON'),
                        help='calculate an illustrative exact-action digest')
    args = parser.parse_args()
    if sum(bool(x) for x in (args.self_test, args.sample, args.template,
                             args.input is not None, args.fingerprint is not None)) != 1:
        parser.error('choose exactly one of --self-test, --sample, --template, --input, --fingerprint')
    if args.template:
        print(json.dumps(demo_input(), indent=2, ensure_ascii=False))
        return 0
    if args.fingerprint:
        try:
            arguments = json.loads(args.fingerprint[1])
            if not isinstance(arguments, dict):
                raise ValueError('arguments must be a JSON object')
            print(action_fingerprint(args.fingerprint[0], arguments))
        except (ValueError, TypeError) as exc:
            print(f'INVALID: {exc}', file=sys.stderr)
            return 2
        return 0
    if args.input is not None:
        try:
            if args.input.stat().st_size > 65536:
                raise ValueError('input exceeds 64 KiB')
            obj = json.loads(args.input.read_text(encoding='utf-8'),
                             parse_constant=lambda x: (_ for _ in ()).throw(ValueError(f'invalid constant: {x}')))
            report = classify_supplied_record(obj)
        except (OSError, UnicodeError, ValueError, TypeError) as exc:
            print(json.dumps({'verdict':'INVALID', 'exit_code':2, 'reason':str(exc)},
                             ensure_ascii=False, indent=2))
            return 2
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return report['exit_code']
    if args.self_test:
        for name, attempt, grant, evidence, review, expected_auth, expected_markers in cases():
            report = examine(attempt=attempt, delegation=grant, evidence=evidence, review=review)
            found = set(report['authorization_failures'] + report['evidence_warnings'])
            if (report['authorization_matches_example'] != expected_auth
                    or not set(expected_markers).issubset(found)):
                raise AssertionError(f'{name}: {report}')
            print(f'PASS {name}: authorization={expected_auth}; flags={sorted(found)}')
        input_self_tests()
        print(f'PASS: {len(cases())} offline example controls')
        return 0
    if args.sample:
        _, attempt, grant, evidence, review, _, _ = cases()[0]
        print(json.dumps(examine(attempt=attempt, delegation=grant,
                                 evidence=evidence, review=review), indent=2, ensure_ascii=False))
        return 0
    parser.print_help()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
