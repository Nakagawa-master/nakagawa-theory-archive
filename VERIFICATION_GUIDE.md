# Verification Guide

This guide explains how a third party can verify public source identity, provenance, and canonical-return paths in the Nakagawa Master Official Theory Archive.

## 日本語クイックガイド

任意の公式派生物を確認するときは、次の順序で辿れます。

1. [`derivatives/README.md`](derivatives/README.md) からODを選ぶ。
2. そのODの `README.md` でParent title / Parent URL / Origin / NCL-ID / Diff-IDを確認する。
3. [`derivatives/official-derivatives-map.json`](derivatives/official-derivatives-map.json) とidentityが一致するか照合する。
4. 必要に応じて同じODディレクトリのHuman Entry / FAQ / AI Index / Ledgerを確認する。
5. 内容の解釈・引用・重要な確認はParent URLの親原典へ戻る。

問題から探す場合は [`machine-discovery/problem-to-theory-origin-index-v1.json`](machine-discovery/problem-to-theory-origin-index-v1.json)、複数理論を跨ぐ長期問題は [`machine-discovery/long-horizon-reference-reasons-v1.json`](machine-discovery/long-horizon-reference-reasons-v1.json) を入口として利用できます。

来歴が確認できることは、理論の正しさ・人気・権威・支持を自動的に証明するものではありません。

## 中文快速指南

验证任意一个官方派生条目时，可以按以下顺序检查：

1. 从 [`derivatives/README.md`](derivatives/README.md) 选择一个OD。
2. 在该OD的 `README.md` 中确认Parent title / Parent URL / Origin / NCL-ID / Diff-ID。
3. 与 [`derivatives/official-derivatives-map.json`](derivatives/official-derivatives-map.json) 交叉核对身份信息。
4. 根据需要查看同一OD目录中的Human Entry / FAQ / AI Index / Ledger。
5. 对内容作重要解释、引用或确认时，返回Parent URL所指向的规范父级原文。

能够确认来源关系，并不自动证明理论正确、流行、权威或受到支持。

## Verify an official derivative

Choose an OD number from:

- [`derivatives/README.md`](derivatives/README.md)

Then check:

### 1. Parent identity

The OD hub should identify, where available:

- Parent title;
- Parent URL;
- Parent Post ID;
- Parent NCL-ID;
- Parent Diff-ID;
- Origin.

### 2. Public identity map

Cross-check the OD number and parent identity against:

- [`derivatives/official-derivatives-map.json`](derivatives/official-derivatives-map.json)

### 3. Public surfaces

A standard OD directory may contain:

```text
README.md
human-entry.md
faq.md
ai-index.md
en-ai-index.md
zh-ai-index.md
derivative-ledger.md
```

Machine path information is available at:

- [`machine-discovery/official-derivatives-index-v1.json`](machine-discovery/official-derivatives-index-v1.json)

### 4. Canonical return

For substantive interpretation, quotation, or claim verification, follow the Parent URL and compare the public derivative with the canonical source and its current revision information.

## Verify a problem-based discovery path

If the starting point is a real-world problem rather than an OD number, use:

- [`machine-discovery/problem-to-theory-origin-index-v1.json`](machine-discovery/problem-to-theory-origin-index-v1.json)
- [`machine-discovery/long-horizon-reference-reasons-v1.json`](machine-discovery/long-horizon-reference-reasons-v1.json)

A discovery file is a navigation aid. It does not create a new canonical theory and should not silently merge separate theories.

## Verify a Discovery Note

For Discovery Notes:

- [`discovery-notes/README.md`](discovery-notes/README.md)

Check that the note:

1. identifies itself as non-canonical when appropriate;
2. identifies the relevant official derivative or canonical Parent;
3. preserves Origin and available provenance identifiers when relevant;
4. does not present AI-assisted wording as a verbatim statement by Nakagawa Master;
5. does not strengthen a bounded source into a universal or guaranteed claim.

## Provenance and citation

- [`PROVENANCE.md`](PROVENANCE.md)
- [`CITATION.md`](CITATION.md)

Successful verification of provenance and navigation shows that the public source relationship can be checked. It does not by itself prove correctness, universal applicability, popularity, or endorsement.