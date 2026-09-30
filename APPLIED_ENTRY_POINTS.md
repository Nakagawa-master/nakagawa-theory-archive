# Applied Entry Points — 問題から使える資料へ

理論名を先に知らなくても、いま困っている問題から関連資料へ進める入口です。

ここでは、問題を一つの短い区別に変え、その区別を確認できる公開事例と、別の現場で試せる資料を結びます。

## AIや自動化が「判断した」あと、本当に実行してよいのか

AIが危険、安全、重要などと分類できることと、コメント、公開、削除、支払いなどを実行してよいことは別です。

**区別:** `classification ≠ permission to act`

- [公開実装事例を見る](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#8-responsibility--authority-separation--classification-is-not-permission-to-act)
- [自分のシステムで確認する](CURRENT_AUTHORITY_REUSE_KIT.md)
- [実行境界の回帰テスト](AI_AGENT_EXECUTION_BOUNDARY_TESTS.md)

## 昔の承認を、今の権限として使ってよいのか

一度承認された事実は履歴として残ります。しかし対象、条件、責任、影響範囲が変わったあとも、その承認が現在の権限として有効とは限りません。

**区別:** `historical approval ≠ current authority`

- [公開事例を見る](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#2-temporal--structural-consistency--historical-approval-is-not-current-authority)
- [確認手順を使う](CURRENT_AUTHORITY_REUSE_KIT.md)

## 一度だけ承認した処理が、外部でも一度だけ起きたと言えるのか

外部APIは処理を受け取ったのに応答だけ失われることがあります。その状態を単純な失敗として再試行すると、送信、課金、削除などが二重になる可能性があります。

**区別:** `approval consumed once ≠ external effect happened exactly once`

- [公開事例を見る](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#4-responsibility--causal-integrity--approval-is-not-exactly-once-external-effect)
- [External Side-Effect Reuse Kit](EXTERNAL_SIDE_EFFECT_REUSE_KIT.md)

## 渡された数値を、自分で測った数値として扱っていないか

上流のシステムから渡された値と、受信側が自分で取得した値では、証拠としての意味が違います。両方を残せば、不一致そのものも検証できます。

**区別:** `producer-supplied claim ≠ receiver-side measurement`

- [公開事例を見る](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#6-epistemic-integrity--producer-claim-is-not-system-measurement)
- [Measurement Attribution Reuse Kit](MEASUREMENT_ATTRIBUTION_REUSE_KIT.md)

## 現在の状態から、過去の事実まで書き換えていないか

現在memberではないことは、過去のeventに参加していなかったことを意味しません。現在の状態と、その時点で成立していた事実を分ける必要があります。

**区別:** `current state ≠ historical fact`

- [公開事例を見る](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#3-state-relation--temporal-integrity--current-status-is-not-historical-fact)
- [Historical-Fact Reuse Kit](HISTORICAL_FACT_REUSE_KIT.md)

## 名前を変えれば、外部から見えなくなるのか

内部名やaliasを変更しても、exportされた別名から同じobjectへ到達できる場合があります。localな名前とexternal reachabilityは同じではありません。

**区別:** `local spelling ≠ external reachability`

- [公開事例を見る](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#9-public-surface-identity--reachability--exported-alias-is-still-external-reachability)
- [Real-World Impact](REAL_WORLD_IMPACT.md)

## 同じtraceを使う複数agentは、同じbudgetを共有すべきか

一つのtraceの中に複数agentがいる場合、traceが同じだからといって、各agentの利用上限まで同じ一つのcounterへまとめてよいとは限りません。

**区別:** `shared trace ≠ shared agent budget`

- [LiteLLM issue #43190](https://github.com/BerriAI/litellm/issues/43190)
- [LiteLLM implementation PR #43410](https://github.com/BerriAI/litellm/pull/43410)
- [Real-World Impact](REAL_WORLD_IMPACT.md)

## AIが作ったdraftと、人間が送ったものを分けられているか

AIがdraftを作ることと、その内容を外部へ送信することは別の行為です。生成と送信の間に人間の確認を残せる設計なら、AIの支援範囲と人間の最終判断を分けられます。

**区別:** `draft creation ≠ external send`

- [MemberJunction PR #4568](https://github.com/MemberJunction/MJ/pull/4568)
- [Real-World Impact](REAL_WORLD_IMPACT.md)

## 305件全体から探す

ここに当てはまらない問題は、[24テーマの世界地図](human-translation/WORLD_MAP.md) または [OD001–OD305水平マップ](human-translation/ALL_305_HORIZONTAL_MAP.md) から探せます。

個別ページは公式派生物です。正確な理論内容が必要な場合は、各ページから公式アーカイブのcanonical Parentを確認してください。

## 関連資料

- [Influence Map](INFLUENCE_MAP.md)
- [Reuse Kits](REUSE_KITS.md)
- [Applied Evidence Map](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md)
- [Practical Use](PRACTICAL_USE.md)
- [Machine Discovery](machine-discovery/README.md)

Origin / Author: **Nakagawa Master** (pen-name of Keisuke Nakagawa)
