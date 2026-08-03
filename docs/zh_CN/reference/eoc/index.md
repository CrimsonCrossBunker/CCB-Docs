---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: eoc.reference
title: 旧文档迁移草稿：eoc
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
- doc/JSON/EFFECT_ON_CONDITION.md
- src/effect_on_condition.cpp
- src/condition.cpp
- src/npctalk.cpp
- data/json/effects_on_condition/example_eocs.json
- tests/npc_talk_test.cpp
source_symbols:
- effect_on_condition::load
- effect_on_conditions::load
- conditional_t::conditional_t
source_queries: []
source_fingerprint: f5ff80cfe7f5b4b6e2e84785d83c869cae6b09fa5d8e24a3010677762a0564b2
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 31c49a95383d3d22a0b508f725c766c519402cb745012b8e5a5586b67ff5fce2
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: zihanZheng, LunaGlaze, Anton Simakov, Maleclypse, GuardianDll, thaelina;
  accepted inventory identities only. Source paths and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: eoc
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/eoc/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/eoc/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/eoc/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/eoc/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/JSON/EFFECT_ON_CONDITION.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/EFFECT_ON_CONDITION.md
- path: src/effect_on_condition.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/effect_on_condition.cpp
- path: src/condition.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/condition.cpp
- path: src/npctalk.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/npctalk.cpp
- path: data/json/effects_on_condition/example_eocs.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/json/effects_on_condition/example_eocs.json
- path: tests/npc_talk_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/npc_talk_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28eoc.reference%29%3A+&body=Document+ID%3A+eoc.reference%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：eoc

本页是 `eoc.reference` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `eoc.reference`
- Target: `reference/eoc/index.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/eoc/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| eoc.reference | doc/JSON/EFFECT_ON_CONDITION.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 当前 CCB EOC 模型

Effect on Condition（EOC）把对话系统的 condition 和 effect 组合成可在对话外调用的
对象。它不是角色身上的 `effect_type` 状态；两者名称接近但 loader、生命周期和用途不同。
当前可用键的完整清单由源码注册生成，见[条件索引](../eoc-conditions.md)与
[效果索引](../eoc-effects.md)，不要从旧正文手工复制一份并声称完整。

### 最小激活 EOC

```jsonc
{
  "type": "effect_on_condition",
  "id": "EOC_CCB_EXAMPLE",
  "eoc_type": "ACTIVATION",
  "condition": { "u_has_trait": "DEBUG_PREVENT_DEATH" },
  "effect": { "u_message": "The example EOC ran." },
  "false_effect": { "u_message": "The condition did not pass." }
}
```

`id` 是其他 JSON、事件和 EOC 引用的稳定标识。引用可以是具名 ID，也可以在接受该格式的
字段中写 inline EOC；loader 会记录具名引用并在一致性检查中报告不存在的 ID。

### 类型、触发与调度

当前 `effect_on_condition::load` 读取 `eoc_type`。未指定且没有 recurrence 时默认为
`ACTIVATION`；存在 `recurrence` 会强制为 `RECURRING`，与其他显式类型组合会报错。
`EVENT` 必须提供 `required_event`。死亡/防止死亡等类型的 talker 绑定和停止条件由各调用点
决定，不能只看 EOC 本身推断。

Recurring EOC 可使用 `condition`、`false_effect` 和 `deactivate_condition`。`global`
决定全局/角色队列，`run_for_npcs` 只能在 `global: true` 时使用。高频 recurrence、遍历
NPC 或地图的效果会产生真实性能成本，应测量而不是猜测。

### condition、effect 与布尔组合

condition 可以是简单字符串或对象。`and`、`or` 接受 condition 数组；`not` 包含一个
字符串或 condition 对象。无法识别的复杂 condition 会在加载时抛错。effect 可以是单项
或按顺序执行的数组，也可以通过 `if`/`then`/`else`、其他 EOC 和上下文变量组成流程。

每个 condition/effect 的参数、默认值、talker 类型和来源见生成索引。索引来自注册信息，
但示例仍需在实际调用上下文测试；“存在某个键”不代表当前 alpha/beta talker 支持它。

### alpha、beta 和 context

EOC 复用了对话命名：通常 `u_` 操作 alpha talker，`npc_` 操作 beta talker，但具体实体
可能是角色、怪物、物品、家具或不存在。事件、死亡、弹药效果等调用点可能缺少一侧；在
访问前用 `has_alpha`/`has_beta` 防护。

变量作用域包括角色侧、beta 侧、世界全局与本次调用 context。`context_val` 只在调用者
确实提供相应键时存在；事件字段也必须对照该 event 的当前 payload。不要把 context 写成
跨存档持久状态，也不要假定 EOC 重新排队后仍保留同一上下文。

### 验证

1. 从生成的 condition/effect 索引确认键、参数和源码位置。
2. 检查调用字段实际提供的 alpha、beta、context 和生命周期。
3. 运行 JSON loader、EOC registry/parser 检查及实际 Mod 集的 `--check-mods`。
4. 用 focused test 覆盖 condition true/false、缺失 talker、缺失变量和重复调用。
5. 对 recurring/event EOC 检查频率、队列、存档重载和性能。

完整示例结构见[EOC 概览](../../eoc/overview.md)和[完整 JSON/EOC 示例 Mod](../../mods/complete-json-eoc-mod.md)。

## 历史与归属

清单中的已接受贡献者为：zihanZheng, LunaGlaze, Anton Simakov, Maleclypse, GuardianDll, thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `d32b9cc880a85480840d82cfa05d256c78a16615`；聚合源指纹为 `f5ff80cfe7f5b4b6e2e84785d83c869cae6b09fa5d8e24a3010677762a0564b2`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/EFFECT_ON_CONDITION.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/EFFECT_ON_CONDITION.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/EFFECT_ON_CONDITION.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
