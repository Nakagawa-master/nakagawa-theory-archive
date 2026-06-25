# Lolipop master.ricette.jp derivatives route test runbook v0.1

status: ready_for_manual_ftp_route_test  
source_of_truth: GitHub registry

## Purpose

Test whether official derivative static HTML can be served under:

```text
https://master.ricette.jp/derivatives/
```

without DNS changes, without Cloudflare custom domain connection, and without creating WordPress posts.

## Test file in GitHub

```text
deploy/lolipop/master-ricette/derivatives/test/index.html
```

## Intended upload destination

Upload this file to the public folder used by `master.ricette.jp` on Lolipop, preserving this relative path:

```text
derivatives/test/index.html
```

If the public folder for `master.ricette.jp` is, for example:

```text
/path/to/master-public/
```

then the final server path should become:

```text
/path/to/master-public/derivatives/test/index.html
```

## Expected URL

```text
https://master.ricette.jp/derivatives/test/
```

## Required checks before upload

1. Confirm the public folder for `master.ricette.jp` in Lolipop.
2. Confirm no existing `derivatives/` directory is used by WordPress or another system.
3. Create only `derivatives/test/` if it does not exist.
4. Upload only `index.html` from the test package.
5. Do not upload Pilot 001 derivative pages yet.
6. Do not remove noindex.
7. Do not generate final sitemap.
8. Do not submit Search Console.
9. Do not change DNS.

## Success condition

The route test page loads at:

```text
https://master.ricette.jp/derivatives/test/
```

and the existing master.ricette.jp WordPress site remains unaffected.

## If successful

Next phase:

1. Mark `master_derivatives_route_test` as successful.
2. Prepare Pilot 001 official derivative pages for the `master.ricette.jp/derivatives/` path.
3. Update canonical URLs from staging paths to `master.ricette.jp/derivatives/...`.
4. Prepare a small manual FTP deployment package.
5. Verify live pages before sitemap or Search Console.

## If failed

Do not force changes. Record the failure and keep `nakagawa-derivatives.pages.dev` as staging while reassessing routing.

## Blocked actions

- DNS changes
- Cloudflare Check DNS records
- derivatives.ricette.jp connection
- noindex transition
- Search Console submission
- final sitemap generation
- bulk FTP upload
- WordPress derivative post creation
