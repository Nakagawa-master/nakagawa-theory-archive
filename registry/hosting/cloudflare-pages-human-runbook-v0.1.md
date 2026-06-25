# Cloudflare Pages Human Runbook v0.1

status: review_only_before_external_action  
source_of_truth: GitHub registry  
project: Pilot 001 static derivative publication path

## Purpose

This runbook prepares the human-facing steps for publishing official static derivative pages through Cloudflare Pages under `derivatives.ricette.jp`.

It does not perform any external action by itself.

## Current architecture

- Origin site: `master.ricette.jp`
- Derivative hub candidate: `derivatives.ricette.jp`
- Repository: `Nakagawa-master/nakagawa-theory-archive`
- Production branch candidate: `main`
- Static output directory: `static`
- WordPress role: origin articles only
- GitHub role: registry, static output, sitemap source of truth
- Cloudflare Pages role: static delivery layer

## Candidate settings for later Cloudflare Pages setup

- Repository: `Nakagawa-master/nakagawa-theory-archive`
- Branch: `main`
- Build command: none / empty / no build
- Output directory: `static`
- Environment variables: none required for Pilot 001
- Custom domain candidate: `derivatives.ricette.jp`

## Required confirmation before any external action

1. Nakagawa Master confirms `derivatives.ricette.jp` as the derivative hub domain.
2. Nakagawa Master confirms Cloudflare Pages as the static delivery route.
3. The preview deployment is checked before custom domain activation.
4. Custom domain and DNS changes are performed only after explicit approval.
5. Final sitemap generation happens only after public URL confirmation.
6. Search Console action happens only after final sitemap confirmation.

## First external setup phase, not yet executed

1. Open Cloudflare dashboard.
2. Create or select a Pages project.
3. Connect GitHub repository.
4. Select `Nakagawa-master/nakagawa-theory-archive`.
5. Select production branch `main`.
6. Set output directory to `static`.
7. Leave build command empty if Cloudflare allows, or use no-build equivalent.
8. Deploy to Cloudflare preview or pages.dev URL.
9. Check the five Pilot 001 pages on the preview URL.

## Second external setup phase, not yet executed

1. Add custom domain `derivatives.ricette.jp`.
2. Confirm DNS or CNAME guidance shown by Cloudflare.
3. Apply DNS only after explicit approval.
4. Confirm that public URLs resolve.
5. Confirm page content, parent URL, parent NCL-ID, and parent Diff-ID.

## Blocked until explicit approval

- Cloudflare Pages project creation if account action is required
- Custom domain connection
- DNS change
- Public route activation
- Final sitemap generation
- Search Console action
- WordPress derivative post creation

## Pilot 001 note

Deviation Ledger full automation is not a prerequisite for Pilot 001 publication.  
The Deviation Ledger remains a separate recovery and review system connected to the origin article and derivative hub when appropriate.

## Rollback principle

If anything is unclear, keep the state as GitHub-only static candidates and do not activate public routing.
