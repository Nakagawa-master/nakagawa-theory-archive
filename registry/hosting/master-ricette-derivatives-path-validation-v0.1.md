# master.ricette.jp/derivatives/ Path Validation v0.1

status: pending_lolipop_folder_check  
source_of_truth: GitHub registry

## Purpose

Validate whether official derivative static HTML pages can be served under:

```text
https://master.ricette.jp/derivatives/
```

This path is now the first candidate for canonical official derivative pages because it preserves the semantic relationship between origin articles and official derivative pages.

## Why this validation is needed

The previous Cloudflare Pages route is technically successful, but it places official derivative pages outside the official archive domain structure.

The preferred semantic placement is:

```text
master.ricette.jp
  ├─ origin articles
  ├─ glossary
  ├─ theory maps
  ├─ deviation ledger
  └─ derivatives/
      └─ official derivative pages
```

## Validation target

Create a very small test page only after the public folder is confirmed:

```text
/derivatives/test/index.html
```

Expected URL:

```text
https://master.ricette.jp/derivatives/test/
```

## Test file content concept

The test file should be minimal and clearly marked as a route test:

```html
<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="robots" content="noindex,nofollow">
  <title>derivatives route test</title>
</head>
<body>
  <h1>derivatives route test</h1>
  <p>This is a temporary route validation file for master.ricette.jp/derivatives/.</p>
</body>
</html>
```

## Required checks before upload

1. Confirm the Lolipop public folder for `master.ricette.jp`.
2. Confirm whether a physical `derivatives/` folder can be created under that public folder.
3. Confirm that this will not overwrite any existing WordPress file or directory.
4. Confirm that WordPress rewrite rules do not immediately capture or block `/derivatives/test/`.
5. Upload only the test file.
6. Keep the test page `noindex,nofollow`.
7. Do not submit anything to Search Console.

## Do not do yet

- Do not upload all Pilot 001 derivative pages.
- Do not remove noindex.
- Do not generate final sitemap.
- Do not submit Search Console.
- Do not change DNS.
- Do not connect `derivatives.ricette.jp`.
- Do not delete or modify WordPress files.

## Success condition

The following URL loads the test page:

```text
https://master.ricette.jp/derivatives/test/
```

and the origin site remains unaffected.

## If successful

Next phase:

1. Prepare official derivative static output path mapping.
2. Adjust canonical URLs from pages.dev to `master.ricette.jp/derivatives/`.
3. Prepare manual FTP deployment package for Pilot 001.
4. Verify live pages.
5. Then prepare final sitemap candidate.

## If failed

Keep Cloudflare pages.dev as staging and re-evaluate deployment route without touching DNS.
