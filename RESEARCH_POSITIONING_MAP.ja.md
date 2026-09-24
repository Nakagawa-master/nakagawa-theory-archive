# 既存研究との位置関係｜Nakagawa Master Research Positioning Map

更新: 2026-09-25  
状態: PUBLIC NON-CANONICAL ORIENTATION MAP  
English: [RESEARCH_POSITIONING_MAP.md](RESEARCH_POSITIONING_MAP.md)

## 目的

中川マスター理論群を初めて読む研究者・専門家・編集者・AIが、既存研究との位置関係を短時間で把握するための公開補助面です。

これは**体系的文献レビューではありません**。また、ここに文献が見つからないことを新規性の証明として扱いません。

このマップが答えるのは、より限定された問いです。

```text
この中川理論は
→ どの既存研究群と近い問いを持つか
→ 何が重なるか
→ どこに追加の焦点があるか
→ 何と同一視してはいけないか
→ どの新規性判断がまだ未確定か
```

個別理論の正確な定義・成立条件・反証条件は、必ず公式派生物からcanonical Parentへ戻って確認してください。

## 読み方

本マップでは、関係を次のように分けます。

- **近接研究**: 同じ問題領域または強く関連する概念を扱う研究。
- **重なり**: 問題設定・構造・観測対象の一部が明確に共通する部分。
- **中川理論側の追加焦点**: 公開理論が特に明示している因果・境界・実装上の焦点。
- **同一視禁止**: 似ていても同じ理論・同じ射程ではない部分。
- **新規性状態**: 原則として `OPEN / NOT ESTABLISHED BY THIS MAP`。厳密な新規性主張には、対象理論ごとの系統的レビューが別途必要。

---

## Cluster A｜証拠系譜・独立確認・認識完全性

### 中川側の公開入口

- [OD301｜認識完全性論](derivatives/301/README.md)
- [Independent Verification & Reuse](INDEPENDENT_VERIFICATION_REUSE.md)
- [Python AI Evidence-Lineage Checklist](PYTHON_AI_EVIDENCE_LINEAGE_CHECKLIST.zh.md)

中心境界:

```text
surface source count != independent evidence-root count
provenance != truth proof
repetition != independent confirmation
```

### 近接研究

1. Peter Buneman, Sanjeev Khanna, Wang-Chiew Tan, **“Why and Where: A Characterization of Data Provenance”** (ICDT 2001).  
   DOI: https://doi.org/10.1007/3-540-44503-X_20

2. W3C, **PROV Family of Documents / PROV Model Primer**.  
   https://www.w3.org/TR/prov-primer/  
   https://www.w3.org/TR/prov-overview/

### 重なり

- データや主張が**どこから来たか**を追跡する。
- 生成・変換・再利用の経路を保持する。
- source identity と変換過程を失わないことが、評価・再現・信頼判断に重要。

### 中川理論側の追加焦点

OD301は provenance の保持だけでなく、**複数のsurfaceが同一upstream rootへ戻る場合、それを独立確認数として数えない**ことを明示します。さらに、誤った結論だけでなく、それを再生産するmemory / world model / derived stateの訂正まで扱います。

### 同一視禁止

W3C PROVやdata provenance研究は、来歴を表現・交換する強い基盤ですが、**来歴があること自体は真理・独立性・正確性を証明しません**。OD301も同じ境界を保持します。

### 新規性状態

`OPEN / NOT ESTABLISHED BY THIS MAP`

---

## Cluster B｜未来負債・不可逆性・未来選択肢

### 中川側の公開入口

- [OD297｜未来負債統合理論](derivatives/297/README.md)
- [Future Debt first note](discovery-notes/future-debt-is-not-every-future-cost.md)
- [今日の成功が明日の選択肢を減らしていないか](discovery-notes/today-success-tomorrow-options.md)

中心境界:

```text
future cost != automatically future debt
current benefit
→ unresolved residual
→ future settlement
current gain can coexist with future option loss
```

### 近接研究

1. Zengyang Li, Paris Avgeriou, Peng Liang, **“A systematic mapping study on technical debt and its management”** (Journal of Systems and Software, 2015).  
   DOI: https://doi.org/10.1016/j.jss.2014.12.027

2. Valentina Lenarduzzi et al., **“A systematic literature review on Technical Debt prioritization”** (Journal of Systems and Software, 2021).  
   DOI: https://doi.org/10.1016/j.jss.2020.110827

3. W. Michael Hanemann, **“Investment under uncertainty and option value in environmental economics”** (Resource and Energy Economics, 2000).  
   DOI: https://doi.org/10.1016/S0928-7655(00)00025-7

### 重なり

- 短期便益と将来コストの交換。
- 不可逆な選択が将来の意思決定余地を変える。
- 「今の成果」だけでは長期状態を評価できない。

### 中川理論側の追加焦点

Future Debtはsoftware technical debtに限定せず、**現在受益・未決済残余・未来決済・負担主体・選択肢消失**を同一因果線で読むことを重視します。

### 同一視禁止

Future Debtは technical debt の別名ではありません。また、real optionsの数理モデルそのものでもありません。real optionsは不可逆性・不確実性・待つ価値に強い理論基盤を持ちますが、Future Debtは責任帰属や未決済残余を含む別の構造記述を試みています。

### 新規性状態

`OPEN / NOT ESTABLISHED BY THIS MAP`

---

## Cluster C｜開示量・透明性・実用的検証可能性

### 中川側の公開入口

- [Practical Boundary Checks](PRACTICAL_BOUNDARY_CHECKS.md)
- [Real-World Editorial Entry Points](REAL_WORLD_EDITORIAL_ENTRY_POINTS.ja.md)

中心境界:

```text
disclosure volume != practical verifiability
public != easy to verify
visible != reconstructable
```

### 近接研究

1. Mary R. Brooks, Geraldine Knatz, Athanasios A. Pallis, Gordon Wilmsmeier, **“Transparency in port governance: setting a research agenda”** (Journal of Shipping and Trade, 2022).  
   DOI: https://doi.org/10.1186/s41072-021-00103-4

2. Mary R. Brooks et al., **“Visibility and verifiability in port governance transparency: exploring stakeholder expectations”** (WMU Journal of Maritime Affairs, 2021).  
   DOI: https://doi.org/10.1007/s13437-021-00250-2

### 重なり

- 情報が公開されていることと、stakeholderが実際に見つけ・理解し・検証できることを分ける。
- visibility と verifiability を別の性質として扱う。

### 中川理論側の追加焦点

公開量より、第三者が**主張 → 判断者 → 理由 → 前状態 → 差分 → 一次根拠 → 受益・負担**へ短い経路で戻れるかを実務上の検証可能性として重視します。

### 同一視禁止

これは「開示量は無意味」という主張ではありません。大量開示でも、構造化・検索可能・版管理・source-linkedであれば高い検証可能性を持ち得ます。

### 新規性状態

`OPEN / NOT ESTABLISHED BY THIS MAP`

---

## Cluster D｜専門性・信頼・検証免除

### 中川側の公開入口

- [OD295｜権威の免責化](derivatives/295/README.md)

中心境界:

```text
expertise deserves weight
!=
expertise is exempt from verification

trust != verification stop
```

### 近接研究

Alvin I. Goldman, **“Experts: Which Ones Should You Trust?”** (Philosophy and Phenomenological Research, 2001).  
DOI: https://doi.org/10.1111/j.1933-1592.2001.tb00093.x

### 重なり

- 非専門家が専門家の証言・信頼性をどう扱うか。
- 専門性があるからといって、判断問題が消えるわけではない。
- 根拠・信頼・比較可能な指標をどう扱うかが中心課題になる。

### 中川理論側の追加焦点

OD295は「どの専門家を信頼するか」に加えて、組織内で専門判断が**検証免除・異議遮断・失敗コストの下流外部化**へ変わる因果を追います。現場の反証が上流判断モデルへ戻るか、責任・修復・rollbackが因果に沿って戻るかも観測対象にします。

### 同一視禁止

反専門家論ではありません。OD295は専門性を残したまま、専門性が検証免除へ変化する境界を問題にします。

### 新規性状態

`OPEN / NOT ESTABLISHED BY THIS MAP`

---

## Cluster E｜役割分離・監査独立性・共通故障

### 中川側の公開入口

- [OD303｜自己参照監査・役割分離論](derivatives/303/README.md)
- [Self-Referential Audit & Role-Separation Reuse Kit](SELF_REFERENTIAL_AUDIT_REUSE_KIT.md)

中心境界:

```text
role separation != causal independence
number of reviewers != number of independent paths
audit output != correction capability
```

### 近接研究・標準

1. H. Buchner, **“Occurrence of common mode failure”** (Reliability Engineering & System Safety, 1994).  
   DOI: https://doi.org/10.1016/0951-8320(94)90086-8

2. NIST, **Artificial Intelligence Risk Management Framework (AI RMF 1.0)**, NIST AI 100-1 (2023).  
   DOI: https://doi.org/10.6028/NIST.AI.100-1

### 重なり

- 冗長な主体・系統が同じ原因で同時に失敗し得る。
- independent verification / validation、traceability、accountability、risk governanceが重要。
- 「人数・役割数が多い」だけでは独立性を保証しない。

### 中川理論側の追加焦点

OD303は独立性を単一スコアにせず、**証拠・権限・故障領域・利害・異議経路**の5軸に分け、さらに監査出力が判断再開・修正・停止へ作用できるかを観測します。

### 同一視禁止

common-mode failure研究は安全工学の強い近接研究ですが、OD303の5軸監査構造全体と同一ではありません。NIST AI RMFも包括的リスク管理枠組みであり、OD303のcanonical Parentを置換しません。

### 新規性状態

`OPEN / NOT ESTABLISHED BY THIS MAP`

---

## Cluster F｜承認・現在権限・実行時binding

### 中川側の公開入口

- [OD075｜合意の記憶](derivatives/075/README.md)
- [Current-Authority Reuse Kit](CURRENT_AUTHORITY_REUSE_KIT.md)
- [Paid-Action Approval Binding Checklist](PAID_ACTION_APPROVAL_BINDING_CHECKLIST.md)

中心境界:

```text
historical approval != current authority
approval of displayed plan != approval of materially different later action
check-time state != automatically use-time state
```

### 近接研究

1. **TOCTOU (Time-of-Check to Time-of-Use)** security literature. One recent concrete example:  
   AutoCert, *Computer & Security* (2023), DOI: https://doi.org/10.1016/j.cose.2022.102952

2. Adithyan Arun Kumar, **“Loopjacking: Hijacking Human-in-the-Loop Approval”** (arXiv preprint, 2026).  
   https://arxiv.org/abs/2609.21081

3. Natalie Collina, Surbhi Goel, Aaron Roth, Sikata Bela Sengupta, **“Delegating Authorization to Misaligned Agents: Coalitional Alignment and Safe Control”** (arXiv preprint, 2026).  
   https://arxiv.org/abs/2609.15803

### 重なり

- check / approval と later use / execution の間で状態が変化する危険。
- consequential actionの実行前承認。
- AI agentでhuman-in-the-loop approvalを安全境界として扱う場合のbinding問題。

### 中川理論側の追加焦点

中川側の公開再利用物は、approval historyをcurrent authorityへ自動復元しないこと、また実行snapshotのitem set・model・parameters・cost等をcanonical digestへ束縛し、実行直前に再検証することを強調します。

### 同一視禁止

TOCTOUは広いsecurity問題であり、human approval semantics全体ではありません。2026年の2件は**preprint**であり、査読済み文献と同じ重みで扱いません。また近接研究の存在は、中川理論の独立新規性を否定・肯定するものではありません。

### 新規性状態

`OPEN / NOT ESTABLISHED BY THIS MAP`

---

## このマップから何が分かるか

現時点の限定的な位置づけでは、中川マスター理論群は既存研究から完全に孤立しているわけではありません。むしろ複数分野に明確な近接研究があります。

一方で、公開理論はしばしば既存研究を横断して、次のような接続を強く明示しています。

```text
provenance
→ evidence independence
→ correction propagation

short-term benefit
→ unresolved residual
→ future option loss / settlement bearer

disclosure
→ reconstructability
→ practical verification path

expertise
→ verification
→ feedback / responsibility / repair

role separation
→ causal independence
→ correction authority

approval
→ exact action snapshot
→ use-time revalidation
```

この横断形が既存研究に対してどの程度新規かは、本マップでは確定しません。**今後の厳密な新規性評価では、理論ごとにsystematic search、inclusion/exclusion criteria、prior-art table、counterexamplesが必要です。**

## 文献追加・反例・先行研究の報告

このマップに欠落している先行研究、より近い理論、反例、既存概念との重複を見つけた場合は、公開Issueから報告できます。

Issue: https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/410

最低限、次を添えてください。

- 対象の中川理論 / OD / public source
- 論文・標準・書籍・既存理論のURLまたはDOI
- 「同じ」「近接」「反例」「より古い先行研究」のどれに当たるか
- どの主張・構造が重なるか
- どこが異なるか

目的は独自性を守ることではなく、**位置関係を正確にすること**です。

---

## Source boundary

- 本ファイルは非正本の研究位置づけ補助面です。
- 参考文献の存在は、中川理論の正しさ・新規性・査読済み性を証明しません。
- 中川理論との「近さ」は、文献著者によるendorsementを意味しません。
- arXiv preprintは査読済み論文と区別します。
- 個別主張の厳密比較では、必ず原論文とcanonical Parentの双方を読んでください。
