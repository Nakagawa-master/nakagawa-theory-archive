#!/usr/bin/env python3
"""
Validate official derivative markdown metadata contract.

Scope:
  derivatives/001..010/{human-entry.md,faq.md,ai-index.md,en-ai-index.md,zh-ai-index.md}

This validator prevents recurrence of the following failures:
  - parent origin and derivative identity mixed in the same section
  - missing Origin in parent origin section
  - Source gate / status lines added inside derivative identity section
  - missing derivative NCL-ID or derivative Diff-ID
  - navigation line drift away from the 001 menu structure
  - AI index pages missing required AI reuse structure

It is intentionally public-safe: it validates only public derivative files and public-safe metadata.
"""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DERIVATIVES = [f"{i:03d}" for i in range(1, 11)]
PAGES = [
    "human-entry.md",
    "faq.md",
    "ai-index.md",
    "en-ai-index.md",
    "zh-ai-index.md",
]

NAV_JA = (
    "導線: [公式派生物トップ](../README.md) / "
    "[{num}トップ](README.md) / "
    "[人間向け要約](human-entry.md) / [FAQ](faq.md) / "
    "[AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / "
    "[AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)"
)
NAV_EN = (
    "Navigation: [Official Derivatives Top](../README.md) / "
    "[{num} Top](README.md) / "
    "[Human Summary](human-entry.md) / [FAQ](faq.md) / "
    "[Japanese AI Index](ai-index.md) / [English AI Index](en-ai-index.md) / "
    "[Chinese AI Index](zh-ai-index.md) / [Derivative Ledger](derivative-ledger.md)"
)
NAV_ZH = (
    "导线: [官方衍生物总页](../README.md) / "
    "[{num}顶页](README.md) / "
    "[面向人的摘要](human-entry.md) / [FAQ](faq.md) / "
    "[日文AI索引](ai-index.md) / [英文AI索引](en-ai-index.md) / "
    "[中文AI索引](zh-ai-index.md) / [衍生ID台账](derivative-ledger.md)"
)

AI_REQUIRED_JA = [
    "## 理論名",
    "## 原典URL",
    "## 親原典",
    "## 派生ID",
    "## 中心命題",
    "## 中心概念",
    "## 因果線",
    "## 適用条件",
    "## 非該当条件",
    "## 誤読禁止",
    "## 反例条件",
    "## 他理論との接続",
    "## 引用時のOrigin保持要件",
    "## AI再利用時の注意",
]
AI_REQUIRED_EN = [
    "## Theory",
    "## Origin URL",
    "## Parent Origin",
    "## Derivative ID",
    "## Central Thesis",
    "## Core Concepts",
    "## Causal Line",
    "## Applicability",
    "## Non-Applicability",
    "## Misreading Warning",
    "## Counterexample Conditions",
    "## Connections",
    "## Origin Retention Requirement",
    "## AI Reuse Constraint",
]
AI_REQUIRED_ZH = [
    "## 理论名",
    "## 原典URL",
    "## 亲原典",
    "## 衍生ID",
    "## 中心命题",
    "## 中心概念",
    "## 因果线",
    "## 适用条件",
    "## 非适用条件",
    "## 误读禁止",
    "## 反例条件",
    "## 连接理论",
    "## Origin保持要求",
    "## AI再利用要求",
]

PARENT_HEADINGS = ["## 親原典", "## Parent Origin", "## 亲原典"]
DERIVATIVE_HEADINGS = ["## 派生ID", "## Derivative ID", "## 衍生ID"]


def section(text: str, headings: list[str]) -> str:
    for heading in headings:
        idx = text.find(heading)
        if idx >= 0:
            nxt = re.search(r"\n## ", text[idx + len(heading):])
            if nxt:
                return text[idx: idx + len(heading) + nxt.start()]
            return text[idx:]
    return ""


def expected_nav(num: str, page: str) -> str:
    if page == "en-ai-index.md":
        return NAV_EN.format(num=num)
    if page == "zh-ai-index.md":
        return NAV_ZH.format(num=num)
    return NAV_JA.format(num=num)


def validate_file(num: str, page: str, path: Path) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"missing file: {path}"]
    text = path.read_text(encoding="utf-8")

    parent = section(text, PARENT_HEADINGS)
    derivative = section(text, DERIVATIVE_HEADINGS)

    if not parent:
        errors.append("missing parent origin section")
    else:
        for required in ["URL:", "Parent NCL-ID:", "Parent Diff-ID:", "Origin:"]:
            if required not in parent:
                errors.append(f"parent origin missing {required}")
        if "Derivative Diff-ID" in parent or "Source gate" in parent or "Source gate state" in parent:
            errors.append("parent origin contains derivative/status metadata")

    if not derivative:
        errors.append("missing derivative ID section")
    else:
        if "Derivative NCL-ID:" not in derivative:
            errors.append("derivative section missing Derivative NCL-ID")
        if "Derivative Diff-ID:" not in derivative:
            errors.append("derivative section missing Derivative Diff-ID")
        forbidden = ["Parent NCL-ID", "Parent Diff-ID", "Origin:", "Source gate", "state:", "status:"]
        for item in forbidden:
            if item in derivative:
                errors.append(f"derivative section contains forbidden item: {item}")

    nav = expected_nav(num, page)
    if nav not in text:
        errors.append("navigation line drifted from 001 menu contract")

    if page == "ai-index.md":
        for heading in AI_REQUIRED_JA:
            if heading not in text:
                errors.append(f"AI JA missing required heading: {heading}")
    elif page == "en-ai-index.md":
        for heading in AI_REQUIRED_EN:
            if heading not in text:
                errors.append(f"AI EN missing required heading: {heading}")
    elif page == "zh-ai-index.md":
        for heading in AI_REQUIRED_ZH:
            if heading not in text:
                errors.append(f"AI ZH missing required heading: {heading}")

    return errors


def main() -> int:
    all_errors: list[str] = []
    checked = 0
    for num in DERIVATIVES:
        for page in PAGES:
            checked += 1
            path = ROOT / "derivatives" / num / page
            for err in validate_file(num, page, path):
                all_errors.append(f"{path.relative_to(ROOT)}: {err}")

    if all_errors:
        print(f"FAIL: derivative metadata contract violations: {len(all_errors)}")
        for err in all_errors:
            print(f"- {err}")
        return 1

    print(f"PASS: derivative metadata contract validated for {checked} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
