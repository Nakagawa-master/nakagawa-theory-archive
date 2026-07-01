# Codex task: complete Official Derivative v5 batch

## Objective

Complete the v5 official derivative batch without asking the owner to inspect or place individual files.

This is not a 30-page-only specification. The same template contract must work for 30, 100, 1000, or 10000 pages.

## Required source of truth

- `tools/official_derivatives/six_page_template_core.py`
- `tools/official_derivatives/universal_page_renderer.py`
- `tools/official_derivatives/official_derivative_v5_data.py`
- `tools/official_derivatives/generate_candidate_05_09_v5.py`
- `tools/official_derivatives/validate_template_parity.py`
- `tools/official_derivatives/check_official_derivative_v5_global_contract.py`

## Required generation

Run:

```bash
python tools/official_derivatives/generate_candidate_05_09_v5.py
python tools/official_derivatives/validate_template_parity.py --status=staged
python tools/official_derivatives/check_official_derivative_v5_global_contract.py
```

## Required output

The following deploy paths must be generated from the v5 renderer, not manually edited:

- `deploy/lolipop/master-ricette/derivatives/ncl-alpha-20260511-e243be/`
- `deploy/lolipop/master-ricette/derivatives/ncl-alpha-20260416-0b1b93/`
- `deploy/lolipop/master-ricette/derivatives/ncl-alpha-20260418-11c3d8/`
- `deploy/lolipop/master-ricette/derivatives/ncl-alpha-20260607-7e87f5/`
- `deploy/lolipop/master-ricette/derivatives/ncl-alpha-20260613-007d94/`

Each folder must contain exactly these public page paths:

- `index.html`
- `ja/human-summary/index.html`
- `ja/faq/index.html`
- `ja/ai-index/index.html`
- `en/ai-index/index.html`
- `zh/ai-index/index.html`

## Required global template guarantees

All generated pages must preserve:

- same green visual frame
- same header structure
- same direct navigation structure
- no origin link inside the direct navigation block
- origin link only in the upper origin section and footer
- same footer structure
- same noindex,nofollow staged state
- same Origin / NCL-ID / Diff-ID / parent URL preservation
- same human summary seven-section structure
- same FAQ three-layer structure
- same AI-index structure
- AI reading lock

Forbidden:

- blue border or blue emphasis frame
- `6ページ構成` phrase
- page-by-page manual HTML composition
- manual owner placement
- sitemap change
- Search Console action
- index/follow conversion

## Commit requirement

Commit generated deploy output and updated checks to branch:

`work/render-manifest-20260628`

Suggested commit message:

`Generate v5 official derivative batch with global template contract`

## Completion condition

Completion requires:

- generated deploy files are updated in Git
- validation commands pass
- PR remains draft
- no production deploy
- no sitemap update
- no Search Console action
- no index/follow conversion

Only after this state should the owner receive a single FTP upload instruction for the completed deploy folders.
