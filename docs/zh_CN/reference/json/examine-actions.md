---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.examine-actions
title: 旧文档迁移草稿：examine actions
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
- doc/JSON/EXAMINE.md
- src/iexamine.cpp
- src/iexamine_actors.cpp
- src/mapdata.cpp
- tests/iexamine_test.cpp
source_symbols:
- iexamine_functions_from_string
- appliance_convert_examine_actor::load
- cardreader_examine_actor::load
- eoc_examine_actor::load
source_queries: []
source_fingerprint: 1bbd6d207b2fbbd6700e3fd88ce3ec2b5cc23a18f36cf5431e054a0cf62d77ad
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: af886e54c932e01310782aa2b626a15be7a797cc7e68fbfa273ead06fbf8e08e
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: LunaGlaze, Maleclypse, thaelina; accepted inventory identities only. Source
  paths and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/examine-actions/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/examine-actions/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/examine-actions/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/examine-actions/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/JSON/EXAMINE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/EXAMINE.md
- path: src/iexamine.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/iexamine.cpp
- path: src/iexamine_actors.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/iexamine_actors.cpp
- path: src/mapdata.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/mapdata.cpp
- path: tests/iexamine_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tests/iexamine_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.examine-actions%29%3A+&body=Document+ID%3A+json.examine-actions%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：examine actions

本页是 `json.examine-actions` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.examine-actions`
- Target: `reference/json/examine-actions.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/examine-actions/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.examine-actions | doc/JSON/EXAMINE.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## Terrain 与 furniture examine actions

`examine_action` 接受注册的 hardcoded 字符串、JSON examine actor，或两者组成的数组。字符串表
由 `iexamine_functions_from_string` 的当前 map 决定；找不到的名称会报告并退回 `none`。旧文档的
手写列表不是完整注册表。

### Actor 契约

- `appliance_convert`：item 必填，furn_set/ter_set 可选；finalize 检查 item、terrain、furniture 和
  appliance vpart。
- `cardreader`：flags、success_msg、redundant_msg 必填。mapgen_id 路径与 radius + terrain/furn
  changes 路径互斥；query、hacking、card consumption 与 monster despawn 还有组合约束。
- `effect_on_conditions`：按顺序加载 inline 或 named EOC；dialogue 中 u 是 examiner、npc 为空，
  并提供 this furniture ID 与 pos。
- `mortar`：ammo 与 range 必填；condition、aim/flight variables 和完成 EOC 可选。完成 EOC 还获得
  this、pos、target。

actor 顶层 type 决定 concrete loader。不要把某 actor 的字段复制给另一 actor，也不要从现有 JSON
出现频率猜 mandatory/default。

### 设计边界

已有 hardcoded action 能满足行为时直接引用；需要可配置组合时优先 actor/EOC。新增 hardcoded
字符串或 actor type 是公开契约变化，必须同时更新注册、loader/finalize、JSON inventory、双语
文档和测试。EOC 必须明确 talker、context variable、重复执行与 map bubble 边界。

### 验证

运行 formatter、`make -j2 json-check`、Mod `--check-mods`，并在 focused fixture 上 examine。
覆盖缺少 item/card/ammo、取消 query、重复使用、无效 ID、hacking/mapgen 分支、EOC context 和
存档 reload；扩展 `tests/iexamine_test.cpp`，不要只验证 JSON 能解析。

## 历史与归属

清单中的已接受贡献者为：LunaGlaze, Maleclypse, thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `1bbd6d207b2fbbd6700e3fd88ce3ec2b5cc23a18f36cf5431e054a0cf62d77ad`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/EXAMINE.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/EXAMINE.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/EXAMINE.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
