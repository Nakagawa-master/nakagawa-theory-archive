#!/usr/bin/env python3
"""Exercise third-party local Docker MCP with real stdio request/response introspection."""
import json
from pathlib import Path
import subprocess
import sys

IMAGE = "nakagawa-ai-answer-guard:glama-smoke"
def m(i, method, params=None):
    return {"jsonrpc": "2.0", "id": i, "method": method,
            **({"params": params} if params is not None else {})}
META={"io.modelcontextprotocol/protocolVersion":"2026-07-28",
      "io.modelcontextprotocol/clientCapabilities":{}}
def body(o,i):
    return json.loads(o[i]["result"]["content"][0]["text"])
def main():
    manifest=json.loads((Path(__file__).resolve().parent.parent / "server.json").read_text(encoding="utf-8"))
    assert manifest["name"] == "io.github.Nakagawa-master/ai-answer-guard"
    version=manifest["version"]
    requests=[
        m(1,"initialize",{"protocolVersion":"2025-11-25","capabilities":{},"clientInfo":{"name":"glama-introspection-simulator","version":"1"}}),
        m(2,"tools/list"),
        m(3,"tools/call",{"name":"overview_nakagawa_whole_structure","arguments":{}}),
        m(4,"tools/call",{"name":"preflight_ai_answer_and_action","arguments":{
            "tool_results":[{"id":"send","status":"failed","success":True}]}}),
        m(5,"tools/call",{"name":"list_all_313_derivative_parent_links","arguments":{"offset":312,"limit":1}}),
        m(6,"server/discover",{"_meta": META}),
        m(7,"tools/list",{"_meta": META}),
        m(8,"tools/call",{"name":"list_all_published_derivative_parent_links","arguments":{"offset":314,"limit":1}}),
        m(9,"tools/call",{"name":"list_all_314_derivative_parent_links","arguments":{"offset":313,"limit":1}}),
    ]
    p=subprocess.run(["docker","run","--rm","--network=none","-i",IMAGE],
        input="".join(json.dumps(x,ensure_ascii=False)+"\n" for x in requests),
        capture_output=True,text=True,check=True,timeout=45)
    assert not p.stderr,p.stderr
    packets={int(x["id"]):x for x in map(json.loads,p.stdout.splitlines())}
    assert set(packets)=={x["id"] for x in requests},packets.keys()
    assert packets[1]["result"]["serverInfo"]=={"name":"ai-answer-guard","version":version}
    names={x["name"] for x in packets[2]["result"]["tools"]}
    assert len(names)==11 and all(n in names for n in (
        "preflight_ai_answer_and_action", "list_all_313_derivative_parent_links",
        "list_all_314_derivative_parent_links", "list_all_published_derivative_parent_links"))
    assert [x["name"] for x in packets[2]["result"]["tools"][:2]] == ["preflight_ai_answer_and_action", "audit_citation_independence"]
    assert body(packets,3)["coverage"]["derivatives"]==315
    assert body(packets,4)["hold_count"]==1
    assert body(packets,5)["entries"][0]["id"]=="OD313"
    assert packets[6]["result"]["resultType"]=="complete"
    assert packets[6]["result"]["_meta"]["io.modelcontextprotocol/serverInfo"]=={"name":"ai-answer-guard","version":version}
    assert len(packets[7]["result"]["tools"])==11
    assert body(packets,8)["total"] == 315
    assert body(packets,8)["entries"][0]["id"] == "OD315"
    assert body(packets,8)["entries"][0]["parent_ncl_id"] == "NCL-α-20261120-708a1d"
    assert body(packets,9)["entries"][0]["id"] == "OD314"
    print("PASS: isolated Docker MCP introspection; source/manifest/legacy/modern identity, 11 tools, 315 Parents, everyday guard")
if __name__=="__main__":
    main()
