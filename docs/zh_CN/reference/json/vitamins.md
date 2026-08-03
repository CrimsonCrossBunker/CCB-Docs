---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.vitamins
title: 旧文档迁移草稿：vitamins
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
- doc/JSON/VITAMIN.md
- src/vitamin.cpp
- src/vitamin.h
- data/json/vitamin.json
- tests/vitamin_test.cpp
source_symbols:
- vitamin::load
source_queries: []
source_fingerprint: a7c81f55e1988cc468b2d6b426ffe2e675666e6607c63a88131c2bda776767d1
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 1ca285efe132588382b631aa267c9692d3991a0465a90cad81885e4aa56c4653
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: zihanZheng, thaelina; accepted inventory identities only. Source paths
  and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/vitamins/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/vitamins/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/vitamins/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/vitamins/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/JSON/VITAMIN.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/VITAMIN.md
- path: src/vitamin.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/vitamin.cpp
- path: src/vitamin.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/vitamin.h
- path: data/json/vitamin.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/vitamin.json
- path: tests/vitamin_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tests/vitamin_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.vitamins%29%3A+&body=Document+ID%3A+json.vitamins%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：vitamins

本页是 `json.vitamins` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.vitamins`
- Target: `reference/json/vitamins.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/vitamins/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.vitamins | doc/JSON/VITAMIN.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## `vitamin` 对象不是只表示营养素

CCB 的 `vitamin` registry 是角色体内随时间变化的通用量系统。`vit_type` 当前接受 `vitamin`、`toxin`、
`drug` 和 `counter`；第一方数据除钙、铁、维生素 C 外，还用它表示药物剂量、mutagen primer、血量相关
计数、过敏原和其他隐藏状态。不要因对象类型名推断其一定会出现在营养 UI。

### Loader 字段

除 generic-factory 所需的 `id`/`type` 外，新定义必须提供 `name`、`vit_type`、`min` 和 `rate`；`max`
可省略且当前默认 `0`。`deficiency` 与 `excess` 引用 effect type；`disease` 与 `disease_excess` 是数量范围
数组，依顺序映射 effect intensity。`weight_per_unit` 允许把质量换算为内部单位。`decays_into` 的每项是
目标 vitamin ID 与增减量，自然代谢一个单位时分别应用。`flags` 是字符串集合，其具体消费者要从当前
代码和数据确认。

```json
{
  "type": "vitamin",
  "id": "example_counter",
  "vit_type": "counter",
  "name": { "str": "Example counter" },
  "min": 0,
  "max": 100,
  "rate": "1 h",
  "excess": "example_effect",
  "disease_excess": [ [ 10, 49 ], [ 50, 100 ] ]
}
```

这是结构示例，不是待添加的第一方 ID。阈值的起止顺序可由 loader 处理，但范围重叠或空洞仍会产生难以
理解的结果；设计时应使用连续、可测试的区间。

## 继承、单位和验证

Vitamin 通过 `generic_factory` 支持 `copy-from`。当前测试覆盖 scalar override，以及对 `flags`、`disease`、
`disease_excess`、`decays_into` 的 `extend`/`delete`。`flags` 作为 set 去重；重复目标的 `decays_into`
条目保持为独立规则，不会自动求和。覆盖已有 `id` 时最后加载定义生效，因此 Mod 必须评估跨加载顺序兼容。

营养型数据在 JSON food 中常以 RDA 百分比表示，其他类型使用内部单位；`rate` 决定每日吸收/衰减换算，
`weight_per_unit` 决定质量换算。新增对象应运行 JSON formatting/loading、vitamin consistency 和
`[vitamin]` 专项测试，并覆盖 effect ID、边界数量、继承、自然衰减、简化营养、显示 flags、摄入延迟及
保存重载。不要把旧 MME 表或第一方数值复制为永久 Schema。

## 历史与归属

清单中的已接受贡献者为：zihanZheng, thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `a7c81f55e1988cc468b2d6b426ffe2e675666e6607c63a88131c2bda776767d1`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/VITAMIN.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/VITAMIN.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/VITAMIN.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
