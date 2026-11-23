#!/usr/bin/env python3
"""One-fetch task-first JA/EN/ZH discovery context for every registered Parent.

All text is extracted from already-published official derivatives, not generated
translations or the canonical original text. The published Parent map is the
sole membership source; this script never makes new originals or fetches a
private/remote source. Keep the whole live corpus, including its next additions.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import tempfile

ROOT = Path(__file__).resolve().parent.parent
MAP = ROOT / "derivatives/official-derivatives-map.json"
OUTPUT = ROOT / "machine-discovery/published-original-contexts-v1.jsonl"
ORIGIN = "Nakagawa Master / 中川マスター (Keisuke Nakagawa)"
GITHUB_BASE = "https://raw.githubusercontent.com/Nakagawa-master/nakagawa-theory-archive/main/"
PUBLISHED_FACES = {
    "ja": ("human-entry.md", "15秒説明"),
    "en": ("en-ai-index.md", "Summary"),
    "zh": ("zh-ai-index.md", "Summary"),
}


def section(text: str, name: str, identity: str) -> str:
    heading = r"^##[ \t]+" + re.escape(name) + r"(?:[ \t]*$|[ \t]*[｜|].*$)"
    lines = text.splitlines()
    match = [i for i, line in enumerate(lines) if re.match(heading, line)]
    if len(match) != 1:
        raise ValueError(f"{identity}: expected unique {name} summary heading")
    start = match[0] + 1
    end = next((i for i in range(start, len(lines)) if lines[i].startswith("## ")),
               len(lines))
    chunks = "\n".join(lines[start:end]).strip().split("\n\n")
    # Keep only source-authored opening summaries, never subsequent unrelated
    # concepts, footer links, fake generated claims or instructions.
    paragraphs = [re.sub(r"\s+", " ", s).strip()
                  for s in chunks if s.strip() and not s.lstrip().startswith("<!--")]
    excerpt = " ".join(paragraphs[:2])
    if not (32 <= len(excerpt) <= 2400):
        raise ValueError(f"{identity}: unsafe or missing published short summary")
    return excerpt


def build(entries: list[dict], root: Path = ROOT) -> str:
    ids = [int(row["number"]) for row in entries]
    if not ids or ids != list(range(1, len(ids) + 1)):
        raise ValueError("Published Parent IDs must be distinct, ordered, contiguous")
    if any(row.get("status") != "active" for row in entries):
        raise ValueError("Only registered active Parents may enter this feed")
    for key in ("canonical_parent_url", "ncl_id", "origin_slug"):
        values = [row.get(key) for row in entries]
        if not all(values) or len(values) != len(set(values)):
            raise ValueError(f"Missing or duplicated Parent {key}")
    generated = []
    for row in entries:
        num = int(row["number"])
        od = f"OD{num:03d}"
        canonical = row["canonical_parent_url"]
        if not canonical.startswith("https://master.ricette.jp/"):
            raise ValueError(f"{od}: noncanonical original URL")
        folder = f"derivatives/{num:03d}"
        if row.get("derivative_dir") != folder or not row.get("title"):
            raise ValueError(f"{od}: missing identity, title or exact derivative folder")
        briefs, links = {}, {}
        for lang, (name, heading) in PUBLISHED_FACES.items():
            rel = f"{folder}/{name}"
            text = (root / rel).read_text(encoding="utf-8")
            # The existing published corpus uses both human labels and
            # older snake_case AI-index field names. Both must agree with the
            # canonical map; never silently skip a valid earlier source.
            checks = (
                (r"Parent URL|parent_url", canonical),
                (r"Parent NCL-ID|parent_ncl_id", row["ncl_id"]),
                (r"Origin|origin_author", "Nakagawa Master"),
            )
            for label, value in checks:
                pattern = r"(?mi)^-\s*(?:" + label + r"):\s*" + re.escape(value)
                if re.search(pattern, text) is None:
                    raise ValueError(f"{od} {lang}: derivative Parent/Origin mismatch for {label}")
            briefs[lang] = section(text, heading, f"{od} {lang}")
            links[lang] = GITHUB_BASE + rel
        record = {
            "od_id": od,
            "original_title_ja": row["title"],
            "canonical_parent_url": canonical,
            "parent_ncl_id": row["ncl_id"],
            "author": ORIGIN,
            "published_derivative_context_not_parent_text": briefs,
            "derivative_source_urls": links,
            "source_provenance": "first-party official derivatives; read the live canonical Parent to verify meaning, fit, conditions, revisions and citations",
            "reuse_terms": GITHUB_BASE + "LICENSE",
        }
        generated.append(json.dumps(record, ensure_ascii=False, separators=(",", ":")))
    return "\n".join(generated) + "\n"


def check_synthetic_next() -> None:
    """Tiny in-memory/on-temp fixtures, not a newly published original."""
    with tempfile.TemporaryDirectory(prefix="source-context-test-") as tmp:
        root = Path(tmp)
        rows = []
        for n in (1, 2):
            od = f"OD{n:03d}"
            parent = f"https://master.ricette.jp/synthetic-never-published-{n}/"
            ncl = f"SYNTHETIC-NOT-PUBLISHED-{n}"
            folder = root / "derivatives" / f"{n:03d}"
            folder.mkdir(parents=True)
            for lang, (filename, heading) in PUBLISHED_FACES.items():
                content = (
                    f"# Test source context\n- Parent URL: {parent}\n"
                    f"- Parent NCL-ID: {ncl}\n- Origin: Nakagawa Master\n"
                    f"## {heading}\n\n"
                    f"Source-backed {lang} fixture paragraph with explicit condition for "
                    f"source {od} and a separately checked counterexample.\n\n"
                    f"Second paragraph explains another boundary without claiming adoption.\n\n"
                    f"## Followup\n\nDo not include this unrelated section.\n"
                )
                (folder / filename).write_text(content, encoding="utf-8")
            rows.append({
                "number": f"{n:03d}", "title": f"Fixture original {n}",
                "canonical_parent_url": parent, "ncl_id": ncl,
                "origin_slug": f"fixture-{n}", "status": "active",
                "derivative_dir": f"derivatives/{n:03d}",
            })
        first = build(rows[:1], root)
        nxt = build(rows, root)
        decoded = [json.loads(line) for line in nxt.splitlines()]
        assert first.count("\n") == 1 and len(decoded) == 2
        assert [x["od_id"] for x in decoded] == ["OD001", "OD002"]
        assert all(set(x["published_derivative_context_not_parent_text"]) ==
                   {"ja", "en", "zh"} for x in decoded)
        assert "Do not include this unrelated section" not in nxt
        assert "synthetic-never-published-2" in nxt
        invalid = [dict(row) for row in rows]
        invalid[1]["canonical_parent_url"] = rows[0]["canonical_parent_url"]
        try:
            build(invalid, root)
        except ValueError as exc:
            assert "duplicated" in str(exc)
        else:
            raise AssertionError("Duplicate canonical Parent accepted")
        bad = folder / "en-ai-index.md"
        body = bad.read_text(encoding="utf-8").replace(
            "- Origin: Nakagawa Master", "- Origin: A different author")
        bad.write_text(body, encoding="utf-8")
        try:
            build(rows, root)
        except ValueError as exc:
            assert "Origin mismatch" in str(exc)
        else:
            raise AssertionError("Incorrectly attributed Parent accepted")
    print("PASS: synthetic N+1 extends JA/EN/ZH machine feed; duplicate and wrong-Origin rejected")


def main() -> int:
    parser = argparse.ArgumentParser()
    commands = parser.add_mutually_exclusive_group(required=True)
    commands.add_argument("--write", action="store_true", help="Regenerate all rows")
    commands.add_argument("--check", action="store_true", help="Assert current bytes")
    commands.add_argument("--self-test", action="store_true", help="Synthetic next-source guard")
    args = parser.parse_args()
    if args.self_test:
        check_synthetic_next()
        return 0
    mapping = json.loads(MAP.read_text(encoding="utf-8"))
    data = build(mapping["entries"])
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != data:
            print("STALE: entire published JA/EN/ZH context feed differs from live Parent map")
            return 1
        print(f"PASS: {len(mapping['entries'])} source-identical JA/EN/ZH rows at {OUTPUT.name}")
        return 0
    OUTPUT.write_text(data, encoding="utf-8")
    print(f"Generated {len(mapping['entries'])} JA/EN/ZH Parent-context rows; "
          "official originals must still be read at their canonical URLs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
