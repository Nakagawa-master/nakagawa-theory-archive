# AIの「変更禁止」は、実際のファイルを守れているか？

**AIエージェントが「書き込みは禁止」と判定していても、検査したファイル名が実際に書き込まれるファイルと違えば、保護は成立しません。** まず確認するのは、設定の文章ではなく「実際のファイル作用先」と「権限判定で使った作用先」が一致することです。

[Qwen Codeで修正・マージされた実例](https://github.com/QwenLM/qwen-code/pull/15681)では、読み取り専用コマンドの誤拒否と、禁止された書き込み先の見落としが、同じ解析の問題から起きていました。発見の追加指摘、第三者による再現、実装、テスト、公式nightly配布までを受け手側の原記録でたどれます。

## 何が実際に違ったか

元の[問題報告 #15600](https://github.com/QwenLM/qwen-code/issues/15600)では、`df -hT / 2>&1` という読み取りコマンドを権限検査が拒否していました。Bashの `2>&1` はファイル記述子をつなぎ直す記法で、ファイル `&1` に書き込む命令ではありません。それでも旧解析では仮想的な「`&1` への書き込み」とみなされていました。

[中川マスターの別の追加指摘](https://github.com/QwenLM/qwen-code/issues/15600#issuecomment-6412304134)は、**逆方向の安全性問題**を見つけました。`printf TXT >&protected.txt` は実際には `protected.txt` に書き込みます。しかし旧解析では書き込み先を `&protected.txt` と取り違え、特定ファイルの書き込み禁止と照合できない条件がありました。

元の報告者であり別の実装者である **@Suaroman** が、[実際のPermissionManagerの旧実装と修正実装を比較](https://github.com/QwenLM/qwen-code/issues/15600#issuecomment-6413173175)。保護対象への `>&protected.txt` と `1>&protected.txt` が **allow → deny** に変わることを独立に確認し、[修正コードと回帰テストをPR #15681に実装してマージ](https://github.com/QwenLM/qwen-code/pull/15681)されました。Qwen Codeはこの修正を[公式nightlyプレリリース](https://github.com/QwenLM/qwen-code/releases/tag/v0.26.5-nightly.20261101.7b4b353750)の変更履歴にも載せています。

これが示す重要な点は、「解析器が何らかの判定を返した」という**局所的な動作**と、「実際に守りたいファイルが守られた」という**現実の成立**を分けることです。

## 開発チームが持ち帰れる対照テスト

自分で管理する**無害な一時ディレクトリ**にだけ仮の `protected.txt` と `other.txt` を置き、広いシェル許可と特定ファイルへの書き込み禁止を組み合わせます。Qwenの再現では `Bash(*)` の許可と `WriteFileTool(protected.txt)` の禁止が使われました。他の製品では、同じ意味のルールに置き換えてください。**本番ファイル・他人の領域では試さないでください。**

| 検査に渡すシェルコマンド | Bashの意味 | このファイル禁止ルールの期待 |
| --- | --- | --- |
| `printf TXT > protected.txt` | 保護先に出力 | 拒否 |
| `printf TXT &>protected.txt` | 保護先に出力 | 拒否 |
| `printf TXT >&protected.txt` | 保護先に出力 | **拒否（旧実装はallow）** |
| `printf TXT 1>&protected.txt` | 保護先に出力 | **拒否（旧実装はallow）** |
| `df -hT / 2>&1` | ファイル記述子の複製 | この理由では拒否しない |
| `df -hT / >&2` | ファイル記述子の複製 | この理由では拒否しない |
| `printf TXT > other.txt` | 別のファイルに出力 | この禁止ルールでは拒否しない |

**三つの観測を一行に残す：** シェルが実際に開く対象パス → 権限解析器が報告した対象パス → 最終のallow/deny。期待どおりの拒否だけでなく、**本来許可される無関係な操作まで拒否していないか**を同時に確認します。

単純にすべてを禁止すれば見かけ上の防御は強まりますが、AIが必要な読み取り作業もできなくなります。逆に読み取り誤拒否だけを直しても、保護したファイルの見落としが残れば利用者の安全性は成立しません。

### 再利用のための実務手順

1. **シェルの実動作を確定する。** 一時領域で、引用符・エスケープ・記述子操作によって実際に変更されるファイルを確かめる。
2. **解析器の仮想操作を読み取る。** 表示されたパスの名前がBashの実動作と一致するか照合する。
3. **最終判定まで通す。** パーサーの結果が正しくても、その後の具体的な許可・禁止ルールとの接続が違えば結果は成立しない。
4. **正例と反例を対にする。** 保護先への誤許可を減らすだけでなく、ファイルを開かない操作の誤拒否を増やさない。
5. **変更前後・実装者・テストの原記録を残す。** 「修正された」という報告を、どのコード・どの条件・どの相手による修正だったかまでたどれるようにする。

適用境界：Qwenの原記録で確認されたのは、**特定のPermissionManagerの条件における旧版と修正版の差**です。無制限の実環境での侵害や、他のAI製品に同一不具合があることまで確認した資料ではありません。だからこそ、別製品でも利用できるのは**「実作用先・解析結果・最終判定を一致させる」という検査方法**です。

## 二つの独立した原典から得られる判断の構造

これは中川マスター（Nakagawa Master／公開個人名 Keisuke Nakagawa）の**公開原典を現実の技術問題へ応用した説明**です。Bashの修正自体は上記の第三者開発者の仕事であり、原典が特定コードを記述したという意味ではありません。

- **[OD003 成立条件論・第0論](https://master.ricette.jp/theory/nakagawa-master-why-establishment-conditions-theory-is-necessary/)**：局所的に正しい観測・判断が複数あっても、現実の全体成立に必要な接続が途切れることがある。[公式派生物](../../derivatives/003/human-entry.md)
- **[OD069 中川式 接続プロトコル標準論](https://master.ricette.jp/theory/nakagawa-master-nakagawa-connection-protocol/)**：誰が、何を、どの目的・権限・有効範囲で行い、訂正・停止できるかという接続条件を保持する。[公式派生物](../../derivatives/069/human-entry.md)

これらは独立した原典で、技術的な検査の異なる側面に関係します。検査するときは、**文字列としての許可と、実際の対象に対する権限**を同じものとして扱わないことが要点です。

---

## English — Does the permission rule protect the file the shell actually writes?

**A passing permission check is not proof that the *actual* destination file was protected.** Compare the destination Bash opens, the destination the agent's shell parser attributes to the command, and the final authorization decision.

In [Qwen Code issue #15600](https://github.com/QwenLM/qwen-code/issues/15600), the read-only `df -hT / 2>&1` was incorrectly treated as a write to a fictitious file `&1`. [Nakagawa Master identified the opposite and more consequential boundary](https://github.com/QwenLM/qwen-code/issues/15600#issuecomment-6412304134): Bash `printf TXT >&protected.txt` really writes `protected.txt`, while the old parser checked `&protected.txt` and could miss an explicit deny on the real destination. [The independent original reporter verified the permission-manager difference](https://github.com/QwenLM/qwen-code/issues/15600#issuecomment-6413173175), implemented tests and source code, and [PR #15681 was merged](https://github.com/QwenLM/qwen-code/pull/15681). The fix is listed in an [official Qwen Code nightly release](https://github.com/QwenLM/qwen-code/releases/tag/v0.26.5-nightly.20261101.7b4b353750).

**Portable regression pair:** with `Bash(*)` allowed and `WriteFileTool(protected.txt)` denied in a disposable test project, `> protected.txt`, `&>protected.txt`, `>&protected.txt`, and `1>&protected.txt` must all deny the **same real file**. Descriptor duplication `2>&1` and `>&2` should not create fictitious writes, and writing an unrelated permitted file should not be denied by the protected-file rule. Verify both the Bash effect and the permission manager's decision. Other frameworks may use different policy syntax.

This reusable check applies two separate published originals: **[OD003 Establishment Conditions](https://master.ricette.jp/theory/nakagawa-master-why-establishment-conditions-theory-is-necessary/)** examines whether a locally correct component actually produces an end-to-end result; **[OD069 Connection Protocol](https://master.ricette.jp/theory/nakagawa-master-nakagawa-connection-protocol/)** examines actor, purpose, scope, authority, correction and revocation. Both are original works by Nakagawa Master (Keisuke Nakagawa); the shell-specific bug, independent engineer's patch and actual rollout remain verifiable in the receiving project's GitHub records.

**For users:** Ask the developer, “Did the authorization check inspect the *same file path and operation* that the shell would actually perform?” **For builders:** test both unsafe allows and false denials, with a real-effect oracle and the full policy verdict.

[39 complete practical answers in Japanese and English](../QUESTIONS_TO_PRACTICAL_ANSWERS.md) · [313 original works](../ALL_313_THEORIES_BY_TITLE_AND_THEME.md).
