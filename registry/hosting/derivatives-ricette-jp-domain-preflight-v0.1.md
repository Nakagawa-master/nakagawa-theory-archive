# derivatives.ricette.jp Domain Preflight v0.1

status: ready_for_custom_domain_preflight  
source_of_truth: GitHub registry  
preview_url: https://nakagawa-derivatives.pages.dev  
custom_domain_candidate: derivatives.ricette.jp

## Purpose

This document defines the final preflight before connecting `derivatives.ricette.jp` to the Cloudflare Pages project.

It does not authorize Search Console action, noindex removal, final sitemap generation, or WordPress changes.

## Current verified state

- Cloudflare Pages project exists.
- Preview URL exists: `https://nakagawa-derivatives.pages.dev`
- Preview pages load correctly.
- Return navigation has been added to the five Pilot 001 derivative pages.
- Candidate / preview labels remain visible.
- `noindex,nofollow` remains intentionally active.
- WordPress remains origin-only.
- GitHub remains the source of truth.

## Custom domain target

- Target domain: `derivatives.ricette.jp`
- Intended role: derivative hub domain
- Origin site remains: `master.ricette.jp`
- Parent article remains: `https://master.ricette.jp/theory/nakagawa-master-nakagawa-os-layer-specification-v1/`

## Human checks before clicking Add custom domain

1. Confirm the Cloudflare Pages project is `nakagawa-derivatives`.
2. Confirm the preview URL is `https://nakagawa-derivatives.pages.dev`.
3. Confirm output directory is `static`.
4. Confirm production branch is `main`.
5. Confirm pages load on preview URL.
6. Confirm `derivatives.ricette.jp` is the intended custom domain.
7. Confirm this is not a root-domain migration and does not affect `master.ricette.jp`.

## Allowed next external action

Only this action is allowed next:

```text
Cloudflare Pages project
→ Custom domains
→ Add custom domain
→ enter derivatives.ricette.jp
```

## Still blocked after adding custom domain

Even after adding the custom domain, the following remain blocked until separate confirmation:

- manual DNS or CNAME changes, if Cloudflare asks for them
- noindex/nofollow removal
- index/follow transition
- final sitemap generation
- Search Console action
- WordPress derivative post creation
- FTP upload

## What to capture after adding the custom domain

After entering `derivatives.ricette.jp`, capture the next Cloudflare screen. It may show one of the following:

- domain is pending verification
- CNAME or DNS instruction
- automatic activation
- ownership or zone warning
- error message

Do not proceed past that screen without review.

## Rollback principle

If Cloudflare shows unclear DNS instructions, stop and keep `nakagawa-derivatives.pages.dev` as the preview-only route.
