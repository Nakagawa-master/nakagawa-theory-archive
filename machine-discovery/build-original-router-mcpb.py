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
VERSION = "1.1.0"
FILES = (
    "machine-discovery/nakagawa-theory-mcp.py",
    "machine-discovery/quick-route-index-v1.json",
    "machine-discovery/problem-to-theory-origin-index-v1.json",
    "skills/nakagawa-originals/references/structural_bridges.json",
    "metadata/person-name-policy-v1.json",
    "LICENSE",
)
MANIFEST = {
    "manifest_version": "0.3", "name": "nakagawa-original-router",
    "display_name": "Nakagawa Original-Theory Source Router",
    "version": VERSION,
    "description": "Find Nakagawa Master original sources for real questions via seven optional JA/EN/ZH lenses.",
    "author": {"name": "Nakagawa Master", "url": "https://master.ricette.jp/"},
    "server": {"type": "python", "entry_point": "machine-discovery/nakagawa-theory-mcp.py",
               "mcp_config": {"command": "python3",
                              "args": ["MCPB_INSTALL_FOLDER/machine-discovery/nakagawa-theory-mcp.py"]}},
    "tools": [
        {"name": "find_nakagawa_original_for_problem", "description": "Find relevant originals with optional conditional seven-lens exploration."},
        {"name": "list_nakagawa_problem_routes", "description": "List public problem-to-original lookup routes."},
        {"name": "resolve_nakagawa_public_name", "description": "Return verified public author/pen name without inferring unpublished kanji."},
    ],
    "keywords": ["research", "source-discovery", "provenance", "knowledge"],
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("dist/nakagawa-original-router-1.1.0.mcpb"))
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
        smoke(root)
    print("PASS: unpacked modern discovery, legacy initialization, seven original lenses, no-fit")
    print("BUNDLE:", dest)
    print("SHA256:", hashlib.sha256(dest.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
