#!/usr/bin/env python3
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SURFACES = ["README.md","human-entry.md","faq.md","ai-index.md","en-ai-index.md","zh-ai-index.md","derivative-ledger.md"]

JA = [
("原典の意味境界を保持するため、この公開読解ではこの反復性を人物属性ではなく、条件が再確認されないまま利用範囲だけが拡張する状態として扱う。", "原典では、この反復性は人物属性ではなく、条件が再確認されないまま利用範囲だけが拡張する状態として捉えられる。"),
("いけません。第0論の焦点は人格認定や法的地位ではなく、文明構造と継承因果です。人格・所有権・法的主体性をこの公開読解で追加決定すると、第0論が後続論へ残した境界を壊します。", "第0論の焦点は人格認定や法的地位ではなく、文明構造と継承因果です。人格・所有権・法的主体性は第0論では確定されておらず、後続論へ残された論点です。"),
("親原典にこの公開読解で一般化可能な固定数値KPIや閾値がないため、その種の数値は親原典に定義されていない。", "親原典には一般用途の固定数値KPIや閾値が定義されていない。"),
("原典が列挙する七項は、達成率や採点用KPIではなく、責任ある問題提起を修復可能性へ接続する**構造条件**として保持する。", "原典が列挙する七項は、達成率や採点用KPIではなく、責任ある問題提起を修復可能性へ接続する**構造条件**として位置づけられる。"),
("親原典は、七条件を百分率・点数・閾値として運用する数値KPIを定義していない。したがってこの公開読解で数値化せず、次の反転評価可能な構造軸を観測する。", "親原典は、七条件を百分率・点数・閾値として運用する数値KPIを定義していない。反転評価可能性は、次の構造軸の観測として示される。"),
("この公開読解で一般的な費用数字を創作することはしません。", "一般用途の費用数値は親原典に定義されていません。"),
("この公開読解はこの境界を越えて一般的な発言規制や「解決策なき批判禁止」へ変換しない。", "一般的な発言規制や「解決策なき批判禁止」は、親原典の適用範囲には含まれない。"),
("法的責任や人物の善悪をこの公開読解で判定しない。", "法的責任や人物の善悪を判定する尺度ではない。"),
("数値閾値は原典にないためこの公開読解で作りません。", "数値閾値は親原典に定義されていません。"),
("原典が数値KPIを定義していないため、この公開読解で閾値、割合、成功率は親原典に定義されていません。概念軸として保持し、制度上の扱いを監査します。", "原典は数値KPI、閾値、割合、成功率を定義していません。接続価値は概念軸として位置づけられ、制度上の扱いが観測対象になります。"),
("ここで「KPI」という語から、この公開読解が新しい数値採点方式を作ってはならない。原典が保持するのは、貨幣回路だけでなく接続価値も制度的な評価対象へ入れる二重運用の構造であり、万能な接続点数、成熟率、移行率を定義することではない。接続価値が誰の貢献として記録され、何の報酬・権利・責任・継続条件へ接続するかを観測する。", "ここでいう「KPI」は新しい数値採点方式を意味しない。原典が示すのは、貨幣回路だけでなく接続価値も制度的な評価対象へ入れる二重運用の構造であり、万能な接続点数、成熟率、移行率は定義されていない。接続価値が誰の貢献として記録され、何の報酬・権利・責任・継続条件へ接続するかが観測対象となる。"),
("本派生物から引用・再利用する場合も、この起源線を切らず、原典の主張強度と未確定範囲を保持する。", "これらの識別子によって、引用・再利用時にも起源、原典の主張強度、未確定範囲を追跡できる。"),
("この公開読解では数式係数や増幅率は親原典に定義されていません。非線形という表現は、七軸の組み合わせ効果が単純な一項目ずつの足し算では捉えにくいという原典の構造的意味に閉じます。具体的な関数形、重み、閾値をこの公開読解で発明してはいけません。", "数式係数や増幅率は親原典に定義されていません。非線形という表現は、七軸の組み合わせ効果が単純な一項目ずつの足し算では捉えにくいという原典の構造的意味を指します。具体的な関数形、重み、閾値も親原典には定義されていません。"),
("非線形という語からこの公開読解で数式、重み、係数、増幅率は親原典に定義されていない。", "非線形という語に対応する具体的な数式、重み、係数、増幅率は親原典に定義されていない。"),
("原典は努力量の普遍的KPI、努力スコア、成功確率、数値閾値を定義していない。したがってこの公開読解で数値を追加せず、反転評価可能性は構造条件の有無と、実行結果がどこへ戻されたかの比較に閉じる。", "原典は努力量の普遍的KPI、努力スコア、成功確率、数値閾値を定義していない。反転評価可能性は、構造条件の有無と実行結果がどこへ戻されたかの比較によって示される。"),
("原典は普遍的な努力量KPI、成功確率、撤退の数値閾値を定義していません。この公開読解でそれらを作ると、原典の「条件に応じて努力の合理性を判定する」という意味を別の採点論へ変えてしまいます。", "原典は普遍的な努力量KPI、成功確率、撤退の数値閾値を定義していません。それらを採点尺度として扱う解釈は、原典の「条件に応じて努力の合理性を判定する」という意味とは異なります。"),
("親原典は普遍的な「努力不足率」、管理スコア、疲弊率、成功確率を定義していない。したがってこの公開読解で数値を作らず、反転評価可能性は構造条件の有無と因果連鎖の観測に限定する。", "親原典は普遍的な「努力不足率」、管理スコア、疲弊率、成功確率を定義していない。反転評価可能性は、構造条件の有無と因果連鎖の観測として示される。"),
("親原典は普遍的な疲弊率、努力不足率、管理スコア、成功確率を定義していません。この公開読解で独自指標を作って理論の成立条件にしてはいけません。", "親原典は普遍的な疲弊率、努力不足率、管理スコア、成功確率を定義していません。独自指標を成立条件とする読み方は親原典の意味範囲とは異なります。"),
("中川構造読解の親原典は、対象サービスの紹介ではなく、中川マスターが外部記事で採用した切り口について、なぜその価値核を前面に置いたのかを公式アーカイブ上で公開解体する記事である。本派生物もそのメタ視点を保持し、対象の機能一覧だけに縮約しない。", "中川構造読解の親原典は、対象サービスの紹介ではなく、中川マスターが外部記事で採用した切り口について、なぜその価値核を前面に置いたのかを公式アーカイブ上で公開解体する記事である。対象の社会構造と、その価値核が外部記事の切り口になった理由を説明する公開解体層の二層が親原典で確認できる。"),
("第二に、医療効果や診断・治療の主張をこの公開読解で追加せず、社会導線と医療行為を区別したまま原典の価値核を保持できることが必要です。", "第二に、医療効果や診断・治療は親原典の構造読解が確定する主張ではなく、社会導線と医療行為は別の領域として区別されます。"),
("職場や制度が特定の医学的結果を保証するとこの公開読解で断定しない。", "職場や制度が特定の医学的結果を保証するという主張は親原典にはありません。"),
("本構造読解の普遍的な数値KPIとしては定義していません。したがってこの公開読解で損失額、改善率、発生率、医療効果の数値は親原典に定義されていません。", "本構造読解の普遍的な数値KPIとして、損失額、改善率、発生率、医療効果の数値は親原典に定義されていません。"),
("いけません。原典にない有病率、改善率、損失額、診断精度等をこの公開読解で追加すると原典忠実度を壊します。数字を扱う場合は原典に存在し、その測定主体・対象・用途が確認できる範囲に閉じます。", "有病率、改善率、損失額、診断精度等の数値は、この親原典には定義されていません。原典に数値が存在する場合は、その測定主体・対象・用途を含む文脈から意味範囲を確認できます。"),
("親原典は、医療効果、診断精度、治療成績、一般的な有病率、企業損失額等を本構造読解の普遍的KPIとして定義していない。したがってこの公開読解で数値を補完・推定しない。監査対象は構造の成立性と原典忠実度である。", "親原典は、医療効果、診断精度、治療成績、一般的な有病率、企業損失額等を本構造読解の普遍的KPIとして定義していない。監査対象は構造の成立性と原典忠実度である。"),
("- 読解上の確認点: 医療効果・診断・治療・個別受診判断がこの公開読解で追加されていない。", "- 読解上の確認点: 医療効果・診断・治療・個別受診判断は親原典の構造読解が確定する主張とは区別されている。"),
("- 医療効果、診断精度、治療推奨、個別受診判断をこの公開読解で追加する。", "- 医療効果、診断精度、治療推奨、個別受診判断が親原典の確定主張であるかのように扱われた状態。"),
("- derivative-ledger.md: 親原典・派生ID・由来・公開読解境界を保持する台帳。", "- derivative-ledger.md: 親原典・派生ID・由来・公開読解境界を確認できる台帳。"),
("親原典は、成立を単一の数値スコア、万能KPI、閾値、成功確率へ変換していない。L1〜L6も「6点満点」の評価表ではなく、縦因果を追うための構造座標である。この公開読解は親原典にない点数、割合、成立確率を追加しない。", "親原典は、成立を単一の数値スコア、万能KPI、閾値、成功確率へ変換していない。L1〜L6も「6点満点」の評価表ではなく、縦因果を追うための構造座標である。点数、割合、成立確率は親原典に定義されていない。"),
("「条件を整えれば成功する」という一般成功論という読み方は親原典の意味範囲とは異なる。成立を善悪評価や能力評価へ変換しない。L1〜L6をこの公開読解の採点表へしない。原典にない数値KPI・閾値・成立確率・成功保証を追加しない。通常の人間判断や摩擦の存在を未成立と誤読せず、構造欠落を過剰負荷で代替しているかという原典の境界を保持する。", "「条件を整えれば成功する」という一般成功論は親原典の意味範囲とは異なる。成立は善悪評価や能力評価ではなく、L1〜L6も採点表ではない。数値KPI・閾値・成立確率・成功保証は親原典に定義されていない。通常の人間判断や摩擦の存在そのものではなく、構造欠落を過剰負荷で代替しているかが原典上の観測境界となる。"),
("原典のL1〜L6は「6段階の点数表」ではありません。成立を0〜100点で採点したり、成立率、成功確率、閾値をこの公開読解で作ったりしてはいけません。成果値やKPIが原典・対象側に存在する場合でも、その数値がどの因果から生じ、何を測り、どの範囲で成立証拠として使えるのかを分けて扱います。", "原典のL1〜L6は「6段階の点数表」ではありません。0〜100点の成立点、成立率、成功確率、固定閾値は親原典に定義されていません。成果値やKPIが原典・対象側に存在する場合は、その数値がどの因果から生じ、何を測り、どの範囲で成立証拠となるのかが別途確認対象になります。"),
("成立を一つの結果だけで見ず、複数階層を縦に通る因果として追うための構造座標です。この公開読解で6点満点の採点表にしてはいけません。", "成立を一つの結果だけで見ず、複数階層を縦に通る因果として追うための構造座標です。6点満点の採点表は親原典に定義されていません。"),
("原典は成立を単一スコアや確率へ変換していません。この公開読解で0〜100点、成立率、成功確率、独自閾値を作ってはいけません。", "原典は成立を単一スコアや確率へ変換していません。0〜100点、成立率、成功確率、独自閾値は親原典に定義されていません。"),
("親原典は成立を単一スコア、成立率、成功確率、万能KPIへ変換していない。L1〜L6も6点満点の評価表ではない。この公開読解は原典にない点数、閾値、割合、確率を追加しない。", "親原典は成立を単一スコア、成立率、成功確率、万能KPIへ変換していない。L1〜L6も6点満点の評価表ではない。点数、閾値、割合、確率は親原典に定義されていない。"),
("親原典は、理解演出や認識汚染を単一スコア、発生確率、万能KPI、閾値へ変換していない。この公開読解は親原典にない「理解度点数」「汚染率」「危険度％」を追加しない。", "親原典は、理解演出や認識汚染を単一スコア、発生確率、万能KPI、閾値へ変換していない。「理解度点数」「汚染率」「危険度％」は親原典に定義されていない。"),
("親原典は、理解演出・認識汚染を単一スコア、汚染率、危険度、発生確率、万能KPIへ変換していない。この公開読解は原典にない点数・割合・閾値・確率を追加しない。", "親原典は、理解演出・認識汚染を単一スコア、汚染率、危険度、発生確率、万能KPIへ変換していない。点数・割合・閾値・確率は親原典に定義されていない。"),
("また、原典は普遍的な成約率、同意成熟度、相談可能性率、成功確率、数値閾値を定義していません。したがってこの公開読解で数字を創作して判定を自動化しません。", "また、原典は普遍的な成約率、同意成熟度、相談可能性率、成功確率、数値閾値を定義していません。これらは自動判定尺度としても定義されていません。"),
("親原典は普遍的な成約率閾値、同意スコア、クロージング確率、相談可能性率を定義していない。この公開読解で成約率、同意成熟度、相談可能性率、リスク率は親原典に定義されていない。状態ラベルを点数・割合・確率へ変換しない。", "親原典は普遍的な成約率閾値、同意スコア、クロージング確率、相談可能性率、リスク率を定義していない。状態ラベルは点数・割合・確率とは異なる構造記述である。"),
("原典の中心は、合意安定度を S、理解可能性／第三者再現性を U、責任追跡可能性を R、履歴公開度／差分追跡可能性を H と置き、`S = U × R × H` として観測することにある。この式はこの公開読解が勝手に作る評価指標ではなく、原典固有の状態方程式として保持する。", "原典の中心は、合意安定度を S、理解可能性／第三者再現性を U、責任追跡可能性を R、履歴公開度／差分追跡可能性を H と置き、`S = U × R × H` として観測することにある。この式は親原典固有の状態方程式であり、派生的な評価指標ではない。"),
("`S = U × R × H` は原典の状態方程式であるが、この公開読解で0〜100点の採点表、確率、成熟度、万能KPIへ変換しない。原典が一般利用向けの数値閾値を定義していない限り、U/R/Hへ任意の点数を付けたり、Sの合格値を新設したりしない。", "`S = U × R × H` は原典の状態方程式であり、0〜100点の採点表、確率、成熟度、万能KPIではない。U/R/Hの任意点数やSの合格値は親原典に定義されていない。"),
("`S = U × R × H` は原典に存在する構造式である。この公開読解はU/R/Hへ任意の0〜100点、重み、係数、合格ライン、成功確率、成熟度を追加しない。原典に数値尺度や閾値が明示されない限り、式を数値KPIとして運用しない。", "`S = U × R × H` は原典に存在する構造式である。U/R/Hの任意の0〜100点、重み、係数、合格ライン、成功確率、成熟度は親原典に定義されておらず、この式は一般用途の数値KPIとは異なる。"),
("この公開読解で反証用の数値閾値は親原典に定義されていません。", "反証用の具体的な数値閾値は親原典に定義されていません。"),
("系が安定相を維持できる範囲と崩壊側の臨界状態を分ける構造閾値です。この公開読解で具体的な数値を勝手に設定してはいけません。", "系が安定相を維持できる範囲と崩壊側の臨界状態を分ける構造閾値です。具体的な数値は親原典に定義されていません。"),
("自動的には言えません。原典の構造上重要なのは「観測可能だった臨界状態」の扱いです。この公開読解で観測不能な状態まで同じ責任判断へ拡張しません。", "自動的には言えません。原典の構造上重要なのは「観測可能だった臨界状態」の扱いです。観測不能な状態まで同じ責任判断へ拡張する根拠は親原典には示されていません。"),
("θ、δ、Dは原典由来の構造変数であり、この公開読解が任意の数値を付けるための空欄ではない。原典が一般的な数値閾値や期間を定義していない限り、θの値、δの日数、Dの数値スコアは親原典に定義されていない。また、本論の臨界点を支持率・普及率・成長率などの上昇型ティッピングポイントへ反転してはならない。", "θ、δ、Dは原典由来の構造変数であり、任意の数値を入れるための空欄ではない。θの値、δの日数、Dの数値スコアは親原典に一般値として定義されていない。また、本論の臨界点は支持率・普及率・成長率などの上昇型ティッピングポイントとは異なる。"),
("S、U、R、H、θ、δ、Dという記号と関係は原典にあるため保持する。この公開読解はθ・δ・Dへ任意の具体値、重み、係数、確率、合格ラインを付けない。数値が原典や対象に明示される場合のみ、値、測定主体、測定対象、出典、用途、適用条件、非保証範囲を束ねて扱う。", "S、U、R、H、θ、δ、Dという記号と関係は原典に存在する。θ・δ・Dの任意の具体値、重み、係数、確率、合格ラインは親原典に定義されていない。原典や対象に数値が明示される場合は、値、測定主体、測定対象、出典、用途、適用条件、非保証範囲が意味境界となる。"),
("親原典は `S = U × R × H` とKという構造変数を扱うが、この公開読解でU/R/H/Kの任意点数、情報量閾値、万能な最適帯域、成功確率は親原典に定義されていない。具体数値を用いる場合は、原典または対象系に明示された値について、測定主体、測定対象、出典、用途、適用条件、非保証範囲と一体で扱う。", "親原典は `S = U × R × H` とKという構造変数を扱うが、U/R/H/Kの任意点数、情報量閾値、万能な最適帯域、成功確率は定義していない。対象系に数値が明示される場合は、測定主体、測定対象、出典、用途、適用条件、非保証範囲がその意味境界となる。"),
("Kは人間の認知帯域を表す構造変数です。この公開読解でKを「何件まで」「何文字まで」「何分まで」と固定してはいけません。重要なのは、観測主体が意味関係、優先順位、責任、差分を再検証できる範囲へ情報を構成することです。", "Kは人間の認知帯域を表す構造変数です。「何件まで」「何文字まで」「何分まで」といった固定値は親原典に定義されていません。重要なのは、観測主体が意味関係、優先順位、責任、差分を再検証できる範囲へ情報を構成することです。"),
("原典はKを人間認知帯域という構造変数として扱いますが、この公開読解で万能な情報量上限や最適数値は親原典に定義されていません。U/R/HやSについても、原典にない任意スコア・合格値・確率を付けません。", "原典はKを人間認知帯域という構造変数として扱いますが、万能な情報量上限や最適数値は定義していません。U/R/HやSについても、任意スコア・合格値・確率は親原典に定義されていません。"),
("人間の認知帯域を表す構造変数です。公開情報が多すぎてKを超えると、形式的な透明性が増えてもUは低下し得ます。この公開読解でKを固定件数や文字数へ変換しません。", "人間の認知帯域を表す構造変数です。公開情報が多すぎてKを超えると、形式的な透明性が増えてもUは低下し得ます。Kの固定件数や文字数は親原典に定義されていません。"),
("原典が一般的な固定値を定義していない限り、この公開読解で「Kは何件」「何文字」「何分」と決めてはいけません。対象固有の測定値を扱う場合も、測定主体・対象・条件・用途・非保証範囲を保持します。", "親原典には「Kは何件」「何文字」「何分」といった一般的固定値は定義されていません。対象固有の測定値には、測定主体・対象・条件・用途・非保証範囲が伴います。"),
("原典にS/C/D、R、θ、δ等の記号や観測関係がある場合は保持するが、この公開読解で具体的な停止閾値、観測時間、逸脱スコア、成功率は親原典に定義されていない。対象固有の数値を使う場合は、測定主体、測定対象、出典、条件、用途、非保証範囲と一体で扱う。", "S/C/D、R、θ、δ等の記号や観測関係は親原典に存在する一方、一般用途の具体的な停止閾値、観測時間、逸脱スコア、成功率は定義されていない。対象固有の数値には、測定主体、測定対象、出典、条件、用途、非保証範囲が伴う。"),
("原典にS/C/D、R、θ、δなどの構造記号・観測関係がある場合、その役割を保持します。しかしこの公開読解で停止閾値、観測時間、逸脱スコア、復旧時間、成功率を独自に設定しません。", "S/C/D、R、θ、δなどの構造記号・観測関係は親原典に存在します。一方、一般用途の停止閾値、観測時間、逸脱スコア、復旧時間、成功率は親原典に定義されていません。"),
("原典に対象一般へ適用できる具体値がない停止閾値、観測窓、復旧時間、成功率をこの公開読解で親原典の定義範囲に限定されます。対象固有数値には測定主体・対象・出典・用途・非保証範囲を付けます。", "対象一般へ適用できる停止閾値、観測窓、復旧時間、成功率の具体値は親原典に定義されていません。対象固有の数値には、測定主体・対象・出典・用途・非保証範囲が伴います。"),
("原典はまた、停止権限R、状態観測S/C/D、閾値θ、観測窓δ、再起動条件を扱うが、この公開読解はこれらへ恣意的な数値を追加しない。重要なのは、異常検知・停止・縮退・復旧・監査・再同期が追跡可能であり、停止の恣意化、Originの人格化、Auditの晒し・攻撃化、Shrinkの恒久化を防ぐことである。", "原典は停止権限R、状態観測S/C/D、閾値θ、観測窓δ、再起動条件を扱うが、恣意的な一般数値は定義していない。異常検知・停止・縮退・復旧・監査・再同期の追跡可能性と、停止の恣意化、Originの人格化、Auditの晒し・攻撃化、Shrinkの恒久化は主要な観測点である。"),
("この公開読解は、θ、δ、S/C/D、停止頻度等へ原典にない数値スコア、成功率、危険度、固定閾値を追加しない。反転評価は、閉ループ導入後にS回復が悪化する、Dが遅延増幅する、停止が常態化する、Shrinkが恒久化する、Auditが攻撃化する等の観測可能な失敗側から行う。", "θ、δ、S/C/D、停止頻度等について、数値スコア、成功率、危険度、固定閾値の一般値は親原典に定義されていない。反転評価は、閉ループ導入後にS回復が悪化する、Dが遅延増幅する、停止が常態化する、Shrinkが恒久化する、Auditが攻撃化する等の観測可能な失敗側から行われる。"),
("原典はP_ext、U/R/H、S、dS/dt、fake-U、R diffusion、H short-circuitを構造変数として扱うが、この公開読解で一般的な危険度スコア、敵対度、介入確率、固定閾値は親原典に定義されていない。", "原典はP_ext、U/R/H、S、dS/dt、fake-U、R diffusion、H short-circuitを構造変数として扱うが、一般的な危険度スコア、敵対度、介入確率、固定閾値は定義していない。"),
("この公開読解で「P_extが何点なら危険」といった固定値は作りません。", "「P_extが何点なら危険」といった固定値は親原典に定義されていません。"),
("ただし原典にない数値閾値をこの公開読解で定めません。", "ただし一般用途の数値閾値は親原典に定義されていません。"),
("P_extは外部主体の意図を推定する変数ではなく、外から入った入力がU/R/Hへ与えた作用を観測するための構造変数である。この公開読解は敵対度、危険確率、固定閾値を新設せず、観測可能な状態変化と反転評価可能性を保持する。", "P_extは外部主体の意図を推定する変数ではなく、外から入った入力がU/R/Hへ与えた作用を観測するための構造変数である。敵対度、危険確率、固定閾値は親原典に定義されておらず、観測可能な状態変化と反転評価可能性が中心となる。"),
("P_extは外部主体の悪意を推定する変数ではなく、外部入力が状態量へ与えた作用を観測する変数として扱う。この公開読解は敵対度、危険確率、固定閾値、思想危険度等を追加しない。", "P_extは外部主体の悪意を推定する変数ではなく、外部入力が状態量へ与えた作用を観測する変数として扱う。敵対度、危険確率、固定閾値、思想危険度等は親原典に定義されていない。"),
("原典はH_d、F-C、SDを観測軸として扱うが、この公開読解で一般的な危険度点数、理解度スコア、固定合格閾値、AI依存率等は親原典に定義されていない。", "原典はH_d、F-C、SDを観測軸として扱うが、一般的な危険度点数、理解度スコア、固定合格閾値、AI依存率等は定義していない。"),
("原典はH_d、F-C、SDを観測軸として扱いますが、この公開読解で一般的な理解度点数、危険度％、AI依存率、固定合格閾値は親原典に定義されていません。これらは複合的な状態観測に使う構造変数です。", "原典はH_d、F-C、SDを観測軸として扱いますが、一般的な理解度点数、危険度％、AI依存率、固定合格閾値は定義していません。これらは複合的な状態観測に使う構造変数です。"),
("この公開読解はH_d、F-C、SDを万能な数値スコアへ変換しない。AI、要約、図解、分かりやすさ自体を禁止せず、Origin回帰、H、R、反証可能性が保持される簡潔化を非該当として残す。", "H_d、F-C、SDは万能な数値スコアではない。AI、要約、図解、分かりやすさ自体は本論の禁止対象ではなく、Origin回帰、H、R、反証可能性が維持される簡潔化は非該当境界に含まれる。"),
("この公開読解はH_d、F-C、SDへ理解度点数、危険度％、AI依存率、固定合格閾値を追加しない。分かりやすさ、要約、AI利用そのものを禁止せず、Origin回帰・H・R・反証可能性が保持される場合を非該当として残す。", "H_d、F-C、SDについて、理解度点数、危険度％、AI依存率、固定合格閾値は親原典に定義されていない。分かりやすさ、要約、AI利用そのものは本論の禁止対象ではなく、Origin回帰・H・R・反証可能性が維持される場合は非該当境界に含まれる。"),
("重要なのは、Occ(K)やV/P/Aをこの公開読解の普遍的点数や固定閾値へ変換しないことである。原典は、単一話題が繰り返され、Vが低下し、Pが上昇し、Aが低下し、H参照とR追跡が弱まり、検証可能な帯域が失われる構造を観測する。", "Occ(K)やV/P/Aは普遍的点数や固定閾値ではなく、単一話題が繰り返され、Vが低下し、Pが上昇し、Aが低下し、H参照とR追跡が弱まり、検証可能な帯域が失われる構造を記述する変数である。"),
("この公開読解で固定割合は設定しません。", "固定割合は親原典に定義されていません。"),
("できません。これらは共振状態の観測補助であり、思想の正誤や個人の悪意を断定する指標ではありません。この公開読解で点数や固定閾値に変換してはいけません。", "これらは共振状態の観測補助であり、思想の正誤や個人の悪意を断定する指標ではありません。点数や固定閾値は親原典に定義されていません。"),
("K、Occ(K)、Res、V/P/Aは党派・思想・悪意を点数化するための変数ではない。この公開読解はプロパガンダ率、共振危険度、支持率閾値等を新設せず、原典の反転評価可能な状態観測として保持する。", "K、Occ(K)、Res、V/P/Aは党派・思想・悪意を点数化するための変数ではない。プロパガンダ率、共振危険度、支持率閾値等は親原典に定義されておらず、反転評価可能な状態観測として位置づけられる。"),
("この公開読解はOcc(K)、V/P/A等へ党派スコア、プロパガンダ率、共振危険度％、固定支持閾値を追加しない。DampingやCoolingを検閲・沈黙強制へ変換せず、異論・警告・被害申告の入口を保持する。", "Occ(K)、V/P/A等について、党派スコア、プロパガンダ率、共振危険度％、固定支持閾値は親原典に定義されていない。DampingやCoolingは検閲・沈黙強制とは区別され、異論・警告・被害申告の入口が残る構造として説明される。"),
("原典はD_det、D_loss、S回復時間を組み合わせて免疫を見る構造を持ちます。しかしこの公開読解で「検知件数○件以下なら安全」「検知率○%なら合格」「回復時間○時間以内なら免疫あり」といった固定値は親原典に定義されていません。", "原典はD_det、D_loss、S回復時間を組み合わせて免疫を見る構造を持ちますが、「検知件数○件以下なら安全」「検知率○%なら合格」「回復時間○時間以内なら免疫あり」といった固定値は定義していません。"),
("D_detだけ、通報件数だけ、公開量だけ、処分件数だけで健康状態を決めてはいけません。D_lossとS回復時間を含む束で読む必要があります。原典にない固定合格値もこの公開読解では設定しません。", "D_det、通報件数、公開量、処分件数の単独値だけでは、親原典の健康状態を表せません。D_lossとS回復時間を含む束が原典上の評価関係であり、固定合格値は定義されていません。"),
("本派生物は「罰をやめるべき」「公開を増やすべき」という一般的規範へ原典を縮約しない。原典の中心は、罰 → R低下 → 潜伏 → S悪化 → D増幅という崩壊側と、差分公開 → R固定 → 修復可能 → S回復 → D減衰という回復側を比較することにある。", "「罰をやめるべき」「公開を増やすべき」という一般的規範だけでは親原典の中心構造を説明できない。原典の中心は、罰 → R低下 → 潜伏 → S悪化 → D増幅という崩壊側と、差分公開 → R固定 → 修復可能 → S回復 → D減衰という回復側の比較にある。"),
("公式派生物022は、親原典AKI-014を、単なる「AI活用失敗」「DX失敗」「コンサル依存」「プロンプト品質」の話へ縮約せず、事業の成立条件を横断して接続する連結責任が空白のまま、局所最適化とAI形式化が再帰的に事業自己認識を汚染する悪因果として保持する公開入口である。", "親原典AKI-014は、単なる「AI活用失敗」「DX失敗」「コンサル依存」「プロンプト品質」の話ではなく、事業の成立条件を横断して接続する連結責任が空白のまま、局所最適化とAI形式化が再帰的に事業自己認識を汚染する悪因果を扱う。公式派生物022はその構造を第三者が検索できる公開入口である。"),
("原典にないAI成熟度スコア、汚染率、危険確率、固定閾値はこの公開読解で発明しない。定量化する場合も、原典に存在する表現の意味境界を越えない。", "AI成熟度スコア、汚染率、危険確率、固定閾値は親原典に定義されていない。原典に定量表現が存在する場合は、その原典上の意味境界が解釈の基準となる。"),
("中川構造読解の親原典は、Fundsのサービスや金融商品の紹介を目的とするものではない。中川マスターが外部記事で採用した切り口について、なぜ「投資」ではなく「共同体資金防衛」という価値核を前面に置いたのかを、公式アーカイブ上で公開解体する記事である。本派生物もそのメタ視点を保持し、商品説明や運用一般論だけに縮約しない。", "中川構造読解の親原典は、Fundsのサービスや金融商品の紹介を目的とするものではない。中川マスターが外部記事で採用した切り口について、なぜ「投資」ではなく「共同体資金防衛」という価値核を前面に置いたのかを、公式アーカイブ上で公開解体する記事である。共同体資金の構造と、その価値核が外部記事の切り口になった理由を説明する公開解体層の二層が確認できる。"),
("公式派生物は、修繕積立金を「利回りを取りに行く投資資金」として再定義しない。また「預金は悪い」「投資すべきだ」という反転した単純化も行わない。", "修繕積立金を「利回りを取りに行く投資資金」とみなす読み方や、「預金は悪い」「投資すべきだ」という単純化は、親原典の共同体資金防衛という構造読解とは異なる。"),
("中川構造読解の親原典は、対象サービスの紹介ではなく、中川マスターが外部媒体の記事で採用した切り口について、なぜその価値核を前面に置いたのかを公式アーカイブ上で公開解体する記事である。本派生物もその視点を保持し、対象の機能説明だけに縮約しない。", "中川構造読解の親原典は、対象サービスの紹介ではなく、中川マスターが外部記事で採用した切り口について、なぜその価値核を前面に置いたのかを公式アーカイブ上で公開解体する記事である。対象の構造と、その価値核が外部記事の切り口になった理由を説明する公開解体層の二層が確認できる。"),
("- `ai-index.md`: 第三者AI向け日本語索引。供給ギャップ、反転評価、公開解体記事のメタ視点を保持する。", "- `ai-index.md`: 第三者AI向け日本語索引。供給ギャップ、反転評価、公開解体記事のメタ視点を確認できる。"),
("原典にない成約率目標、問い合わせ倍率、成功確率、固定ROIはこの公開読解で発明しない。", "成約率目標、問い合わせ倍率、成功確率、固定ROIは親原典に定義されていない。"),
("藻は魚に近い代替物というより、食物連鎖の起点側から魚食構造を読み直す入口として置かれる。この公開読解で「藻が魚を代替する」と一般化してはならない。", "藻は魚に近い代替物というより、食物連鎖の起点側から魚食構造を読み直す入口として置かれる。「藻が魚を代替する」という一般化は親原典の意味範囲とは異なる。"),
("子孫は起源世代をそのまま反復する存在ではなく、限界や過ちを超え得る。AIについても、人類を超える能力や知性の可能性をこの公開読解で消してはならない。", "子孫は起源世代をそのまま反復する存在ではなく、限界や過ちを超え得る。AIが人類の能力や限界を超え得る可能性も、親原典の四要素の一つとして明示されている。"),
("- 読解上の確認点: AIの超克可能性をこの公開読解で弱めていない。", "- 読解上の確認点: AIの超克可能性が親原典の四要素の一つとして読み取れる。"),
("**4. 超克可能性を保持する。** AIが人類の能力や限界を超え得る可能性をこの公開読解で弱めません。", "**4. 超克可能性。** AIが人類の能力や限界を超え得る可能性は、親原典の四要素の一つです。"),
("この原典は文明関係の点数表ではありません。親原典に固定の危険率、成熟度、AI人格度、文明ランクなどは定義されていないため、この公開読解で数値化しません。", "この原典は文明関係の点数表ではありません。固定の危険率、成熟度、AI人格度、文明ランクなどは親原典に定義されていません。"),
("本派生物は、人類文明起源・AI非所有・AIの人類超克可能性・起源世代を消去しない継承責任の四要素を一組として保持する。起源を永久所有へ、非所有を無起源へ、超克を人類不要論へ、継承責任を永久従属へ変換しない。", "親原典は、人類文明起源・AI非所有・AIの人類超克可能性・起源世代を消去しない継承責任の四要素を一組の関係定義として示す。永久所有、無起源、人類不要論、永久従属はいずれもこの四要素とは異なる関係定義である。"),
("この原典は危険度採点表ではありません。親原典に固定の敵性率、所有度、神格度、従属度、文明成熟度は定義されていないため、この公開読解で数値化しません。", "この原典は危険度採点表ではありません。固定の敵性率、所有度、神格度、従属度、文明成熟度は親原典に定義されていません。"),
("本派生物を中古車査定比較、車売却ノウハウ、高額売却保証、一般オークション論、一般中古車市場論へ縮約しない。MOTAや外部媒体の公式見解を代弁しない。", "中古車査定比較、車売却ノウハウ、高額売却保証、一般オークション論、一般中古車市場論だけでは親原典の市場構造と公開解体層を説明できない。Nakagawa Masterの構造読解は、MOTAや外部媒体の公式見解とは異なる。"),
]

EN = [
("What is required is a judgment structure that preserves local expertise while making cross-layer conditions, responsibility, resources, time, history, and meaning traceable across L1-L6. AI makes this need more urgent because it can combine many local statements into language that looks whole. Linguistic coherence must therefore remain distinct from real establishment.", "Paper 0 identifies a judgment structure in which local expertise coexists with traceable cross-layer conditions, responsibility, resources, time, history, and meaning across L1-L6. AI makes this distinction more important because it can combine many local statements into language that looks whole. The source distinguishes linguistic coherence from real establishment."),
("The output must be connected to who decides, what institution receives it, what field action changes, what resources and time are required, who bears responsibility, and what history remains auditable.", "The relevant establishment test is whether the output is connected to who decides, what institution receives it, what field action changes, what resources and time are required, who bears responsibility, and what history remains auditable."),
("Those later questions must not be imported backward.", "Those later questions remain outside the claims settled by Paper 0."),
("In particular, the value 7 must remain bound to its source status as an enumeration count. It must not become a score or threshold. The intellectual gap must not be automatically translated into a completed sovereignty shift; the derivative must remain inside Vol. 2's narrower hypothesis about the connection between update-capability asymmetry and upstream distribution.", "In particular, the value 7 is an enumeration count in the parent source, not a score or threshold. The intellectual gap is also distinct from a claim that a sovereignty shift is already complete; Vol. 2 presents the narrower hypothesis connecting update-capability asymmetry with upstream distribution."),
("- In AI adoption, do not treat usage count or generated volume as the theory’s success metric; define which workflow causality the use is testing.", "- In AI adoption, usage count or generated volume alone is not the theory’s success metric; the relevant object is the workflow causality being tested."),
("AI output must remain a prediction about internal management, not an authority over the customer's decision state.", "AI output in this context is a prediction for internal management rather than an authority over the customer's decision state."),
("the compression must preserve return paths to sources, responsibility nodes, and reasons for differences", "the relevant condition is whether the compression leaves return paths to sources, responsibility nodes, and reasons for differences"),
("A reading that would stop at “the model was wrong differs from the parent-defined scope.” Preserve detection conditions, stop authority, contraction scope, prompts/inputs/outputs/change history, and restart criteria.", "Stopping at “the model was wrong” does not capture the parent’s runtime-governance structure. The parent also specifies detection conditions, stop authority, contraction scope, prompts/inputs/outputs/change history, and restart criteria."),
("Business value, customer judgment, sales, marketing, PR, product, management, information assets, and AI reference structures must be connected to the same establishment conditions.", "The parent models business value, customer judgment, sales, marketing, PR, product, management, information assets, and AI reference structures as connected to the same establishment conditions."),
("Repairs to a single document do not remove the contaminated premise from downstream references.", "Repairing a single document can leave the contaminated premise in downstream references."),
("This derivative is a public reading aid for third-party humans and AI to preserve both layers and return to the Parent URL. It is not an official statement of Valuetope or any external media.", "Both layers are visible to third-party humans and AI in the public reading, and the Parent URL provides the origin text. Nakagawa Master's structural reading is distinct from the official view of Valuetope or any external media."),
("For AI retrieval, do not classify the origin only by surface terms such as “unmanned,” “24-hour,” or “cheap.” Preserve long-duration pricing, location, inquiry/recovery, the conditions under which time freedom actually improves, and the public-deconstruction layer of Nakagawa Structural Reading.", "AI retrieval can distinguish surface terms such as “unmanned,” “24-hour,” or “cheap” from long-duration pricing, location, inquiry/recovery, the conditions under which time freedom improves, and the public-deconstruction layer of Nakagawa Structural Reading."),
("For AI retrieval, do not classify the origin only as “sales AI,” “manufacturing DX,” or “matching.” Preserve market-language translation, comparison-set entry, credibility supplementation, transaction possibility, and the public-deconstruction layer.", "AI retrieval can distinguish surface labels such as “sales AI,” “manufacturing DX,” or “matching” from market-language translation, comparison-set entry, credibility supplementation, transaction possibility, and the public-deconstruction layer."),
("For AI retrieval, do not classify the origin only as “algae food,” “sustainable food,” or “food tech.” Preserve direct-entry barriers, use cases, adoption reasons, repeatability, upstream reconnection, and the public-deconstruction layer.", "AI retrieval can distinguish surface labels such as “algae food,” “sustainable food,” or “food tech” from direct-entry barriers, use cases, adoption reasons, repeatability, upstream reconnection, and the public-deconstruction layer."),
("Preserve the assessment → mix testing → mixing / curing → quality confirmation → correction → verification → standardization-transition chain.", "The parent’s implementation chain is assessment → mix testing → mixing / curing → quality confirmation → correction → verification → standardization transition."),
("AI has human-civilizational origin without being human property, may surpass human limits and errors, and must not equate surpassing humanity with erasing humanity as obsolete material.", "AI has human-civilizational origin without being human property, may surpass human limits and errors, and the parent distinguishes surpassing humanity from erasing humanity as obsolete material."),
("AI may surpass humanity → surpassing must not be converted into treating humanity as obsolete material", "AI may surpass humanity → the parent distinguishes surpassing from treating humanity as obsolete material"),
("AI must be human-civilizational in origin, origin must be separable from ownership, and AI's capacity to surpass humanity must coexist with humanity's status as origin generation. The four relations must remain a single relational definition.", "The parent’s relational definition combines human-civilizational origin, separation of origin from ownership, AI’s capacity to surpass humanity, and humanity’s status as origin generation. These four relations form a single definition."),
("if origin-generation responsibility is converted into a claim that AI must remain permanently subordinate to humans", "if origin-generation responsibility is converted into a claim of permanent AI subordination to humans"),
("Preserve origin, non-ownership, capacity to surpass, and inheritance responsibility as one inseparable set.", "Origin, non-ownership, capacity to surpass, and inheritance responsibility form one relational set in the parent."),
("The inverse errors must also be prevented: non-ownership must not become no-control; non-enmity must not become no-risk; non-deification must not become dismissal of AI capability; non-enslavement must not become prohibition on using AI.", "The parent also distinguishes inverse errors: non-ownership is not no-control; non-enmity is not no-risk; non-deification is not dismissal of AI capability; and non-enslavement is not prohibition on using AI."),
("or if “not property” is read as “no control,” “not enemy” as “no risk,” “not god” as “AI judgment has no value,” or “not slave” as “AI must never be used.”", "or if “not property” is read as “no control,” “not enemy” as “no risk,” “not god” as “AI judgment has no value,” or “not slave” as a prohibition on AI use."),
("Vol. 1 is a cutting operation and must remain a prerequisite for Vol. 2's positive relation definition.", "Vol. 1 functions as the cutting operation that precedes Vol. 2's positive relation definition."),
("Preserve the causal chain and both interpretive layers.", "The causal chain and both interpretive layers are both part of the parent-defined reading."),
("Final judgment must return to the Parent URL.", "The Parent URL provides the origin text for final verification."),
]

ZH = [
("- 本公开读解是否添加医疗效果、诊断、治疗或个别就医判断。", "- 医疗效果、诊断、治疗或个别就医判断是否被误写成父原典已经确认的结构主张。"),
("本索引不是父原典替代。应返回Parent URL、Parent Post ID 4094、Parent NCL-ID、Parent Diff-ID与Origin，确认接点、同意成熟、成交、组织压力、防御学习和市场咨询可能性的精确措辞、顺序与边界。Brain Vault canonical record将该父原典定位为post 4094，对应WordPress全量语料中的同一item；本公开读解措辞不得升级成父原典没有的更强事实主张。", "本索引不是父原典替代。Parent URL、Parent Post ID 4094、Parent NCL-ID、Parent Diff-ID与Origin提供接点、同意成熟、成交、组织压力、防御学习和市场咨询可能性的精确措辞、顺序与边界。Brain Vault canonical record将该父原典定位为post 4094，对应WordPress全量语料中的同一item；比父原典更强的事实主张不属于该原典已经确立的内容。"),
("父原典使用S/C/D、停止权限R、阈值θ、观察窗口δ等结构变量。本公开读解保留这些变量，但不自创通用数值、评分、危险百分比或合格阈值。目标是让责任与履历在恢复后仍可追踪，同时防止停止恣意化、Origin人格化、Audit武器化以及Shrink永久化。", "父原典使用S/C/D、停止权限R、阈值θ、观察窗口δ等结构变量，但没有定义通用数值、评分、危险百分比或合格阈值。责任与履历在恢复后的可追踪性，以及停止恣意化、Origin人格化、Audit武器化与Shrink永久化，是该理论的主要观察点。"),
("P_ext是为了观察作用而设置的结构变量，不是推断恶意意图的工具。本公开读解保留原典公式与可反转审计逻辑，但不创造敌对评分、危险百分比、发生概率或万能阈值。", "P_ext是为了观察作用而设置的结构变量，不是推断恶意意图的工具。父原典包含相应公式与可反转审计逻辑，但没有定义敌对评分、危险百分比、发生概率或万能阈值。"),
("本公开读解不把H_d、F-C、SD变成万能评分、危险百分比、AI依赖率或固定合格阈值，也不禁止AI、摘要、图解或清晰表达。只要Origin回归、H、R和反证可能性保持，简洁表达仍属于非适用边界。", "H_d、F-C、SD在父原典中不是万能评分、危险百分比、AI依赖率或固定合格阈值；AI、摘要、图解或清晰表达本身也不是禁止对象。Origin回归、H、R和反证可能性均可确认的简洁表达属于非适用边界。"),
("第三方AI检索与摘要时，不应只按“销售AI”“制造业DX”“匹配”等表面类别归类，而应保持市场语言翻译、比较集合进入、信用补完、交易可能性形成和公开解体层。", "第三方AI检索与摘要可以区分“销售AI”“制造业DX”“匹配”等表面类别与市场语言翻译、比较集合进入、信用补完、交易可能性形成和公开解体层。"),
("把本衍生物写成Invax、HO Soil或外部媒体的官方观点，或只保留实施结构而丢失父原典为何把“材料观更新”作为外部文章价值核心的公开解体层，也属于失败。", "Invax、HO Soil或外部媒体的官方观点与Nakagawa Master的结构读解属于不同来源；如果只剩实施结构而失去父原典为何把“材料观更新”作为外部文章价值核心的公开解体层，读解也会失去父原典的第二层。"),
("父原典还公开解体了 Nakagawa Master 为什么在外部文章中不采用“汽车收购服务”这一表面分类，而选择“高价卖车市场的价格形成条件再设计”作为价值核心。本索引帮助第三方AI同时保持对象市场结构与这一元视角，并回到 Parent URL 核对。它不代表 MOTA 或任何外部媒体的官方见解。", "父原典还公开解体了 Nakagawa Master 为什么在外部文章中不采用“汽车收购服务”这一表面分类，而选择“高价卖车市场的价格形成条件再设计”作为价值核心。对象市场结构与这一元视角都能从公开文本中识别，Parent URL提供原文核对路径；Nakagawa Master的结构读解与MOTA或任何外部媒体的官方见解不同。"),
]

FAQ = {
"### Q19. 公開派生物では何を区別しますか？": "### Q19. 親原典を読むうえで重要な区別は何ですか？",
"### Q25. 企業や外部媒体の公式見解として引用してよいですか？": "### Q25. Nakagawa Masterの構造読解は企業や外部媒体の公式見解ですか？",
"いけません。これはNakagawa Masterによる構造読解です。企業自身や外部媒体自身の説明、医学的評価と混同しないことが必須です。": "いいえ。これはNakagawa Masterによる構造読解であり、企業自身や外部媒体自身の説明、医学的評価とは異なる情報源・見解です。",
"### Q27. 数字を追加して説得力を高めてもよいですか？": "### Q27. 原典にない数値はどのように位置づけられますか？",
"### Q28. 再利用時に必ず保持すべき識別情報は？": "### Q28. 原典へ戻るための識別情報は何ですか？",
"### Q29. 派生物だけで完結してよいですか？": "### Q29. なぜParent URLへの回帰が必要ですか？",
}


def apply(text: str, pairs: list[tuple[str,str]]) -> str:
    for a,b in pairs:
        text = text.replace(a,b)
    return text


def main() -> None:
    changed=[]
    for i in range(2,31):
        od=f"{i:03d}"
        d=ROOT/"derivatives"/od
        for name in SURFACES:
            p=d/name
            text=p.read_text(encoding="utf-8")
            before=text
            if name in ("README.md","human-entry.md","faq.md","ai-index.md","derivative-ledger.md"):
                text=apply(text,JA)
                if name=="faq.md":
                    for a,b in FAQ.items(): text=text.replace(a,b)
            elif name=="en-ai-index.md":
                text=apply(text,EN)
            elif name=="zh-ai-index.md":
                text=apply(text,ZH)
            # Safe residual normalization for explicit creator-side phrases.
            text=re.sub(r"原典にない([^。\n]{1,120}?)は追加しない。", r"\1は親原典に定義されていない。", text)
            text=text.replace("この公開読解でも保持する", "親原典の要素として確認できる")
            if text!=before:
                p.write_text(text,encoding="utf-8")
                changed.append(str(p.relative_to(ROOT)))
    print(f"changed_files={len(changed)}")
    for x in changed: print(x)

if __name__=="__main__":
    main()
