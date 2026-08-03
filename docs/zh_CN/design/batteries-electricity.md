---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: design-batteries-electricity
title: 旧文档迁移草稿：batteries electricity
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
- doc/design-balance-lore/batteries_and_electricity.md
- data/json/items/battery.json
- data/json/vehicleparts/battery.json
- src/vehicle_part.cpp
- tests/battery_mod_test.cpp
source_symbols: []
source_queries: []
source_fingerprint: b3069bfcdaf5049a556adec6f61a4d44916319fd2acaf3a4bfb77ba468d5fdc0
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: d6228a69b65e05b3d6777edb7824ea753861e7d54740960687a009b2b363a4d6
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: thaelina; accepted inventory identities only. Source paths and Git history
  remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: design
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/design/batteries-electricity/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/design/batteries-electricity/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/design/batteries-electricity/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/design/batteries-electricity/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/design-balance-lore/batteries_and_electricity.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/batteries_and_electricity.md
- path: data/json/items/battery.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/items/battery.json
- path: data/json/vehicleparts/battery.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/vehicleparts/battery.json
- path: src/vehicle_part.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/vehicle_part.cpp
- path: tests/battery_mod_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/tests/battery_mod_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28design-batteries-electricity%29%3A+&body=Document+ID%3A+design-batteries-electricity%0ALanguage%3A+zh_CN%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：batteries electricity

本页是 `design-batteries-electricity` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `design-batteries-electricity`
- Target: `design/batteries-electricity.md`
- Replacement: design-batteries-electricity
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| design-batteries-electricity | doc/design-balance-lore/batteries_and_electricity.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 电池模型的边界

CCB 刻意不模拟完整电路。手持设备的供电主要抽象为容量、耗电和兼容电池类别；电压、电流、串并联
电芯以及真实接口通常不直接暴露。这个取舍让玩家关注设备能运行多久、要携带多少能源以及能否补给，
而不是解决接线问题。若某种高功率设备确实需要限制，应使用现有可见契约表达，不要假设存在未注册的
电气模拟。

## 当前数据表示

当前电池单元由物品数据中的 `MAGAZINE` 对象表示，使用电池弹药类别、容量、默认内容和 flags 描述
储能。可换电池的工具通过 `MAGAZINE_WELL` pocket 和兼容限制接收电池；适配器、ammo restrictions、
flags 及对应代码和测试共同决定实际兼容性。`data/json/items/battery.json` 是当前第一方电池数据的入口
之一，其中的型号范围已经超过旧文档表格，包括特殊或原子能电池，因此旧表不能作为完整清单。

大型载具储能和手持工具电池并非同一个可互换接口。修改任一侧前，沿当前 item、pocket、ammo、
vehicle part 注册和测试分别追踪，不要仅根据显示名称推断兼容。

## 添加或校准设备

1. 从可信的实际运行时间和功率资料估算量级，并记录资料条件；制造商的最佳情况宣传不能直接当作测试值。
2. 选择现有最接近的电池类别，让容量与设备耗电共同得到合理运行时间。不要为了还原多个实体电芯而无故新增类型。
3. 检查工具的 pocket、ammo restrictions、默认电池、可用适配器、充电路径和拆装行为。
4. 覆盖空电池、部分电量、满电、错误类别、适配器、保存重载和充电等边界。
5. 运行 JSON 加载与电池专项测试；若改变公开 JSON 字段或兼容关系，同时记录 Mod 和文档影响。

设备真实世界电池寿命很短或功率很高时，应提高估算精度；低功耗且余量很大的设备可以采用更宽松的
近似。最终目标是可信的使用时长和清楚的玩家决策，而不是表面上精确但未被运行时实现的电气参数。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `b3069bfcdaf5049a556adec6f61a4d44916319fd2acaf3a4bfb77ba468d5fdc0`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/design-balance-lore/batteries_and_electricity.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/batteries_and_electricity.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/batteries_and_electricity.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
