#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "derivatives"
IDS = [f"{i:03d}" for i in range(1, 11)]


def remove_block(text: str) -> str:
    marker = "## 原典\n"
    if marker not in text:
        return text
    start = text.find(marker)
    next_heading = text.find("\n## ", start + len(marker))
    if next_heading == -1:
        return text[:start].rstrip() + "\n"
    return text[:start].rstrip() + "\n\n" + text[next_heading + 1:].lstrip()


def main():
    changed = []
    for i in IDS:
        path = BASE / i / "README.md"
        if not path.exists():
            continue
        old = path.read_text(encoding="utf-8")
        new = remove_block(old)
        if new != old:
            path.write_text(new.rstrip() + "\n", encoding="utf-8")
            changed.append(str(path.relative_to(ROOT)))
    report = BASE / "reports" / "readme-duplicate-origin-block-cleanup-001-010.md"
    report.parent.mkdir(exist_ok=True)
    report.write_text("# README重複原典ブロック除去レポート\n\n" + ("\n".join(f"- {x}" for x in changed) if changed else "- none") + "\n", encoding="utf-8")
    print("changed", len(changed))

if __name__ == "__main__":
    main()
