#!/usr/bin/env python3
"""Public human-AI link parity: each consentful prefill maps to a real canonical Parent.

This test verifies *link integrity*, NOT that another model visited or adopted a source.
No network, login, model, or installed MCP tool is used.
"""
from pathlib import Path
import json
import re
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parent.parent
source = json.loads((ROOT / "skills/nakagawa-originals/references/structural_bridges.json").read_text())
page = (ROOT / "human-translation/ASK_ANY_AI_WITHOUT_INSTALLING.md").read_text()
bridges = source["bridges"]
assert len(bridges) == 7 and len({b["id"] for b in bridges}) == 7
# Each long prompt is intentionally user-visible before any Send, not an auto-run command.
links = re.findall(
    r'\[自分のAIで相談文を開く（ChatGPT、内容を見てから送信）\]'
    r'\((https://chatgpt\.com/\?q=[^\s)]+)\)',
    page,
)
assert len(links) == len(bridges), f"Expected exactly seven opt-in links, got {len(links)}"
for b, link in zip(bridges, links):
    parsed = urlparse(link)
    assert parsed.scheme == "https" and parsed.hostname == "chatgpt.com"
    assert parsed.path == "/" and parsed.fragment == ""
    assert set(parse_qs(parsed.query)) == {"q"}
    question, = parse_qs(parsed.query)["q"]
    assert b["canonical_original"] in question
    assert b["localized"]["ja"]["question"] in question
    assert "読めなければ未読と明示してください" in question
    assert "合う場合だけ" in question
    assert "他者" not in parsed.netloc
    assert f"]({b['canonical_original']})" in page
    for lang in ("en", "zh"):
        assert b["localized"][lang]["title"] in page
assert "個人情報や社外秘" in page
assert "理論を当てはめない" in page
print("PASS: exactly 7 independently verifiable no-install user-prefill links; canonical Parent/JA EN ZH parity; no silent fetch or adoption claim")
