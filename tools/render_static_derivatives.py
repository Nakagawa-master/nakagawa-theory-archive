#!/usr/bin/env python3
"""Render GitHub-managed derivative markdown files into static HTML candidates.

This helper is intentionally small and dependency-free for the first Pilot 001
render test. It does not deploy files, create WordPress posts, submit sitemaps,
or connect any hosting service.
"""

from __future__ import annotations

import html
import pathlib
import re
from dataclasses import dataclass
from datetime import date

ROOT = pathlib.Path(__file__).resolve().parents[1]
PARENT_TITLE = "Nakagawa OS L1-L7 layer specification"
PARENT_URL = "https://master.ricette.jp/theory/nakagawa-master-nakagawa-os-layer-specification-v1/"
PARENT_NCL_ID = "NCL-α-20251124-e4c70c"
PARENT_DIFF_ID = "DIFF-20251124-0012"
PARENT_NCL_SLUG = "ncl-alpha-20251124-e4c70c"


@dataclass(frozen=True)
class RenderTarget:
    source_path: str
    output_path: str
    language: str
    derivative_type: str
    title: str


TARGETS = [
    RenderTarget(
        "registry/derivatives/by-parent/NCL-alpha-20251124-e4c70c/public-index/ja-human-summary.md",
        "static/derivatives/ncl-alpha-20251124-e4c70c/ja/human-summary/index.html",
        "ja",
        "human_summary",
        "Nakagawa OS L1-L7 layer specification｜人間向け要約",
    ),
    RenderTarget(
        "registry/derivatives/by-parent/NCL-alpha-20251124-e4c70c/public-index/ja-faq.md",
        "static/derivatives/ncl-alpha-20251124-e4c70c/ja/faq/index.html",
        "ja",
        "faq",
        "Nakagawa OS L1-L7 layer specification｜FAQ",
    ),
    RenderTarget(
        "registry/derivatives/by-parent/NCL-alpha-20251124-e4c70c/public-index/ja-ai-index.md",
        "static/derivatives/ncl-alpha-20251124-e4c70c/ja/ai-index/index.html",
        "ja",
        "ai_index",
        "Nakagawa OS L1-L7 layer specification｜AI索引",
    ),
    RenderTarget(
        "registry/derivatives/by-parent/NCL-alpha-20251124-e4c70c/public-index/en-ai-index.md",
        "static/derivatives/ncl-alpha-20251124-e4c70c/en/ai-index/index.html",
        "en",
        "ai_index",
        "Nakagawa OS L1-L7 layer specification | AI Index",
    ),
    RenderTarget(
        "registry/derivatives/by-parent/NCL-alpha-20251124-e4c70c/public-index/zh-ai-index.md",
        "static/derivatives/ncl-alpha-20251124-e4c70c/zh/ai-index/index.html",
        "zh",
        "ai_index",
        "Nakagawa OS L1-L7 layer specification｜AI索引",
    ),
]


def inline_markdown(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"`(.+?)`", r"<code>\1</code>", escaped)
    return escaped


def markdown_to_html(markdown: str) -> str:
    blocks: list[str] = []
    in_list = False
    in_code = False
    code_lines: list[str] = []

    for raw_line in markdown.splitlines():
        line = raw_line.rstrip()

        if line.startswith("```"):
            if in_code:
                blocks.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
                code_lines = []
                in_code = False
            else:
                if in_list:
                    blocks.append("</ul>")
                    in_list = False
                in_code = True
            continue

        if in_code:
            code_lines.append(raw_line)
            continue

        if not line.strip():
            if in_list:
                blocks.append("</ul>")
                in_list = False
            continue

        if line.startswith("#"):
            if in_list:
                blocks.append("</ul>")
                in_list = False
            level = min(len(line) - len(line.lstrip("#")), 6)
            content = line[level:].strip()
            blocks.append(f"<h{level}>{inline_markdown(content)}</h{level}>")
            continue

        if line.startswith("- "):
            if not in_list:
                blocks.append("<ul>")
                in_list = True
            blocks.append(f"<li>{inline_markdown(line[2:].strip())}</li>")
            continue

        if in_list:
            blocks.append("</ul>")
            in_list = False
        blocks.append(f"<p>{inline_markdown(line)}</p>")

    if in_code:
        blocks.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
    if in_list:
        blocks.append("</ul>")

    return "\n".join(blocks)


def render_page(target: RenderTarget, markdown: str) -> str:
    public_path = "/" + str(pathlib.Path(target.output_path).parent).removeprefix("static/").replace("\\", "/") + "/"
    body = markdown_to_html(markdown)
    today = date.today().isoformat()
    return f"""<!doctype html>
<html lang=\"{html.escape(target.language)}\">
<head>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
  <title>{html.escape(target.title)}</title>
  <link rel=\"canonical\" href=\"{html.escape(public_path)}\">
  <meta name=\"derivative-type\" content=\"{html.escape(target.derivative_type)}\">
  <meta name=\"parent-url\" content=\"{html.escape(PARENT_URL)}\">
  <meta name=\"parent-ncl-id\" content=\"{html.escape(PARENT_NCL_ID)}\">
  <meta name=\"parent-diff-id\" content=\"{html.escape(PARENT_DIFF_ID)}\">
  <meta name=\"render-status\" content=\"rendered_candidate\">
  <meta name=\"lastmod\" content=\"{today}\">
</head>
<body>
  <main>
    <header>
      <p><strong>Derivative candidate:</strong> {html.escape(target.derivative_type)} / {html.escape(target.language)}</p>
      <p><strong>Original article:</strong> <a href=\"{html.escape(PARENT_URL)}\">{html.escape(PARENT_TITLE)}</a></p>
      <p><strong>Parent NCL-ID:</strong> {html.escape(PARENT_NCL_ID)} / <strong>Parent Diff-ID:</strong> {html.escape(PARENT_DIFF_ID)}</p>
      <p><strong>Notice:</strong> This is a derivative index page candidate, not the original article.</p>
    </header>
    <article>
{body}
    </article>
  </main>
</body>
</html>
"""


def main() -> None:
    rendered = 0
    for target in TARGETS:
        source = ROOT / target.source_path
        output = ROOT / target.output_path
        if not source.exists():
            raise FileNotFoundError(f"Missing source file: {target.source_path}")
        markdown = source.read_text(encoding="utf-8")
        html_text = render_page(target, markdown)
        for required in (PARENT_URL, PARENT_NCL_ID, PARENT_DIFF_ID, "not the original article"):
            if required not in html_text:
                raise ValueError(f"Rendered output missing required value: {required}")
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(html_text, encoding="utf-8")
        rendered += 1
    print(f"Rendered {rendered} static derivative candidate files.")


if __name__ == "__main__":
    main()
