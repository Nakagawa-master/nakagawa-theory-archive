# Codex Handoff｜Candidate 10-19 Verified Catalog Generation

status: private-staged handoff

## Purpose

Generate the candidate 10-19 origin catalog from the verified origin overlay without manual TSV editing.

This handoff exists because direct long TSV updates and direct workflow edits were blocked during the operation. The correct path is script-based generation.

## Source files

- tools/official_derivatives/next_10_public_origin_discovery_input.tsv
- tools/official_derivatives/next_10_verified_origin_overlay_20260629.tsv
- tools/official_derivatives/build_next_10_origin_catalog_from_verified_overlay.py
- tools/official_derivatives/check_next_10_public_origin_discovery.py
- tools/official_derivatives/check_next_10_verified_origin_overlay.py
- tools/official_derivatives/check_next_10_origin_catalog.py

## Required commands

```bash
python tools/official_derivatives/check_next_10_public_origin_discovery.py
python tools/official_derivatives/check_next_10_verified_origin_overlay.py
python tools/official_derivatives/build_next_10_origin_catalog_from_verified_overlay.py
python tools/official_derivatives/check_next_10_origin_catalog.py
```

## Expected result

- discovery rows: 10
- verified overlay rows: 9
- origin catalog rows after build: 9
- ready_for_candidate rows: 0
- page_generation: false
- production_deploy: false
- sitemap_update: false
- search_console_action: false
- index_follow_conversion: false

## Boundary

This does not select sources for queue.
This does not generate candidate 10-19 pages.
This does not publish.
This does not update sitemap.
This does not call Search Console.
This does not convert pages to index/follow.

## Next safe step after pass

Commit the generated next_10_origin_catalog_candidate_10_19.tsv if and only if the validator passes.
