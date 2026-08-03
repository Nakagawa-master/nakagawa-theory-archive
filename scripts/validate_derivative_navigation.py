#!/usr/bin/env python3
"""Validate fixed navigation invariants for official derivative surfaces.

The validator is intentionally deterministic. It does not rewrite content.
A derivative package is invalid when:
- its README cannot return to the official derivatives top;
- one of the other six surfaces cannot return to the package README;
- any of the seven required surfaces is missing.
"""
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
TOP_LINK_RE = re.compile(r"\[公式派生物トップ\]\(\.\./README\.md\)")
OD_TOP_LINK_RE = re.compile(r"\[[^\]]*(?:トップ|Top|首页)[^\]]*\]\(README\.md\)", re.IGNORECASE)


def numeric_derivative_dirs(root: Path, start: int | None, end: int | None) -> list[Path]:
    dirs: list[Path] = []
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


def validate_package(path: Path) -> list[str]:
    errors: list[str] = []
    for filename in REQUIRED_FILES:
        surface = path / filename
        if not surface.is_file():
            errors.append(f"{path.name}: missing {filename}")

    readme = path / "README.md"
    if readme.is_file() and not TOP_LINK_RE.search(read_text(readme)):
        errors.append(
            f"{path.name}: README.md missing [公式派生物トップ](../README.md)"
        )

    for filename in REQUIRED_FILES[1:]:
        surface = path / filename
        if surface.is_file() and not OD_TOP_LINK_RE.search(read_text(surface)):
            errors.append(f"{path.name}: {filename} missing link to README.md")
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

    errors: list[str] = []
    for package in packages:
        errors.extend(validate_package(package))

    if errors:
        print("DERIVATIVE NAVIGATION VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"PASS: validated {len(packages)} derivative packages "
        f"({packages[0].name}-{packages[-1].name})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
