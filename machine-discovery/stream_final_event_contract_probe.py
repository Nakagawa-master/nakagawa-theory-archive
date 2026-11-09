#!/usr/bin/env python3
"""Offline evidence checker for FINAL streamed tool calls and Responses item consistency.

All inputs are provided by the operator; this tool neither connects to an LLM nor
proves that the trace is authentic. Run on synthetic or redacted observations.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

EXAMPLE = {
    "case": "synthetic-two-tools-one-committed",
    "outcome": "completed",
    "events": [
        {"stage": "provisional", "tool_calls": ["A", "B"]},
        {"stage": "committed", "tool_calls": ["A"]},
    ],
    "final_response_tool_calls": ["A"],
    "executed_tool_calls": ["A"],
}


def tool_ids(value: object, field: str) -> list[str]:
    if not isinstance(value, list) or any(not isinstance(v, str) or not v.strip() for v in value):
        raise ValueError(f"{field} must be a list of nonempty tool-call identifiers")
    if len(set(value)) != len(value):
        raise ValueError(f"{field} must identify distinct call occurrences (use distinct IDs)")
    return value



def check_responses_items(trace):
    """Check consistency of caller-supplied Responses stream item snapshots.

    No provider/HTTP verification. JSON object key ordering has no semantic effect.
    """
    if not isinstance(trace, dict) or trace.get('contract') != 'responses_items':
        return {'result': 'INVALID_INPUT', 'reason': 'contract must be responses_items'}
    events = trace.get('events')
    if not isinstance(events, list) or not events:
        return {'result': 'INVALID_INPUT', 'reason': 'events must be a nonempty list'}
    added, done, completed = {}, {}, None
    for n, event in enumerate(events):
        if not isinstance(event, dict) or not isinstance(event.get('type'), str):
            return {'result': 'INVALID_INPUT', 'reason': f'events[{n}] needs type'}
        kind = event['type']
        if kind not in ('response.output_item.added','response.output_item.done','response.completed'):
            continue
        if kind == 'response.completed':
            if completed is not None:
                return {'result':'FAIL','reason':'multiple response.completed snapshots'}
            completed = event.get('response')
            if not isinstance(completed, dict):
                return {'result':'INVALID_INPUT','reason':'completed.response needs object'}
            continue
        index = event.get('output_index')
        item = event.get('item')
        if type(index) is not int or index < 0 or not isinstance(item, dict):
            return {'result':'INVALID_INPUT','reason':f'events[{n}] needs nonnegative integer output_index and item object'}
        if kind.endswith('.added'):
            if index in added:
                return {'result':'FAIL','reason':f'duplicate added event for index {index}'}
            added[index] = item
        else:
            if index in done:
                return {'result':'FAIL','reason':f'duplicate done event for index {index}'}
            done[index] = item
    if completed is None:
        return {'result':'NOT_ASSESSED','reason':'no response.completed snapshot provided'}
    output = completed.get('output')
    if not isinstance(output,list) or not all(isinstance(x,dict) for x in output):
        return {'result':'INVALID_INPUT','reason':'completed.response.output must be an array of objects'}
    if set(done) != set(range(len(output))) or set(added) != set(range(len(output))):
        return {'result':'FAIL','reason':'added/done indices do not cover completed output one-for-one', 'added_indices':sorted(added),'done_indices':sorted(done),'output_size':len(output)}
    for index, item in enumerate(output):
        first = added[index]
        last = done[index]
        if first.get('type') != last.get('type'):
            return {'result':'FAIL','reason':f'item type changed at index {index}'}
        if last.get('type') == 'reasoning' and not isinstance(first.get('summary'),list):
            return {'result':'FAIL','reason':f'added reasoning item {index} has no summary array'}
        if item != last:
            return {'result':'FAIL','reason':f'completed output item {index} differs from corresponding done item (JSON structure)'}
    return {'result':'PASS','reason':'all added/done/completed item snapshots agree structurally (supplied trace only)','checked_items':len(output)}


def synthetic_responses_self_test():
    added={'type':'reasoning','id':'r1','summary':[]}
    done={'type':'reasoning','id':'r1','summary':[{'type':'summary_text','text':'ok'}]}
    calls=[{'type':'function_call','id':'c1','call_id':'x','arguments':'{}','name':'hello'}]
    events=[{'type':'response.output_item.added','output_index':0,'item':added},
            {'type':'response.output_item.done','output_index':0,'item':done},
            {'type':'response.output_item.added','output_index':1,'item':calls[0]},
            {'type':'response.output_item.done','output_index':1,'item':calls[0]},
            {'type':'response.completed','response':{'output':[done,calls[0]]}}]
    good={'contract':'responses_items','events':events}
    assert check_responses_items(good)['result']=='PASS'
    bad_missing={'contract':'responses_items','events':[{'type':'response.output_item.added','output_index':0,'item':{'type':'reasoning','id':'r1'}},*events[1:]]}
    assert check_responses_items(bad_missing)['result']=='FAIL'
    bad_rebuild={'contract':'responses_items','events':[*events[:-1],{'type':'response.completed','response':{'output':[{'type':'reasoning','id':'r1','content':[]},calls[0]]}}]}
    assert check_responses_items(bad_rebuild)['result']=='FAIL'
    # Different object key order is not a protocol error by itself.
    reordered={'type':'function_call','name':'hello','arguments':'{}','call_id':'x','id':'c1'}
    assert check_responses_items({'contract':'responses_items','events':[ *events[:-1],{'type':'response.completed','response':{'output':[done,reordered]}}]})['result']=='PASS'
    assert check_responses_items({'contract':'responses_items','events':events[:-1]})['result']=='NOT_ASSESSED'
    assert check_responses_items({'contract':'responses_items','events':[events[0],events[1],events[-1]]})['result']=='FAIL'
    return 'PASS: six Responses event-contract cases'


def check(trace: object) -> dict[str, object]:
    if isinstance(trace, dict) and trace.get("contract") == "responses_items":
        return check_responses_items(trace)
    if not isinstance(trace, dict):
        raise ValueError("trace must be a JSON object")
    outcome = trace.get("outcome")
    if outcome not in ("completed", "validation_error", "early_stopped"):
        raise ValueError("outcome must be completed, validation_error or early_stopped")
    events = trace.get("events")
    if not isinstance(events, list):
        raise ValueError("events must be a list")
    committed = []
    for i, event in enumerate(events):
        if not isinstance(event, dict) or event.get("stage") not in ("provisional", "committed"):
            raise ValueError(f"events[{i}] must have stage provisional or committed")
        ids = tool_ids(event.get("tool_calls"), f"events[{i}].tool_calls")
        if event["stage"] == "committed":
            committed.append((i, ids))
    if len(committed) > 1:
        return {"result": "FAIL", "reason": "Multiple committed final events: check final-event ownership"}
    if committed and committed[0][0] != len(events) - 1:
        return {"result": "FAIL", "reason": "A provisional event follows the committed final event"}
    final = tool_ids(trace.get("final_response_tool_calls"), "final_response_tool_calls")
    executed = tool_ids(trace.get("executed_tool_calls"), "executed_tool_calls")
    if outcome == "early_stopped":
        if committed:
            return {"result": "FAIL", "reason": "An early-stopped stream was presented as a committed final event"}
        return {"result": "NOT_ASSESSED", "reason": "Partial stream: final validation and upstream close/aclose require separate evidence"}
    if outcome == "validation_error":
        if committed:
            return {"result": "FAIL", "reason": "A rejected final response was already emitted as a committed event"}
        if executed:
            return {"result": "FAIL", "reason": "Tool execution occurred despite final validation error"}
        return {"result": "PASS", "reason": "No committed event or execution after validation error (trace claim only)"}
    if not committed:
        return {"result": "FAIL", "reason": "Completed run lacks a captured committed final event"}
    emitted = committed[0][1]
    if emitted != final or final != executed:
        return {"result": "FAIL", "reason": "Event-time committed calls, validated final response and execution differ", "committed": emitted, "final": final, "executed": executed}
    return {"result": "PASS", "reason": "Committed event agrees with validated final response and next-step executed calls (trace claim only)", "calls": emitted}


def self_test() -> None:
    synthetic_responses_self_test()
    def run(outcome: str, events: list[dict], final: list[str], executed: list[str]) -> str:
        return str(check({"outcome": outcome, "events": events, "final_response_tool_calls": final, "executed_tool_calls": executed})["result"])
    provisional = {"stage": "provisional", "tool_calls": ["A", "B"]}
    good = {"stage": "committed", "tool_calls": ["A"]}
    bad = {"stage": "committed", "tool_calls": ["A", "B"]}
    assert run("completed", [provisional, good], ["A"], ["A"]) == "PASS"
    assert run("completed", [provisional, bad], ["A"], ["A"]) == "FAIL"
    assert run("completed", [provisional, good], ["A"], ["A", "B"]) == "FAIL"
    assert run("completed", [provisional], ["A"], ["A"]) == "FAIL"
    assert run("validation_error", [provisional], [], []) == "PASS"
    assert run("validation_error", [bad], [], []) == "FAIL"
    assert run("validation_error", [provisional], [], ["A"]) == "FAIL"
    assert run("early_stopped", [provisional], [], []) == "NOT_ASSESSED"
    assert run("early_stopped", [good], ["A"], []) == "FAIL"
    try:
        check({"outcome": "completed", "events": [good], "final_response_tool_calls": ["A", "A"], "executed_tool_calls": ["A"]})
    except ValueError:
        pass
    else:
        raise AssertionError("Duplicate call IDs must be rejected")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("trace", nargs="?", type=Path, help="JSON trace captured at actual event emission and next-step execution")
    p.add_argument("--sample", action="store_true", help="Print a synthetic example JSON trace")
    p.add_argument("--self-test", action="store_true", help="Run deterministic positive/negative and malformed-case checks")
    args = p.parse_args()
    if args.self_test:
        self_test()
        print("Self-test PASS: 16 bounded contracts (10 tool-call + 6 Responses-item cases)")
        return 0
    if args.sample:
        print(json.dumps(EXAMPLE, ensure_ascii=False, indent=2))
        return 0
    if args.trace is None:
        p.error("pass a JSON trace, --sample, or --self-test")
    try:
        result = check(json.loads(args.trace.read_text(encoding="utf-8")))
    except (OSError, ValueError, json.JSONDecodeError) as e:
        print(json.dumps({"result": "INVALID_INPUT", "reason": str(e)}, ensure_ascii=False))
        return 2
    print(json.dumps(result, ensure_ascii=False))
    return {"PASS": 0, "FAIL": 1, "NOT_ASSESSED": 3}[str(result["result"])]


if __name__ == "__main__":
    raise SystemExit(main())
