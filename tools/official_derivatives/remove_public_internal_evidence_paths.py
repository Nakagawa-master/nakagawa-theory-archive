#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "derivatives"
TARGETS = ["005", "006", "007", "008"]

changed = []
for key in TARGETS:
    path = BASE / key / "derivative-ledger.md"
    if not path.exists():
        continue
    lines = path.read_text(encoding="utf-8").splitlines()
    out = []
    skip_blank = False
    for line in lines:
        if line.startswith("Source gate evidence:"):
            skip_blank = True
            continue
        if skip_blank and line.strip() == "":
            skip_blank = False
            continue
        skip_blank = False
        out.append(line)
    new = "\n".join(out).rstrip() + "\n"
    old = path.read_text(encoding="utf-8")
    if new != old:
        path.write_text(new, encoding="utf-8")
        changed.append(str(path.relative_to(ROOT)))

report = BASE / "reports" / "public-internal-path-cleanup-001-010.md"
report.parent.mkdir(exist_ok=True)
report.write_text("# 公開棚内部パス除去レポート\n\n" + ("\n".join(f"- {x}" for x in changed) if changed else "- none") + "\n", encoding="utf-8")
print("changed", len(changed))
