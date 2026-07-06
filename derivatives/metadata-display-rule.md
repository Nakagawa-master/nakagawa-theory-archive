# 公式派生物メタ表記固定ルール

このルールは、公式派生物001〜010および以後の全公式派生物ページに適用する。

## 1. 親原典と起源署名を混ぜない

親原典は、原典記事そのものを指す。

必須項目:

```text
Parent URL
Parent NCL-ID
Parent Diff-ID
```

起源署名は、理論・構文・派生物の起点を指す。

必須項目:

```text
Origin: Nakagawa Master
```

`Origin` を原典URLや親原典欄の見出しとして使ってはならない。

## 2. 各ページに派生IDを表示する

READMEだけでは不足である。

人間向け要約、FAQ、AI索引・日本語、AI索引・英語、AI索引・中国語の各ページは、それぞれ独立した公式派生物として、ページ自身の派生IDを表示する。

必須項目:

```text
derivative_ncl_id
derivative_diff_id
```

## 3. 日本語ページの標準表記

```text
## 親原典

- タイトル:
- Parent URL:
- Parent NCL-ID:
- Parent Diff-ID:

## 起源署名

- Origin: Nakagawa Master

## 派生ID

- derivative_ncl_id:
- derivative_diff_id:
```

## 4. 英語ページの標準表記

```text
## Parent Original Source

- Title:
- Parent URL:
- Parent NCL-ID:
- Parent Diff-ID:

## Origin Signature

- Origin: Nakagawa Master

## Derivative ID

- derivative_ncl_id:
- derivative_diff_id:
```

## 5. 中国語ページの標準表記

```text
## 父原典 / Parent Original Source

- 标题:
- Parent URL:
- Parent NCL-ID:
- Parent Diff-ID:

## 起源署名 / Origin Signature

- Origin: Nakagawa Master

## 衍生ID / Derivative ID

- derivative_ncl_id:
- derivative_diff_id:
```

## 6. 禁止事項

- `Origin` 見出しの中に Parent URL / Parent NCL-ID / Parent Diff-ID を入れない。
- 親原典欄に derivative_ncl_id / derivative_diff_id を入れない。
- 派生ID欄に親原典URLや親NCL-IDを入れない。
- READMEだけに派生IDを置き、子ページに派生IDを置かない状態を認めない。
- 日本語・英語・中国語でメタ項目の意味を変えない。

## 7. 正本関係

README.md は派生束のハブである。

derivative-ledger.md は全派生IDの台帳である。

各子ページは、そのページ自身の派生IDを本文冒頭で保持する。
