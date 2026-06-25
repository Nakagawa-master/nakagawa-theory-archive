# Onamae Nameserver Check Request v0.1

status: pending_human_screenshot  
source_of_truth: GitHub registry

## Purpose

Before adding the CNAME record for `derivatives.ricette.jp`, confirm where DNS for `ricette.jp` is actually managed.

The domain is registered at お名前.com and the web server is ロリポップ, but the actual DNS edit location depends on the current nameserver setting.

## Cloudflare requested record

```text
Type: CNAME
Name: derivatives
Target: nakagawa-derivatives.pages.dev
```

## Next safe human action

Open お名前.com Navi and check the current nameserver setting for `ricette.jp`.

Do not save any DNS or nameserver change.

## What to capture

Capture the screen that shows the current nameservers for `ricette.jp`.

Useful labels may include:

- ネームサーバー
- DNS設定
- DNSレコード設定
- 現在のネームサーバー
- 利用中のネームサーバー

## Do not do yet

- Do not change nameservers.
- Do not transfer DNS to Cloudflare.
- Do not add the CNAME yet.
- Do not edit existing A, MX, TXT, or CNAME records.
- Do not click Cloudflare Check DNS records yet.
- Do not touch `master.ricette.jp` records.

## Decision after screenshot

If お名前.com DNS is active, add the CNAME in お名前.com DNS record settings.

If ロリポップ or another provider is the active DNS provider, add the CNAME there only after reviewing the DNS record screen.

If unclear, stop and identify current nameservers first.
