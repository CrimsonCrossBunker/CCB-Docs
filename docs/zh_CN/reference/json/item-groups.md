---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.item-groups
title: 旧文档迁移草稿：item groups
language: zh_CN
status: draft
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
last_human_reviewer: Pending human review
source_paths:
- doc/JSON/ITEM_SPAWN.md
- src/item_factory.cpp
- src/item_group.cpp
- data/json/itemgroups/Food/food.json
- tests/item_group_test.cpp
- tests/item_spawn_test.cpp
source_symbols:
- Item_factory::load_item_group
- item_group::load_item_group
- Item_spawn_data::relic_generator::load
source_queries: []
source_fingerprint: 396e03a55ee867b47adbf915b320f8fe9c67208316db94fbab24608855f051be
authority: docs-explanation
verified_commit: 02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 27786c6fbc7d13d0750c8a150334402fcf26b3e25fb8356b429ac7e2047e3567
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: dumb-kevin, thaelina; accepted inventory identities only. Source paths
  and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/item-groups/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/item-groups/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/item-groups/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/item-groups/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
source_urls:
- path: doc/JSON/ITEM_SPAWN.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/ITEM_SPAWN.md
- path: src/item_factory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/item_factory.cpp
- path: src/item_group.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/item_group.cpp
- path: data/json/itemgroups/Food/food.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/data/json/itemgroups/Food/food.json
- path: tests/item_group_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/tests/item_group_test.cpp
- path: tests/item_spawn_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/tests/item_spawn_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.item-groups%29%3A+&body=Document+ID%3A+json.item-groups%0ALanguage%3A+zh_CN%0AVerified+commit%3A+02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：item groups

本页是 `json.item-groups` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.item-groups`
- Target: `reference/json/item-groups.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/item-groups/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.item-groups | doc/JSON/ITEM_SPAWN.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 当前 CCB item group 契约

`item_group` 描述“生成什么”，不是物品本身。`Item_factory::load_item_group` 读取命名组，
`item_group::load_item_group` 也可在怪物掉落、配方副产物等位置读取匿名内联组。引用的
item、group、container 和事件必须使用已加载的稳定 ID。

### collection 与 distribution

```jsonc
{
  "type": "item_group",
  "id": "ccb_example_supplies",
  "subtype": "distribution",
  "entries": [
    { "item": "water_clean", "prob": 70 },
    { "item": "bandages", "prob": 30 }
  ]
}
```

- `distribution` 把 entry 的 `prob` 当相对权重，进行一次分布选择。
- `collection` 独立评估各 entry，`prob` 表示该 entry 被包含的百分比机会。
- 缺省/旧 subtype 按 distribution 处理；新内容应显式写出意图。

entry 用 `item` 引用物品、用 `group` 引用另一组。`items`/`groups` 是只适合简单 ID 与
概率的快捷形式；需要 damage、charges、count、container、event、fault、variant 或
变量时使用完整 `entries` 对象。若同时填写快捷数组和 `entries`，它们会全部加入，
不会自动去重。

### 容器、弹药与递归

group 级 `ammo`/`magazine` 是加载枪械、工具和弹匣时的百分比机会；entry 的显式
`charges` 等修饰可能覆盖默认装填行为。`container-item`、`container-group`、sealed 与
overflow 行为会影响嵌套和容量。多 magazine-well 物品不能用一个含糊的 `charges`
值分摊到所有 well；应按当前 loader 规则和真实物品测试。

嵌套 group 可以形成深链，错误递归、空分布或不存在的 ID 可能直到加载/生成时才显现。
保持层级浅，并用 `item_group::items_from` 相关测试覆盖概率之外的结构不变量。

### 在 Mod 中扩展现有组

当前实现只允许 item group 从**相同 ID** 的既有组 `copy-from`，并通过 `extend` 加入：

```jsonc
{
  "type": "item_group",
  "id": "ccb_example_supplies",
  "copy-from": "ccb_example_supplies",
  "subtype": "distribution",
  "extend": {
    "entries": [ { "item": "aspirin", "prob": 10 } ]
  }
}
```

没有 `copy-from` 的同 ID 定义会重建/覆盖 group，而不是隐式追加。加载顺序和 Mod 依赖
因此属于契约的一部分；不要假定两个 Mod 的同 ID patch 能交换顺序。

### 内联组与验证

某些字段接受 group ID、内联对象或 entry 数组。内联组会获得内部唯一 ID，不能在其他
位置引用，适合只使用一次的掉落或副产物。默认 subtype 由调用位置决定，所以从别处
复制数组前要检查该字段的 loader。

验证时运行 JSON formatter/loader、ID 检查和 `--check-mods`。对关键掉落补充 focused
test，覆盖空结果、容器溢出、charges/magazine、event gate 与可能的递归；不要用一次
Debug 菜单抽样证明概率正确。

## 历史与归属

清单中的已接受贡献者为：dumb-kevin, thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b`；聚合源指纹为 `396e03a55ee867b47adbf915b320f8fe9c67208316db94fbab24608855f051be`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/ITEM_SPAWN.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/ITEM_SPAWN.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/ITEM_SPAWN.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
