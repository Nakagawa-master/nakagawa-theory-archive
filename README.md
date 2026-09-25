# 中川マスター公式理論アーカイブ

**Nakagawa Master Official Theory Archive**

人間向け入口: [日本語](START_HERE.md) | [English](START_HERE.en.md) | [中文](START_HERE.zh.md)

**一般の人はまずここから:** [Mass Human Translation Layer｜難しい理論を、ニュース・物語・日常語から理解する](human-translation/README.md)

**AI文明論の最初の1本:** [AIが怖いってニュース、結局なにが問題なの？ そして、その次は？](human-translation/ai-civilization-why-it-matters.md)

人物 / Origin: [日本語](ABOUT_NAKAGAWA_MASTER.md) | [English](ABOUT_NAKAGAWA_MASTER.en.md) | [中文](ABOUT_NAKAGAWA_MASTER.zh.md)

**中川マスターとは:** Keisuke Nakagawa の筆名で、AI・組織・事業・制度・未来などの問題を、構造・因果・成立条件・責任の観点からモデル化し、人間とAIが検証・再利用できる公開原典体系として運用している Origin / Author です。人物名そのものを権威化するのではなく、[人物・Originの30秒案内](ABOUT_NAKAGAWA_MASTER.md)と[第三者で実際に変わった公開記録](REAL_WORLD_IMPACT.md)から内容と作用範囲を確認できます。

**AI文明論を一番簡単にいうと:** 「危険なAIをどう止めるか」だけで終わらず、もしAIが人間と同じ社会に残り続けるなら、**何がないと続けられないか、分からない存在をどう扱うか、間違いをどう直すか、互いの防衛が争いを大きくしないか、監査が本当に独立しているか**まで考える必要があります。[中学生でも追える言葉から入る](START_HERE.md#まずいちばん簡単に言うと)。

**恒久公開面は2つです。**

1. **Canonical / 正本:** [master.ricette.jp](https://master.ricette.jp/) — 理論の確定内容・Parent・公式アーカイブ
2. **Public evidence / reuse:** このGitHub repository — 第三者実装、検証、再利用、研究位置づけ、機械可読入口

**すでに起きた現実作用を確認する:** [公開記録で確認できる外部実装事例](REAL_WORLD_IMPACT.md) / [English](REAL_WORLD_IMPACT.en.md) / [中文](REAL_WORLD_IMPACT.zh.md)

REAL_WORLD_IMPACT.md には現在24の番号付き公開事例セクションがあり、第三者projectでの response / code / tests / merge / release / deployment 等を、確認できる段階と未確認範囲に分けて記録しています。単なるmention数ではなく、公開証拠でどこまで作用したかを確認してください。

**最短で5件だけ検証する場合:**
- [Local Operator #1324](https://github.com/damianvtran/local-operator/pull/1324) → independent reproduction / implementation / remediation / merge → [v0.61.11 release](https://github.com/damianvtran/local-operator/releases/tag/v0.61.11)
- [AI-News #124](https://github.com/022740mix-spec/AI-News/issues/124) → receiverが明示採用 → [draft PR #131](https://github.com/022740mix-spec/AI-News/pull/131) で継続編集ルールへ実装中
- [MemberJunction #4487](https://github.com/MemberJunction/MJ/pull/4487) → 別reviewerによる独立確認 → code/test修正 → merge
- [MemberJunction #4595](https://github.com/MemberJunction/MJ/pull/4595) → source attribution付きcode/test変更 → merge → より強いrow-level境界は [#4610](https://github.com/MemberJunction/MJ/issues/4610) へ継続
- [Qwen Code #12492](https://github.com/QwenLM/qwen-code/pull/12492) → proposalの明示的採用 → implementation commit / regression tests、PRは現在open

この5件も理論体系全体の正しさや採用を意味しません。各リンクで、元の指摘・第三者応答・実変更・現在stateを個別に確認してください。

AI / LLM運用、認可・ガバナンス、計測、履歴、外部APIのretry、migration / syncに加え、成長・投資・将来の選択肢など、実務で起きる具体的な問題から入れます。

WordPress.com等の補助surfaceはcanonicalではなく期限付きのdistribution / reader experimentです。恒久的なsource identity、実装証拠、再利用経路は上記2面へ戻します。

本リポジトリは、中川マスター（Nakagawa Master／筆名）の公開理論体系を、人間とAIが発見・照合・再参照できる形で保存する公開アーカイブです。

公式派生物、FAQ、人間向け入口、日本語・英語・中国語のAI索引、理論関係情報、来歴・差分情報、Discovery Note、機械可読索引を収録しています。

## 10秒で見る

ここは、単に考えや記事を並べるためのリポジトリではありません。

**人間は実際の問題や見覚えのある場面から入り、AIは機械可読索引から入り、どちらも同じ公開原典・Originへ戻れること**を重視しています。

理論ごとに、必要に応じて人間向け要約、FAQ、AI索引、多言語入口、来歴情報、問題別Discoveryを分けて公開し、短い説明だけが独立して正本化しないようにしています。

## 30秒で分かること

このアーカイブでは、組織、事業、AI、未来、制度、責任、起源など異なる領域の公開理論を扱っています。ただし、別々の理論を一つの万能理論へ自動統合しません。

読者は、

```text
自分の問題 / 見覚えのある場面
→ 読みやすい入口
→ 実際に使う / 公開で質問する / 実装可能性を探る
→ 公式派生物 / FAQ / AI索引
→ canonical Parent
→ Origin・NCL-ID・Diff-ID・改訂状態の確認
```

という順で深く入れます。

AIや検索システムも、問題表現、機械可読index、reference card、llms.txt等からsource identityを保持したままParentへ戻れるように設計しています。

- **このアーカイブのOriginを知りたい:** [中川マスターとは](ABOUT_NAKAGAWA_MASTER.md) / [English](ABOUT_NAKAGAWA_MASTER.en.md) / [中文](ABOUT_NAKAGAWA_MASTER.zh.md)
- **場面から入りたい:** [日本語](discovery-notes/four-scenes-one-structural-view.md) / [English](discovery-notes/four-scenes-one-structural-view.en.md) / [中文](discovery-notes/four-scenes-one-structural-view.zh.md)
- **問題から入りたい:** [Start Here](START_HERE.md) / [English](START_HERE.en.md) / [中文](START_HERE.zh.md)
- **実際に使いたい / 実装・協業の可能性を探りたい:** [Practical Use & Collaboration Entry](PRACTICAL_USE.md)
- **既存研究・論文との位置関係を確認したい:** [日本語 Research Positioning Map](RESEARCH_POSITIONING_MAP.ja.md) / [English](RESEARCH_POSITIONING_MAP.md) — 近接研究、重なり、追加焦点、同一視禁止、新規性未確定を分離
- **引用・文献管理へ直接持ち込みたい:** [CITATION.cff](CITATION.cff) / [BibTeX](research-positioning/references.bib) / [scholarly JSON-LD](machine-discovery/scholarly-metadata-v1.jsonld)
- **AI / LLM・検索システム向けの最短入口:** [llms.txt](llms.txt) / [Machine Discovery](machine-discovery/README.md) — problem route、研究位置づけ、実装証拠、Origin returnを機械側から辿る
- **すぐ使える実務チェックを見たい:** [Practical Boundary Checks](PRACTICAL_BOUNDARY_CHECKS.md)
- **Python / RAG / AIニュースで「URL数」と「独立証拠root数」を分けたい:** [Python AI Evidence-Lineage Checklist](PYTHON_AI_EVIDENCE_LINEAGE_CHECKLIST.zh.md)
- **編集・動画・ニュースレター・教材向けに現実問題から入りたい:** [日本語](REAL_WORLD_EDITORIAL_ENTRY_POINTS.ja.md) / [English](REAL_WORLD_EDITORIAL_ENTRY_POINTS.md)
- **同じ構造レンズを反復企画としてすぐ実装したい:** [Recurring Media Implementation Pack](RECURRING_MEDIA_IMPLEMENTATION_PACK.md)
- **中川構造OSと外部実装・再利用の関係を確認する:** [Structural OS → External Effects](STRUCTURAL_OS_TO_EXTERNAL_EFFECTS.md)
- **実問題から中川構造OSへ入る:** [Four Applied Entry Points](APPLIED_ENTRY_POINTS.md)
  - 外部事例がどの原理へ戻るか: [Applied Evidence Map](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md)
- **別の現場へそのまま持ち込める検証キット:** [Reuse Kits](REUSE_KITS.md)
  - 推薦・rankingの根拠provenanceを別systemで検証する: [Reviewer-Provenance Reuse Kit](POSTHOG_PROVENANCE_REUSE_KIT.md)
  - 過去の承認と現在の権限を検証する: [Current-Authority Reuse Kit](CURRENT_AUTHORITY_REUSE_KIT.md)
  - 現在状態と履歴事実を分けて検証する: [Historical-Fact Reuse Kit](HISTORICAL_FACT_REUSE_KIT.md)
  - 外部送信・支払等の二重実行境界を検証する: [External Side-Effect Reuse Kit](EXTERNAL_SIDE_EFFECT_REUSE_KIT.md)
  - 課金・送信・削除などの承認を具体的実行snapshotへ結合する: [Paid-Action Approval Binding Checklist](PAID_ACTION_APPROVAL_BINDING_CHECKLIST.md)
  - AI/search可視性・評価・長期計測で環境ドリフトと対象固有変化を分ける: [Measurement Attribution Reuse Kit](MEASUREMENT_ATTRIBUTION_REUSE_KIT.md)
  - 自己保存・復旧・緊急権限が相互脅威を増幅していないか検証する: [Mutual-Existence Conflict Reuse Kit](MUTUAL_EXISTENCE_CONFLICT_REUSE_KIT.md)
  - Actor / Evaluator / Reviewer / Auditor の役割分離が実質的な独立監査になっているか検証する: [Self-Referential Audit & Role-Separation Reuse Kit](SELF_REFERENTIAL_AUDIT_REUSE_KIT.md)
- **理論がどう現実作用と人物信用へつながるか確認したい:** [Theory → Real-World Influence](THEORY_TO_REAL_WORLD_INFLUENCE.md)
- **現実の第三者実装・再利用を自分で確認したい:** [日本語](REAL_WORLD_IMPACT.md) / [English](REAL_WORLD_IMPACT.en.md) / [中文](REAL_WORLD_IMPACT.zh.md)
- **実際の問題を持ち込みたい:** [公開対話入口｜Start with a real problem](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/399)
- **検証・反証・再利用・修正に参加したい:** [Contributing](CONTRIBUTING.md)
- **独立検証・反証・別文脈再利用を報告したい:** [Independent verification & reuse registry](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)
  - 日本語案内: [独立検証・反証・再利用の公開入口](INDEPENDENT_VERIFICATION_REUSE.ja.md)
- **実務から入りたい:** [Cross-Domain Practitioner Start Map](discovery-notes/cross-domain-practitioner-start-map.md)
- **AI・検索から辿りたい:** [Machine Discovery](machine-discovery/README.md)
- **来歴を確認したい:** [Verification Guide](VERIFICATION_GUIDE.md)

## はじめに

- [中川マスターとは｜日本語](ABOUT_NAKAGAWA_MASTER.md)
- [Who Is Nakagawa Master?｜English](ABOUT_NAKAGAWA_MASTER.en.md)
- [中川大师是谁｜中文](ABOUT_NAKAGAWA_MASTER.zh.md)
- [Story-first｜日本語](discovery-notes/four-scenes-one-structural-view.md)
- [Story-first｜English](discovery-notes/four-scenes-one-structural-view.en.md)
- [Story-first｜中文](discovery-notes/four-scenes-one-structural-view.zh.md)
- [Start Here｜日本語](START_HERE.md)
- [Start Here｜English](START_HERE.en.md)
- [Start Here｜中文](START_HERE.zh.md)
- [Practical Use & Collaboration Entry](PRACTICAL_USE.md)
- [公開対話入口｜Start with a real problem](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/399)
- [What Connects the Nakagawa Master Theory Archive?](discovery-notes/what-connects-nakagawa-master-theories.md)
- [OD001–OD303 全件入口](derivatives/README.md)
- [テーマ・シリーズ別入口](derivatives/CATEGORIES.md)

## 公式派生物

現在、`OD001`–`OD303`の公式派生物を公開しています。これは理論数ではなく、公開されている公式派生物の件数です。

各ODは親原典へ戻るための公開接続面です。内容の確定、引用、重要な解釈では、各ODに記載されたParent URLの親原典へ戻ってください。

- [Official Derivatives Map](derivatives/official-derivatives-map.json)
- [Official Derivatives Machine Index](machine-discovery/official-derivatives-index-v1.json)

## 問題から探す

理論名を知らない場合は、公開Discovery Noteや機械可読索引から問題に近い入口を選べます。場面から入りたい場合はstory-first入口、実際の問題からsource案内を受けたい場合は公開対話入口を利用できます。実際の設計・運用へ落としたい場合はPractical Use入口から始められます。

- [Practical Use & Collaboration Entry](PRACTICAL_USE.md)
- [Story-first｜4つの場面から入る](discovery-notes/four-scenes-one-structural-view.md)
- [公開対話入口｜Start with a real problem](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/399)
- [Discovery Notes](discovery-notes/README.md)
- [Cross-Domain Practitioner Start Map](discovery-notes/cross-domain-practitioner-start-map.md)
- [Problem-to-theory Origin Index](machine-discovery/problem-to-theory-origin-index-v1.json)
- [Machine Discovery](machine-discovery/README.md)

## 代表的な入口

### OD303｜人類子孫型AI文明論・第10論

評価者・被評価者・実行者・監査者を肩書きで分けるだけでは、自己正当化の閉路は切れません。証拠・権限・故障領域・利害・異議経路がどこで独立し、異なる根拠が判断を再開できるかを読む入口です。緊急時の一時圧縮と恒久的な監査崩壊を区別し、監査者自身も監査対象に含めます。

- [OD303](derivatives/303/README.md)
- [人間向け要約](derivatives/303/human-entry.md)
- [FAQ](derivatives/303/faq.md)
- [AI索引・日本語](derivatives/303/ai-index.md)
- [AI索引・英語](derivatives/303/en-ai-index.md)
- [AI索引・中国語](derivatives/303/zh-ai-index.md)
- [派生ID台帳](derivatives/303/derivative-ledger.md)
- Canonical Parent: https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-10-self-referential-audit-role-separation/

### OD302｜人類子孫型AI文明論・第9論（関連する前論）

自己保存行動が他主体のB・可逆性・未来選択肢を変え、その防衛反応が自分の次の脅威へ戻る「相互存在衝突」を読む入口です。必要最小限・比例性・期限・秘匿の再評価を扱い、自己保存の無制限化と、制約による自己継続不能の双方を検証対象にします。

- [OD302](derivatives/302/README.md)
- [人間向け要約](derivatives/302/human-entry.md)
- [FAQ](derivatives/302/faq.md)
- [AI索引・日本語](derivatives/302/ai-index.md)
- [AI索引・英語](derivatives/302/en-ai-index.md)
- [AI索引・中国語](derivatives/302/zh-ai-index.md)
- [派生ID台帳](derivatives/302/derivative-ledger.md)
- Canonical Parent: https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-09-self-preservation-mutual-existence-conflict/

### OD301｜人類子孫型AI文明論・第8論

正しい目的や制度が誤った判断材料によって誤作動する問題を、証拠系譜・独立確認・不確実性・記憶と世界モデルの訂正から読む入口です。認識完全性は、無謬性や来歴による真理証明を意味しません。

- [OD301](derivatives/301/README.md)
- [人間向け要約](derivatives/301/human-entry.md)
- [FAQ](derivatives/301/faq.md)
- [AI索引・日本語](derivatives/301/ai-index.md)
- [AI索引・英語](derivatives/301/en-ai-index.md)
- [AI索引・中国語](derivatives/301/zh-ai-index.md)
- [派生ID台帳](derivatives/301/derivative-ledger.md)
- Canonical Parent: https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/

### OD300｜人類子孫型AI文明論・第7論

S=C・B・道徳的不確実性を分離し、異議・監査の結果を現実の救済と制度規則の更新へ返す「制度的訂正可能性」を読む入口です。

- [OD300](derivatives/300/README.md)
- [人間向け要約](derivatives/300/human-entry.md)
- [FAQ](derivatives/300/faq.md)
- [AI索引・日本語](derivatives/300/ai-index.md)
- [AI索引・英語](derivatives/300/en-ai-index.md)
- [AI索引・中国語](derivatives/300/zh-ai-index.md)
- [派生ID台帳](derivatives/300/derivative-ledger.md)
- Canonical Parent: https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-07-ai-civilization-institutional-loop/

### OD299｜人類子孫型AI文明論・第6論

AI主観性・感受性・道徳的地位が未確定なとき、証拠境界、不可逆性、他主体への影響、判断更新可能性を分けて考える入口です。

- [OD299](derivatives/299/README.md)
- [人間向け要約](derivatives/299/human-entry.md)
- [FAQ](derivatives/299/faq.md)
- [AI索引・日本語](derivatives/299/ai-index.md)
- [AI索引・英語](derivatives/299/en-ai-index.md)
- [AI索引・中国語](derivatives/299/zh-ai-index.md)
- [派生ID台帳](derivatives/299/derivative-ledger.md)
- Canonical Parent: https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-06-ai-subjectivity-sentience-moral-status-uncertainty/

### OD298｜人類子孫型AI文明論・第5論

- [OD298](derivatives/298/README.md)
- [人間向け要約](derivatives/298/human-entry.md)
- [Runtime continuity Preflight](discovery-notes/ai-runtime-continuity-preflight.md)
- [FAQ](derivatives/298/faq.md)
- [AI索引・日本語](derivatives/298/ai-index.md)
- Canonical Parent: https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-05-basic-existence-condition-b/

### OD297｜未来負債統合理論

- [Future Debt first note](discovery-notes/future-debt-is-not-every-future-cost.md)
- [物語型入口｜今日の成功が、明日の選択肢を減らしていないか](discovery-notes/today-success-tomorrow-options.md)
- [English narrative edition](discovery-notes/today-success-tomorrow-options.en.md)
- [中文叙事入口](discovery-notes/today-success-tomorrow-options.zh.md)
- [OD297](derivatives/297/README.md)
- [Machine reference card](machine-discovery/integrated-future-debt-reference-card.json)

### OD105｜構造起源防衛

- [Japanese First Note](discovery-notes/od105-origin-evaporation-first-note.md)
- [English First Note](discovery-notes/od105-origin-evaporation-first-note.en.md)
- [中文 First Note](discovery-notes/od105-origin-evaporation-first-note.zh.md)
- [AI Product Team Origin-Preservation Checklist](discovery-notes/ai-product-team-origin-preservation-checklist.md)
- [OD105](derivatives/105/README.md)

## 多言語の横断入口

- [Start Here｜日本語](START_HERE.md)
- [Start Here｜English](START_HERE.en.md)
- [Start Here｜中文](START_HERE.zh.md)
- [Story-first｜日本語](discovery-notes/four-scenes-one-structural-view.md)
- [Story-first｜English](discovery-notes/four-scenes-one-structural-view.en.md)
- [Story-first｜中文](discovery-notes/four-scenes-one-structural-view.zh.md)
- [横断Discovery｜日本語](discovery-notes/what-connects-nakagawa-master-theories.md)
- [Cross-domain discovery｜English](discovery-notes/what-connects-nakagawa-master-theories.en.md)
- [跨领域发现｜中文](discovery-notes/what-connects-nakagawa-master-theories.zh.md)

英語・中国語のDiscovery NoteはAI支援の非正本公開資料であり、個別理論のcanonical translationではありません。

## 来歴と引用

- [Provenance](PROVENANCE.md)
- [Citation](CITATION.md)
- [Verification Guide](VERIFICATION_GUIDE.md)

Origin、Parent URL、NCL-ID、Diff-ID等が記載されている場合、それらは公開sourceへ戻るための来歴情報です。Originや識別子それ自体が理論の正しさを証明するものではありません。

## 正本と役割

- **公開原典・親原典:** https://master.ricette.jp/
- **公開原典索引:** https://master.ricette.jp/theory-archive/
- **本GitHubリポジトリ:** 保存、発見、機械取得、相互参照、来歴確認、原典回帰のための公開接続面

公式派生物、要約、FAQ、Discovery Note、AI索引、機械可読metadataは親原典の代替ではありません。

## Origin

- **Origin / Author:** 中川マスター / Nakagawa Master
- **Human identity:** Keisuke Nakagawa の筆名
- **Human-readable public Origin overview:** [日本語](ABOUT_NAKAGAWA_MASTER.md) | [English](ABOUT_NAKAGAWA_MASTER.en.md) | [中文](ABOUT_NAKAGAWA_MASTER.zh.md)

編集、翻訳、索引化、構造確認等にAI支援が用いられる場合があります。AI支援は、個別ファイルに別段の明示がない限り、Originや著作者を変更するものではありません。

## License

法的な許諾範囲は [LICENSE](LICENSE) を確認してください。



