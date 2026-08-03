---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.faction-missions
title: 旧文档迁移草稿：faction missions
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
- doc/JSON/FACTION_MISSIONS.md
- src/faction_mission.cpp
- src/faction_camp.cpp
- data/json/faction_missions.json
- tests/faction_camp_test.cpp
source_symbols:
- faction_mission::load
source_queries: []
source_fingerprint: 06cdbc4c15861847dfbef5486ae1b1c427c73774ff0cc485322ff8a7b5e2cd93
authority: docs-explanation
verified_commit: 02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 21e4cbc9e5aeae5b73b62b5ea4757ea42d1155adef28b6e39c00acc17dc37c4e
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
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/faction-missions/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/faction-missions/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/faction-missions/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/faction-missions/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
source_urls:
- path: doc/JSON/FACTION_MISSIONS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/FACTION_MISSIONS.md
- path: src/faction_mission.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/faction_mission.cpp
- path: src/faction_camp.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/faction_camp.cpp
- path: data/json/faction_missions.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/data/json/faction_missions.json
- path: tests/faction_camp_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/tests/faction_camp_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.faction-missions%29%3A+&body=Document+ID%3A+json.faction-missions%0ALanguage%3A+zh_CN%0AVerified+commit%3A+02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：faction missions

本页是 `json.faction-missions` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.faction-missions`
- Target: `reference/json/faction-missions.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/faction-missions/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.faction-missions | doc/JSON/FACTION_MISSIONS.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## Faction mission 数据边界

`faction_mission` generic factory 当前主要提供 basecamp mission 的名称、说明和展示元数据。
任务如何选择目标、派出 NPC、计算收获/风险和修改地图仍多由 `faction_camp.cpp` 等 C++ consumer
实现。新增 JSON object 不会自动创造一套可执行 mission。

### Loader fields

name 与 desc 必填。skill、difficulty、risk、activity、time、positions、items_label、
items_possibilities、effects 和 footer 可选。difficulty/risk 只接受 NONE、VERY_LOW、LOW、MEDIUM、
HIGH、VERY_HIGH；activity 字符串必须存在于 activity level map，否则会报告 invalid。

这些 time/effects/items 字段是翻译后的说明，不是结构化 duration、loot table 或 effect program。
它们必须准确描述对应 hardcoded consumer，但不能替代 consumer 的测试。

### 新增或修改流程

先找到读取 mission ID 的 camp code 和解锁条件，再更新 display object。核对最大 positions、实际
duration、skill training、food/gear transfer、failure/risk 和 repeat semantics。若想数据驱动新
行为，需要先设计公开 execution contract、loader 和测试；不能把自然语言 effects 当执行指令。

### 验证

运行 formatter、`make -j2 json-check`、Mod `--check-mods`。实际在 camp menu 检查零/一/多 NPC
显示、翻译、不可用原因、开始/返回和重复任务。新增 ID 或行为时扩展 faction camp focused tests，
并确保显示文字与真实实现一致。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b`；聚合源指纹为 `06cdbc4c15861847dfbef5486ae1b1c427c73774ff0cc485322ff8a7b5e2cd93`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/FACTION_MISSIONS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/FACTION_MISSIONS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/FACTION_MISSIONS.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
