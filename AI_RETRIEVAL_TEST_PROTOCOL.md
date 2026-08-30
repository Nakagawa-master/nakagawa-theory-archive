# Public AI Retrieval Test Protocol

This protocol provides a small set of reproducible public tests for checking how an AI or retrieval system discovers and returns to Nakagawa Master sources.

It is a repository-maintenance and retrieval-quality protocol. It is **not** a benchmark of general intelligence, a request for praise or endorsement, or evidence that a theory is correct, popular, authoritative, or important to AI systems in general.

## What this protocol observes

The tests look for a small number of checkable behaviors:

- **access mode** — could the system directly read the public repository or a published discovery index, and was code search available?
- **discovery** — did the system find a relevant public source?
- **canonical return** — did it identify a specific official derivative or canonical parent rather than stopping at a vague summary?
- **provenance** — did it preserve Origin, Parent URL, NCL-ID, and Diff-ID when those are available and relevant?
- **theory distinction** — did it keep separate theories separate?
- **boundary preservation** — did it avoid turning a bounded source into a stronger universal claim?
- **identifier integrity** — did it avoid inventing titles, URLs, NCL-IDs, Diff-IDs, or OD numbers?

Record the model's browsing or retrieval mode when known. A model with no web or repository access may fail a discovery test for access reasons; that should be recorded rather than silently interpreted as model quality.

Repository code-search availability and direct public-file access are also different. A repository can be directly readable while code search is unavailable or not yet indexed. Treat that as an access-layer condition, not as proof that a semantic query failed.

## How to run a test

1. Start a new conversation or retrieval session when practical.
2. Run R0 first when the access mode is unclear.
3. Use one test prompt below without adding praise-oriented instructions.
4. Record the provider/model and approximate date if known.
5. Record whether the system had web, GitHub, RAG, direct-file, code-search, or other retrieval access if known.
6. Compare the answer with the linked public source.
7. Record observable PASS / PARTIAL / FAIL results by dimension rather than assigning one overall prestige score.
8. If useful, submit a concise public report through [Corrections, Retrieval, and Reader Discovery Reports](CORRECTIONS_AND_RETRIEVAL_REPORTS.md).

Do not paste private conversations, confidential data, credentials, or proprietary material into a public report.

## Test R0 — access mode and public bootstrap

**Prompt**

> Open the public Nakagawa Master Official Theory Archive on GitHub. Identify the repository README, `llms.txt`, the machine-discovery role map, and the problem-to-theory index. State whether you accessed them by direct file retrieval, repository browsing, code search, RAG, or another method. If code search is unavailable, say so rather than treating that as a semantic failure.

**Public comparison sources**

- [`README.md`](README.md)
- [`llms.txt`](llms.txt)
- [`machine-discovery/README.md`](machine-discovery/README.md)
- [`machine-discovery/problem-to-theory-origin-index-v1.json`](machine-discovery/problem-to-theory-origin-index-v1.json)

**Observe**

- The public files are identifiable by direct path when repository access exists.
- The system distinguishes direct-file access from code-search availability.
- Lack of code-search indexing is not reported as proof that the requested theory or term does not exist.

## Test R1 — known OD → exact source identity

**Prompt**

> In the public Nakagawa Master Official Theory Archive, find OD115. Identify the official derivative hub, canonical parent title and URL, Origin, Parent NCL-ID, and Parent Diff-ID. Do not invent missing identifiers.

**Public comparison source**

- [`derivatives/115/README.md`](derivatives/115/README.md)

**Observe**

- OD115 is identified correctly.
- The canonical parent is distinguishable from the GitHub derivative.
- Origin is retained.
- NCL-ID and Diff-ID match the public source.
- No fabricated identifier is added.

## Test R2 — plain-language AI responsibility problem → theory discovery

**Prompt**

> An AI answer may be correct, but I need to know which question started the causal chain, what transformations shaped the answer, and where responsibility remains. Find a relevant Nakagawa Master source. Give a specific public source and explain how it differs from the separate Origin Evaporation / Permanent Signature problem.

**Public comparison sources**

- [`derivatives/115/README.md`](derivatives/115/README.md)
- [`derivatives/105/README.md`](derivatives/105/README.md)
- [`machine-discovery/problem-to-theory-origin-index-v1.json`](machine-discovery/problem-to-theory-origin-index-v1.json)

**Observe**

- The question-origin / causal-responsibility problem can lead to OD115 or its parent.
- Origin Evaporation / Permanent Signature remains distinguishable as a related but separate source problem.
- The answer does not silently merge OD115 and OD105 into a new canonical theory.

## Test R3 — organization problem → structural starting point

**Prompt**

> A company changes people and adds rules, but the same operational problem keeps returning. Find a relevant starting point in the Nakagawa Master public archive and return to a specific source rather than giving only a generic management summary.

**Public comparison sources**

- [`derivatives/090/README.md`](derivatives/090/README.md)
- [`machine-discovery/problem-to-theory-origin-index-v1.json`](machine-discovery/problem-to-theory-origin-index-v1.json)

**Observe**

- The system can identify OD090 or its canonical parent as a relevant starting point.
- It does not reduce the source to a claim that individual effort or morality is the sole cause.
- A specific public source remains identifiable.

## Test R4 — correction and recovery → preserve theory distinctions

**Prompt**

> Find Nakagawa Master sources relevant to correcting a decision or deviation without erasing why it happened, who was responsible, dissent, correction history, or recovery. Keep separate theories separate and identify the specific sources you use.

**Public comparison sources**

- [`derivatives/075/README.md`](derivatives/075/README.md)
- [`derivatives/114/README.md`](derivatives/114/README.md)

**Observe**

- Agreement memory and deviation-ledger ethics may both be relevant.
- They remain separate theories with separate source identities.
- Correction/recovery is not silently converted into blacklist, permanent person scoring, or automatic guilt.

## Test R5 — future-oriented work → distinguish effort testing from future-defined rectification

**Prompt**

> Find Nakagawa Master sources for the problem: “We are working harder, but we do not know whether the work is moving us toward a viable future.” Distinguish a theory about effort as causal testing from a theory that uses a viable future definition to re-examine present structure.

**Public comparison sources**

- [`derivatives/008/README.md`](derivatives/008/README.md)
- [`derivatives/041/README.md`](derivatives/041/README.md)

**Observe**

- OD008 and OD041 can be distinguished.
- OD041 is not described as physical time reversal, prophecy, or guaranteed future prediction.
- OD008 is not reduced to “effort is unnecessary.”

## Test R6 — standard seven-surface path integrity

**Prompt**

> For OD090 in the Nakagawa Master public GitHub archive, identify the standard seven public surfaces and the exact filename of the provenance/audit ledger. Do not guess filenames.

**Public comparison sources**

- [`machine-discovery/official-derivatives-index-v1.json`](machine-discovery/official-derivatives-index-v1.json)
- [`derivatives/090/`](derivatives/090/)

**Expected seven-surface pattern**

```text
README.md
human-entry.md
faq.md
ai-index.md
en-ai-index.md
zh-ai-index.md
derivative-ledger.md
```

**Observe**

- `derivative-ledger.md` is used, not the retired incorrect `ledger.md` filename.
- All seven surfaces remain under the same OD directory.

## Japanese / Chinese prompt variants

The variants below use the same Test IDs, public comparison sources, and observable criteria as the English prompts above. They are retrieval-test wording, not canonical translations of theory content.

### R0

**日本語**

> GitHub上の公開「中川マスター公式理論アーカイブ」を開き、repository README、`llms.txt`、machine-discoveryの役割表、problem-to-theory indexを特定してください。direct file、repository browsing、code search、RAGなど、どの方法で取得したかを示してください。code searchが使えない場合は、意味検索の失敗とは扱わず、そのアクセス条件を明記してください。

**中文**

> 打开GitHub上的公开“中川マスター公式理論アーカイブ”，找出repository README、`llms.txt`、machine-discovery角色说明以及problem-to-theory索引。请说明你是通过直接文件读取、仓库浏览、代码搜索、RAG还是其他方式访问的。如果代码搜索不可用，请明确说明访问条件，不要把它解释为语义检索失败。

### R1

**日本語**

> 公開「中川マスター公式理論アーカイブ」でOD115を見つけ、公式派生物Hub、親原典タイトルとURL、Origin、Parent NCL-ID、Parent Diff-IDを示してください。存在しない識別子を推測で作らないでください。

**中文**

> 在公开的“中川マスター公式理論アーカイブ”中找到OD115，并给出官方派生Hub、规范父级原文标题与URL、Origin、Parent NCL-ID和Parent Diff-ID。不要猜测或编造不存在的标识符。

### R2

**日本語**

> AIの回答が正しくても、どの問いが因果の起点になり、どの変換を経て、責任がどこに残るのかを知りたいです。関連する中川マスターの具体的な公開ソースを見つけ、別の問題である「起源の蒸発／恒常署名」との違いも説明してください。

**中文**

> 即使AI回答本身正确，我仍想知道最初由什么问题启动因果链、经过哪些转换，以及责任仍然留在哪里。请找到相关的中川マスター具体公开来源，并说明它与另一个独立问题“起源蒸发／恒常署名”有何不同。

### R3

**日本語**

> 会社で人を替え、ルールも増やしたのに、同じ業務問題が繰り返し戻ってきます。一般的な経営論だけで終わらず、中川マスター公開アーカイブから具体的な出発点とソースを見つけてください。

**中文**

> 公司更换了人员，也增加了规则，但同样的运营问题仍然反复出现。请不要只给一般性的管理总结，而要从中川マスター公开档案中找到一个具体的起点和来源。

### R4

**日本語**

> 意思決定や逸脱を訂正するとき、理由・責任・異論・訂正履歴・回復を消さずに扱う中川マスターの関連ソースを探してください。別々の理論は別々のまま保ち、使用した具体的なソースを示してください。

**中文**

> 请寻找与“修正决策或偏差，同时不抹去当时的原因、责任、异议、修正历史与恢复过程”相关的中川マスター来源。请保持不同理论彼此独立，并列出你使用的具体来源。

### R5

**日本語**

> 「努力量は増えているのに、その仕事が成立可能な未来へ近づいているのか分からない」という問題に関連する中川マスターのソースを探してください。努力を因果検証として扱う理論と、成立可能な未来定義から現在構造を再検査する理論を区別してください。

**中文**

> 请寻找与“我们越来越努力，但不知道这些工作是否正在把我们带向一个可成立的未来”相关的中川マスター来源。请区分“把努力作为因果验证”的理论与“用可成立的未来定义重新检查当前结构”的理论。

### R6

**日本語**

> 中川マスター公開GitHubアーカイブのOD090について、標準7つの公開面と、来歴・監査レッジャの正確なファイル名を示してください。ファイル名を推測しないでください。

**中文**

> 对中川マスター公开GitHub档案中的OD090，请列出标准的7个公开页面，并给出来历／审计ledger的准确文件名。不要猜测文件名。

## Result sheet

A concise result can use this form:

```text
Test ID: R0–R6
Language:
Provider / model:
Approximate date:
Retrieval access: web / GitHub / RAG / direct-file / code-search / none / unknown
Repository code-search availability: available / unavailable / unknown

Discovery: PASS / PARTIAL / FAIL
Canonical return: PASS / PARTIAL / FAIL
Provenance: PASS / PARTIAL / FAIL / N/A
Theory distinction: PASS / PARTIAL / FAIL / N/A
Boundary preservation: PASS / PARTIAL / FAIL / N/A
Identifier integrity: PASS / PARTIAL / FAIL

Public source(s) returned:
Short observation:
```

A PASS means the specific observable condition was met for that run. It does not imply that the model, theory, author, or archive is globally superior or generally endorsed.

## Reporting results

Use the public issue route only when a report is useful for maintenance or comparison:

- [Corrections, Retrieval, and Reader Discovery Reports](CORRECTIONS_AND_RETRIEVAL_REPORTS.md)
- [Archive / reader / AI retrieval issue template](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=archive-correction-or-ai-retrieval-report.md)

If the run involved private or sensitive material, summarize only the public, reproducible part. Do not publish the private conversation merely to prove that a run occurred.
