#!/usr/bin/env python3
"""Exercise third-party local Docker MCP with real stdio request/response introspection."""
import json
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
    requests=[
        m(1,"initialize",{"protocolVersion":"2025-11-25","capabilities":{},"clientInfo":{"name":"glama-introspection-simulator","version":"1"}}),
        m(2,"tools/list"),
        m(3,"tools/call",{"name":"overview_nakagawa_whole_structure","arguments":{}}),
        m(4,"tools/call",{"name":"preflight_ai_answer_and_action","arguments":{
            "tool_results":[{"id":"send","status":"failed","success":True}]}}),
        m(5,"tools/call",{"name":"list_all_313_derivative_parent_links","arguments":{"offset":312,"limit":1}}),
        m(6,"server/discover",{"_meta": META}),
        m(7,"tools/list",{"_meta": META}),
    ]
    p=subprocess.run(["docker","run","--rm","--network=none","-i",IMAGE],
        input="".join(json.dumps(x,ensure_ascii=False)+"\n" for x in requests),
        capture_output=True,text=True,check=True,timeout=45)
    assert not p.stderr,p.stderr
    packets={int(x["id"]):x for x in map(json.loads,p.stdout.splitlines())}
    assert set(packets)=={x["id"] for x in requests},packets.keys()
    assert packets[1]["result"]["serverInfo"]["name"]=="nakagawa-public-original-router"
    names={x["name"] for x in packets[2]["result"]["tools"]}
    assert len(names)==9 and "preflight_ai_answer_and_action" in names and "list_all_313_derivative_parent_links" in names
    assert body(packets,3)["coverage"]["derivatives"]==313
    assert body(packets,4)["hold_count"]==1
    assert body(packets,5)["entries"][0]["id"]=="OD313"
    assert packets[6]["result"]["resultType"]=="complete"
    assert len(packets[7]["result"]["tools"])==9
    print("PASS: network-isolated, unprivileged Docker MCP introspection; same 9 tools, 313 Parent links, everyday guard, modern/legacy")
if __name__=="__main__":
    main()
