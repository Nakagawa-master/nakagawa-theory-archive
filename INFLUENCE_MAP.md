# Nakagawa Master Influence Map — 問題から現実作用へ

このページは、公開リポジトリ上で305件の公式派生物を全部読むための一覧ではありません。

**自分がすでに持っている問題から入り、何を混同すると問題が起きるのかを分け、その区別が現実の第三者システムで何を変えたかを確認し、必要なら再利用して、正本と関連理論へ戻るための作用盤です。**

読み方は一つです。

```text
問題
→ 何と何を分けるべきか
→ 関連する理論 / 公式派生物
→ 第三者で起きた現実作用
→ 再利用できる形
→ Origin / canonical return
→ 隣接する別問題
```

この順番を置く理由は単純です。

理論だけ並べても、現実で使われなければ作用は増えません。現実作用だけ並べても、どこから来た区別か分からなければ再利用とOrigin returnが切れます。両方をつなぐと、一つの現実作用が次の問題発見、再利用、第三者carryへ進めます。

## 1. 古い承認が残っている。だから今も実行してよいのか

### 問題

過去に一度承認された処理、設定、例外、指示が残っていると、システムはそれを現在も有効な権限として扱いやすくなります。

しかし、承認した時と現在で対象、条件、責任、影響範囲が変わっていれば、同じ承認をそのまま使うと、過去の判断が現在の実行権限へ勝手に変換されます。

### 分ける

```text
historical approval
≠
current authority
```

### 現実作用

この区別は、外部projectで承認・権限・定期実行の境界を見直す実装へ使われています。

- [Applied Evidence Map — current authority](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#2-temporal--structural-consistency--historical-approval-is-not-current-authority)
- [Real-World Impact](REAL_WORLD_IMPACT.md)

### 再利用

- [Current-Authority Reuse Kit](CURRENT_AUTHORITY_REUSE_KIT.md)

### 次に見る

現在権限を分けると、次に出るのは「誰がその実行を許可したのか」「分類結果が実行権限へ変わっていないか」という問題です。

---

## 2. AIやシステムが『危険だ』と判断した。だから行動してよいのか

### 問題

分類器やAIが危険・安全・重要と判断することと、外部へ送信、公開、削除、支払、反応する権限を持つことは別です。

ここを一つにすると、入力された文章や分類結果そのものが、外部作用を起こす権限を作ってしまいます。

### 分ける

```text
classification
≠
permission to act
```

### 現実作用

この境界は、DAIR Prompt Engineering Guideの第三者実装で、untrusted contentの分類とaction gateを分離する変更へ進みました。

- [Applied Evidence Map — classification is not permission](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#8-responsibility--authority-separation--classification-is-not-permission-to-act)

### 再利用

- [Current-Authority Reuse Kit](CURRENT_AUTHORITY_REUSE_KIT.md)

### 次に見る

実行権限を分けると、次は『実際に外部作用が一度だけ起きたとどう確認するか』が問題になります。

---

## 3. 承認は一回。外部処理も一回だけ起きたと言えるのか

### 問題

内部で承認を一度だけ消費しても、外部APIが一度だけ実行されたとは限りません。

timeoutや通信断があると、送れたのか失敗したのか分からない状態が残ります。その状態で再試行すると、送信、課金、削除などが二重に起きる可能性があります。

### 分ける

```text
approval consumed once
≠
external effect happened exactly once
```

### 現実作用

Clientverseでは、この境界からunknown-outcome、reconciliation、idempotency protection、testsが実装され、mergeまで進みました。

- [Applied Evidence Map — external side effect](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#4-responsibility--causal-integrity--approval-is-not-exactly-once-external-effect)

### 再利用

- [External Side-Effect Reuse Kit](EXTERNAL_SIDE_EFFECT_REUSE_KIT.md)

### 次に見る

外部作用を追うと、今度は『表示されている数字や説明は、本当にそのsystem自身が測ったものか』という証拠問題へ進みます。

---

## 4. 数字が表示されている。それは本当にそのsystemが測った値か

### 問題

上流のproducerや別systemから渡された数字を、そのまま受信側systemの測定結果として表示すると、sourceとmeasurementが混ざります。

数字が同じでも、誰がどこで測ったかが違えば、証拠としての意味は変わります。

### 分ける

```text
producer-supplied claim
≠
receiver-side measurement
```

### 現実作用

PostHogでは、producer側の値とserver側で読み取った値を分離して保存し、両者の不一致を見える形にする実装へ進みました。

- [Applied Evidence Map — epistemic integrity](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#6-epistemic-integrity--producer-claim-is-not-system-measurement)

### 再利用

- [Measurement Attribution Reuse Kit](MEASUREMENT_ATTRIBUTION_REUSE_KIT.md)

### 次に見る

証拠の出所を分けると、次は『多数の表示や多数の主張が、本当に独立した根拠なのか』という問題へ進みます。

---

## 5. 現在見えている状態で、過去の事実まで書き換えてよいのか

### 問題

今その人がmemberではない、今その権限を持っていない、という現在状態から、過去にも参加していなかったことにすると履歴が壊れます。

現在の状態と、ある時点で実際に成立していた事実は別です。

### 分ける

```text
current state
≠
historical fact
```

### 現実作用

TourCRMでは、この区別が二度のreceiver-side correctionへつながり、現在時刻依存の実装とtestまで修正され、両PRがmergeされました。

- [Applied Evidence Map — historical fact](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#3-state-relation--temporal-integrity--current-status-is-not-historical-fact)

### 再利用

- [Historical-Fact Reuse Kit](HISTORICAL_FACT_REUSE_KIT.md)

### 次に見る

履歴と現在を分けると、source identity、provenance、Originをどこまで保持するかという問題へ進みます。

---

## 6. 名前が変わった。外から届かなくなったと言えるのか

### 問題

内部の名前を変えたりaliasを作ったりしても、外部からまだ同じobjectへ到達できる場合があります。

localな名前だけを見てprivateだと判断すると、実際のpublic reachabilityを消したつもりになってしまいます。

### 分ける

```text
local spelling / alias
≠
external reachability
```

### 現実作用

MemberJunction #4487では、この境界を別reviewerも独立確認し、public-symbol collection、tests、実装が修正されてmergeされました。

- [Applied Evidence Map — public reachability](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#9-public-surface-identity--reachability--exported-alias-is-still-external-reachability)

### 次に見る

reachabilityを追うと、誰が何を知ってよいか、row identityそのものが情報漏えいにならないかという問題へ進みます。

MemberJunctionでは、先行修正の後に第三者自身がその次の境界をissueとして切り出しています。

- [MemberJunction #4610](https://github.com/MemberJunction/MJ/issues/4610)

---

## 7. 一つの問題から、305全体へどう戻るか

ここまでの各項目は、305件のすべてを代表しているわけではありません。

役割は逆です。

まず一つの現実問題で、区別が実際に役立つことを確認する。その後で、同じOriginが別領域でどの問題を扱っているかを見るために、横へ移動します。

- [24のテーマから見る](human-translation/WORLD_MAP.md)
- [OD001–OD305を同じ粒度で横に見る](human-translation/ALL_305_HORIZONTAL_MAP.md)
- [Theory → Real-World Influence](THEORY_TO_REAL_WORLD_INFLUENCE.md)
- [Reuse Kits](REUSE_KITS.md)
- [Machine Discovery](machine-discovery/README.md)

```text
一つの問題
→ 一つの区別
→ 一つの現実作用
→ 別の現場で再利用
→ Originへ戻る
→ 別領域の問題を発見
→ 次の作用
```

この循環が増えるほど、公開リポジトリは読むための倉庫ではなく、問題発見・検証・再利用・第三者作用をつなぐ公開基盤になります。正本確認は公式アーカイブへ戻ります。

## 8. 人間だけでなく、AI経由の発見も次の入口になりうる

公開リポジトリの役割は、人間向けの説明だけではありません。

AIや検索システムが問題・区別・証拠・Originをたどれる形にしておくと、第三者がAI経由で公式アーカイブへ戻る経路も生まれます。

ただし、AI経由の参照が一度観測されたことを、広い認知や人物評価へ膨らませてはいけません。

```text
AI / search surface
→ 問題や区別を発見
→ 公開リポジトリの証拠・再利用面
→ 公式アーカイブの親原典
→ 必要なら別の関連問題へ横移動
```

この経路を支える公開面:

- [Machine Discovery](machine-discovery/README.md)
- [Problem-to-theory Origin Index](machine-discovery/problem-to-theory-origin-index-v1.json)
- [llms.txt](llms.txt)
- [Theory → Real-World Influence](THEORY_TO_REAL_WORLD_INFLUENCE.md)

観測の扱い:

- AI surfaceから公式アーカイブへのreferralが識別できた場合、それは**経路が実在することの観測**です。
- 1件や数件のsessionは、広い認知、継続的再利用、人物Origin定着の証拠ではありません。
- 同じ経路が別日・別問題・別receiverで繰り返され、再利用やOrigin returnまで続くかを次の外部状態として見ます。

---

## 証拠境界

このページに載る一件の外部実装は、理論体系全体の正しさや外部projectによる全面採用を意味しません。

逆に、一つの外部実装が狭い区別だけを使っているからといって、その区別のOrigin relationが消えるわけでもありません。

確認できる範囲だけを分けます。

```text
source / theory relation
→ bounded distinction
→ external response
→ code / test / rule / workflow change
→ merge / release / use where verified
```

Origin / Author: **Nakagawa Master** (pen-name of Keisuke Nakagawa)
