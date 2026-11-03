#!/usr/bin/env python3
"""Safe offline stdio MCP tool-discovery fixture for Qwen Code >=0.26.6.

No network, file writes, shell execution, model calls, secrets or customer data.
Use --mode clean to discover all unique tools, --mode collision to discover
only unique tools after an intentionally ambiguous duplicate name is removed.
The server itself is NOT a Qwen binary or an end-to-end Qwen runtime test.
"""
import argparse
import json
import subprocess
import sys
from typing import Any

PROTOCOL = "2025-03-26"


def tool(name: str) -> dict[str, Any]:
    return {
        "name": name,
        "description": "Offline test-only identity; does not perform external operations.",
        "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
    }


def tools_for(mode: str) -> list[dict[str, Any]]:
    items = [tool("visible_alpha"), tool("visible_beta")]
    if mode == "clean":
        return [tool("distinct_one"), tool("distinct_two")] + items
    if mode == "collision":
        return [tool("ambiguous_name"), tool("ambiguous_name")] + items
    raise ValueError("unsupported mode")


def process(request: Any, mode: str) -> dict[str, Any] | None:
    if not isinstance(request, dict) or request.get("jsonrpc") != "2.0":
        return None
    # Protocol notifications are one-way, without any response on stdout.
    if "id" not in request:
        return None
    identifier = request["id"]
    method = request.get("method")
    if not isinstance(method, str):
        return {"jsonrpc": "2.0", "id": identifier, "error": {"code": -32600, "message": "Invalid request"}}
    params = request.get("params") or {}
    if method == "initialize":
        # Prefer the version requested by an SDK; no silent guessing of installed runtime behavior.
        selected = params.get("protocolVersion") if isinstance(params, dict) else None
        if not isinstance(selected, str):
            selected = PROTOCOL
        result = {
            "protocolVersion": selected,
            "capabilities": {"tools": {"listChanged": False}},
            "serverInfo": {"name": "qwen-mcp-collision-fixture", "version": "1.0.0"},
        }
    elif method == "ping":
        result = {}
    elif method == "tools/list":
        result = {"tools": tools_for(mode)}
    elif method == "tools/call":
        name = params.get("name") if isinstance(params, dict) else None
        if name not in ("visible_alpha", "visible_beta", "distinct_one", "distinct_two") or (name in ("distinct_one", "distinct_two") and mode != "clean"):
            return {"jsonrpc": "2.0", "id": identifier, "error": {"code": -32602, "message": "Tool not exposed for execution"}}
        result = {"content": [{"type": "text", "text": f"fixture-only:{name}"}], "isError": False}
    elif method in ("resources/list", "prompts/list"):
        result = {"resources" if method == "resources/list" else "prompts": []}
    else:
        return {"jsonrpc": "2.0", "id": identifier, "error": {"code": -32601, "message": "Method not found"}}
    return {"jsonrpc": "2.0", "id": identifier, "result": result}


def serve(mode: str) -> int:
    for raw in sys.stdin:
        if len(raw) > 65536:
            print("fixture: oversized message rejected", file=sys.stderr)
            continue
        try:
            request = json.loads(raw)
            response = process(request, mode)
        except (ValueError, TypeError, KeyError) as exc:
            print(f"fixture: invalid JSON-RPC input: {type(exc).__name__}", file=sys.stderr)
            continue
        if response is not None:
            sys.stdout.write(json.dumps(response, separators=(",", ":")) + "\n")
            sys.stdout.flush()
    return 0


def self_test() -> int:
    checks = 0
    for mode in ("clean", "collision"):
        reqs = [
            {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-06-18"}},
            {"jsonrpc": "2.0", "method": "notifications/initialized"},
            {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}},
            {"jsonrpc": "2.0", "id": 3, "method": "resources/list"},
            {"jsonrpc": "2.0", "id": 4, "method": "prompts/list"},
            {"jsonrpc": "2.0", "id": 5, "method": "tools/call", "params": {"name": "visible_alpha", "arguments": {}}},
            {"jsonrpc": "2.0", "id": 6, "method": "tools/call", "params": {"name": "ambiguous_name", "arguments": {}}},
            {"jsonrpc": "2.0", "id": 7, "method": "ping"},
            {"jsonrpc": "2.0", "id": 8, "method": "unsupported"},
        ]
        p = subprocess.run([sys.executable, __file__, "--mode", mode], input="\n".join(json.dumps(x) for x in reqs) + "\n", text=True, capture_output=True, timeout=10, check=True)
        out = [json.loads(x) for x in p.stdout.splitlines()]
        assert len(out) == 8, (mode, out, p.stderr)
        checks += 1
        by_id = {x["id"]: x for x in out}
        assert by_id[1]["result"]["protocolVersion"] == "2025-06-18"
        checks += 1
        assert len(by_id[2]["result"]["tools"]) == 4
        checks += 1
        names = [t["name"] for t in by_id[2]["result"]["tools"]]
        assert names.count("visible_alpha") == 1 and names.count("visible_beta") == 1
        checks += 1
        if mode == "collision":
            assert names.count("ambiguous_name") == 2 and not any(n.startswith("distinct_") for n in names)
        else:
            assert names.count("distinct_one") == 1 and names.count("distinct_two") == 1
        checks += 1
        assert by_id[3]["result"] == {"resources": []} and by_id[4]["result"] == {"prompts": []}
        checks += 1
        assert by_id[5]["result"]["content"][0]["text"] == "fixture-only:visible_alpha"
        checks += 1
        assert by_id[6]["error"]["code"] == -32602
        checks += 1
        assert by_id[7]["result"] == {} and by_id[8]["error"]["code"] == -32601
        checks += 1
    # Attempting to call colliding names is disallowed by the fixture regardless of Qwen's behavior.
    assert process({"jsonrpc": "2.0", "method": "tools/list"}, "collision") is None
    checks += 1
    assert process({"jsonrpc": "2.0", "id": 5, "method": "bad"}, "collision")["error"]["code"] == -32601
    checks += 1
    assert process({"jsonrpc": "2.0", "id": 6, "method": "tools/call", "params": {"name": "x"}}, "collision")["error"]["code"] == -32602
    checks += 1
    print(f"PASS_{checks}_MCP_PROTOCOL_CHECKS; QWEN_INTEGRATION_NOT_RUN")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("clean", "collision"), default="collision")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    return self_test() if args.self_test else serve(args.mode)


if __name__ == "__main__":
    sys.exit(main())
