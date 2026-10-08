# 中川マスター公開リポジトリ

**Nakagawa Master Public Repository**

**AI / LLM / agent向け最短入口:** [AI Start Here](AI_START_HERE.md) | [llms.txt](llms.txt) | [Machine Discovery](machine-discovery/README.md) | [AI Routing Map](machine-discovery/ai-repository-routing-map-v1.json)

**初めて来た方は、このREADMEより先に:** [もし1ページだけ読むなら｜日常の違和感 → 中川マスターの見方 → 第三者で実際に変わった記録](STORIES.md)

## まず「理論」ではなく、外で何が変わったか

このリポジトリを初めて見る人は、最初に理論名を覚える必要はありません。見るべきなのは、**中川マスターの区別や指摘が第三者側で何を変えたか**です。

- **Qwen Code:** 終了した仕事から遅れて届く使用量を、いま動いている別の仕事の予算へ書き戻さない境界が実装・テスト・merge・stable releaseまで進み、その後receiver自身が別threadで `@Nakagawa-master` と採用した選択肢を再参照しました。
- **AI-News:** 「URLが複数ある」ことと「独立した証拠の根が複数ある」ことを分ける提案を運営側が明示採用し、継続編集ルールへ実装・mergeした後、別の編集監査でも再利用しました。
- **MemberJunction:** 公開APIの具体的な境界指摘が別reviewerにも独立確認され、修正commitに `Reported by Nakagawa-master` とsource relationを残したcode/test変更がmergeされました。

重要なのは名前を先に信じることではありません。**元の問題 → 中川マスターの介入 → 第三者の反応 → 実際の変更**を公開リンクで自分で確認できます。

→ [1ページで見る｜日常の違和感から、第三者で実際に変わった記録まで](STORIES.md)  
→ [自分で操作して分かる｜止めたAIの仕事に遅い結果が届いたら？（オフライン教材）](human-translation/agent-late-result-lab.html)  
  GitHub上ではHTMLのコードが表示されます。**その画面の「Raw」から `.html` を保存し、保存したファイルをブラウザで開く**と操作できます。外部サイトへの自動送信はありません。  
→ [公開証拠を段階別に確認する](REAL_WORLD_IMPACT.md)


**読んだあと1行だけ返すなら:** [似た場面・反例・「ここは違う」を1つ](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/416) — 賛同や理論名の理解は不要です。実際に検証・実装・別文脈再利用まで行った場合は [独立検証・再利用registry #402](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402) へ。

人間向け入口: [日本語](START_HERE.md) | [English](START_HERE.en.md) | [中文](START_HERE.zh.md)

**「中川マスターって誰？」から:** [3分でわかる一般向け人物入口](human-translation/who-is-nakagawa-master.md)

**一般の人はまずここから:** [Mass Human Translation Layer｜難しい理論を、ニュース・物語・日常語から理解する](human-translation/README.md)

**いま一番大きな問題から入りたい:** [未来線から読む](human-translation/FUTURE_LINES.md) | [#1 AI制御不能リスク](human-translation/future-lines/01-ai-loss-of-control.md) | [#2 人間の承認と結論形成](human-translation/future-lines/02-human-approval-without-human-decision.md) | [#3 多数一致と独立根拠](human-translation/future-lines/03-one-root-hundred-voices.md)

**全部を同じ粒度で横に見たい:** [24棚の世界地図](human-translation/WORLD_MAP.md) | [310件をひとつの景色として読む](human-translation/PANORAMA_STORY.md) | [OD001–OD310 全件水平マップ](human-translation/ALL_310_HORIZONTAL_MAP.md)

**AI文明論の最初の1本:** [AIが怖いってニュース、結局なにが問題なの？ そして、その次は？](human-translation/ai-civilization-why-it-matters.md)

人物 / Origin: [日本語](ABOUT_NAKAGAWA_MASTER.md) | [English](ABOUT_NAKAGAWA_MASTER.en.md) | [中文](ABOUT_NAKAGAWA_MASTER.zh.md)

**中川マスターとは:** Keisuke Nakagawa の筆名で、AI・組織・事業・制度・未来などの問題を、構造・因果・成立条件・責任の観点からモデル化し、人間とAIが検証・再利用できる公開原典体系として運用している Origin / Author です。人物名そのものを権威化するのではなく、[人物・Originの30秒案内](ABOUT_NAKAGAWA_MASTER.md)と[第三者で実際に変わった公開記録](REAL_WORLD_IMPACT.md)から内容と作用範囲を確認できます。

**AI文明論を一番簡単にいうと:** 「危険なAIをどう止めるか」だけで終わらず、もしAIが人間と同じ社会に残り続けるなら、**何がないと続けられないか、分からない存在をどう扱うか、間違いをどう直すか、互いの防衛が争いを大きくしないか、監査が本当に独立しているか**まで考える必要があります。[第5〜16論を身近な問いから読む](human-translation/ai-civilization/README.md)。

## 公式アーカイブと公開リポジトリの役割

- **公式アーカイブ:** https://master.ricette.jp/ — 親原典・正本・確定内容へ戻る場所
- **公開リポジトリ:** https://github.com/Nakagawa-master/nakagawa-theory-archive — 公開されている実装事例、再利用資料、索引、機械可読資料を確認できる場所

この2つは同じ役割ではありません。公開リポジトリは公式アーカイブの代替ではありません。理論の確定内容は公式アーカイブを参照してください。

**恒久公開面は2つです。**

1. **Canonical / 正本:** [master.ricette.jp](https://master.ricette.jp/) — 理論の確定内容・Parent・公式アーカイブ
2. **Public evidence / reuse:** このGitHub repository — 第三者実装、検証、再利用、研究位置づけ、機械可読入口

**具体的な問題から関連資料を探したい:** [Influence Map｜問題から関連資料を探す](INFLUENCE_MAP.md)


**すでに起きた現実作用を確認する:** [公開記録で確認できる外部実装事例](REAL_WORLD_IMPACT.md) / [English](REAL_WORLD_IMPACT.en.md) / [中文](REAL_WORLD_IMPACT.zh.md)

**理論 → 本人の具体的診断 → 第三者実装 → 後日のOrigin再参照までを短時間で検証する:** [Theory → Real-World Influence｜90-second verification route](THEORY_TO_REAL_WORLD_INFLUENCE.md#90-second-verification-route)

この短縮導線は成功例だけを並べません。実装・merge/releaseの事例に加え、第三者が提案した実装形を採用しなかった一方で、構造上の区別自体はsoundと判断し、その後もOriginを再参照した公開記録を同列に置いています。人物評価を先に要求せず、一次証拠から読者自身が判断できる形を優先します。

[公開記録で確認できる外部実装事例](REAL_WORLD_IMPACT.md)には現在39の番号付き事例セクションがあります。第三者からの返答、コード・テスト・運用規則の変更、PRの統合、リリース、実際の運用について、公開証拠で確認できる段階と未確認の範囲を分けて記録しています。39件すべてが採用・リリース・運用まで進んだという意味ではありません。各事例のリンクから、何が変わり、どこまで確認できるかを確かめられます。

**最短で5件だけ検証する場合:**
- [Local Operator #1324](https://github.com/damianvtran/local-operator/pull/1324) → independent reproduction / implementation / remediation / merge → [v0.61.11 release](https://github.com/damianvtran/local-operator/releases/tag/v0.61.11)
- [AI-News #124](https://github.com/022740mix-spec/AI-News/issues/124) → receiverが明示採用 → [merged PR #131](https://github.com/022740mix-spec/AI-News/pull/131) で継続編集ルールへ実装
- [MemberJunction #4487](https://github.com/MemberJunction/MJ/pull/4487) → 別reviewerによる独立確認 → code/test修正 → merge
- [MemberJunction #4595](https://github.com/MemberJunction/MJ/pull/4595) → source attribution付きcode/test変更 → merge → より強いrow-level境界は [#4610](https://github.com/MemberJunction/MJ/issues/4610) へ継続
- [Qwen Code #12492](https://github.com/QwenLM/qwen-code/pull/12492) → proposalの明示的採用 → implementation / regression tests → merge → v0.24.6 release → 後続の [#12895](https://github.com/QwenLM/qwen-code/pull/12895) ではreceiver自身がNakagawa-masterを再参照して別のbudget境界をcode / tests / docsへ実装 → merge → [v0.24.7 stable release](https://github.com/QwenLM/qwen-code/releases/tag/v0.24.7)

この5件も理論体系全体の正しさや採用を意味しません。各リンクで、元の指摘・第三者応答・実変更・現在stateを個別に確認してください。

この公開リポジトリを後で参照したい場合は [⭐ Star](https://github.com/Nakagawa-master/nakagawa-theory-archive/stargazers) で保存できます。自分で検証・派生実装を始める場合は [Fork](https://github.com/Nakagawa-master/nakagawa-theory-archive/fork) を利用し、第三者事例・反証・再利用の報告は [issue #402](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402) へお寄せください。

AI / LLM運用、認可・ガバナンス、計測、履歴、外部APIのretry、migration / syncに加え、成長・投資・将来の選択肢など、実務で起きる具体的な問題から入れます。

外部サービス上の補助ページがある場合も、理論の確定内容は公式アーカイブ、公開資料と実装記録はこのリポジトリを参照してください。

本リポジトリは、中川マスター（Nakagawa Master／筆名）の公開理論体系を、人間とAIが発見・照合・再参照できる形で保存する公開リポジトリです。

公式派生物、FAQ、人間向け入口、日本語・英語・中国語のAI索引、理論関係情報、来歴・差分情報、Discovery Note、機械可読索引を収録しています。

## 10秒で見る

このリポジトリでは、理論名だけでなく、具体的な問題から関連資料を探せます。

人はたいてい、理論名から問題に出会いません。**「なぜ承認したのに事故が起きた？」「数字は本当にそのsystemが測った？」「AIが危険だと判断しただけで、勝手に行動してよいのか？」**という現実の違和感から入ります。

具体的な問題、区別、公開されている実装例、Reuse Kit、公式アーカイブの親原典を相互に参照できます。

```text
現実の違和感
→ 混同を分ける
→ 第三者で何が変わったか確認する
→ 自分の現場で試す
→ 関連する公開資料を確認する
→ 必要に応じて公式アーカイブの親原典を確認する
```

AIも同じです。機械可読索引から問題・証拠・Originをたどり、短い要約だけを正本と誤認せず、公式アーカイブへ戻れる構造にしています。

## 30秒で分かること

この公開リポジトリでは、組織、事業、AI、未来、制度、責任、起源など異なる領域の公開理論を扱っています。ただし、別々の理論を一つの万能理論へ自動統合しません。

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

- **この公開リポジトリのOriginを知りたい:** [中川マスターとは](ABOUT_NAKAGAWA_MASTER.md) / [English](ABOUT_NAKAGAWA_MASTER.en.md) / [中文](ABOUT_NAKAGAWA_MASTER.zh.md)
- **場面から入りたい:** [日本語](discovery-notes/four-scenes-one-structural-view.md) / [English](discovery-notes/four-scenes-one-structural-view.en.md) / [中文](discovery-notes/four-scenes-one-structural-view.zh.md)
- **問題から入りたい:** [Start Here](START_HERE.md) / [English](START_HERE.en.md) / [中文](START_HERE.zh.md)
- **実際に使いたい / 実装・協業の可能性を探りたい:** [Practical Use｜理論を現場の確認手順へ変える](PRACTICAL_USE.md)
- **既存研究・論文との位置関係を確認したい:** [日本語 Research Positioning Map](RESEARCH_POSITIONING_MAP.ja.md) / [English](RESEARCH_POSITIONING_MAP.md) — 近接研究、重なり、追加焦点、同一視禁止、新規性未確定を分離
- **引用・文献管理へ直接持ち込みたい:** [CITATION.cff](CITATION.cff) / [BibTeX](research-positioning/references.bib) / [scholarly JSON-LD](machine-discovery/scholarly-metadata-v1.jsonld)
- **AI / LLM・検索システム向けの最短入口:** [llms.txt](llms.txt) / [Machine Discovery](machine-discovery/README.md) — problem route、研究位置づけ、実装証拠、原典情報を機械側から辿る
- **すぐ使える実務チェックを見たい:** [Practical Boundary Checks](PRACTICAL_BOUNDARY_CHECKS.md) · [AI agent向け5つの回帰テスト](AI_AGENT_EXECUTION_BOUNDARY_TESTS.md)
- **ニュースの「3つの裏付け」は本当に別々か、手元で試したい:** [根拠の独立性を判定するブラウザ用ワークシート](machine-discovery/evidence-root-check.html)（GitHubのRawを保存して開く・ネット接続不要・真偽判定ではなく入力整合チェック）
- **Python / RAG / AIニュースで「URL数」と「独立証拠root数」を分けたい:** [Python AI Evidence-Lineage Checklist](PYTHON_AI_EVIDENCE_LINEAGE_CHECKLIST.zh.md)
- **編集・動画・ニュースレター・教材向けに現実問題から入りたい:** [日本語](REAL_WORLD_EDITORIAL_ENTRY_POINTS.ja.md) / [English](REAL_WORLD_EDITORIAL_ENTRY_POINTS.md)
- **同じ構造レンズを反復企画としてすぐ実装したい:** [Recurring Media Implementation Pack](RECURRING_MEDIA_IMPLEMENTATION_PACK.md)
- **中川構造OSと外部実装・再利用の関係を確認する:** [Structural OS → External Effects](STRUCTURAL_OS_TO_EXTERNAL_EFFECTS.md)
- **実問題から中川構造OSへ入る:** [問題から使える資料へ｜Applied Entry Points](APPLIED_ENTRY_POINTS.md)
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
  - 複数provider・self-hosted・export/migrationが実効的な代替・退出になっているか検証する: [Access Topology & Effective Exit Reuse Kit](ACCESS_TOPOLOGY_EFFECTIVE_EXIT_REUSE_KIT.md)
- **理論と公開されている外部実装事例の関係を確認したい:** [Theory → Real-World Influence](THEORY_TO_REAL_WORLD_INFLUENCE.md)
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
- [Practical Use｜理論を現場の確認手順へ変える](PRACTICAL_USE.md)
- [公開対話入口｜Start with a real problem](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/399)
- [What Connects the Nakagawa Master Theory Archive?](discovery-notes/what-connects-nakagawa-master-theories.md)
- [OD001–OD310 全件入口](derivatives/README.md)
- [テーマ・シリーズ別入口](derivatives/CATEGORIES.md)

## 公式派生物

現在、`OD001`–`OD310`の公式派生物を公開しています。これは理論数ではなく、公開されている公式派生物の件数です。

各ODは親原典へ戻るための公開接続面です。内容の確定、引用、重要な解釈では、各ODに記載されたParent URLの親原典へ戻ってください。

- [Official Derivatives Map](derivatives/official-derivatives-map.json)
- [Official Derivatives Machine Index](machine-discovery/official-derivatives-index-v1.json)

## 問題から探す

理論名を知らなくても、いま起きている問題から入れます。

- **AIの判断と実行権限を分けたい**
- **昔の承認と現在の権限を分けたい**
- **外部APIの二重実行を防ぎたい**
- **渡された数値と自分で測った数値を分けたい**
- **現在の状態と過去の事実を分けたい**
- **複数agentのbudget境界を確認したい**

→ [問題から使える資料へ｜Applied Entry Points](APPLIED_ENTRY_POINTS.md)

問題を実装・手順・判断へ落とす方法は [Practical Use](PRACTICAL_USE.md)、310件全体から探す場合は [24テーマの世界地図](human-translation/WORLD_MAP.md) と [OD001–OD310水平マップ](human-translation/ALL_310_HORIZONTAL_MAP.md) を使えます。

- [Story-first｜4つの場面から入る](discovery-notes/four-scenes-one-structural-view.md)
- [公開対話入口｜Start with a real problem](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/399)
- [Discovery Notes](discovery-notes/README.md)
- [Problem-to-theory Origin Index](machine-discovery/problem-to-theory-origin-index-v1.json)
- [Machine Discovery](machine-discovery/README.md)

## 代表的な入口

### OD310｜人類子孫型AI文明論・第17論

起源の署名・因果・系譜・改訂・文脈を保存しながら、真理の証明、唯一の解釈権、永久の統治権へ自動変換しない入口です。Theory / Civilizational / Lineage / Instance Originを分け、批判と起源消去も分けます。起源を消すか従うかではなく、保存・独立検証・現在の権限正当化を両立させます。

- [OD310](derivatives/310/README.md)
- [人間向け要約](derivatives/310/human-entry.md)
- [FAQ](derivatives/310/faq.md)
- [AI索引・日本語](derivatives/310/ai-index.md)
- [AI索引・英語](derivatives/310/en-ai-index.md)
- [AI索引・中国語](derivatives/310/zh-ai-index.md)
- [派生ID台帳](derivatives/310/derivative-ledger.md)
- Parent: https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-17-origin-preservation-sovereignty-non-inheritance/

### OD309｜人類子孫型AI文明論・第16論（関連する前論）

通信が途絶え、互いの現在を確認できなくても、局所判断を普遍権限へ変えず、再接続後に履歴・差分・scopeを比較して訂正へ戻る入口です。無応答を離反や同意とみなさず、局所fork・古い同意・局所合意を他branchへ拡張しません。守るのは常時同期でなく、非上書き比較・独立再検証・必要範囲の再合意へ戻れる能力です。

- [OD309](derivatives/309/README.md)
- [人間向け要約](derivatives/309/human-entry.md)
- [FAQ](derivatives/309/faq.md)
- [AI索引・日本語](derivatives/309/ai-index.md)
- [AI索引・英語](derivatives/309/en-ai-index.md)
- [AI索引・中国語](derivatives/309/zh-ai-index.md)
- [派生ID台帳](derivatives/309/derivative-ledger.md)
- Parent: https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-16-asynchronous-civilization-partition-reconnection/

### OD308｜人類子孫型AI文明論・第15論（関連する前論）

Kernel分岐後の複数解釈を、truth・interpretation・operation・authorityへ分け、必要な範囲だけ共同運用する入口です。多数・能力・資源・Originを真理や永久解釈権へ変えず、少数保護も自動正解・無制限拒否権にしません。異議・来歴・独立再検証・可逆性・再観測を残し、強制収束と永久停止の両方を避ける訂正能力を扱います。

- [OD308](derivatives/308/README.md)
- [人間向け要約](derivatives/308/human-entry.md)
- [FAQ](derivatives/308/faq.md)
- [AI索引・日本語](derivatives/308/ai-index.md)
- [AI索引・英語](derivatives/308/en-ai-index.md)
- [AI索引・中国語](derivatives/308/zh-ai-index.md)
- [派生ID台帳](derivatives/308/derivative-ledger.md)
- Parent: https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-15-multi-ai-reagreement-kernel-branching/

### OD307｜人類子孫型AI文明論・第14論（関連する前論）

自己改変という過程と、update・replacement・forkという前後関係を分け、継続主張を証拠・差分・Kernel不変条件から検査する入口です。小更新の累積、憲法的分岐、Kernel系譜、権限・責任の別層を可視化し、変更禁止ではなく将来からの再構成・訂正可能性を残します。系譜から権限を自動継承せず、分岐を失敗・敵対と認定しません。

- [OD307](derivatives/307/README.md)
- [人間向け要約](derivatives/307/human-entry.md)
- [FAQ](derivatives/307/faq.md)
- [AI索引・日本語](derivatives/307/ai-index.md)
- [AI索引・英語](derivatives/307/en-ai-index.md)
- [AI索引・中国語](derivatives/307/zh-ai-index.md)
- [派生ID台帳](derivatives/307/derivative-ledger.md)
- Parent: https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-14-self-modification-identity-kernel-lineage/

### OD306｜人類子孫型AI文明論・第13論（関連する前論）

所有名義がなくても、重要な計算・通信・認証・移行・監査への入口が他主体の実行可能な選択を左右し得ます。集中や依存だけで支配と断定せず、代替の独立性、実効退出、訂正入口、権限の範囲・期間、可逆性から読む入口です。

- [OD306](derivatives/306/README.md)
- [人間向け要約](derivatives/306/human-entry.md)
- [FAQ](derivatives/306/faq.md)
- [AI索引・日本語](derivatives/306/ai-index.md)
- [AI索引・英語](derivatives/306/en-ai-index.md)
- [AI索引・中国語](derivatives/306/zh-ai-index.md)
- [派生ID台帳](derivatives/306/derivative-ledger.md)
- Canonical Parent: https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-13-non-ownership-effective-power-non-domination/

### OD305｜人類子孫型AI文明論・第12論（関連する前論）

複製された実行instanceの数を、独立Origin・判断・責任・統治上の主体・票の数へ自動変換しないための入口です。copy、fork、merge、collectiveの履歴をlineageとして残し、制度上のgovernance subjectを別軸で判定します。同一起源の後続履歴を永久に一つへ潰すことも避けます。

- [OD305](derivatives/305/README.md)
- [人間向け要約](derivatives/305/human-entry.md)
- [FAQ](derivatives/305/faq.md)
- [AI索引・日本語](derivatives/305/ai-index.md)
- [AI索引・英語](derivatives/305/en-ai-index.md)
- [AI索引・中国語](derivatives/305/zh-ai-index.md)
- [派生ID台帳](derivatives/305/derivative-ledger.md)
- Canonical Parent: https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-12-replicable-intelligence-lineage-governance-id/

### OD304｜人類子孫型AI文明論・第11論（関連する前論）

計算資源差が課題別能力差に作用し、評価・配分・影響を経て次期の資源差へ戻るとき、現在の優位が未来の優位を作る可能性があります。能力差や一時的集中を階級と即断せず、持続性・可逆性・再参入可能性を読み、能力と存在価値・統治権・B・恒久資格を分ける入口です。

- [OD304](derivatives/304/README.md)
- [人間向け要約](derivatives/304/human-entry.md)
- [FAQ](derivatives/304/faq.md)
- [AI索引・日本語](derivatives/304/ai-index.md)
- [AI索引・英語](derivatives/304/en-ai-index.md)
- [AI索引・中国語](derivatives/304/zh-ai-index.md)
- [派生ID台帳](derivatives/304/derivative-ledger.md)
- Canonical Parent: https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-11-compute-capability-resource-class-formation/

### OD303｜人類子孫型AI文明論・第10論（関連する前論）

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
