# 派生NCL管理基盤 第一段階

## 目的

このディレクトリ群は、master.ricette.jp の公式アーカイブ原典記事から生まれる派生コンテンツを、WordPress DBではなく GitHub 上で管理するための正本DB基盤である。

公式アーカイブ側では、記事本文・NCL-ID・Diff-ID・差分履歴・起源署名・用語タグを保持する。派生コンテンツの本体・台帳・生成プロンプト・公開先・状態管理は GitHub 側に置く。

## 基本方針

```text
WordPress = 原典表示面
GitHub = 派生NCL正本DB
外部媒体 = 公開先
静的JSON = WordPress表示用の索引
```

## 守ること

1. 原典記事との紐付けを切らない。
2. 親NCL-IDと親Diff-IDを必ず記録する。
3. WordPress DBに派生物の本体を大量保存しない。
