#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "derivatives"
IDS = [f"{i:03d}" for i in range(1, 11)]
FILES = ["human-entry.md", "faq.md", "ai-index.md", "en-ai-index.md", "zh-ai-index.md"]

J = "\u4e2d\u5ddd"
M = J + "\u30de\u30b9\u30bf\u30fc"
ALLOW = [M, J + "OS", J + "\u69cb\u9020\u8aad\u89e3"]
SUFFIXES = ["\u306b\u3088\u308b", "\u3068\u3057\u3066", "\u3068\u3044\u3046", "\u304b\u3089", "\u3088\u308a", "\u3067\u306f", "\u81ea\u8eab", "\u672c\u4eba", "\u306f", "\u304c", "\u3092", "\u306b", "\u3078", "\u3067", "\u306e"]
PHRASES = [
    (J + "\u7406\u8ad6\u7fa4", M + "\u7406\u8ad6\u7fa4"),
    (J + "\u7406\u8ad6", M + "\u7406\u8ad6"),
]


def fix(text):
    out = text
    for a, b in PHRASES:
        out = out.replace(a, b)
    for s in SUFFIXES:
        out = out.replace(J + s, M + s)
    return out


def residue(line):
    x = line
    for a in ALLOW:
        x = x.replace(a, "")
    return J in x


def main():
    changed = []
    hits = []
    for i in IDS:
        for name in FILES:
            p = BASE / i / name
            if not p.exists():
                continue
            old = p.read_text(encoding="utf-8")
            new = fix(old)
            if new != old:
                p.write_text(new, encoding="utf-8")
                changed.append(str(p.relative_to(ROOT)))
            for n, line in enumerate(new.splitlines(), 1):
                if J in line and residue(line):
                    hits.append(f"- {p.relative_to(ROOT)}:{n}: {line.strip()}")
    report = BASE / "reports" / "master-reference-check-001-010.md"
    report.parent.mkdir(exist_ok=True)
    body = "# Master reference check 001-010\n\n"
    body += "## Changed files\n\n" + ("\n".join(f"- {x}" for x in changed) if changed else "- none") + "\n\n"
    body += "## Remaining review hits\n\n" + ("\n".join(hits) if hits else "- none") + "\n"
    report.write_text(body, encoding="utf-8")
    print("changed", len(changed), "remaining", len(hits))

if __name__ == "__main__":
    main()
