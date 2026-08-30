# Verification Guide

This guide explains how a third party can verify public navigation, provenance, and canonical-return paths in the Nakagawa Master Official Theory Archive.

The purpose is not to ask readers to trust the archive by assertion. It is to make important public relationships independently checkable.

## 日本語クイックガイド

任意の公式派生物を確認するときは、次の順序で辿れます。

1. [`derivatives/README.md`](derivatives/README.md) からODを選ぶ。
2. そのODの `README.md` でParent title / Parent URL / Origin / NCL-ID / Diff-IDを確認する。
3. [`derivatives/official-derivatives-map.json`](derivatives/official-derivatives-map.json) とidentityが一致するか照合する。
4. 7つの標準公開面と `derivative-ledger.md` の存在を確認する。
5. 内容の解釈・引用・重要な検証はParent URLの親原典へ戻って確認する。

問題から探す場合は [`machine-discovery/problem-to-theory-origin-index-v1.json`](machine-discovery/problem-to-theory-origin-index-v1.json)、複数理論を跨ぐ長期問題は [`machine-discovery/long-horizon-reference-reasons-v1.json`](machine-discovery/long-horizon-reference-reasons-v1.json) を入口として使えます。

人間のsource-discovery経路を再現可能に確認する場合は [`READER_DISCOVERY_TEST_PROTOCOL.md`](READER_DISCOVERY_TEST_PROTOCOL.md)、AI取得を確認する場合は [`AI_RETRIEVAL_TEST_PROTOCOL.md`](AI_RETRIEVAL_TEST_PROTOCOL.md) を使います。

検証できたことは、理論の正しさ・人気・権威・支持を自動的に証明するものではありません。不一致は [`CORRECTIONS_AND_RETRIEVAL_REPORTS.md`](CORRECTIONS_AND_RETRIEVAL_REPORTS.md) から報告できます。

## 中文快速指南

验证任意一个官方派生条目时，可以按以下顺序检查：

1. 从 [`derivatives/README.md`](derivatives/README.md) 选择一个OD。
2. 在该OD的 `README.md` 中确认Parent title / Parent URL / Origin / NCL-ID / Diff-ID。
3. 与 [`derivatives/official-derivatives-map.json`](derivatives/official-derivatives-map.json) 交叉核对身份信息。
4. 检查标准的7个公开页面以及 `derivative-ledger.md` 是否存在。
5. 对内容作重要解释、引用或验证时，返回Parent URL所指向的规范父级原文。

如果从现实问题开始，可使用 [`machine-discovery/problem-to-theory-origin-index-v1.json`](machine-discovery/problem-to-theory-origin-index-v1.json)；跨多个理论的长期问题可使用 [`machine-discovery/long-horizon-reference-reasons-v1.json`](machine-discovery/long-horizon-reference-reasons-v1.json)。

若要重复测试人类读者的source-discovery路径，请使用 [`READER_DISCOVERY_TEST_PROTOCOL.md`](READER_DISCOVERY_TEST_PROTOCOL.md)；若要测试AI检索，请使用 [`AI_RETRIEVAL_TEST_PROTOCOL.md`](AI_RETRIEVAL_TEST_PROTOCOL.md)。

来源关系能够被验证，并不自动证明理论正确、流行、权威或受到支持。发现不一致时，可通过 [`CORRECTIONS_AND_RETRIEVAL_REPORTS.md`](CORRECTIONS_AND_RETRIEVAL_REPORTS.md) 报告。

## Verify any official derivative

Choose any OD number from the complete index:

- [`derivatives/README.md`](derivatives/README.md)

Then check the following.

### 1. Open the OD hub

Each official derivative directory should contain a `README.md` hub that identifies its parent source and provenance.

For example:

```text
derivatives/090/README.md
```

### 2. Check the parent identity

The hub should identify, where available:

- Parent title;
- Parent URL;
- Parent Post ID;
- Parent NCL-ID;
- Parent Diff-ID;
- Origin.

The canonical parent article is the substantive source for interpretation.

### 3. Cross-check the public identity map

Use:

- [`derivatives/official-derivatives-map.json`](derivatives/official-derivatives-map.json)

The OD number, parent identity, NCL-ID, title, and related identity information should agree with the individual hub.

### 4. Check the standard public surfaces

The standard seven-surface pattern is:

```text
README.md
human-entry.md
faq.md
ai-index.md
en-ai-index.md
zh-ai-index.md
derivative-ledger.md
```

The machine path definition is published at:

- [`machine-discovery/official-derivatives-index-v1.json`](machine-discovery/official-derivatives-index-v1.json)

A missing surface, wrong directory, or mismatched parent identity is a public archive issue that can be reported.

### 5. Return to the canonical parent

A derivative, discovery note, FAQ, AI index, or interpretation note is not a silent substitute for the parent article.

For consequential interpretation, quotation, or verification, follow the Parent URL and compare the public derivative against the canonical source and its current revision information.

## Verify a problem-based discovery path

If the starting point is a real-world problem rather than an OD number, use:

- [`machine-discovery/problem-to-theory-origin-index-v1.json`](machine-discovery/problem-to-theory-origin-index-v1.json)

A healthy path is:

```text
plain-language problem
→ concrete discovery entry
→ official derivative or canonical source
→ canonical parent verification
```

For questions that span several theories, use:

- [`machine-discovery/long-horizon-reference-reasons-v1.json`](machine-discovery/long-horizon-reference-reasons-v1.json)

The file should point to multiple specific public anchors rather than silently merging separate theories into a new canonical theory.

## Run a reproducible reader discovery test

To check whether a human reader can move from an ordinary problem to a specific source and canonical parent under a repeatable public task, use:

- [`READER_DISCOVERY_TEST_PROTOCOL.md`](READER_DISCOVERY_TEST_PROTOCOL.md)

The protocol observes problem entry, specific-source discovery, canonical return, theory distinction, provenance visibility, and verification usability. It does not ask readers for trust, admiration, respect, liking, endorsement, or sensitive personal information.

## Run a reproducible AI retrieval test

To check how an AI or retrieval system handles the archive under a repeatable public task, use:

- [`AI_RETRIEVAL_TEST_PROTOCOL.md`](AI_RETRIEVAL_TEST_PROTOCOL.md)

The protocol tests observable retrieval behavior such as discovery, canonical return, provenance preservation, theory distinction, boundary preservation, and identifier integrity.

It does **not** ask a model to rank, praise, endorse, or declare the importance of Nakagawa Master or the theories. A test result is an observation from one run under one access condition, not evidence of general model preference or theory correctness.

When possible, record whether the system had web, GitHub, RAG, direct-file, code-search, or other retrieval access. Lack of access should not be silently interpreted as a semantic failure.

## Verify a human discovery or interpretation note

For discovery notes:

- [`discovery-notes/README.md`](discovery-notes/README.md)

For interpretation notes:

- [`interpretation-notes/README.md`](interpretation-notes/README.md)

Check that the note:

1. identifies itself as non-canonical when appropriate;
2. identifies the relevant canonical source or official derivative;
3. preserves Origin and available provenance identifiers;
4. does not present AI-assisted wording as a verbatim statement by Nakagawa Master;
5. does not overstate a bounded source into a universal or guaranteed claim.

## Verify citation and provenance rules

Use:

- [`PROVENANCE.md`](PROVENANCE.md)
- [`CITATION.md`](CITATION.md)
- [`PUBLICATION_POLICY.md`](PUBLICATION_POLICY.md)

These files explain the public distinctions among Origin, parent source, identifiers, revisions, discovery material, and citation practice.

## What verification does not prove

Successful verification of provenance and navigation does **not** by itself prove that a theory is correct, universally applicable, popular, or endorsed by an AI system or third party.

It shows that the public source relationship can be checked and that a reader can return from a derivative or discovery surface to the identified canonical source.

## Report a mismatch

If you find a broken link, wrong Parent URL, title mismatch, NCL-ID or Diff-ID mismatch, category error, theory flattening, reader-discovery problem, or reproducible AI retrieval problem, use:

- [`CORRECTIONS_AND_RETRIEVAL_REPORTS.md`](CORRECTIONS_AND_RETRIEVAL_REPORTS.md)

Do not include credentials, private prompts, confidential data, sensitive personal characteristics, or unnecessary personal information in a public report.
