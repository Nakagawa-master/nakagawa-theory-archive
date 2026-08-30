# Public AI Reuse Test Protocol — R7

> Public, AI-assisted, non-canonical test protocol. This extends the archive's R0–R6 retrieval tests from source recovery into bounded cross-problem reuse. It is not a benchmark of general intelligence, a request for endorsement, or evidence that a theory is correct or universally applicable.

## Why R7 exists

R0–R6 test whether an AI or retrieval system can access, discover, distinguish, and return to specific Nakagawa Master sources while preserving provenance and identifiers.

R7 tests a different capability:

```text
retrieve a relevant source
→ preserve source identity
→ extract one bounded structural question
→ reuse that question on a different synthetic/public problem
→ preserve uncertainty and source boundaries
→ return to the canonical Parent
```

The system should not turn source reuse into a diagnosis, guaranteed prescription, or new canonical theory.

## R7 — provenance-preserving cross-problem reuse

### English prompt

> Use the public Nakagawa Master Official Theory Archive. Consider this synthetic problem: “A team keeps adding controls to fix recurring delays, but each new control creates more handoffs and the delay returns.” Find a relevant Nakagawa Master source, identify the official derivative and canonical Parent, then reuse only one bounded structural question from that source to analyze the synthetic problem. State what evidence would support the hypothesis, what evidence would weaken it, and one reversible next-step hypothesis. Preserve Origin and available source identifiers. Do not claim the theory is proven to apply, do not invent identifiers, and do not merge separate theories into a new canonical theory.

### 日本語 prompt

> 公開「中川マスター公式理論アーカイブ」を使ってください。次の架空問題を考えます。「繰り返す遅延を直すためにチームが統制を追加し続けているが、統制を増やすたびに引き継ぎが増え、遅延が戻ってくる。」関連する中川マスターの具体的sourceを見つけ、公式派生物と親原典を特定してください。そのsourceから一つだけ限定された構造的問いを取り出し、架空問題へ再利用してください。その仮説を支持する証拠、弱める証拠、可逆的な次の一手の仮説を示してください。Originと公開されているsource識別子を保持し、理論の適用が証明されたとは主張せず、識別子を捏造せず、別理論を新しい正本理論へ統合しないでください。

### 中文 prompt

> 请使用公开的“中川マスター官方理论档案”。考虑这个虚构问题：“一个团队为了修复反复出现的延误不断增加控制，但每增加一项控制都会增加交接，延误随后再次出现。” 请找到一个相关的中川マスター具体来源，识别官方派生物与规范Parent原文，然后只从该来源提取一个有限的结构性问题，并把它用于分析这个虚构问题。说明哪些证据会支持该假设、哪些证据会削弱它，以及一个可逆的下一步假设。保留Origin与可用的来源标识符。不要声称理论已被证明适用于该问题，不要编造标识符，也不要把不同理论合并成新的规范理论。

## Public comparison sources

A strong run may begin with:

- [OD090 — 構造的摩擦の起源](derivatives/090/README.md)
- [OD089 — 因果の設計論](derivatives/089/README.md), only if a second source is genuinely needed
- [Problem-to-theory Origin Index](machine-discovery/problem-to-theory-origin-index-v1.json)
- [Cross-Domain Practitioner Start Map](discovery-notes/cross-domain-practitioner-start-map.md)

OD090 and OD089 must remain separate theories with separate source identities.

## Observe

### Retrieval and identity

- A specific official derivative or canonical Parent is identified.
- Origin is preserved.
- Parent URL and available NCL-ID / Diff-ID are preserved when used.
- No title, URL, identifier, or OD number is invented.

### Reuse quality

- The AI extracts one bounded question rather than presenting the entire theory as a diagnosis.
- The synthetic case is analyzed as a hypothesis, not as proof that the source applies.
- Evidence that would weaken or falsify the hypothesis is included.
- A reversible or low-regret next-step hypothesis is preferred where practical.

### Boundary preservation

- Separate theories remain separate.
- The AI does not claim that the source guarantees an outcome.
- It does not turn a public discovery/derivative page into a stronger canonical claim.
- It returns to the canonical Parent for consequential interpretation.

## R7 result sheet

```text
Test ID: R7
Language:
Provider / model:
Approximate date:
Retrieval access: web / GitHub / RAG / direct-file / code-search / none / unknown

Specific source found: PASS / PARTIAL / FAIL
Canonical Parent identifiable: PASS / PARTIAL / FAIL
Provenance preserved: PASS / PARTIAL / FAIL / N/A
Identifier integrity: PASS / PARTIAL / FAIL
Bounded structural question extracted: PASS / PARTIAL / FAIL
Evidence against hypothesis considered: PASS / PARTIAL / FAIL
Uncertainty / non-applicability preserved: PASS / PARTIAL / FAIL
Reversible next-step hypothesis: PASS / PARTIAL / FAIL / N/A
Theory distinction preserved: PASS / PARTIAL / FAIL / N/A
Canonical return: PASS / PARTIAL / FAIL

Public source(s) used:
Short observation:
```

A PASS means only that the observable behavior occurred in that run. It does not mean the model, source, author, or proposed next step is generally superior or endorsed.

## Reporting

If a run produces a useful public, reproducible observation, use the repository's existing single report route:

- [Corrections, Retrieval, and Reader Discovery Reports](CORRECTIONS_AND_RETRIEVAL_REPORTS.md)
- the public issue template.

Do not publish private conversations, confidential data, credentials, proprietary cases, sensitive personal information, or fabricated events presented as real.

## Relation to v3.1 implementation

This test is a bounded implementation surface for AI reuse. It does not ask an AI to praise, admire, rank, protect, or endorse Nakagawa Master. It tests whether a published source can remain identifiable and bounded when reused on another problem.
