---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.npc-factions
title: 旧文档迁移草稿：npc factions
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
last_human_reviewer: Pending human review
source_paths:
- doc/JSON/FACTIONS.md
- src/faction.cpp
- src/faction.h
- data/json/npcs/factions.json
- tests/faction_price_rules_test.cpp
source_symbols:
- faction_template::load
source_queries: []
source_fingerprint: 4286ef41984cda33091800af8d905c278d43fb2e7037271da4169486e94cfc75
authority: docs-explanation
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: a7316547f229ed816e820ee74dfe65f69f16f26324ca92ab8e906af89051461c
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
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/npc-factions/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/npc-factions/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/npc-factions/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/npc-factions/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: doc/JSON/FACTIONS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/JSON/FACTIONS.md
- path: src/faction.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/faction.cpp
- path: src/faction.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/faction.h
- path: data/json/npcs/factions.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/json/npcs/factions.json
- path: tests/faction_price_rules_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tests/faction_price_rules_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.npc-factions%29%3A+&body=Document+ID%3A+json.npc-factions%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：npc factions

本页是 `json.npc-factions` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.npc-factions`
- Target: `reference/json/npc-factions.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/npc-factions/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.npc-factions | doc/JSON/FACTIONS.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## NPC faction 契约

`FACTION` template 由 `faction_template` 加载，随后实例化为世界 faction。当前 constructor
强制读取 `id`、`name`、`description`、`likes_u`、`respects_u`、`known_by_u`、`size`、
`power`、`wealth`；trust、food、currency、price rules、claims、monster faction、relations
与 epilogues 是附加契约。

### 身份、关系与经济

Faction ID 会进入 NPC、dialogue、mission、camp、EOC 与存档，显示名可翻译但 ID 不可随意
改名。`relations` 是按目标 faction ID 的方向性 bitset；A 对 B 的 kill/watch/share 等关系
不自动保证 B 对 A 对称。每个目标和 relation flag 必须用当前注册表验证。

`currency` 会加入 price rule。Rule 可匹配 item group/flag 等当前 item-group 条件，并设置
markup、premium、fixed adjustment 或 price。交易结果还受 NPC、供应、技能与其他系统影响，
不能只用一件商品验证。

### 世界状态和兼容

Template 是新 faction 的初始值；world save 可以拥有已变化的 likes/respect/trust、wealth、
food 与成员状态。修改 template 不等于迁移已有世界。删除/改名 ID 前必须设计存档和所有
跨对象引用迁移。

Epilogue snippet、monster faction、currency/item group 和 mission ID 需通过 consistency
check。`known_by_u`、limited area claim 与 lone-wolf 影响 UI/world behavior，应有具体场景测试。

### 验证

运行 formatter、`make -j2 json-check`、`--check-mods`，并运行 faction price/mission/camp/
NPC dialogue tests。覆盖双向关系、偷窃/攻击、交易规则、food/wealth、epilogue、新世界与旧
存档、Mod 组合和缺失目标 ID。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `4286ef41984cda33091800af8d905c278d43fb2e7037271da4169486e94cfc75`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/FACTIONS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/FACTIONS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/FACTIONS.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
