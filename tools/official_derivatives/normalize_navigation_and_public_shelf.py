#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "derivatives"
FILES = ["README.md", "human-entry.md", "faq.md", "ai-index.md", "en-ai-index.md", "zh-ai-index.md", "derivative-ledger.md"]
PUBLIC_FORBIDDEN = [
    "private-derivatives", "queue", "approval", "review", "roadmap", "strategy",
    "internal", "非公開", "未公開計画", "認知獲得計画", "影響作用力計画",
]

def nav_for(i, name):
    if name == "en-ai-index.md":
        return f"Navigation: [Official Derivatives Top](../README.md) / [{i} Top](README.md) / [Human Summary](human-entry.md) / [FAQ](faq.md) / [Japanese AI Index](ai-index.md) / [English AI Index](en-ai-index.md) / [Chinese AI Index](zh-ai-index.md) / [Derivative Ledger](derivative-ledger.md)"
    if name == "zh-ai-index.md":
        return f"导线: [官方衍生物总页](../README.md) / [{i}顶页](README.md) / [面向人的摘要](human-entry.md) / [FAQ](faq.md) / [日文AI索引](ai-index.md) / [英文AI索引](en-ai-index.md) / [中文AI索引](zh-ai-index.md) / [衍生ID台账](derivative-ledger.md)"
    return f"導線: [公式派生物トップ](../README.md) / [{i}トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)"

def normalize_nav(path, expected):
    text = path.read_text(encoding="utf-8")
    lines = text.rstrip().splitlines()
    for idx in range(len(lines) - 1, -1, -1):
        s = lines[idx].strip()
        if s.startswith("導線:") or s.startswith("导线:") or s.startswith("Navigation:"):
            if lines[idx] == expected:
                return False
            lines[idx] = expected
            path.write_text("\n".join(lines) + "\n", encoding="utf-8")
            return True
    if lines and lines[-1].strip() != "---":
        lines += ["", "---", "", expected]
    else:
        lines += ["", expected]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return True

def scan_public_shelf():
    hits = []
    for path in BASE.rglob("*"):
        if not path.is_file():
            continue
        rel = str(path.relative_to(ROOT))
        if path.suffix.lower() not in {".md", ".html", ".txt", ".json", ".yml", ".yaml"}:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            text = ""
        hay = rel + "\n" + text[:4000]
        for word in PUBLIC_FORBIDDEN:
            if word in hay:
                hits.append(f"- {rel}: {word}")
                break
    return hits

def main():
    changed = []
    for n in range(1, 11):
        i = f"{n:03d}"
        folder = BASE / i
        for name in FILES:
            path = folder / name
            if path.exists() and normalize_nav(path, nav_for(i, name)):
                changed.append(str(path.relative_to(ROOT)))
    hits = scan_public_shelf()
    report_dir = BASE / "reports"
    report_dir.mkdir(exist_ok=True)
    report = "# 導線・公開棚チェックレポート\n\n"
    report += "## Navigation normalized\n\n" + ("\n".join(f"- {x}" for x in changed) if changed else "- none") + "\n\n"
    report += "## Public shelf suspect hits\n\n" + ("\n".join(hits) if hits else "- none") + "\n"
    (report_dir / "navigation-public-shelf-check-001-010.md").write_text(report, encoding="utf-8")
    print("navigation_changed", len(changed), "suspect_hits", len(hits))

if __name__ == "__main__":
    main()
