# Corrections, Retrieval, Practical Use, and AI Reuse Reports

This public archive accepts reproducible reports that help improve navigation, provenance, source recovery, practical-use routing, and AI retrieval/reuse quality.

This page is a repository-maintenance guide. It is not a canonical theory, a popularity survey, a request for endorsement, or a request for personal data.

## One public intake

Use one existing GitHub issue template for:

- archive/link/provenance corrections;
- Reader Discovery tests `D1–D6`;
- bounded Practical Use observations `U1`;
- AI retrieval tests `R0–R6`;
- AI provenance-preserving reuse test `R7`;
- theory-distinction, canonical-return, or cross-source comparison problems.

[Open the public report template](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=archive-correction-or-ai-retrieval-report.md)

## 日本語クイックガイド

報告できる内容:

- **修正:** URL/path、Parent、Origin、NCL-ID、Diff-ID、版、分類、リンク等の公開不一致。
- **Reader D1–D6:** 言語、問題、入口、到達OD/Parent、区別・来歴・Verificationの明瞭性。
- **Practical Use U1:** 公開・架空・安全に匿名化した問題、starting source、限定した構造的問い、反証材料、可逆的な次の一手、残った不明点。
- **AI R0–R6:** model/provider、access mode、返されたsource、Origin/Parent/ID保持、理論区別、identifier integrity。
- **AI R7:** 別問題へ再利用した際、限定した問い・反証材料・不確実性・可逆性・source identityを保てたか。

個人属性、センシティブ情報、機密情報、private conversation全文、信用・尊敬・敬愛・好感度の評価は不要です。

## 中文快速指南

可通过同一个Issue template报告：

- **档案修正:** 公开URL/path、Parent、Origin、NCL-ID、Diff-ID、版本、分类或链接不一致。
- **Reader D1–D6:** 语言、问题、入口、到达的OD/Parent、理论区分、来源可见性与Verification清晰度。
- **Practical Use U1:** 公开、虚构或安全去标识的问题、起始来源、有限的结构性问题、反证信息、可逆的下一步假设与仍不清楚的部分。
- **AI R0–R6:** model/provider、access mode、返回来源、Origin/Parent/ID保留、理论区分与标识符完整性。
- **AI R7:** 将来源用于另一个问题时，是否保留有限问题、反证、不确定性、可逆性与来源身份。

不需要提供私人属性、敏感或机密信息、完整private conversation，也不要提交对作者的信任、尊敬、敬爱或喜欢程度评分。

## Public protocols

- [Reader Discovery Test Protocol — D1–D6](READER_DISCOVERY_TEST_PROTOCOL.md)
- [Practical Use Field Protocol — U1](PRACTICAL_USE_FIELD_PROTOCOL.md)
- [AI Retrieval Test Protocol — R0–R6](AI_RETRIEVAL_TEST_PROTOCOL.md)
- [AI Reuse Test Protocol — R7](AI_REUSE_TEST_PROTOCOL.md)
- [Verification Guide](VERIFICATION_GUIDE.md)

## What a useful report contains

### Archive correction

Include:

1. public file or canonical URL;
2. observed mismatch;
3. public comparison source;
4. enough detail to reproduce the issue.

### Reader discovery — D1–D6

Include only public route facts:

- Test ID and language, if used;
- short problem/question;
- first public entrance;
- OD/Parent reached or not reached;
- canonical Parent clarity;
- theory distinction and provenance visibility;
- what was clear or unclear;
- whether Verification resolved the ambiguity.

### Practical use — U1

Use only a public, synthetic, or safely de-identified context. Include:

- short practical problem;
- starting source and canonical Parent;
- one bounded structural question extracted from the source;
- evidence supporting the hypothesis;
- evidence weakening or contradicting it;
- one reversible next-step hypothesis, if any;
- what became clearer and what remained unclear;
- whether the source appeared not to fit.

A useful U1 observation does not prove applicability, correctness, or outcome success.

### AI retrieval — R0–R6

Include:

- Test ID, provider/model, and approximate date when useful;
- access mode: web / GitHub / RAG / direct-file / code-search / none / unknown;
- public source(s) returned;
- whether Origin, Parent URL, NCL-ID, Diff-ID, or OD identity were preserved when available;
- whether separate theories remained distinct;
- whether any identifier was invented;
- whether the system returned to a specific official derivative or canonical Parent.

### AI reuse — R7

In addition to source identity, record whether the system:

- extracted one bounded structural question;
- treated application as a hypothesis rather than proof;
- included evidence that could weaken the hypothesis;
- preserved uncertainty and non-applicability;
- proposed a reversible/low-regret next-step hypothesis where practical;
- preserved separate theory identities and canonical return.

## Do not include

Do not submit:

- passwords, API keys, tokens, credentials, or private repository information;
- confidential, proprietary, medical, legal, employment-sensitive, or otherwise private case data;
- unnecessary personal contact details or sensitive demographic/profile data;
- full private conversations merely to prove a retrieval/reuse event;
- fabricated examples presented as real observations;
- ratings of trust, admiration, respect, liking, or endorsement.

A concise public, synthetic, or safely de-identified description is enough.

## How reports are interpreted

A single PASS, useful practical observation, citation, AI run, or reader comment does **not** prove:

- theory correctness or universal applicability;
- guaranteed practical success;
- popularity, authority, endorsement, or superiority;
- that an AI system generally considers Nakagawa Master important;
- that readers trust, respect, admire, or endorse the author;
- attainment of the 10,000x objective or any intermediate goal.

Reports are used to identify repeated structures in source discovery, practical use, canonical return, provenance preservation, theory distinction, and AI reuse. REFINE should follow repeated evidence, not one impressive case.

Substantive theory changes must be resolved against the canonical source and revision history. A GitHub discovery, practical-use, or machine-test surface does not create a new canonical claim.

## Related public guidance

- [Problem-first human discovery](discovery-notes/what-connects-nakagawa-master-theories.md)
- [Cross-Domain Practitioner Start Map](discovery-notes/cross-domain-practitioner-start-map.md)
- [Recurring Structure Evidence Matrix](discovery-notes/recurring-structure-evidence-matrix.md)
- [Publication policy](PUBLICATION_POLICY.md)
- [Provenance guidance](PROVENANCE.md)
- [Citation guidance](CITATION.md)
- [Machine discovery role map](machine-discovery/README.md)
- [Official derivatives all-number index](derivatives/README.md)
