#!/usr/bin/env python3
"""Build a public AI-readable fulltext mirror from WordPress origin pages.

This script is intentionally strict. It does not create a valid mirror when the
origin body, audit bundle, reference cluster, NCL-ID, and Diff-ID cannot be
observed. Failed targets are reported as blocked instead of inferred.
"""

from __future__ import annotations

import html
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[2]
TARGETS = ROOT / "origin-fulltext" / "origin-fulltext-targets.json"
OUT_DIR = ROOT / "origin-fulltext" / "articles"
REPORT = ROOT / "origin-fulltext" / "origin-fulltext-build-report.json"
MANIFEST = ROOT / "origin-fulltext" / "manifest.json"
USER_AGENT = "NakagawaOriginFulltextMirror/1.0"

REQUIRED_MARKERS = {
    "ncl": "NCL-",
    "diff": "DIFF-",
    "integrated_audit": "統合監査要旨",
    "local_audit": "局所監査要旨",
    "reference_cluster": "参照束",
    "origin_signature": "Origin:",
}


def fetch(url: str, timeout: int = 90) -> Tuple[int, str, bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as res:
            body = res.read()
            charset = res.headers.get_content_charset() or "utf-8"
            return int(res.status), charset, body
    except Exception as exc:  # noqa: BLE001
        return 0, "utf-8", str(exc).encode("utf-8", errors="ignore")


def strip_tags(raw: str) -> str:
    raw = re.sub(r"<script[\s\S]*?</script>", "\n", raw, flags=re.I)
    raw = re.sub(r"<style[\s\S]*?</style>", "\n", raw, flags=re.I)
    raw = re.sub(r"<br\s*/?>", "\n", raw, flags=re.I)
    raw = re.sub(r"</p>", "\n\n", raw, flags=re.I)
    raw = re.sub(r"</h[1-6]>", "\n\n", raw, flags=re.I)
    raw = re.sub(r"<[^>]+>", "\n", raw)
    raw = html.unescape(raw)
    raw = re.sub(r"[ \t\r\f\v]+", " ", raw)
    raw = re.sub(r"\n{3,}", "\n\n", raw)
    return raw.strip()


def rest_url_for(origin_url: str) -> str:
    parsed = urllib.parse.urlparse(origin_url)
    slug = parsed.path.rstrip("/").split("/")[-1]
    return f"{parsed.scheme}://{parsed.netloc}/wp-json/wp/v2/posts?slug={urllib.parse.quote(slug)}&_fields=id,slug,title,content,excerpt,date,modified,status,link"


def extract_from_rest(raw: bytes, charset: str) -> Tuple[str, Dict[str, Any]]:
    text = raw.decode(charset, errors="replace")
    meta: Dict[str, Any] = {"route": "rest", "raw_bytes": len(raw)}
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        meta["rest_json"] = "invalid"
        return "", meta
    if not isinstance(data, list) or not data:
        meta["rest_json"] = "empty"
        return "", meta
    post = data[0]
    meta.update({
        "post_id": post.get("id"),
        "slug": post.get("slug"),
        "date": post.get("date"),
        "modified": post.get("modified"),
        "status": post.get("status"),
        "link": post.get("link"),
    })
    rendered = ""
    content = post.get("content") or {}
    if isinstance(content, dict):
        rendered = str(content.get("rendered") or "")
    return strip_tags(rendered), meta


def extract_from_html(raw: bytes, charset: str) -> str:
    return strip_tags(raw.decode(charset, errors="replace"))


def marker_state(text: str) -> Dict[str, bool]:
    return {key: marker in text for key, marker in REQUIRED_MARKERS.items()}


def first_match(pattern: str, text: str) -> str:
    m = re.search(pattern, text)
    return m.group(1).strip() if m else ""


def build_markdown(target: Dict[str, Any], text: str, meta: Dict[str, Any], markers: Dict[str, bool]) -> str:
    ncl = first_match(r"(NCL[-A-Za-z0-9_α-ωΑ-Ωぁ-んァ-ヶ一-龠・ー]+)", text)
    diff = first_match(r"(DIFF[-A-Za-z0-9_]+)", text)
    lines = [
        "# " + target["title"],
        "",
        "canonical_origin_url: " + target["canonical_url"],
        "source_acquisition_method: wordpress_rest_then_html_fallback",
        "validation_state: " + ("pass" if all(markers.values()) else "blocked"),
        "ncl_id_observed: " + (ncl or "not_observed"),
        "diff_id_observed: " + (diff or "not_observed"),
        "modified: " + str(meta.get("modified") or "not_observed"),
        "",
        "## Marker validation",
    ]
    for key, value in markers.items():
        lines.append(f"- {key}: {'pass' if value else 'fail'}")
    lines += ["", "## Full origin text", "", text]
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    targets: List[Dict[str, Any]] = json.loads(TARGETS.read_text(encoding="utf-8"))
    report: List[Dict[str, Any]] = []
    manifest: List[Dict[str, Any]] = []
    now = time.strftime("%Y-%m-%dT%H:%M:%S%z")

    for target in targets:
        slug = target["slug"]
        rest_url = rest_url_for(target["canonical_url"])
        rest_status, rest_charset, rest_body = fetch(rest_url)
        rest_text, meta = extract_from_rest(rest_body, rest_charset)
        html_status, html_charset, html_body = fetch(target["canonical_url"])
        html_text = extract_from_html(html_body, html_charset)
        text = rest_text if len(rest_text) >= len(html_text) else html_text
        source_route = "rest" if text == rest_text else "html"
        markers = marker_state(text)
        is_valid = all(markers.values()) and len(text) > 10000
        mirror_path = OUT_DIR / f"{slug}.md"
        meta["source_route"] = source_route
        meta["html_status"] = html_status
        meta["rest_status"] = rest_status
        meta["html_bytes"] = len(html_body)
        meta["rest_bytes"] = len(rest_body)
        meta["text_chars"] = len(text)
        meta["validated_at"] = now
        md = build_markdown(target, text, meta, markers)
        mirror_path.write_text(md, encoding="utf-8")
        item = {
            "slug": slug,
            "title": target["title"],
            "canonical_url": target["canonical_url"],
            "mirror_file_path": str(mirror_path.relative_to(ROOT)),
            "fulltext_status": "pass" if is_valid else "blocked",
            "audit_bundle_status": "pass" if markers.get("integrated_audit") and markers.get("local_audit") and markers.get("reference_cluster") else "blocked",
            "ncl_status": "pass" if markers.get("ncl") else "blocked",
            "diff_status": "pass" if markers.get("diff") else "blocked",
            "source_route": source_route,
            "text_chars": len(text),
            "html_status": html_status,
            "rest_status": rest_status,
            "last_validated_at": now,
        }
        report.append({**item, "markers": markers, "rest_url": rest_url})
        manifest.append(item)

    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
