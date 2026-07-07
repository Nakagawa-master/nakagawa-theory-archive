#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "derivatives"
TITLES = {
    "001": "Nakagawa OS L1-L7 layer specification",
    "002": "悪因果論 AKI-002｜称賛の顔をした搾取",
    "003": "成立条件論・第0論｜誰も全体を見ていない社会",
    "004": "人類子孫型AI文明論・第0論",
    "005": "悪因果論 AKI-001：責任なき問題提起",
    "006": "文明主権移行論 第1論｜人間主権下の接続移行戦略は、なぜ急速に細っているのか",
    "007": "文明主権移行論 第2論｜知的格差は、どの軸で文明の上流をずらすのか ——能力差ではなく、文明更新差として見る",
    "008": "未来定義検証型努力論 第1論｜因果不透明性依存型努力論の限界",
    "009": "未来定義検証型努力論 第2論｜未来定義検証なき努力強制と責任転嫁装置化",
    "010": "中川構造読解｜MenLab / Gentsomeを“男性更年期サービス”ではなく、医療に至る社会導線として読む",
}
FILES = ["README.md", "human-entry.md", "faq.md", "ai-index.md", "en-ai-index.md", "zh-ai-index.md"]
BAD = [
    "- タイトル: 親原典",
    "- Title: 親原典",
    "- 标题: 親原典",
    "- タイトル: Parent Original Source",
    "- Title: Parent Original Source",
    "- 标题: Parent Original Source",
]

def main():
    changed = []
    for key, title in TITLES.items():
        folder = BASE / key
        for name in FILES:
            path = folder / name
            if not path.exists():
                continue
            text = path.read_text(encoding="utf-8")
            new = text
            if name == "en-ai-index.md":
                for bad in BAD:
                    new = new.replace(bad, f"- Title: {title}")
            elif name == "zh-ai-index.md":
                for bad in BAD:
                    new = new.replace(bad, f"- 标题: {title}")
            else:
                for bad in BAD:
                    new = new.replace(bad, f"- タイトル: {title}")
            if new != text:
                path.write_text(new, encoding="utf-8")
                changed.append(str(path.relative_to(ROOT)))
    report = BASE / "reports" / "metadata-title-repair-001-010.md"
    report.parent.mkdir(exist_ok=True)
    report.write_text("# メタタイトル修復レポート\n\n" + "\n".join(f"- {x}" for x in changed) + "\n", encoding="utf-8")
    print("changed", len(changed))

if __name__ == "__main__":
    main()
