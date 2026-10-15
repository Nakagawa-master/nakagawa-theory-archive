#!/usr/bin/env python3
"""Compare exact local release candidates with GitHub's draft Release asset digests.

Input is an exported GitHub Releases API JSON response, not an API token or URL.
This read-only check cannot prove that the API is authentic, that a tag points
to the intended commit, or that anyone subsequently downloaded these bytes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import stat
import sys
import tempfile
from pathlib import Path
from typing import Any

SHA256 = re.compile(r"sha256:([0-9a-fA-F]{64})\Z")
VALID_NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*\Z")


def inspect(asset_dir: Path, release: Any, expected: list[str], tag: str | None) -> dict[str, Any]:
    issues: list[str] = []
    checked = 0

    if not isinstance(release, dict):
        return {"verdict": "FAIL", "checked": 0, "issues": ["release JSON is not an object"]}
    if release.get("draft") is not True:
        issues.append("release is not a draft: check before publication")
    if tag is not None and release.get("tag_name") != tag:
        issues.append("release tag differs from the requested tag")
    if not expected or len(set(expected)) != len(expected) or any(
        not isinstance(n, str) or not VALID_NAME.fullmatch(n) or n in (".", "..")
        for n in expected
    ):
        return {"verdict": "FAIL", "checked": 0, "issues": issues + ["unsafe, empty or duplicate expected names"]}

    assets = release.get("assets")
    if not isinstance(assets, list):
        return {"verdict": "FAIL", "checked": 0, "issues": issues + ["release.assets must be an array"]}
    by_name: dict[str, dict[str, Any]] = {}
    for item in assets:
        if not isinstance(item, dict) or not isinstance(item.get("name"), str):
            issues.append("malformed release asset")
            continue
        name = item["name"]
        if name in by_name:
            issues.append(f"duplicate remote asset: {name}")
        by_name[name] = item

    absent = sorted(set(expected) - set(by_name))
    extra = sorted(set(by_name) - set(expected))
    if absent:
        issues.append("missing remote assets: " + ", ".join(absent))
    if extra:
        issues.append("unexpected remote assets: " + ", ".join(extra))

    for name in expected:
        remote = by_name.get(name)
        if remote is None:
            continue
        f = asset_dir / name
        try:
            st = f.lstat()
            if not stat.S_ISREG(st.st_mode):
                issues.append(f"{name}: local candidate is not a regular file")
                continue
            h = hashlib.sha256()
            with f.open("rb") as stream:
                for part in iter(lambda: stream.read(1024 * 1024), b""):
                    h.update(part)
        except OSError as exc:
            issues.append(f"{name}: cannot read local candidate: {type(exc).__name__}")
            continue

        checked += 1
        if remote.get("state") != "uploaded":
            issues.append(f"{name}: remote asset is not in uploaded state")
        size = remote.get("size")
        if type(size) is not int or size != st.st_size:
            issues.append(f"{name}: remote byte size differs from local candidate")
        digest = remote.get("digest")
        match = SHA256.fullmatch(digest) if isinstance(digest, str) else None
        if match is None:
            issues.append(f"{name}: missing or malformed remote sha256 digest")
        elif match.group(1).lower() != h.hexdigest():
            issues.append(f"{name}: remote sha256 differs from local candidate")
    return {"verdict": "PASS" if not issues else "FAIL", "checked": checked, "issues": issues,
            "boundary": "GitHub API asset digests vs supplied local bytes only; tag ancestry and download not checked"}


def self_test() -> None:
    names = ["bundle.tar.gz", "bundle.manifest.json", "SHA256SUMS.txt"]
    with tempfile.TemporaryDirectory() as temp:
        folder = Path(temp)
        original = [b"abc", b'{"version":1}', b"deadbeef"]
        for name, data in zip(names, original):
            (folder / name).write_bytes(data)

        def fixture() -> dict[str, Any]:
            return {"draft": True, "tag_name": "v0.1.0-test", "assets": [
                {"name": name, "size": len(data), "digest": "sha256:" + hashlib.sha256(data).hexdigest(),
                 "state": "uploaded"}
                for name, data in zip(names, original)
            ]}

        def check(release: Any, expected: list[str] | None = None) -> dict[str, Any]:
            return inspect(folder, release, names if expected is None else expected, "v0.1.0-test")

        assert check(fixture())["verdict"] == "PASS", "matching candidates"
        (folder / names[0]).write_bytes(b"abd")
        assert any("sha256 differs" in x for x in check(fixture())["issues"]), "same-sized changed bytes"
        (folder / names[0]).write_bytes(original[0])
        altered = fixture()
        del altered["assets"][0]["digest"]
        assert any("missing or malformed" in x for x in check(altered)["issues"]), "missing digest"
        altered = fixture()
        altered["assets"][0]["size"] += 1
        assert any("byte size differs" in x for x in check(altered)["issues"]), "wrong size"
        altered = fixture()
        altered["assets"].append(dict(altered["assets"][0]))
        assert any("duplicate remote" in x for x in check(altered)["issues"]), "duplicate asset"
        altered = fixture()
        altered["assets"].append({"name": "other", "size": 0, "digest": "none"})
        assert any("unexpected remote" in x for x in check(altered)["issues"]), "extra asset"
        altered = fixture()
        altered["draft"] = False
        assert any("not a draft" in x for x in check(altered)["issues"]), "published release"
        assert any("unsafe" in x for x in check(fixture(), ["../secrets"])["issues"]), "path traversal"
        (folder / names[0]).unlink()
        (folder / names[0]).symlink_to(folder / names[1])
        assert any("not a regular file" in x for x in check(fixture())["issues"]), "symlink"
    print("PASS: 9 self-tests (including same-size altered bytes, missing digest, malformed inventory)")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true", help="run nine local synthetic checks")
    parser.add_argument("--asset-dir", type=Path)
    parser.add_argument("--release-json", type=Path)
    parser.add_argument("--asset", action="append", default=[], help="expected basename; repeat for each asset")
    parser.add_argument("--tag", help="expected release tag")
    opts = parser.parse_args()
    if opts.self_test:
        self_test()
        return 0
    if not opts.asset_dir or not opts.release_json or not opts.asset:
        parser.error("specify --asset-dir, --release-json and one or more --asset, or --self-test")
    try:
        release = json.loads(opts.release_json.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        print(json.dumps({"verdict": "INVALID_INPUT", "error": type(error).__name__}))
        return 2
    result = inspect(opts.asset_dir, release, opts.asset, opts.tag)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
