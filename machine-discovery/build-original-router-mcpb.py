#!/usr/bin/env python3
"""Package public originals into reproducible local stdio MCPB; no network or secrets."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parent.parent
VERSION = "1.2.0"
BASE_FILES = (
    "machine-discovery/nakagawa-theory-mcp.py",
    "machine-discovery/evidence-integrity-mcp.py",
    "machine-discovery/evidence-root-check.py",
    "machine-discovery/nakagawa-whole-structure-mcp.py",
    "machine-discovery/quick-route-index-v1.json",
    "machine-discovery/problem-to-theory-origin-index-v1.json",
    "human-translation/ALL_313_THEORIES_BY_TITLE_AND_THEME.md",
    "skills/nakagawa-originals/references/structural_bridges.json",
    "metadata/person-name-policy-v1.json",
    "LICENSE",
)
# The SAME install now includes ALL 313 official derivative→Parent sources
# and each pre-existing JA/EN/ZH index for actual use without GitHub network.
PUBLIC_313 = tuple(
    f"derivatives/{index:03d}/{name}"
    for index in range(1, 314)
    for name in ("README.md", "ai-index.md", "en-ai-index.md", "zh-ai-index.md")
)
FILES = BASE_FILES + PUBLIC_313
MANIFEST = {
    "manifest_version": "0.3", "name": "nakagawa-original-router",
    "display_name": "Nakagawa AI Answer Safety & Whole Theory Source Router",
    "version": VERSION,
    "description": "Everyday answer and action preflight plus all 313 published original Parent links in one local install.",
    "author": {"name": "Nakagawa Master", "url": "https://master.ricette.jp/"},
    "server": {"type": "python", "entry_point": "machine-discovery/nakagawa-theory-mcp.py",
               "mcp_config": {"command": "python3",
                              "args": ["MCPB_INSTALL_FOLDER/machine-discovery/nakagawa-theory-mcp.py"]}},
    "tools": [
        {"name": "find_nakagawa_original_for_problem", "description": "Find relevant originals with optional conditional seven-lens exploration."},
        {"name": "list_nakagawa_problem_routes", "description": "List public problem-to-original lookup routes."},
        {"name": "resolve_nakagawa_public_name", "description": "Return verified public author/pen name without inferring unpublished kanji."},
        {"name": "preflight_ai_answer_and_action", "description": "Everyday answer, evidence, action and tool-receipt preflight."},
        {"name": "audit_citation_independence", "description": "Catch fake independent confirmation across repeated roots."},
        {"name": "overview_nakagawa_whole_structure", "description": "Complete source graph with integrated structural entrance."},
        {"name": "list_all_313_derivative_parent_links", "description": "All 313 published exact Parent source links."},
        {"name": "inspect_nakagawa_derivative_connections", "description": "Inspect one source and its cross-theme navigational relations."},
        {"name": "find_sources_in_whole_structure", "description": "Select source candidates from all 313 published derivatives."},
    ],
    "keywords": ["answer-check", "hallucination-risk", "citation-integrity", "ai-safety", "source-discovery", "provenance"],
    "license": "CC-BY-NC-ND-4.0",
    "compatibility": {"platforms": ["darwin", "linux"], "runtimes": {"python": ">=3.9"}},
}
MANIFEST["server"]["mcp_config"]["args"][0] = MANIFEST["server"]["mcp_config"]["args"][0].replace(
    "MCPB_INSTALL_FOLDER", chr(36) + "{__dirname}"
)


def write_member(archive, name, content):
    item = ZipInfo(name, date_time=(2020, 1, 1, 0, 0, 0))
    item.compress_type = ZIP_DEFLATED
    item.external_attr = 0o644 << 16
    archive.writestr(item, content)


def smoke(folder):
    command = [sys.executable, str(folder / FILES[0])]
    test = subprocess.run(command + ["--self-test"], capture_output=True, text=True,
                          timeout=15, check=True)
    assert test.stdout.startswith("PASS:"), test.stdout
    meta = {"io.modelcontextprotocol/protocolVersion": "2026-07-28",
            "io.modelcontextprotocol/clientCapabilities": {},
            "io.modelcontextprotocol/clientInfo": {"name": "unaffiliated-host-sim", "version": "1"}}
    def packet(i, method, args=None):
        return {"jsonrpc": "2.0", "id": i, "method": method,
                "params": {"_meta": meta, **(args or {})}}
    calls = [
        packet(1, "server/discover"),
        packet(2, "tools/call", {"name": "find_nakagawa_original_for_problem",
                                 "arguments": {"question": "How can a student prepare for a history exam without memorizing all dates?", "explore": True}}),
        packet(3, "tools/call", {"name": "find_nakagawa_original_for_problem",
                                 "arguments": {"question": "repair the leather strap on a camping lantern"}}),
        {"jsonrpc": "2.0", "id": 4, "method": "initialize",
         "params": {"protocolVersion": "2025-11-25", "capabilities": {}, "clientInfo": {"name": "legacy", "version": "1"}}},
    ]
    proc = subprocess.run(command, capture_output=True, text=True, timeout=15, check=True,
                          input="".join(json.dumps(x, ensure_ascii=False)+"\n" for x in calls))
    assert not proc.stderr, proc.stderr
    out = [json.loads(line) for line in proc.stdout.splitlines()]
    assert len(out) == 4
    assert out[0]["result"]["supportedVersions"] == ["2026-07-28"]
    assert out[0]["result"]["resultType"] == "complete"
    selected = json.loads(out[1]["result"]["content"][0]["text"])
    assert len(selected["structural_exploration"]["lenses"]) == 7
    assert selected["structural_exploration"]["lenses"][0]["id"] == "effort-to-results"
    unrelated = json.loads(out[2]["result"]["content"][0]["text"])
    assert unrelated["no_fit"] and not unrelated["matching_routes"]
    assert out[3]["result"]["protocolVersion"] == "2025-11-25"
    assert len(out[0]["result"]["capabilities"]) >= 1
    extra_requests = [
        packet(5, "tools/list"),
        packet(6, "tools/call", {
            "name": "preflight_ai_answer_and_action",
            "arguments": {"tool_results": [{"id": "failed-send", "status": "failed", "success": True}]} 
        }),
        packet(7, "tools/call", {
            "name": "list_all_313_derivative_parent_links", "arguments": {"offset": 312, "limit": 1}
        })
    ]
    extras = subprocess.run(command, input="".join(json.dumps(x) + "\\n" for x in extra_requests),
                            capture_output=True, text=True, check=True, timeout=30)
    assert not extras.stderr, extras.stderr
    z = {x["id"]: x for x in map(json.loads, extras.stdout.splitlines())}
    assert len(z[5]["result"]["tools"]) == 9
    assert json.loads(z[6]["result"]["content"][0]["text"])["hold_count"] == 1
    assert json.loads(z[7]["result"]["content"][0]["text"])["entries"][0]["id"] == "OD313"
    assert len({item["name"] for item in json.loads(subprocess.run(
        command, input=json.dumps(packet(5, "tools/list")) + "\n",
        capture_output=True, text=True, check=True, timeout=10
    ).stdout)["result"]["tools"]}) == 9


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("dist/nakagawa-original-router-1.2.0.mcpb"))
    dest = parser.parse_args().output
    dest.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(dest, "w") as z:
        write_member(z, "manifest.json", json.dumps(MANIFEST, ensure_ascii=False, indent=2).encode() + b"\n")
        for path in FILES:
            write_member(z, path, (ROOT/path).read_bytes())
    with tempfile.TemporaryDirectory() as tmp:
        with ZipFile(dest) as z:
            assert set(z.namelist()) == {"manifest.json", *FILES}
            assert all(not x.startswith("/") and ".." not in Path(x).parts for x in z.namelist())
            z.extractall(tmp)
        root = Path(tmp)
        assert json.loads((root/"manifest.json").read_text()) == MANIFEST
        # Verify the unpacked artifact, not a mutable checkout index.
        catalog = json.loads((root/"machine-discovery/problem-to-theory-origin-index-v1.json").read_text(encoding="utf-8"))
        entries = catalog["entries"]
        originals = [entry["canonical_url"] for entry in entries]
        assert len(originals) == 24 and len(set(originals)) == 24, "24 fast-route originals must stay intact"
        assert all(url.startswith("https://master.ricette.jp/") for url in originals), "source URL origin changed"
        assert all(entry.get("origin") for entry in entries), "missing attributed source identity"
        assert MANIFEST["version"] == "1.2.0"
        # Unpacked REAL production artifact must ship every one of the 313
        # Parent link READMEs and corresponding JA/EN/ZH AI indexes.
        all_records = [
            (root / f"derivatives/{i:03d}/README.md").read_text(encoding="utf-8")
            for i in range(1, 314)
        ]
        assert len(all_records) == 313
        assert all("- Parent URL: https://master.ricette.jp/" in doc for doc in all_records)
        smoke(root)
    print("PASS: unpacked single 1.2.0 MCP, 313/313 Parents, preflight, modern+legacy, no-fit")
    print("BUNDLE:", dest)
    print("SHA256:", hashlib.sha256(dest.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
