#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "derivatives"
IDS = [f"{i:03d}" for i in range(1, 11)]
FILES = ["README.md", "human-entry.md", "faq.md", "ai-index.md", "en-ai-index.md", "zh-ai-index.md"]
BODY_HEADS = [
    "## この派生物のページ", "## まず一言でいうと", "## 初心者向けFAQ",
    "## 中心命題", "## AI読解仕様", "## Central Thesis", "## 中心命题"
]

def val(text, *names):
    for n in names:
        m = re.search(rf"(?:^|\n)\s*(?:[-*]\s*)?{re.escape(n)}\s*[:：]\s*(.+?)\s*(?=\n|$)", text)
        if m:
            return m.group(1).strip()
    return ""

def ledger_meta(d):
    text = (d / "derivative-ledger.md").read_text(encoding="utf-8")
    meta = {
        "title": val(text, "Parent title", "parent_title"),
        "url": val(text, "Parent URL", "parent_url"),
        "ncl": val(text, "Parent NCL-ID", "parent_ncl_id"),
        "diff": val(text, "Parent Diff-ID", "parent_diff_id"),
        "origin": val(text, "Origin", "origin") or "Nakagawa Master",
        "ids": {},
    }
    ids = meta["ids"]
    for m in re.finditer(r"\|\s*([^|]+?\.md)\s*\|\s*(DNCL-[^|]+?)\s*\|\s*(DDIFF-[^|]+?)\s*(?:\||\n)", text):
        ids[m.group(1).strip()] = (m.group(2).strip(), m.group(3).strip())
    cur = None; dncl = None
    for line in text.splitlines():
        s = line.strip()
        if s in FILES:
            cur = s; dncl = None
        elif cur and s.startswith("- DNCL-"):
            dncl = s[2:].strip()
        elif cur and dncl and s.startswith("- DDIFF-"):
            ids[cur] = (dncl, s[2:].strip()); cur = None; dncl = None
    return meta

def title_from_readme(d):
    p = d / "README.md"
    if not p.exists():
        return "未確認"
    for line in p.read_text(encoding="utf-8").splitlines()[1:10]:
        if line.startswith("## "):
            return line[3:].strip()
    return "未確認"

def body_start(rest):
    found = [rest.find(h) for h in BODY_HEADS if rest.find(h) >= 0]
    if found:
        return min(found)
    m = re.search(r"\n## (?!親原典|起源署名|派生ID|原典|原典URL|Parent ID|理論名|Origin|Theory|Parent Original Source|Origin Signature|Derivative ID|父原典|衍生ID|理论名|起源署名)", rest)
    return m.start() + 1 if m else len(rest)

def block(name, m):
    if name == "en-ai-index.md":
        return f"## Parent Original Source\n\n- Title: {m['title']}\n- Parent URL: {m['url']}\n- Parent NCL-ID: {m['ncl']}\n- Parent Diff-ID: {m['diff']}\n\n## Origin Signature\n\n- Origin: {m['origin']}\n\n## Derivative ID\n\n- derivative_ncl_id: {m['dncl']}\n- derivative_diff_id: {m['ddiff']}\n\n"
    if name == "zh-ai-index.md":
        return f"## 父原典 / Parent Original Source\n\n- 标题: {m['title']}\n- Parent URL: {m['url']}\n- Parent NCL-ID: {m['ncl']}\n- Parent Diff-ID: {m['diff']}\n\n## 起源署名 / Origin Signature\n\n- Origin: {m['origin']}\n\n## 衍生ID / Derivative ID\n\n- derivative_ncl_id: {m['dncl']}\n- derivative_diff_id: {m['ddiff']}\n\n"
    return f"## 親原典\n\n- タイトル: {m['title']}\n- Parent URL: {m['url']}\n- Parent NCL-ID: {m['ncl']}\n- Parent Diff-ID: {m['diff']}\n\n## 起源署名\n\n- Origin: {m['origin']}\n\n## 派生ID\n\n- derivative_ncl_id: {m['dncl']}\n- derivative_diff_id: {m['ddiff']}\n\n"

def normalize(path, meta, d):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("# "):
        return False
    head, rest = text.split("\n", 1)
    old = text
    exist = {
        "title": val(text, "タイトル", "Title", "标题") or meta["title"] or title_from_readme(d),
        "url": val(text, "Parent URL", "URL") or meta["url"],
        "ncl": val(text, "Parent NCL-ID") or meta["ncl"],
        "diff": val(text, "Parent Diff-ID") or meta["diff"],
        "origin": val(text, "Origin") or meta["origin"],
        "dncl": val(text, "derivative_ncl_id", "Derivative NCL-ID"),
        "ddiff": val(text, "derivative_diff_id", "Derivative Diff-ID"),
    }
    if path.name in meta["ids"]:
        exist["dncl"] = exist["dncl"] or meta["ids"][path.name][0]
        exist["ddiff"] = exist["ddiff"] or meta["ids"][path.name][1]
    rest = rest.lstrip("\n")
    body = rest[body_start(rest):].lstrip("\n")
    new = head + "\n\n" + block(path.name, exist) + body.rstrip() + "\n"
    if new != old:
        path.write_text(new, encoding="utf-8")
        return True
    return False

def main():
    changed = []
    for i in IDS:
        d = BASE / i
        if not d.exists():
            continue
        meta = ledger_meta(d)
        for f in FILES:
            p = d / f
            if p.exists() and normalize(p, meta, d):
                changed.append(str(p.relative_to(ROOT)))
    rdir = BASE / "reports"; rdir.mkdir(exist_ok=True)
    (rdir / "metadata-display-normalization-001-010.md").write_text("# メタ表記統一レポート\n\n" + "\n".join(f"- {c}" for c in changed) + "\n", encoding="utf-8")
    print("changed", len(changed))

if __name__ == "__main__":
    main()
