# Cloudflare Pages Preview Execution Package v0.1

status: ready_for_human_preview_setup  
source_of_truth: GitHub registry  
repository: `Nakagawa-master/nakagawa-theory-archive`  
branch: `main`  
static_output_directory: `static`  
custom_domain_candidate: `derivatives.ricette.jp`

## Purpose

This package defines the exact Cloudflare Pages preview setup target for Pilot 001 static derivative pages.

The first external step is preview creation only.  
It does not authorize custom domain connection, DNS changes, final sitemap generation, or Search Console action.

## Current candidate pages

The preview should expose the following paths on a Cloudflare Pages preview or pages.dev URL:

- `/`
- `/derivatives/`
- `/derivatives/ncl-alpha-20251124-e4c70c/`
- `/derivatives/ncl-alpha-20251124-e4c70c/ja/human-summary/`
- `/derivatives/ncl-alpha-20251124-e4c70c/ja/faq/`
- `/derivatives/ncl-alpha-20251124-e4c70c/ja/ai-index/`
- `/derivatives/ncl-alpha-20251124-e4c70c/en/ai-index/`
- `/derivatives/ncl-alpha-20251124-e4c70c/zh/ai-index/`

## Cloudflare Pages project settings

Use these values for the preview setup:

- Project source: GitHub repository
- Repository: `Nakagawa-master/nakagawa-theory-archive`
- Production branch: `main`
- Build command: empty if accepted, otherwise `exit 0`
- Build output directory: `static`
- Root directory: repository root
- Environment variables: none required for Pilot 001

## Preview-only indexing policy

All static candidate pages currently contain:

```html
<meta name="robots" content="noindex,nofollow">
```

This is intentional for the preview phase.

The robots policy should only be changed after:

1. Cloudflare preview loads correctly.
2. `derivatives.ricette.jp` route is approved.
3. Custom domain and DNS are confirmed.
4. Final sitemap scope is reviewed.
5. Search Console timing is approved.

## Human preview checks

After Cloudflare creates the preview URL, check:

1. Landing page loads.
2. Derivatives index page loads.
3. Pilot 001 parent derivative index loads.
4. All five derivative pages load.
5. Original article link points to `master.ricette.jp`.
6. Parent NCL-ID appears or is present in metadata.
7. Parent Diff-ID appears or is present in metadata.
8. Each page states that it is not the original article.
9. No WordPress post was created.
10. No Search Console action was taken.
11. No DNS change was made.

## Still blocked

- Custom domain connection
- DNS/CNAME changes
- Public route activation as `derivatives.ricette.jp`
- Changing robots from `noindex,nofollow` to `index,follow`
- Final sitemap generation
- Search Console action
- WordPress derivative post creation
- FTP upload

## Next status if preview succeeds

If preview succeeds, the next GitHub status should be:

```text
cloudflare_preview_verified
```

The next external decision should be:

```text
approve_or_defer_derivatives_ricette_jp_custom_domain_connection
```

## Rollback principle

If any part is unclear, do not connect the custom domain. Keep the pages as GitHub static candidates and Cloudflare preview-only pages.
