# PR35 Owner Transfer Runbook

## Purpose

Prepare the PR35 staged derivative folders for owner-side server transfer without changing sitemap, Search Console, or index state.

## Preconditions

1. Official derivative generation check passes.
2. `tools/official_derivatives/pr35_transfer_manifest.tsv` exists.
3. `tools/official_derivatives/check_pr35_transfer_manifest.py` passes.
4. PR remains draft until owner-side transfer is complete.
5. No sitemap submission is performed in this step.
6. No Search Console submission is performed in this step.
7. No index/follow conversion is performed in this step.

## Scope

- folders: 13
- pages: 78
- source path root: `deploy/lolipop/master-ricette/derivatives/`
- target path root: `/derivatives/`

## Owner-side action

Use `pr35_transfer_manifest.tsv` as the authoritative folder list.
For each row, transfer the local folder root to the matching target folder root.
Do not add folders that are not listed in the manifest.
Do not remove existing production files.
Do not modify sitemap or Search Console during this step.

## Completion check

After transfer, verify that each listed folder has six expected page paths.
Keep pages noindex/nofollow until a later index-state decision is explicitly prepared.
