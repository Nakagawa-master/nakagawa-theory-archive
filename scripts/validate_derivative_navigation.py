#!/usr/bin/env python3
"""Validate immutable Official Derivative surface and Factory v1 invariants."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_FILES = (
    "README.md",
    "human-entry.md",
    "faq.md",
    "ai-index.md",
    "en-ai-index.md",
    "zh-ai-index.md",
    "derivative-ledger.md",
)
README_FOOTER = "導線: [公式派生物トップ](../README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)"
OD_TOP_LINK_RE = re.compile(r"\[[^\]]*(?:トップ|Top|首页)[^\]]*\]\(README\.md\)", re.IGNORECASE)
IDENTITY_PATTERNS = {
    "parent_url": re.compile(r"Parent URL:\s*(\S+)"),
    "parent_ncl": re.compile(r"Parent NCL-ID:\s*(\S+)"),
    "parent_diff": re.compile(r"Parent Diff-ID:\s*(\S+)"),
    "derivative_ncl": re.compile(r"derivative_ncl_id:\s*(\S+)"),
    "derivative_diff": re.compile(r"derivative_diff_id:\s*(\S+)"),
}
FACTORY_V1_START = 67
README_HEADINGS = (
    "## 親原典",
    "## 派生ID",
    "## 中心命題",
    "## 因果線",
    "## 構造層",
    "## 状態モデル",
    "## 適用例",
    "## 測定・監査点",
    "## 成立条件",
    "## 失敗条件",
    "## 反証条件",
    "## 必須の区別",
    "## 誤読禁止",
    "## 親原典へ戻る理由",
)
MIN_CHARS = {
    "README.md": 2200,
    "human-entry.md": 1500,
    "faq.md": 5000,
    "ai-index.md": 1400,
    "en-ai-index.md": 1400,
    "zh-ai-index.md": 1400,
    "derivative-ledger.md": 900,
}


def numeric_derivative_dirs(root: Path, start: int | None, end: int | None) -> list[Path]:
    dirs = []
    for path in root.iterdir():
        if not path.is_dir() or not re.fullmatch(r"\d{3}", path.name):
            continue
        number = int(path.name)
        if start is not None and number < start:
            continue
        if end is not None and number > end:
            continue
        dirs.append(path)
    return sorted(dirs, key=lambda p: int(p.name))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def identity(text: str) -> dict[str, str]:
    found = {}
    for key, pattern in IDENTITY_PATTERNS.items():
        match = pattern.search(text)
        if match:
            found[key] = match.group(1)
    return found


def validate_navigation(path: Path, texts: dict[str, str]) -> list[str]:
    errors = []
    readme = texts.get("README.md", "")
    if README_FOOTER not in readme:
        errors.append(f"{path.name}: README.md missing exact canonical footer")
    for filename in REQUIRED_FILES[1:]:
        text = texts.get(filename, "")
        if text and not OD_TOP_LINK_RE.search(text):
            errors.append(f"{path.name}: {filename} missing link to README.md")
    return errors


def validate_factory_v1(path: Path, texts: dict[str, str]) -> list[str]:
    errors = []
    number = int(path.name)
    if number < FACTORY_V1_START:
        return errors

    readme = texts["README.md"]
    positions = []
    for heading in README_HEADINGS:
        pos = readme.find(heading)
        if pos < 0:
            errors.append(f"{path.name}: README missing heading {heading}")
        positions.append(pos)
    if all(pos >= 0 for pos in positions) and positions != sorted(positions):
        errors.append(f"{path.name}: README heading order differs from Factory v1")

    for filename, minimum in MIN_CHARS.items():
        if len(texts[filename].strip()) < minimum:
            errors.append(f"{path.name}: {filename} below density floor {minimum}")

    faq = texts["faq.md"]
    for heading in ("第1層｜基礎理解", "第2層｜構造・因果", "第3層｜境界・監査・反証"):
        if heading not in faq:
            errors.append(f"{path.name}: FAQ missing layer {heading}")
    questions = re.findall(r"^###\s+Q\d+\.", faq, flags=re.MULTILINE)
    if len(questions) != 30:
        errors.append(f"{path.name}: FAQ requires exactly 30 questions, found {len(questions)}")

    baseline = identity(readme)
    if len(baseline) != len(IDENTITY_PATTERNS):
        errors.append(f"{path.name}: README identity block incomplete")
    for filename in REQUIRED_FILES[1:]:
        current = identity(texts[filename])
        for key, expected in baseline.items():
            if current.get(key) != expected:
                errors.append(f"{path.name}: {filename} identity mismatch for {key}")

    ledger = texts["derivative-ledger.md"]
    if "factory_version: 1.0" not in ledger:
        errors.append(f"{path.name}: ledger missing factory_version: 1.0")
    if "generation_mode: SINGLE_WORK_PACKET_DETERMINISTIC_RENDER" not in ledger:
        errors.append(f"{path.name}: ledger missing deterministic generation mode")
    return errors


def validate_package(path: Path) -> list[str]:
    errors = []
    texts = {}
    for filename in REQUIRED_FILES:
        surface = path / filename
        if not surface.is_file():
            errors.append(f"{path.name}: missing {filename}")
        else:
            texts[filename] = read_text(surface)
    if len(texts) != len(REQUIRED_FILES):
        return errors
    errors.extend(validate_navigation(path, texts))
    errors.extend(validate_factory_v1(path, texts))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="derivatives")
    parser.add_argument("--start", type=int)
    parser.add_argument("--end", type=int)
    args = parser.parse_args()
    root = Path(args.root)
    if not root.is_dir():
        print(f"ERROR: derivative root not found: {root}", file=sys.stderr)
        return 2
    packages = numeric_derivative_dirs(root, args.start, args.end)
    if not packages:
        print("ERROR: no derivative packages found", file=sys.stderr)
        return 2
    errors = []
    for package in packages:
        errors.extend(validate_package(package))
    if errors:
        print("OFFICIAL DERIVATIVE VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"PASS: validated {len(packages)} packages ({packages[0].name}-{packages[-1].name})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
