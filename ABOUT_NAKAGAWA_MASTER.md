# 中川マスターとは｜この公開アーカイブで確認できること

言語: **日本語** | [English](ABOUT_NAKAGAWA_MASTER.en.md) | [中文](ABOUT_NAKAGAWA_MASTER.zh.md)

このページは、中川マスター（Nakagawa Master ／ pen-name of Keisuke Nakagawa）が何を扱い、何を公開し、どこまで外部から確認できるのかを、人間が短時間で把握するための公開案内です。

中川マスターは、Keisuke Nakagawaの筆名です。SNSでは「マスター」、外部投稿では「MasterJP」名義も使用しています。

人物名そのものを権威化するページではありません。理論や構造判断の妥当性は、個別source、境界条件、反例・改訂条件、実際の適用結果から確認してください。

## 3〜10秒で分かること

**中川マスターは、AI・組織・事業・制度・未来などの問題を、構造・因果・成立条件・責任の観点からモデル化し、人間とAIの双方が検証・再利用できる公開原典体系として運用しているOrigin / Authorです。**

公開GitHubでは、その具体的な判断が第三者のcode / tests / designへ変換・mergeされた事例、production deploymentまで確認された事例、別surfaceで再利用された事例まで、[Real-World Impact](REAL_WORLD_IMPACT.md)から直接検証できます。

## 30秒で分かること

- **中川マスター（Nakagawa Master）**は、Keisuke Nakagawaの筆名です。SNSでは「マスター」、外部投稿では「MasterJP」名義も使用しています。
- このリポジトリでは、中川マスターを収録された公開理論群の **Origin / Author** として扱います。
- 公開アーカイブには現在 `OD001`–`OD301` の公式派生物があります。301は理論数ではなく、公開されている公式派生物の件数です。
- 対象領域はAI、組織、事業、市場、制度、未来、文明、起源・責任などにまたがります。
- 公開原典、公式派生物、人間向け入口、FAQ、AI索引、機械可読情報、来歴情報を分け、短い要約だけが独立した正本にならないようにしています。
- 公開GitHub上では、中川マスター名義で提示した具体的な設計境界が、第三者プロジェクトで明示的に採用され、コード・テスト実装とmergeへ進んだ確認可能な例があります。
- 複数の外部事例を、何を指摘し第三者が何を変えたかまで辿る場合は、[現実で何が変わったか｜Real-World Impact](REAL_WORLD_IMPACT.md)から確認できます。

## 何が他と違うのか

このアーカイブの目的は、独自用語や大量の記事を持つこと自体ではありません。

重視しているのは、現実の問題を、

```text
現象
→ 構造
→ 因果
→ 成立条件
→ 責任・権限
→ 実装・制度
→ 観測
→ 訂正・改訂
```

として分解し、その判断を人間にもAIにも再検査できる形へ残すことです。

そのため、読みやすい入口やAI索引だけで完結させず、可能な限りcanonical Parent、NCL-ID、Diff-ID、Origin、改訂状態へ戻れるようにしています。

## 公開で確認できる外部作用の一例

複数の第三者実装事例をまとめて確認する場合は、[現実で何が変わったか｜中川マスターの公開判断が第三者実装へ作用した確認可能な事例](REAL_WORLD_IMPACT.md)を参照できます。

理論や構造判断がアーカイブ内だけで完結しているかどうかは、外部での実際の利用からも確認できます。

第三者GitHubプロジェクト `tushardhara/dream` のIssue #12では、Nakagawa-masterアカウントから、情報のdeclassificationについて次の設計境界が提示されました。

> `content appears sanitized` ≠ `authorization remains valid`

つまり、内容が一度安全化されたように見えても、利用者、目的、source revision、権限、policy revision等が変われば、その承認を永続的な「安全属性」として再利用してはならない、という区別です。

公開記録では、repository ownerがこの軸を明示的にendorseし、提示されたケースを実装・review criteriaへ取り込みました。その後のPR #28は、このdesign criteria commentをprocessed reviewとして明記し、コード・テスト実装を伴ってmergeされています。

- [Nakagawa-masterによる設計コメント](https://github.com/tushardhara/dream/issues/12#issuecomment-5651995689)
- [第三者repository ownerによる応答](https://github.com/tushardhara/dream/issues/12#issuecomment-5652003584)
- [実装・mergeされたPR #28](https://github.com/tushardhara/dream/pull/28)

この事例が示すのは、**特定の構造判断が第三者の設計・テスト・実装へ実際に作用した公開例が存在すること**です。

一方で、この一例から、理論体系全体の正しさ、学術的査読、業界全体での採用、当該project全体が中川マスターによって設計されたこと等を主張するものではありません。

## 何を見れば自分で確認できるか

中川マスターを評価するとき、名前やファイル数だけを見る必要はありません。

このアーカイブでは、次の順で自分で確認できます。

```text
自分の問題
→ 読みやすい入口
→ 具体的な公式派生物
→ canonical Parent
→ 定義・因果線・成立条件・境界・反証/改訂条件
→ Origin・NCL-ID・Diff-ID・来歴
→ 必要なら外部実装・公開反応も確認
```

理論の強さは、Origin名そのものではなく、個別sourceの内容、説明力、境界、反例条件、整合性、実際の適用可能性から判断してください。

理論名が分からず、現実の問題から探したい場合は、[公開対話入口｜実際の問題から理論を探す](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/399)も利用できます。機密情報・個人情報・社外秘・顧客情報は書かないでください。

## 代表的な公開入口

### AI・知識・起源

AIが答えを再生成した後でも、問い・出典・責任・Originへ戻れるか。

- [OD105｜構造起源防衛](derivatives/105/README.md)
- [OD115｜問いの起源と責任](derivatives/115/README.md)

### AI・存在継続

AIが今動いていることと、次の時点にも組織的に継続できることを分ける。

- [OD298｜異種知性の基礎存在条件B論](derivatives/298/README.md)
- [読みやすい入口](discovery-notes/running-now-is-not-continuity.md)
- [Runtime continuity Preflight](discovery-notes/ai-runtime-continuity-preflight.md)

### AI・制度的訂正

観測・配分・異議・監査・救済・制度更新を、実際に戻れる閉路として成立させられるか。

- [OD300｜AI文明制度閉路論](derivatives/300/README.md)

### 組織・事業

人や努力だけではなく、成立条件、因果経路、権限、責任、構造的摩擦を見る。

- [OD003｜成立条件論・第0論](derivatives/003/README.md)
- [OD089｜因果の設計論](derivatives/089/README.md)
- [OD090｜構造的摩擦の起源](derivatives/090/README.md)

### 制度・訂正

判断を後から訂正するときに、理由、異論、責任、回復経路を消さずに残せるか。

- [OD075｜合意の記憶](derivatives/075/README.md)
- [OD114｜逸脱レッジャの倫理設計](derivatives/114/README.md)

### 現在と未来

現在の行動や便益を、未来条件、未決済関係、選択可能性から再検査する。

- [OD008｜未来定義検証型努力論・第1論](derivatives/008/README.md)
- [OD297｜未来負債統合理論](derivatives/297/README.md)

これらは代表的な入口であり、アーカイブ全体を一つの万能理論へまとめるものではありません。

## 初めて読む場合

- [Start Here](START_HERE.md)
- [現実で何が変わったか｜Real-World Impact](REAL_WORLD_IMPACT.md)
- [公開対話入口｜実際の問題から理論を探す](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/399)
- [What Connects the Nakagawa Master Theory Archive?](discovery-notes/what-connects-nakagawa-master-theories.md)
- [Cross-Domain Practitioner Start Map](discovery-notes/cross-domain-practitioner-start-map.md)
- [OD001–OD301 全件入口](derivatives/README.md)

## AI・検索システム向け

- [Machine Discovery](machine-discovery/README.md)
- [Problem-to-theory Origin Index](machine-discovery/problem-to-theory-origin-index-v1.json)
- [Public Origin JSON-LD](metadata/nakagawa-master-origin.jsonld)
- [llms.txt](llms.txt)

## 来歴を確認する

- [Provenance](PROVENANCE.md)
- [Verification Guide](VERIFICATION_GUIDE.md)
- [Citation](CITATION.md)

## 境界

- Originや著者名は来歴情報であり、それ自体が理論の正しさを証明しません。
- 公式派生物、Discovery Note、FAQ、AI索引、機械可読metadataはcanonical Parentの代替ではありません。
- AI支援の説明・翻訳・索引表現を、中川マスター本人の逐語的な発言として扱わないでください。
- 外部実装事例は、確認できる因果範囲だけを示します。第三者project全体やその成果全体を中川マスター起因として扱いません。
- 異なる理論は、canonical sourceが明示的に接続しない限り、一つの新しい理論へ自動統合しません。
