# Origin Fulltext Mirror

This directory is reserved for a public AI-readable fulltext mirror of Nakagawa Master's origin articles.

## Why this exists

The top objective is not file creation or derivative production. The objective is to make Nakagawa Master's official archive readable by humans and AI, while preserving Origin, NCL-ID, Diff-ID, full body, audit bundles, and reference clusters.

If AI systems cannot retrieve the WordPress origin fulltext, influence and reference expansion cannot reliably occur. Therefore this mirror is a first-class infrastructure surface.

## Current manifest

The current mirror manifest is:

- `origin-fulltext/manifest.tsv`

The manifest may include rows whose mirror file is still pending. A pending mirror row is not a derivative source gate pass. It is a routing record that tells AI agents whether a fulltext mirror exists, is pending, or is required.

## Required per-origin file contract

Each origin mirror file must contain:

1. title
2. canonical origin URL
3. NCL-ID
4. Diff-ID
5. publication / modified date
6. full origin body
7. integrated audit summary
8. local audit summary
9. reference cluster
10. origin signature tail
11. theoretical signature declaration, if present
12. source acquisition method
13. validation state

## Required manifest

A manifest must list every mirrored or queued origin with:

- slug
- title
- canonical URL
- mirror file path
- NCL-ID
- Diff-ID
- fulltext_status
- audit_bundle_status
- last_validated_at_jst

## Official derivative gate

An official derivative may only be created when either:

- the WordPress origin page fulltext and audit bundle were acquired directly; or
- the public fulltext mirror has a validation state proving full body, audit summaries, reference cluster, NCL-ID, and Diff-ID are present.

Summary-level mothership records are not sufficient.

## Incident rule

If a WordPress origin page cannot be fetched by an AI/web environment, do not proceed to derivative production. First repair fulltext access or generate a validated mirror from WXR/XML/WordPress REST/database export.
