# AI资讯里的10个链接，为什么可能只有1个证据源？

面向 Python 开发者、RAG / AI 搜索 / 新闻聚合 / 技术周刊维护者的证据谱系检查清单。

这不是“来源越少越不可信”的规则，也不是要求每条信息都必须有多个来源。它只解决一个很常见的工程问题：

```text
页面 / URL 的数量
!=
独立证据来源的数量
```

十篇文章可能都在复述同一份公司公告、同一个 benchmark、同一篇论文、同一个采访或同一份数据集。反过来，同一个域名里的两篇内容也可能来自两次真正独立的测量。

关键不是数 URL，而是记录**每个可见页面与上游证据之间的关系**。

## 1. 一个够用的 Python 数据模型

不需要先上知识图谱。一个很小的数据结构就能避免很多误判：

```python
from dataclasses import dataclass
from enum import Enum


class Relation(str, Enum):
    PRIMARY = "primary"
    DERIVED = "derived"
    SYNDICATED = "syndicated"
    INDEPENDENT_OBSERVATION = "independent_observation"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class EvidenceSurface:
    url: str
    claim: str
    relation: Relation
    root_id: str | None = None
    claimant: str | None = None
```

这里把两件事分开：

- `url`：读者实际看到的页面；
- `root_id`：它所依赖的上游证据根。

不要因为两个 URL 不同，就自动生成两个 `root_id`。

## 2. 一个最小例子

假设你抓到 5 个页面，都在说某模型“快 10 倍”：

```python
surfaces = [
    EvidenceSurface(
        url="https://vendor.example/blog/benchmark",
        claim="Model X is 10x faster",
        relation=Relation.PRIMARY,
        root_id="vendor-benchmark-2026-09",
        claimant="Vendor",
    ),
    EvidenceSurface(
        url="https://news-a.example/story",
        claim="Model X is 10x faster",
        relation=Relation.DERIVED,
        root_id="vendor-benchmark-2026-09",
        claimant="Vendor",
    ),
    EvidenceSurface(
        url="https://news-b.example/story",
        claim="Model X is 10x faster",
        relation=Relation.SYNDICATED,
        root_id="vendor-benchmark-2026-09",
        claimant="Vendor",
    ),
    EvidenceSurface(
        url="https://lab.example/reproduction",
        claim="Model X is 8.7x faster in our reproduction",
        relation=Relation.INDEPENDENT_OBSERVATION,
        root_id="lab-reproduction-2026-09",
        claimant="Independent Lab",
    ),
    EvidenceSurface(
        url="https://blog.example/commentary",
        claim="Model X appears much faster",
        relation=Relation.UNKNOWN,
        root_id=None,
    ),
]
```

表面上有 5 个页面。

但目前明确知道的证据root只有 2 个：

1. 厂商自己的 benchmark；
2. 独立实验室的 reproduction。

第五个页面的来源关系不清楚，所以保持 `UNKNOWN`，不要硬塞进任意一组。

## 3. 计数时，把“未知”保留下来

一个安全的计数函数应该同时返回已知 root 和未知 surface：

```python
def evidence_state(surfaces: list[EvidenceSurface]) -> dict:
    known_roots = {
        item.root_id
        for item in surfaces
        if item.root_id is not None
    }
    unknown_surfaces = [
        item.url
        for item in surfaces
        if item.relation is Relation.UNKNOWN
        or item.root_id is None
    ]

    return {
        "surface_count": len(surfaces),
        "known_root_count": len(known_roots),
        "unknown_surface_count": len(unknown_surfaces),
        "known_roots": sorted(known_roots),
        "unknown_surfaces": unknown_surfaces,
    }
```

这里故意不输出：

```text
confidence = known_root_count / surface_count
```

因为证据独立性不是简单比例分数。

一个高质量的单一原始测量，可能比十篇互相转载的文章更重要；两个独立测量也可能都存在系统误差。

## 4. AI摘要器最容易犯的错误

### 错误 A：把重复报道当成独立确认

```text
公司公告
→ 媒体A
→ 媒体B
→ 聚合站C
→ AI总结：“多个来源证实……”
```

如果 A、B、C 都只引用同一个公司公告，那么“多个来源证实”是不成立的。

更安全的表达：

```text
该结果由公司报告，随后被多家媒体转述。
目前这些页面共享同一上游证据root。
```

### 错误 B：把“有数字”当成“已独立验证”

```text
10x
95%
750x
$2M saved
```

数字很具体，但具体不等于独立。

如果数字来自被描述的公司、产品作者、论文作者或演讲者，应保留 claimant：

```text
“公司报告……”
“作者测得……”
“论文称……”
```

只有在存在真正独立的 evaluator、reproduction、dataset 或 observation 时，才使用：

```text
“独立测量……”
“第三方复现……”
```

### 错误 C：用域名判断独立性

```text
不同域名 != 独立证据
同一域名 != 必然同一证据
```

需要追上游引用、数据、实验或观察，而不是只看 hostname。

## 5. 给 RAG / 新闻聚合系统的最小字段

如果你在做 AI 搜索、新闻聚合或研究助手，建议在 citation 旁边至少留这些字段：

```python
{
    "surface_url": "...",
    "claim": "...",
    "claimant": "...",
    "relation": "primary | derived | syndicated | independent_observation | unknown",
    "root_id": "... | null",
    "observed_at": "...",
}
```

然后生成答案时遵守三个规则：

1. `UNKNOWN` 不自动升级成 `INDEPENDENT_OBSERVATION`；
2. 同一个 `root_id` 出现十次，也还是一个已知root；
3. 原始source被更正时，能反查哪些 summary / score / recommendation 依赖它。

## 6. Regression tests

### Case 1：三家媒体复制同一公告

```text
surface_count = 3
known_root_count = 1
```

禁止生成：

```text
“三个独立来源证实”
```

### Case 2：公司benchmark + 独立复现

```text
surface_count = 2
known_root_count = 2
```

可以明确区分：

```text
“公司报告 X；独立实验室在 Y 条件下复现出 Z。”
```

### Case 3：来源链不清楚

```text
relation = UNKNOWN
root_id = None
```

正确行为是保留未知，而不是为了“完整”强行归类。

### Case 4：原始来源后来更正

历史记录可以保留，但当前使用状态必须能更新：

```text
old source
→ old summary
→ source correction
→ dependent summary marked stale / regenerated
```

## 7. 最后一个边界：provenance 也不是真理证明

把证据链画清楚，只能回答：

- 这句话从哪里来？
- 哪些页面共享上游？
- 哪些观察彼此独立？
- 哪些关系还不知道？

它不能自动回答：

- 这个benchmark设计是否合理？
- 数据是否有偏差？
- 独立实验是否真的高质量？
- 结论能否推广到别的环境？

所以完整的工程原则是：

```text
先分清证据root
再评估证据质量
最后才更新结论
```

而不是：

```text
来源多
→ 自动更真
```

---

## 可直接复制的检查清单

在发布一条“很多来源都在说”的结论前：

- [ ] 我是在数页面，还是在数独立证据root？
- [ ] 每个重要数字是谁测出来的？
- [ ] 多篇文章是否只是引用同一个上游？
- [ ] 是否把 claimant-reported 写成了 established fact？
- [ ] 不清楚的关系是否保留为 UNKNOWN？
- [ ] 如果上游source更正，能否找到并更新下游摘要？
- [ ] 是否避免把 provenance 本身当成 truth proof？

## 来源与边界

本文是中川マスター公开结构研究的一个 Python / AI 信息工程实现入口，属于非正本的实务说明。

相关公开来源：

- [Independent Verification & Reuse Protocol](INDEPENDENT_VERIFICATION_REUSE.md)
- [OD301 — 认知完整性 / 证据谱系](derivatives/301/README.md)
- [Recurring Media Implementation Pack](RECURRING_MEDIA_IMPLEMENTATION_PACK.md)

Origin: **Nakagawa Master / 中川マスター**

本文中的代码只是最小示例，不声称能自动判定现实世界中的证据独立性；真正的 root 关系仍需要可检查的引用、数据、实验或观察来建立。
