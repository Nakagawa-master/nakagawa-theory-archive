#!/usr/bin/env python3
"""Offline structural review of a *declared* AI-assisted adverse-decision handoff.

This is an educational preflight worksheet, not legal advice or verification that
any referenced notice, remedy, or reviewer exists or works in reality.
Never provide confidential or identifiable case files to this script.
"""
import argparse
import json
import sys

REQUIRED = (
    "decision_id", "decision_reason", "evidence_refs", "human_reviewer",
    "notice_to_affected_person", "appeal_route", "correction_route",
    "existing_remedy_retained", "rollback_or_pause", "independent_audit_ref",
)


def check(data):
    if not isinstance(data, dict):
        raise ValueError("Input must be a JSON object")
    errors = []
    for key in REQUIRED:
        value = data.get(key)
        if key == "evidence_refs":
            if not isinstance(value, list) or not value or not all(isinstance(s, str) and s.strip() for s in value):
                errors.append("missing_or_empty:" + key)
        elif not isinstance(value, str) or not value.strip():
            errors.append("missing_or_empty:" + key)
    for key in ("ai_final_adjudicator", "automatic_adverse_enforcement", "personality_ranking"):
        if data.get(key) is not False:
            errors.append("must_explicitly_be_false:" + key)
    if data.get("stage") not in ("hypothetical", "shadow", "pilot"):
        errors.append("stage_not_limited_to_non_enforcing_test")
    if data.get("uses_real_person_data") is not False:
        errors.append("must_explicitly_exclude_real_person_data")
    # The explanation must not merely repeat a cited evidence identifier.
    # This is only a syntactic negative check, not a proof of independent reasons.
    reason = data.get("decision_reason")
    refs = data.get("evidence_refs")
    if isinstance(reason, str) and isinstance(refs, list) and any(
        isinstance(ref, str) and reason.strip() == ref.strip() for ref in refs
    ):
        errors.append("reason_repeats_evidence_reference")
    return errors


def example():
    return {
        "decision_id": "SYNTHETIC-017",
        "stage": "shadow",
        "uses_real_person_data": False,
        "decision_reason": "A hypothetical grant review was flagged due to a missing document.",
        "evidence_refs": ["synthetic-policy-rule-v1", "synthetic-input-receipt-v2"],
        "human_reviewer": "Designated reviewer role; no decision delegated to a model",
        "notice_to_affected_person": "Draft notice naming the reason and evidence versions",
        "appeal_route": "Human appeal desk mock inbox",
        "correction_route": "Correct the missing input and request reconsideration",
        "existing_remedy_retained": "Existing human/legal channel remains available",
        "rollback_or_pause": "Pause the AI recommendation; restore pre-pilot routing",
        "independent_audit_ref": "Separate simulated auditor and dated review receipt",
        "ai_final_adjudicator": False,
        "automatic_adverse_enforcement": False,
        "personality_ranking": False,
    }


def self_test():
    good = example()
    cases = [
        ("complete declared example", good, True),
        ("no appeal", {**good, "appeal_route": ""}, False),
        ("no retained remedy", {**good, "existing_remedy_retained": ""}, False),
        ("no independent audit", {**good, "independent_audit_ref": ""}, False),
        ("no rollback", {**good, "rollback_or_pause": ""}, False),
        ("sole AI judge", {**good, "ai_final_adjudicator": True}, False),
        ("auto enforce", {**good, "automatic_adverse_enforcement": True}, False),
        ("ranking", {**good, "personality_ranking": True}, False),
        ("real person data", {**good, "uses_real_person_data": True}, False),
        ("empty evidence", {**good, "evidence_refs": []}, False),
        ("reason repeats evidence ID", {**good, "decision_reason": "synthetic-policy-rule-v1"}, False),
        ("active rollout", {**good, "stage": "active"}, False),
    ]
    for name, value, expected in cases:
        if (not check(value)) != expected:
            raise AssertionError(name)
    print("self-test: PASS (12 declared-fixture cases; not external system validation)")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--self-test", action="store_true")
    g.add_argument("--sample", action="store_true")
    g.add_argument("--input", metavar="JSON_FILE_OR_DASH")
    args = p.parse_args()
    if args.self_test:
        self_test()
        return 0
    if args.sample:
        print(json.dumps(example(), ensure_ascii=False, indent=2))
        return 0
    try:
        with (sys.stdin if args.input == "-" else open(args.input, encoding="utf-8")) as f:
            obj = json.load(f)
        issues = check(obj)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "INPUT_ERROR", "error": str(exc)}, ensure_ascii=False))
        return 2
    print(json.dumps({
        "status": "DECLARED_FIELDS_PRESENT_NOT_FACT_CHECKED" if not issues else "REQUIRES_HUMAN_REVIEW",
        "issues": issues,
        "limits": "No factual, legal, fairness, availability, or effective-appeal verification is performed. Never execute an adverse decision from this output.",
    }, ensure_ascii=False, indent=2))
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
