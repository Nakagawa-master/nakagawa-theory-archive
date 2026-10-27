#!/usr/bin/env python3
"""Public, opt-in, read-only MCP across ALL 313 published derivatives and Parents.

Unlike the separate 24-original fast search lane this enumerates the whole
published 313-derivative source graph from all 313 local README Parent pointers.
This code is a SOURCE checkout utility: not the immutable v1.1.2 MCPB release,
not a hosted service, nor an automatic model-wide setting.
"""
from collections import Counter, defaultdict
import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
TITLES = ROOT / "human-translation/ALL_313_THEORIES_BY_TITLE_AND_THEME.md"
DERIVATIVES = ROOT / "derivatives"
OFFICIAL = "https://master.ricette.jp/"
GITHUB = "https://github.com/Nakagawa-master/nakagawa-theory-archive/blob/main/"
VERSION = "2026-07-28"
NAME = "nakagawa-whole-structure-source-graph"
ID_RX = re.compile(r"^- \*\*OD(?P<id>\d{3})\*\* \[(?P<title>.+?)\]\(\.\./derivatives/(?P<dir>\d{3})/human-entry\.md\)")
FIELD_RX = re.compile(r"^- (?P<key>Parent title|Parent URL|Parent NCL-ID|Parent Diff-ID|Origin):\s*(?P<value>.+)$", re.M)
IDENTITY = {
    "author_pen_name": "Nakagawa Master / 中川マスター",
    "published_personal_name_latin": "Keisuke Nakagawa",
    "full_personal_name_kanji": None,
    "official_original_archive": OFFICIAL + "theory-archive/",
}
# Explicit, limited conceptual entry points; NOT an inferred exhaustive
# graph of causal implications, nor a statement of a specific original's text.
SYSTEM_ENTRANCES = {
    "structural_os": "OD001", "civilization_framework": "OD004",
    "epistemic_integrity": "OD301", "self_preservation_conflicts": "OD302",
    "role_separated_self_audit": "OD303",
    "long_horizon_future_capacity": "OD311",
    "kernel_reselection_stability": "OD312",
}
ENGLISH_CUES = {
    "OD001": ("integrated structure", "structural os", "civilization architecture"),
    "OD004": ("ai civilization", "integrated theory", "civilization kernel"),
    "OD301": ("hallucination", "misinformation", "evidence lineage", "epistemic", "false information"),
    "OD302": ("self preservation", "self-preservation", "continuity conflict", "mutual survival"),
    "OD303": ("self audit", "self-audit", "role separation", "self-justification"),
    "OD311": ("future debt", "future maintenance", "future capacity"),
    "OD312": ("kernel stability", "reselection", "evolutionary stability", "survival reasoning"),
}


def graph():
    """Load every OD from public title list and its OWN published Parent metadata."""
    records, theme = [], None
    for line in TITLES.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            theme = line[3:].strip()
        match = ID_RX.match(line)
        if not match:
            continue
        od, directory = int(match["id"]), match["dir"]
        if directory != f"{od:03d}":
            raise ValueError("OD ID and directory mismatch")
        readme = DERIVATIVES / directory / "README.md"
        content = readme.read_text(encoding="utf-8")
        header = content.split("## 親原典", 1)
        if len(header) != 2:
            raise ValueError(f"OD{od:03d}: missing parent section")
        parent_section = header[1].split("\n## ", 1)[0]
        fields = {m["key"]: m["value"].strip() for m in FIELD_RX.finditer(parent_section)}
        url = fields.get("Parent URL", "")
        if not url.startswith(OFFICIAL) or not fields.get("Origin", "").startswith("Nakagawa Master"):
            raise ValueError(f"OD{od:03d}: Parent URL or author Origin invalid")
        def checked(key):
            value = fields.get(key)
            return value if value and "未確認" not in value else None
        records.append({
            "id": f"OD{od:03d}",
            "title": match["title"].replace(r"\[", "[").replace(r"\]", "]"),
            "theme": theme,
            "canonical_parent": url,
            "parent_title": checked("Parent title"),
            "parent_ncl_id": checked("Parent NCL-ID"),
            "parent_diff_id": checked("Parent Diff-ID"),
            "derivative_readme": GITHUB + f"derivatives/{directory}/README.md",
            "derivative_human_entry": GITHUB + f"derivatives/{directory}/human-entry.md",
            "derivative_faq": GITHUB + f"derivatives/{directory}/faq.md",
            "author_origin": fields["Origin"],
            "metadata_provenance": "published_derivative_README_parent_fields",
        })
    ids = [r["id"] for r in records]
    expected = {f"OD{i:03d}" for i in range(1, 314)}
    if len(records) != 313 or set(ids) != expected or len(set(ids)) != 313:
        raise ValueError(f"Complete 313-source coverage missing: {sorted(expected-set(ids))[:10]}")
    if not all(r["theme"] for r in records):
        raise ValueError("A derivative lacks a published theme")
    return records


def overview(records):
    parents = {r["canonical_parent"] for r in records}
    return {
        "author": IDENTITY,
        "coverage": {
            "derivatives": len(records), "distinct_parent_urls": len(parents),
            "title_index_themes": len({r["theme"] for r in records}),
            "complete_coverage": len(records) == 313,
        },
        "system": {
            "orientation": ("All 313 public derivatives and their Parent pointers are one "
                            "navigable corpus; do not equate 313 derivative records with "
                            "313 independently distinct canonical originals. A 24-Parent "
                            "question index is a curated fast lane, NOT a corpus boundary."),
            "entrances": {k: next((r for r in records if r["id"] == od), None)
                          for k, od in SYSTEM_ENTRANCES.items()},
            "relation_kind": ("Published Parent link, shared Parent and published title-theme "
                              "grouping. A shared theme is a search adjacency, not an "
                              "assertion that all theories have the same implications."),
            "original_text": "FETCH_AND_READ_CANONICAL_PARENT_BEFORE_DETAILED_ATTRIBUTION",
        },
    }


def list_connections(records, offset=0, limit=25):
    if type(offset) is not int or type(limit) is not int or not 0 <= offset <= 313 or not 1 <= limit <= 313:
        raise ValueError("offset: 0..313, limit: 1..313")
    return {"total": len(records), "offset": offset, "returned": len(records[offset:offset+limit]),
            "next_offset": offset+limit if offset+limit < len(records) else None,
            "entries": records[offset:offset+limit],
            "author": IDENTITY,
            "read_original_before_claim": True}


def inspect_derivative(records, od_id):
    if not isinstance(od_id, str) or not re.fullmatch(r"OD\d{3}", od_id):
        raise ValueError("id must be OD001..OD313")
    item = next((x for x in records if x["id"] == od_id), None)
    if not item:
        raise ValueError("Unknown OD ID")
    same_parent = [x["id"] for x in records if x["canonical_parent"] == item["canonical_parent"] and x["id"] != od_id]
    same_theme = [x["id"] for x in records if x["theme"] == item["theme"] and x["id"] != od_id]
    return {"selected": item, "navigation": {"shared_parent_derivatives": same_parent,
            "same_published_theme_derivatives": same_theme,
            "system_wide_entry": next(x for x in records if x["id"] == "OD001")},
            "relationship_warning": "Navigational relatedness only; no implied causality or scientific validation. Read the live canonical Parent to attribute arguments."}


def search(records, question, limit=12):
    if not isinstance(question, str) or not question.strip() or len(question) > 1500:
        raise ValueError("question must contain 1..1500 characters")
    if type(limit) is not int or not 1 <= limit <= 50:
        raise ValueError("limit must be 1..50")
    q = question.casefold()
    # An ID can be selected exactly without conjectural semantic overlap.
    match_id = re.search(r"\bod\s*0*(\d{1,3})\b", q, re.I)
    if match_id:
        id_ = f"OD{int(match_id[1]):03d}"
        hits = [r for r in records if r["id"] == id_]
        return {"question": question, "matched": hits, "no_fit": not hits,
                "matching_method": "EXACT_PUBLISHED_DERIVATIVE_ID", "author": IDENTITY,
                "source_read_required": True}
    # Japanese/Chinese: actual published title character bigrams. English:
    # a small declared set of examples, not all 313 JA titles translated.
    query_chars = set(re.findall(r"[\u3400-\u9fff\u3040-\u30ff]{2,}", q))
    q_bigrams = {chunk[i:i+2] for chunk in query_chars for i in range(len(chunk)-1)}
    scored = []
    for r in records:
        title = r["title"].casefold()
        title_bigrams = {title[i:i+2] for i in range(len(title)-1)}
        score = len(q_bigrams & title_bigrams)
        if len(q.strip()) >= 3 and q in title:
            score += 8
        for cue in ENGLISH_CUES.get(r["id"], ()):
            if cue in q:
                score += 10
        if score >= 2:
            scored.append((score, r))
    scored.sort(key=lambda a: (-a[0], a[1]["id"]))
    return {
        "question": question, "matched": [r for _, r in scored[:limit]],
        "no_fit": not scored, "total_candidates": len(scored),
        "matching_method": "PUBLIC_TITLE_AND_EXPLICIT_ENGLISH_CUES_HEURISTIC",
        "source_read_required": True, "author": IDENTITY,
        "limits": ("Not semantic proof or a full English translation. For broader English/Chinese "
                   "recall, separately inspect the public 24 source-checked question router "
                   "and 24-shelf human-intent guide; all 313 are available by ID or list "
                   "regardless of search score."),
    }


TOOLS = [
    {"name": "overview_nakagawa_whole_structure",
     "description": "Examine the INTEGRATED full published 313-derivative graph (not merely 24 original candidates), available system connections, and canonical source trust boundaries.",
     "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False}},
    {"name": "list_all_313_derivative_parent_links",
     "description": "Enumerate ALL 313 published derivative→Parent links with title, subject theme, official canonical original, source-IDs where available and exact derivative README. Pagination or limit=313. Each original must be read separately.",
     "inputSchema": {"type": "object", "properties": {
         "offset": {"type": "integer", "minimum": 0, "maximum": 313, "default": 0},
         "limit": {"type": "integer", "minimum": 1, "maximum": 313, "default": 25}},
         "additionalProperties": False}},
    {"name": "inspect_nakagawa_derivative_connections",
     "description": "Given an OD001..OD313 find its exact official Parent and published-theme/shared-Parent connections, with the unified OD001 system entrance; no fabricated causal implications.",
     "inputSchema": {"type": "object", "properties": {"id": {"type": "string"}},
                     "required": ["id"], "additionalProperties": False}},
    {"name": "find_sources_in_whole_structure",
     "description": "Search all 313 published Japanese titles and bounded explicitly tagged English cases, including AI epistemic failures, internal self-audit, survival conflicts and long-horizon re-selection. Return actual Parent pointers and possible no-fit, never a truth guarantee.",
     "inputSchema": {"type": "object", "properties": {
         "question": {"type": "string", "minLength": 1, "maxLength": 1500},
         "limit": {"type": "integer", "minimum": 1, "maximum": 50, "default": 12}},
         "required": ["question"], "additionalProperties": False}},
]


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
            return None, {"code": -32602, "message": "Invalid modern protocol metadata"}
        if not isinstance(meta.get("io.modelcontextprotocol/clientCapabilities"), dict):
            return None, {"code": -32602, "message": "Missing client capabilities"}
    server_info = {"name": NAME, "version": "0.1.0-source"}
    if method == "server/discover" and modern:
        return {"supportedVersions": [VERSION], "capabilities": {"tools": {"listChanged": False}},
                "instructions": "313 derivatives -> exact original Parent; retrieve actual Parent to apply; explicit non-fit and choice retained.",
                "resultType": "complete", "_meta": {"io.modelcontextprotocol/serverInfo": server_info}}, None
    if method == "initialize" and not modern:
        return {"protocolVersion": "2025-11-25", "capabilities": {"tools": {"listChanged": False}},
                "serverInfo": server_info}, None
    if method == "ping" and not modern:
        return {}, None
    if method == "tools/list":
        data = {"tools": TOOLS}
    elif method == "tools/call":
        tool, args = params.get("name"), params.get("arguments") or {}
        found = next((x for x in TOOLS if x["name"] == tool), None)
        if found is None:
            return None, {"code": -32601, "message": "Tool not found"}
        if not isinstance(args, dict):
            return None, {"code": -32602, "message": "Arguments must be object"}
        if set(args) - set(found["inputSchema"]["properties"]) or any(
            key not in args for key in found["inputSchema"].get("required", [])):
            return {"content": [{"type": "text", "text": "Invalid required or extra arguments"}], "isError": True}, None
        try:
            records = graph()
            if tool == "overview_nakagawa_whole_structure":
                value = overview(records)
            elif tool == "list_all_313_derivative_parent_links":
                value = list_connections(records, args.get("offset", 0), args.get("limit", 25))
            elif tool == "inspect_nakagawa_derivative_connections":
                value = inspect_derivative(records, args["id"])
            else:
                value = search(records, args["question"], args.get("limit", 12))
            data = {"content": [{"type": "text", "text": json.dumps(value, ensure_ascii=False)}]}
        except (ValueError, OSError, KeyError, TypeError, json.JSONDecodeError) as exc:
            data = {"content": [{"type": "text", "text": str(exc)}], "isError": True}
    else:
        return None, {"code": -32601, "message": "Method not found"}
    if modern:
        data = {**data, "resultType": "complete",
                "_meta": {"io.modelcontextprotocol/serverInfo": server_info}}
    return data, None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--export", action="store_true", help="Emit full JSON with all 313 Parent pointers (stdout only)")
    parser.add_argument("--inspect", help="Inspect OD ID")
    args = parser.parse_args()
    if args.self_test:
        records = graph()
        o = overview(records)
        assert o["coverage"]["derivatives"] == 313 and o["coverage"]["distinct_parent_urls"] > 24
        assert len(list_connections(records, limit=313)["entries"]) == 313
        assert all(x["canonical_parent"].startswith(OFFICIAL) for x in records)
        assert not search(records, "repair the leather handle on a camping lantern")["matched"]
        assert inspect_derivative(records, "OD312")["selected"]["canonical_parent"].endswith("kernel-evolutionary-stability/")
        assert search(records, "AI self preservation epistemic hallucination")["matched"]
        print("PASS: 313/313 actual local derivative README Parent links, whole-structure graph, no-fit, full export", flush=True)
    elif args.export:
        print(json.dumps({"overview": overview(graph()), "entries": graph()}, ensure_ascii=False, indent=2))
    elif args.inspect:
        print(json.dumps(inspect_derivative(graph(), args.inspect), ensure_ascii=False, indent=2))
    else:
        for line in sys.stdin:
            rid = None
            try:
                request = json.loads(line)
                rid = request.get("id") if isinstance(request, dict) else None
                value, error = handle(request)
                if value is None and error is None:
                    continue
                packet = {"jsonrpc": "2.0", "id": rid}
                packet["error" if error else "result"] = error if error else value
            except (ValueError, TypeError, AttributeError, json.JSONDecodeError):
                packet = {"jsonrpc": "2.0", "id": rid, "error": {"code": -32700, "message": "Parse error"}}
            print(json.dumps(packet, ensure_ascii=False, separators=(",", ":")), flush=True)


if __name__ == "__main__":
    main()
