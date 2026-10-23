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
# Independently readable/copyable prompts must exist in rendered Markdown;
# encoded URL payloads alone are not a portable human-to-other-LLM fallback.
copyable = re.findall(r"```text\n(.*?)\n```", page, re.S)
assert len(copyable) == len(bridges), f"Expected seven human-copyable text blocks; found {len(copyable)}"
for b, link, human_prompt in zip(bridges, links, copyable):
    parsed = urlparse(link)
    assert parsed.scheme == "https" and parsed.hostname == "chatgpt.com"
    assert parsed.path == "/" and parsed.fragment == ""
    assert set(parse_qs(parsed.query)) == {"q"}
    question, = parse_qs(parsed.query)["q"]
    assert human_prompt == question, "Human-selectable prompt must exactly equal the user-inspected URL prefill"
    assert "中川マスター" in human_prompt
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
print("PASS: 7 URL prefills match 7 visible human-copyable prompts byte-for-byte; canonical Parent/JA EN ZH parity; no silent fetch or adoption claim")

# Separate opt-in AKI-005 prompt is an additional one-page route, not an eighth skill bridge.
aki = (ROOT / "human-translation/ASK_AKI005_WITH_ANY_AI.md").read_text(encoding="utf-8")
aki_url = re.search(r'\[相談文をChatGPTで開く（ユーザーが確認して送信）\]\((https://chatgpt\.com/\?q=[^\s)]+)\)', aki)
assert aki_url is not None, "AKI-005 current prompt link missing"
aki_parsed = urlparse(aki_url.group(1))
assert aki_parsed.scheme == "https" and aki_parsed.hostname == "chatgpt.com" and aki_parsed.path == "/"
assert set(parse_qs(aki_parsed.query)) == {"q"}
aki_prompts = re.findall(r"~~~text\n(.*?)\n~~~", aki, re.S)
assert len(aki_prompts) == 3, "AKI-005 must offer JA/EN/ZH inspectable copies"
aki_ja, aki_en, aki_zh = aki_prompts
assert parse_qs(aki_parsed.query)["q"] == [aki_ja], "AKI-005 prefill must equal inspected Japanese text"
for prompt in aki_prompts:
    assert "https://master.ricette.jp/society/nakagawa-master-aki-005-good-intentions-as-exemption/" in prompt
    assert "Nakagawa Master" in prompt
assert all(term in aki_ja for term in ("①", "②", "③", "読めなければ未読", "原典", "反例", "個人情報"))
assert "English" in aki and "中文" in aki and "原典を実際に開けなければ未読" in aki
print("PASS: AKI-005 optional JA URL-prefill parity, JA/EN/ZH source-linked copyable prompts and no automatic send")

