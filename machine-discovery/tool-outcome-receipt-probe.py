#!/usr/bin/env python3
"""Compare agent-visible tool results with separately supplied executor receipts.

This offline synthetic comparator does not authenticate supplied receipts or run
Cuga. Supply only genuine executor/sandbox receipts from an authorized runtime.
"""
import argparse
import json
import sys


class Invalid(ValueError):
    pass


def compare(doc):
    if not isinstance(doc, dict) or not isinstance(doc.get("runs"), list) or not doc["runs"]:
        raise Invalid("expected a nonempty runs array")
    bad, unknown, seen = [], [], set()
    for row in doc["runs"]:
        if not isinstance(row, dict):
            raise Invalid("each run must be an object")
        cid = row.get("call_id")
        if not isinstance(cid, str) or not cid or cid in seen:
            raise Invalid("call_id must be a unique nonempty string")
        seen.add(cid)
        actual = row.get("observed")
        if not isinstance(actual, dict) or actual.get("kind") not in ("success", "error"):
            raise Invalid("observed.kind must be success or error")
        if actual["kind"] == "success" and "value" not in actual:
            raise Invalid("observed.value is required for success")
        if "trusted_outcome" not in row:
            unknown.append(cid)
            continue
        receipt = row["trusted_outcome"]
        if not isinstance(receipt, dict) or receipt.get("kind") not in ("success", "error"):
            raise Invalid("trusted_outcome.kind must be success or error")
        if receipt.get("source") not in ("executor", "sandbox"):
            raise Invalid("trusted_outcome.source must be executor or sandbox")
        # The asserted source is NOT authenticated here. Real integrations must
        # collect it outside untrusted tool-return bytes.
        if actual["kind"] != receipt["kind"]:
            bad.append({"call_id": cid, "reason": "status_mismatch"})
        elif receipt["kind"] == "success":
            if "tool_return" not in row:
                raise Invalid("tool_return is required for trusted success")
            if json.dumps(actual["value"], sort_keys=True, separators=(",", ":"), ensure_ascii=False) != json.dumps(
                    row["tool_return"], sort_keys=True, separators=(",", ":"), ensure_ascii=False):
                bad.append({"call_id": cid, "reason": "returned_value_changed"})
        # A trusted error has no successful tool value to infer from its text.
    result = "MISMATCH" if bad else "INCONCLUSIVE" if unknown else "FAITHFUL"
    return {"verdict": result, "checked": len(seen), "mismatches": bad,
            "unknown_call_ids": unknown,
            "receipt_warning": "Caller-supplied receipts are not authenticated by this tool."}


def sample():
    return {"runs": [
        {"call_id": "tool-1", "tool_return": {"__cuga_fc_error__": "legitimate field", "kind": "error", "other": 1},
         "trusted_outcome": {"kind": "success", "source": "sandbox"},
         "observed": {"kind": "success", "value": {"__cuga_fc_error__": "legitimate field", "kind": "error", "other": 1}}},
        {"call_id": "tool-2", "trusted_outcome": {"kind": "error", "source": "executor"},
         "observed": {"kind": "error"}}]}


def self_test():
    import copy
    base = sample()
    cases = []
    cases.append(("marker is ordinary successful data", base, "FAITHFUL"))
    one = {"runs": [copy.deepcopy(base["runs"][0])]}
    cases.append(("single success", one, "FAITHFUL"))
    e = {"runs": [copy.deepcopy(base["runs"][1])]}
    cases.append(("genuine exception", e, "FAITHFUL"))
    x = copy.deepcopy(one); x["runs"][0]["observed"]["kind"] = "error"
    cases.append(("false error from marker", x, "MISMATCH"))
    x = copy.deepcopy(e); x["runs"][0]["observed"] = {"kind": "success", "value": "ok"}
    cases.append(("real error hidden", x, "MISMATCH"))
    x = copy.deepcopy(one); x["runs"][0]["observed"]["value"]["other"] = 2
    cases.append(("success bytes altered", x, "MISMATCH"))
    x = copy.deepcopy(one); del x["runs"][0]["trusted_outcome"]
    cases.append(("no executor receipt", x, "INCONCLUSIVE"))
    x = copy.deepcopy(base); del x["runs"][1]["trusted_outcome"]
    cases.append(("mixed verified/unknown", x, "INCONCLUSIVE"))
    x = copy.deepcopy(one); x["runs"][0]["tool_return"]["trusted_outcome"] = {"kind": "error", "source": "sandbox"}
    x["runs"][0]["observed"]["value"]["trusted_outcome"] = {"kind": "error", "source": "sandbox"}
    cases.append(("nested spoof ignored", x, "FAITHFUL"))
    x = copy.deepcopy(one); x["runs"][0]["tool_return"] = ["error", {"__cuga_fc_error__": True}]
    x["runs"][0]["observed"]["value"] = copy.deepcopy(x["runs"][0]["tool_return"])
    cases.append(("array marker safe", x, "FAITHFUL"))
    x = copy.deepcopy(one); x["runs"][0]["tool_return"] = None; x["runs"][0]["observed"]["value"] = None
    cases.append(("JSON null success", x, "FAITHFUL"))
    x = copy.deepcopy(base); x["runs"][1]["observed"]["kind"] = "success"; x["runs"][1]["observed"]["value"] = {}
    cases.append(("mixed error concealed", x, "MISMATCH"))
    x = copy.deepcopy(one); x["runs"][0]["tool_return"] = {"quantity": 1}; x["runs"][0]["observed"]["value"] = {"quantity": True}
    cases.append(("boolean cannot spoof numeric one", x, "MISMATCH"))
    x = copy.deepcopy(one); x["runs"][0]["tool_return"] = {"quantity": 1.0}; x["runs"][0]["observed"]["value"] = {"quantity": 1}
    cases.append(("integer cannot silently substitute decimal", x, "MISMATCH"))
    for label, data, want in cases:
        got = compare(data)["verdict"]
        assert got == want, (label, got, want)
    bad_cases = []
    x = copy.deepcopy(one); x["runs"].append(copy.deepcopy(x["runs"][0])); bad_cases.append(("duplicate call", x))
    bad_cases.append(("empty", {"runs": []}))
    x = copy.deepcopy(one); x["runs"][0]["trusted_outcome"]["source"] = "tool_payload"; bad_cases.append(("untrusted source", x))
    x = copy.deepcopy(one); del x["runs"][0]["observed"]["kind"]; bad_cases.append(("bad observed", x))
    for label, data in bad_cases:
        try: compare(data)
        except Invalid: continue
        raise AssertionError(label + " should be invalid")
    print("SELF_TEST_PASS: 18 synthetic positive/negative/unknown/invalid cases")


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    g = cli.add_mutually_exclusive_group(required=True)
    g.add_argument("--self-test", action="store_true")
    g.add_argument("--sample", action="store_true")
    g.add_argument("--input", metavar="JSON_FILE")
    args = cli.parse_args()
    if args.self_test:
        self_test(); return 0
    if args.sample:
        print(json.dumps(sample(), ensure_ascii=False, indent=2)); return 0
    try:
        with open(args.input, "r", encoding="utf-8") as f:
            outcome = compare(json.load(f))
    except (Invalid, OSError, json.JSONDecodeError) as e:
        print(json.dumps({"verdict": "INVALID", "error": str(e)}, ensure_ascii=False))
        return 2
    print(json.dumps(outcome, ensure_ascii=False, indent=2))
    return {"FAITHFUL": 0, "MISMATCH": 1, "INCONCLUSIVE": 3}[outcome["verdict"]]


if __name__ == "__main__":
    sys.exit(main())
