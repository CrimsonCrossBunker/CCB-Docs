---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.inheritance
title: 旧文档迁移草稿：inheritance
language: zh_CN
status: active
doc_type: explanation
audiences:
- new-contributor
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 365
last_human_reviewer: LYHGLYTX
source_paths:
- doc/JSON/JSON_INHERITANCE.md
- src/generic_factory.h
- src/generic_factory.cpp
- src/init.cpp
- tests/generic_factory_test.cpp
source_symbols:
- generic_factory::load
source_queries: []
source_fingerprint: 76ca6fc5abc73f10dffb3ed498ff09916d84b6c9ce62382a15ab58d823cb365c
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: a3af487030b9687050c5e5dd7f185c19fa7ba6653cf7a331b8a2b59228fb45ea
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: zihanZheng, ehughsbaird, thaelina; accepted inventory identities only.
  Source paths and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/inheritance/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/inheritance/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/inheritance/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/inheritance/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/JSON/JSON_INHERITANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/JSON_INHERITANCE.md
- path: src/generic_factory.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/generic_factory.h
- path: src/generic_factory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/generic_factory.cpp
- path: src/init.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/init.cpp
- path: tests/generic_factory_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/generic_factory_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.inheritance%29%3A+&body=Document+ID%3A+json.inheritance%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：inheritance

本页是 `json.inheritance` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.inheritance`
- Target: `reference/json/inheritance.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/inheritance/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.inheritance | doc/JSON/JSON_INHERITANCE.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 当前 CCB JSON 继承规则

`copy-from` 不是所有 JSON object type 自动拥有的语言特性。许多类型使用
`generic_factory`，另一些拥有专用实现，仍有类型完全不支持。每次使用前都要从当前
注册函数进入 loader，确认该对象真正实现了哪些操作。

### generic_factory 的加载顺序

对使用 `generic_factory` 的对象，典型顺序是：

1. 若有 `copy-from`，先查找已加载的具体对象或 `abstract`。
2. 父对象尚未加载时把子对象放入 deferred 队列，稍后重试。
3. 复制父对象，再由子对象的 loader 覆盖或调整字段。
4. `abstract` 只供继承；同一对象同时写 `abstract` 和真实 `id` 会报错。
5. finalize/check 阶段解析交叉 ID，并可能发现加载阶段未能证明的问题。

因此加载顺序通常可以由 deferred 处理，但不代表循环继承合法，也不代表跨 Mod 的覆盖
顺序无关。

### 四种修改方式

```jsonc
{
  "type": "ITEM",
  "id": "ccb_example_child",
  "copy-from": "ccb_example_parent",
  "name": { "str": "example child" },
  "relative": { "weight": "50 g" },
  "proportional": { "price": 1.2 },
  "extend": { "flags": [ "WATER_FRIENDLY" ] },
  "delete": { "flags": [ "FRAGILE" ] }
}
```

- 顶层直接字段通常替换继承值。
- `relative` 在 reader 支持时对父值做增量。
- `proportional` 在 reader 支持时对父值乘系数。
- `extend`/`delete` 在支持的容器 reader 上添加/删除成员。

这些只是意图，不是保证。没有 `copy-from` 时使用这些块会被拒绝或警告；不支持的类型、
字段或 reader 可能报错、忽略或采用专用行为。尤其不能因为 `ITEM.flags` 支持
`extend`，就推断任意对象的任意数组也支持。

### abstract、真实对象与链深度

`abstract` 适合表达一组定义始终共享的稳定基础，不能在游戏中作为真实 ID 使用。优先
保持一至两层、含义窄的继承；长链会让一次父项调整隐式改变多个 Mod/对象，也会使存档
兼容和数值审阅困难。纯显示差异若已有 variant 机制，通常不需要新继承链。

### 专用实现示例

- `recipe_dictionary::load` 自己延迟并复制 recipe；recipe 内联 requirements 有额外替换规则。
- item group 只允许从同 ID 的既有 group 复制，且 `extend` 由其专用 loader 读取。
- 部分对象可能默认扩展某些容器，另一些对象只支持 `copy-from` 而不支持四种修改块。

不要维护一份声称永久完整的“支持类型列表”。以当前 object registry 定位注册，再检查
loader、reader 和测试。

### 审阅与验证

1. 明确父项来自哪个 core/Mod、其加载顺序和稳定 ID。
2. 检查直接字段是 replacement、merge 还是专用语义。
3. 对照 reader 确认 `relative`/`proportional` 的单位与范围。
4. 用现有测试或最小 Mod 覆盖链、缺失父项、重复 ID 与 finalize。
5. 运行 formatter、`make -j2 json-check` 和实际 Mod 集的 `--check-mods`。

如果无法从实现证明某字段支持继承操作，改为显式完整定义或先补测试，不要靠加载未报错
推断行为。

## 历史与归属

清单中的已接受贡献者为：zihanZheng, ehughsbaird, thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `d32b9cc880a85480840d82cfa05d256c78a16615`；聚合源指纹为 `76ca6fc5abc73f10dffb3ed498ff09916d84b6c9ce62382a15ab58d823cb365c`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/JSON_INHERITANCE.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/JSON_INHERITANCE.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/JSON_INHERITANCE.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
