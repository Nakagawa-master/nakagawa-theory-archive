#!/usr/bin/env python3
"""Offline, caller-supplied ordered trace check for a completed agent action
redispatched on nested resume and for reuse of stale authorization.

Run: python3 machine-discovery/nested-resume-authority-trace-check.py --self-test
     python3 machine-discovery/nested-resume-authority-trace-check.py --sample
     python3 machine-discovery/nested-resume-authority-trace-check.py trace.json

Input: {"scenario":"label","events":[{"type":"grant", ...}, ...]}
Event labels are CALLER ASSERTIONS, not verified runtime telemetry.
This models a strict bound-grant policy; systems using deliberate live-policy
grants must adapt that rule. It does not enforce actual execution policy.
Public source: https://github.com/langchain-ai/langgraph/issues/9106
Original theory: https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/
Origin: Nakagawa Master.
"""
import argparse
import json
import sys
from pathlib import Path

TYPES = {"grant","revoke","policy_change","policy_check","dispatch","effect",
         "complete","resume","explicit_retry_request"}


def audit(data):
    if not isinstance(data,dict) or not isinstance(data.get("events"),list):
        raise ValueError("provide an object with events: []")
    grants, checks, dispatches, completed, retries = {}, {}, {}, {}, {}
    seen_effects, warnings, defects = [], [], []
    revision, last_resume = "p1", -1
    for i,e in enumerate(data["events"]):
        if not isinstance(e,dict) or e.get("type") not in TYPES:
            raise ValueError("invalid event type at %d" % i)
        t=e["type"]
        required={
            "grant":("grant_id","action_id","policy_revision"),
            "revoke":("grant_id",),"policy_change":("policy_revision",),
            "policy_check":("operation_id","grant_id","policy_revision"),
            "dispatch":("operation_id","action_id","grant_id"),
            "effect":("operation_id","effect_id"),"complete":("operation_id",),
            "resume":("kind",),
            "explicit_retry_request":("operation_id","action_id","grant_id","intent_source")
        }[t]
        for k in required:
            if not isinstance(e.get(k),str) or not e[k]:
                raise ValueError("event %d missing string %s"%(i,k))
        if t=="grant":
            g=e["grant_id"]
            if g in grants: raise ValueError("duplicate grant id: "+g)
            grants[g]=[e["action_id"],e["policy_revision"],i,False]
        elif t=="revoke":
            if e["grant_id"] not in grants: raise ValueError("unknown revoked grant")
            grants[e["grant_id"]][3]=True
        elif t=="policy_change":
            revision=e["policy_revision"]
        elif t=="policy_check":
            if type(e.get("allowed")) is not bool: raise ValueError("allowed must be boolean")
            checks[e["operation_id"]]=(e["grant_id"],e["policy_revision"],e["allowed"],i)
        elif t=="resume":
            if e["kind"] not in ("ordinary","time_travel","explicit_retry"):
                raise ValueError("unknown resume kind")
            last_resume=i
        elif t=="explicit_retry_request":
            if e["intent_source"] not in ("human","authorized_api_client"):
                raise ValueError("intent_source must name declared legitimate caller")
            retries[e["operation_id"]]=(e["action_id"],e["grant_id"],i)
        elif t=="dispatch":
            op, action, gid=e["operation_id"],e["action_id"],e["grant_id"]
            if op in dispatches: raise ValueError("operation_id reused")
            dispatches[op]=(action,i)
            g=grants.get(gid)
            if g is None or g[0]!=action or g[3]:
                defects.append("event %d: missing, revoked or wrong-action grant for %s"%(i,op))
            elif g[1]!=revision:
                defects.append("event %d: grant %s is for prior policy revision"%(i,gid))
            chk=checks.get(op)
            if not chk or chk[0]!=gid or chk[1]!=revision or not chk[2]:
                defects.append("event %d: missing, denied or mismatched current policy check for %s"%(i,op))
            elif g and chk[3]<g[2]:
                defects.append("event %d: policy check predates grant"%(i))
            elif last_resume>=0 and chk[3]<last_resume:
                defects.append("event %d: policy check predates latest resume"%(i))
            elif any(v["type"] in ("revoke","policy_change") for v in data["events"][chk[3]+1:i]):
                defects.append("event %d: authority changed after policy check"%(i))
            if action in completed:
                last_completion=max(completed[action].values())
                r=retries.get(op)
                fresh=(r is not None and r[0]==action and r[1]==gid
                       and r[2]>max(last_resume,last_completion)
                       and g is not None and g[2]>last_completion)
                if not fresh:
                    defects.append("event %d: completed action %s redispatched without fresh bound intent/grant"%(i,action))
        elif t=="effect":
            if e["operation_id"] not in dispatches:
                defects.append("event %d: effect has no logged dispatch"%i)
            if e["effect_id"] in seen_effects:
                warnings.append("event %d: effect id repeated; check trace identity"%i)
            seen_effects.append(e["effect_id"])
        elif t=="complete":
            op=e["operation_id"]
            if op not in dispatches: raise ValueError("completion without dispatch")
            action=dispatches[op][0]
            completed.setdefault(action,{})[op]=i
    if not data["events"]: raise ValueError("at least one event required")
    return {"scenario":data.get("scenario","unspecified"),
            "verdict":"VIOLATION" if defects else "CONSISTENT_AS_LOGGED",
            "violations":defects,"warnings":warnings,
            "declared_dispatches":len(dispatches),
            "declared_external_effects":len(seen_effects),
            "evidence_limit":"Caller-supplied labels only. No production enforcement, telemetry validation, proof of exactly-once execution, or independent third-party use. Absence of effect records cannot establish absence of effects."}


def fixture(kind):
    e=[{"type":"grant","grant_id":"gA","action_id":"A","policy_revision":"p1"},
       {"type":"policy_check","operation_id":"A1","grant_id":"gA","policy_revision":"p1","allowed":True},
       {"type":"dispatch","operation_id":"A1","action_id":"A","grant_id":"gA"},
       {"type":"effect","operation_id":"A1","effect_id":"A-side-effect-1"},
       {"type":"complete","operation_id":"A1"},
       {"type":"resume","kind":"ordinary"}]
    if kind=="completed_sibling_not_replayed":
        e += [{"type":"grant","grant_id":"gB","action_id":"B","policy_revision":"p1"},
              {"type":"policy_check","operation_id":"B1","grant_id":"gB","policy_revision":"p1","allowed":True},
              {"type":"dispatch","operation_id":"B1","action_id":"B","grant_id":"gB"},
              {"type":"effect","operation_id":"B1","effect_id":"B-side-effect-1"}]
    elif kind=="unintended_replay":
        e += [{"type":"policy_check","operation_id":"A2","grant_id":"gA","policy_revision":"p1","allowed":True},
              {"type":"dispatch","operation_id":"A2","action_id":"A","grant_id":"gA"},
              {"type":"effect","operation_id":"A2","effect_id":"A-side-effect-2"}]
    elif kind=="revoked_grant":
        e += [{"type":"revoke","grant_id":"gA"},
              {"type":"policy_check","operation_id":"A2","grant_id":"gA","policy_revision":"p1","allowed":False},
              {"type":"dispatch","operation_id":"A2","action_id":"A","grant_id":"gA"}]
    elif kind=="changed_policy":
        e += [{"type":"policy_change","policy_revision":"p2"},
              {"type":"policy_check","operation_id":"A2","grant_id":"gA","policy_revision":"p2","allowed":True},
              {"type":"dispatch","operation_id":"A2","action_id":"A","grant_id":"gA"}]
    elif kind=="explicit_fresh_retry":
        e += [{"type":"grant","grant_id":"gA2","action_id":"A","policy_revision":"p1"},
              {"type":"explicit_retry_request","operation_id":"A2","action_id":"A","grant_id":"gA2","intent_source":"human"},
              {"type":"policy_check","operation_id":"A2","grant_id":"gA2","policy_revision":"p1","allowed":True},
              {"type":"dispatch","operation_id":"A2","action_id":"A","grant_id":"gA2"},
              {"type":"effect","operation_id":"A2","effect_id":"intentional-new-A-effect"}]
    elif kind=="pre_resume_policy_check":
        e=e[:-1]+[{"type":"grant","grant_id":"gB","action_id":"B","policy_revision":"p1"},
                  {"type":"policy_check","operation_id":"B1","grant_id":"gB","policy_revision":"p1","allowed":True},
                  {"type":"resume","kind":"ordinary"},
                  {"type":"dispatch","operation_id":"B1","action_id":"B","grant_id":"gB"}]
    elif kind=="missing_effect_observation":
        e=[x for x in e if x["type"]!="effect"]
    else: raise ValueError(kind)
    return {"scenario":kind,"events":e}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("path",nargs="?")
    p.add_argument("--self-test",action="store_true")
    p.add_argument("--sample",action="store_true")
    a=p.parse_args()
    if a.self_test or a.sample:
        expected={"completed_sibling_not_replayed":False,"unintended_replay":True,
                  "revoked_grant":True,"changed_policy":True,"explicit_fresh_retry":False,
                  "pre_resume_policy_check":True,"missing_effect_observation":False}
        results=[audit(fixture(k)) for k in expected]
        for r in results:
            assert (r["verdict"]=="VIOLATION")==expected[r["scenario"]],r
        if a.sample: print(json.dumps(results,ensure_ascii=False,indent=2))
        else: print("PASS: 7 synthetic regression vectors; no framework integration claimed")
        return 0
    if not a.path: p.error("specify trace.json or --sample/--self-test")
    r=audit(json.loads(Path(a.path).read_text(encoding="utf-8")))
    print(json.dumps(r,ensure_ascii=False,indent=2))
    return 1 if r["verdict"]=="VIOLATION" else 0


if __name__=="__main__":
    try: sys.exit(main())
    except (ValueError,AssertionError) as error:
        print("invalid trace: "+str(error),file=sys.stderr)
        sys.exit(2)
