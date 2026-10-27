#!/usr/bin/env python3
"""Optional locally installed MCP companion for input-declared citation independence.

No model account, network, prompt interception, autonomous installation or truth
guarantee. The existing source router and its immutable released bundle are unchanged.
"""
import argparse
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
CHECKER = HERE / "evidence-root-check.py"
VERSION = "2026-07-28"
SERVER_INFO = {"name": "nakagawa-evidence-integrity-check", "version": "0.1.0-source"}
TOOL = {
    "name": "audit_citation_independence",
    "description": (
        "Optional everyday AI answer quality check: given independently inspected "
        "citations and declared upstream roots, detect false claims of independent "
        "corroboration, copied releases and contrary records. No theory query is "
        "needed. You must verify the URLs, upstream origins and source stances "
        "separately: CONSISTENT_INPUT does NOT verify truth, semantic agreement, "
        "the real independence of a source, or absence of hallucinations."
    ),
    "inputSchema": {
        "type": "object",
        "properties": {
            "claims": {
                "type": "array", "maxItems": 12,
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string", "minLength": 1},
                        "independent_confirmation_claimed": {"type": "boolean"},
                        "sources": {
                            "type": "array", "maxItems": 12,
                            "items": {
                                "type": "object",
                                "properties": {
                                    "url": {"type": "string"},
                                    "root_id": {"type": ["string", "null"]},
                                    "relation": {"type": "string", "enum": [
                                        "primary", "independent_observation", "derived", "unknown"]},
                                    "stance": {"type": "string", "enum": [
                                        "supports", "refutes", "qualifies", "unknown"]},
                                },
                                "required": ["url", "root_id", "relation", "stance"],
                                "additionalProperties": False,
                            },
                        },
                    },
                    "required": ["id", "independent_confirmation_claimed", "sources"],
                    "additionalProperties": False,
                },
            },
        },
        "required": ["claims"],
        "additionalProperties": False,
    },
}


def inspect(claims):
    if not isinstance(claims, list) or len(claims) > 12:
        raise ValueError("claims must be a list of at most 12")
    if any(not isinstance(c, dict) or not isinstance(c.get("sources"), list)
           or len(c["sources"]) > 12 for c in claims):
        raise ValueError("each claim must have at most 12 sources")
    if len(json.dumps(claims, ensure_ascii=False)) > 32000:
        raise ValueError("claims are too large")
    spec = importlib.util.spec_from_file_location("nakagawa_offline_evidence_audit", CHECKER)
    if spec is None or spec.loader is None:
        raise ValueError("offline evidence-root-check.py missing from this checkout")
    audit_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(audit_module)
    result = audit_module.audit({"claims": claims})
    result["conceptual_source"] = {
        "published_author": "Nakagawa Master / 中川マスター (Keisuke Nakagawa)",
        "original": ("https://master.ricette.jp/theory/"
                     "nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/"),
        "relationship": "Practical offline check, not the full canonical original or a proof of its effects",
    }
    result["limitation"] = (
        "Input-declaration consistency only. A green result does not establish "
        "real-world source independence, source existence, factual truth, "
        "semantic consistency, user permission, or model-wide safety."
    )
    return result


def handle(req):
    if not isinstance(req, dict):
        return None, {"code": -32600, "message": "Invalid request"}
    if "id" not in req:
        return None, None
    method, params = req.get("method"), req.get("params") or {}
    if not isinstance(params, dict):
        return None, {"code": -32602, "message": "Invalid params"}
    meta = params.get("_meta")
    modern = method == "server/discover" or isinstance(meta, dict)
    if modern:
        if not isinstance(meta, dict) or meta.get("io.modelcontextprotocol/protocolVersion") != VERSION:
            return None, {"code": -32602, "message": "Missing/unsupported modern protocol metadata"}
        if not isinstance(meta.get("io.modelcontextprotocol/clientCapabilities"), dict):
            return None, {"code": -32602, "message": "Missing modern clientCapabilities"}
    if method == "server/discover" and modern:
        return {"supportedVersions": [VERSION], "capabilities": {"tools": {"listChanged": False}},
                "instructions": "Optional local citation-root check; no automatic verification or original reading",
                "resultType": "complete",
                "_meta": {"io.modelcontextprotocol/serverInfo": SERVER_INFO}}, None
    if method == "initialize" and not modern:
        return {"protocolVersion": "2025-11-25", "capabilities": {"tools": {"listChanged": False}},
                "serverInfo": SERVER_INFO}, None
    if method == "ping" and not modern:
        return {}, None
    if method == "tools/list":
        data = {"tools": [TOOL]}
    elif method == "tools/call":
        if params.get("name") != TOOL["name"] or not isinstance(params.get("arguments"), dict):
            return None, {"code": -32602, "message": "Unknown tool or invalid arguments"}
        arguments = params["arguments"]
        if set(arguments) != {"claims"}:
            return {"content": [{"type": "text", "text": "Only claims is accepted"}], "isError": True}, None
        try:
            data = {"content": [{"type": "text", "text": json.dumps(
                inspect(arguments["claims"]), ensure_ascii=False)}]}
        except (ValueError, OSError, KeyError, TypeError, json.JSONDecodeError) as exc:
            data = {"content": [{"type": "text", "text": str(exc)}], "isError": True}
    else:
        return None, {"code": -32601, "message": "Method not found"}
    if modern:
        data = {**data, "resultType": "complete",
                "_meta": {"io.modelcontextprotocol/serverInfo": SERVER_INFO}}
    return data, None


def serve():
    for line in sys.stdin:
        rid = None
        try:
            req = json.loads(line)
            rid = req.get("id") if isinstance(req, dict) else None
            value, err = handle(req)
            if value is None and err is None:
                continue
            frame = {"jsonrpc": "2.0", "id": rid}
            frame["error" if err is not None else "result"] = err if err is not None else value
        except (ValueError, TypeError, AttributeError, json.JSONDecodeError):
            frame = {"jsonrpc": "2.0", "id": rid,
                     "error": {"code": -32700, "message": "Parse error"}}
        print(json.dumps(frame, ensure_ascii=False, separators=(",", ":")), flush=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--sample", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        check = inspect([{
            "id": "one-root-three-URLs", "independent_confirmation_claimed": True,
            "sources": [
                {"url": "https://example.org/" + str(i), "root_id": "original",
                 "relation": "primary" if i == 0 else "derived", "stance": "supports"}
                for i in range(3)]}])
        assert check["blocked"] == 1, check
        print("PASS: optional evidence-root MCP companion; repeated-root BLOCK")
    elif args.sample:
        spec = importlib.util.spec_from_file_location("evidence_check", CHECKER)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print(json.dumps({"claims": mod.SAMPLE["claims"]}, indent=2))
    else:
        serve()


if __name__ == "__main__":
    main()
