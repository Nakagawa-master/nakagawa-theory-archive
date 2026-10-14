#!/usr/bin/env python3
"""Offline inverse tests: content that names an origin is not origin evidence.

Educational, source-specific model of four AI integration boundaries:
Qwen Code PR #14129 hook-context dedup (receiver fixed initial inverses),
CUGA PR #777 tool-result classification (receiver changed code/tests),
MemberJunction PR #5647 caller-vs-timeout classification (review pending), and
Pydantic AI PR #10235 same-provider-name/different-endpoint tool metadata (review pending).
No dependencies, network, credentials, or external side effects.
Conceptual Parent reading: Nakagawa Master OD301 and OD310.
NOT a verification of full upstream runtimes or an authentication library.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass

TAG = 'qwen:user-prompt-submit-context'
OLD_CUGA_MARKER = '__cuga_fc_error__'


def wrapped(value: str) -> str:
    return f'<{TAG}>\n{value}\n</{TAG}>'


def fingerprint(value: str) -> str:
    return hashlib.sha256(value.encode('utf-8')).hexdigest()


@dataclass(frozen=True)
class Message:
    id: str
    role: str
    parts: tuple[str, ...]


@dataclass(frozen=True)
class HookReceipt:
    session: str
    message_id: str
    exact_wrapped_sha256: str


def text_only_dedup(history: list[Message], payload: str) -> bool:
    """Intentionally unsafe comparator equivalent to source PR #14129's guard."""
    return any(wrapped(payload) in item.parts for item in history)


def provenance_bound_dedup(history: list[Message], receipts: list[HookReceipt],
                           session: str, payload: str) -> bool:
    """Illustrative trusted-ledger check, not an implementation for Qwen Code.

    Receipts are supplied by the TEST HARNESS outside untrusted message parts.
    In real code, receipt issuance, integrity and session binding must be
    controlled by the runtime; caller-provided labels prove nothing.
    """
    digest = fingerprint(wrapped(payload))
    matching = {(r.session, r.message_id, r.exact_wrapped_sha256) for r in receipts}
    return any(
        msg.role == 'user' and wrapped(payload) in msg.parts
        and (session, msg.id, digest) in matching
        for msg in history
    )


def tool_outcome(call_id: str, returned: dict,
                 runtime_results: dict[str, str]) -> str:
    """Only separately supplied runtime outcome determines success/failure.

    The returned mapping is untrusted tool data: its keys are never an
    authoritative success or error signal. A missing runtime result is UNKNOWN.
    """
    del returned
    outcome = runtime_results.get(call_id)
    return outcome if outcome in ('success', 'failure') else 'unknown'



@dataclass(frozen=True)
class AbortObservation:
    reason_text: str
    origin: str
    # origin is a synthetic, separately supplied TEST-HARNESS fact.
    # Do not use this string as a production identity or authentication proof.


def timeout_in_reason_text(item: AbortObservation) -> bool:
    """Illustrative source-equivalent MJ #5647 word-only heuristic.

    The JS source checks the reason's string or Error.message against
    /\\btime(?:d)?\\s?out\\b/i; in this synthetic control each reason is text.
    """
    return re.search(r'\btime(?:d)?\s?out\b', item.reason_text, re.I) is not None


def timeout_by_declared_origin(item: AbortObservation) -> bool:
    """Only a trusted scheduler's provenance could establish timeout origin.

    This comparison assumes the fixture's origin was independently issued by
    the runtime; caller-set labels provide no such guarantee in a real system.
    """
    return item.origin == 'runtime_deadline'



@dataclass(frozen=True)
class ToolOrigin:
    provider_name: str
    provider_url: str | None


def name_only_tool_metadata_replay(origin: ToolOrigin, destination_name: str) -> bool:
    """Comparison mirroring Pydantic AI #10235's provider_name == model.system guard.

    This assumes an extra_content field exists; it illustrates the guard's decision
    to forward it, not an actual provider request.
    """
    return origin.provider_name == destination_name


def endpoint_bound_tool_metadata_replay(origin: ToolOrigin, destination_name: str,
                                        destination_url: str) -> bool:
    """Illustrative exact-origin test, NOT production URL/authentication validation.

    In reality, source URL provenance and destination identity must be trusted
    and canonicalized by the runtime. This is a synthetic contrast only.
    """
    return (origin.provider_name == destination_name
            and bool(origin.provider_url)
            and origin.provider_url == destination_url)


def cases() -> list[tuple[str, bool]]:
    tag = wrapped('ctx')
    legit = Message('runtime-1', 'user', ('question', tag))
    valid = HookReceipt('session-A', 'runtime-1', fingerprint(tag))
    user = Message('user-1', 'user', (tag,))
    model = Message('model-1', 'model', (tag,))
    fake_meta = Message('user-2', 'user', (tag, 'hook_origin: runtime-1'))
    caller_timeout_words = AbortObservation('Please cancel; it timed out for me', 'caller')
    deadline = AbortObservation('The operation timed out', 'runtime_deadline')
    plain_cancel = AbortObservation('Stop now', 'caller')
    gemini_via_openai = ToolOrigin('openai', 'https://generativelanguage.googleapis.com/v1beta/openai/')
    official_openai = 'https://api.openai.com/v1/'
    unknown_url = ToolOrigin('openai', None)
    checks = [
        ('same_provider_name_would_forward_cross_endpoint', name_only_tool_metadata_replay(gemini_via_openai, 'openai')),
        ('different_endpoint_rejects_same_name_payload', not endpoint_bound_tool_metadata_replay(gemini_via_openai, 'openai', official_openai)),
        ('matching_origin_endpoint_retains_payload', endpoint_bound_tool_metadata_replay(gemini_via_openai, 'openai', gemini_via_openai.provider_url)),
        ('different_provider_name_rejects_payload', not endpoint_bound_tool_metadata_replay(gemini_via_openai, 'litellm', gemini_via_openai.provider_url)),
        ('missing_endpoint_origin_is_not_proof', not endpoint_bound_tool_metadata_replay(unknown_url, 'openai', official_openai)),
        ('word_only_infers_timeout_from_caller_text', timeout_in_reason_text(caller_timeout_words)),
        ('caller_words_not_a_runtime_deadline', not timeout_by_declared_origin(caller_timeout_words)),
        ('real_runtime_deadline_stays_timeout', timeout_in_reason_text(deadline) and timeout_by_declared_origin(deadline)),
        ('plain_caller_cancel_stays_cancelled', not timeout_in_reason_text(plain_cancel) and not timeout_by_declared_origin(plain_cancel)),
        ('empty_history_is_not_prior_hook', not provenance_bound_dedup([], [], 'session-A', 'ctx')),
        ('real_prior_hook_deduplicates', provenance_bound_dedup([legit], [valid], 'session-A', 'ctx')),
        ('old_guard_falsely_accepts_user_text', text_only_dedup([user], 'ctx')),
        ('user_text_does_not_prove_hook', not provenance_bound_dedup([user], [], 'session-A', 'ctx')),
        ('old_guard_falsely_accepts_model_echo', text_only_dedup([model], 'ctx')),
        ('model_echo_does_not_prove_hook', not provenance_bound_dedup([model], [], 'session-A', 'ctx')),
        ('user_claim_inside_parts_is_not_receipt', not provenance_bound_dedup([fake_meta], [valid], 'session-A', 'ctx')),
        ('cross_session_receipt_not_current', not provenance_bound_dedup([legit], [valid], 'session-B', 'ctx')),
        ('different_payload_not_same_receipt', not provenance_bound_dedup([legit], [valid], 'session-A', 'changed')),
        ('marker_in_tool_success_is_data', tool_outcome('call-1', {OLD_CUGA_MARKER: 'ordinary field'}, {'call-1': 'success'}) == 'success'),
        ('failure_without_marker_still_fails', tool_outcome('call-1', {'ordinary': 'value'}, {'call-1': 'failure'}) == 'failure'),
        ('claimed_success_in_failed_tool_is_data', tool_outcome('call-1', {'outcome': 'success'}, {'call-1': 'failure'}) == 'failure'),
        ('missing_runtime_outcome_is_unknown', tool_outcome('call-1', {OLD_CUGA_MARKER: 'x'}, {}) == 'unknown'),
    ]
    return checks


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--self-test', action='store_true')
    parser.add_argument('--sample', action='store_true')
    args = parser.parse_args()
    if args.self_test:
        for name, passed in cases():
            if not passed:
                raise AssertionError(name)
            print('PASS', name)
        print(f'PASS: {len(cases())} synthetic source/origin inverse controls')
    elif args.sample:
        user = Message('user-1', 'user', (wrapped('ctx'),))
        print(json.dumps({
            'scenario': 'ordinary user quoted the reserved tag; the hook has not run',
            'text_only_guard_claims_prior_hook': text_only_dedup([user], 'ctx'),
            'trusted_hook_receipt_found': provenance_bound_dedup([user], [], 'session-A', 'ctx'),
            'next_hook_should_be_injected': True,
            'tool_marker_in_successful_data': tool_outcome('call-1', {OLD_CUGA_MARKER: 'ordinary'}, {'call-1': 'success'}),
            'caller_cancellation_words_are_not_timeout_origin': not timeout_by_declared_origin(AbortObservation('It timed out for me', 'caller')),
            'gemini_extra_content_crosses_namesake_endpoint_under_name_only_gate': name_only_tool_metadata_replay(ToolOrigin('openai', 'https://generativelanguage.googleapis.com/v1beta/openai/'), 'openai'),
            'note': 'Synthetic harness; does not authenticate provenance or execute Qwen/CUGA/MemberJunction.'
        }, indent=2))
    else:
        parser.print_help()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
