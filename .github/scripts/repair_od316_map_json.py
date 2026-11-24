from __future__ import annotations

import json
import subprocess
from pathlib import Path

MAP = Path("derivatives/official-derivatives-map.json")
ENTRY_316 = {
    "number": "316",
    "ncl_id": "NCL-α-20261124-ca981a",
    "origin_slug": "nakagawa-master-human-descendant-ai-civilization-theory-22-human-transformation-absence-civilizational-succession",
    "title": "人類子孫型AI文明論・第22論｜人類変質・不在条件下の文明継承論⸻起源文明の常時承認なしに歴史と実効的な非支配・訂正を引き継げるか",
    "derivative_dir": "derivatives/316",
    "status": "active",
    "canonical_parent_url": "https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-22-human-transformation-absence-civilizational-succession/",
}

revisions = subprocess.check_output(
    ["git", "rev-list", "HEAD", "--", str(MAP)], text=True
).splitlines()

baseline = None
for revision in revisions:
    try:
        raw = subprocess.check_output(
            ["git", "show", f"{revision}:{MAP.as_posix()}"], text=True
        )
        candidate = json.loads(raw)
    except (subprocess.CalledProcessError, json.JSONDecodeError):
        continue
    entries = candidate.get("entries", [])
    if len(entries) == 315 and str(entries[-1].get("number")) == "315":
        baseline = candidate
        break

if baseline is None:
    raise SystemExit("VALID_OD315_MAP_BASELINE_NOT_FOUND")

baseline["version"] = "2.3.20-od316-json-repaired"
baseline["updated_jst"] = "2026-11-24"
baseline["entries"].append(ENTRY_316)
MAP.write_text(
    json.dumps(baseline, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
)

subprocess.run(["git", "config", "user.name", "Nakagawa-master"], check=True)
subprocess.run(["git", "config", "user.email", "karyu.owner@gmail.com"], check=True)
subprocess.run(["git", "add", str(MAP)], check=True)
subprocess.run(
    ["git", "commit", "-m", "Repair canonical official derivative map JSON through OD316"],
    check=True,
)
subprocess.run(["git", "push", "origin", "HEAD:main"], check=True)
print("PUBLIC_OD316_MAP_JSON_REPAIRED entries=316")
