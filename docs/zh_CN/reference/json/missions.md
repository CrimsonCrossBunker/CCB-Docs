---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.missions
title: 旧文档迁移草稿：missions
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
- doc/JSON/MISSIONS_JSON.md
- src/missiondef.cpp
- src/mission.cpp
- src/npctalk.cpp
- data/json/npcs/missiondef.json
- tests/mission_test.cpp
source_symbols:
- mission_type::load
- json_talk_topic::load
source_queries: []
source_fingerprint: 90916cbbaf2e611bfa285016f1f427a59e2ca50fa3b823d47a027a8d50cdf550
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 58c3fce4fdc81002571830451c34bfcbe12593713715ddb57b7714986e8e252e
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: Maleclypse, thaelina; accepted inventory identities only. Source paths
  and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/missions/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/missions/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/missions/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/missions/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/JSON/MISSIONS_JSON.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/MISSIONS_JSON.md
- path: src/missiondef.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/missiondef.cpp
- path: src/mission.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/mission.cpp
- path: src/npctalk.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/npctalk.cpp
- path: data/json/npcs/missiondef.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/npcs/missiondef.json
- path: tests/mission_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/tests/mission_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.missions%29%3A+&body=Document+ID%3A+json.missions%0ALanguage%3A+zh_CN%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：missions

本页是 `json.missions` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.missions`
- Target: `reference/json/missions.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/missions/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.missions | doc/JSON/MISSIONS_JSON.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 当前 CCB mission_definition 模型

`mission_definition` 是可分配任务的模板。运行时 mission 实例引用其稳定 ID，并保存状态、
目标、deadline、giver 等数据；重命名已发布 ID 会影响存档、NPC 对话和 follow-up 链。
任务目标、对话和 start/end/fail 行为跨 mission loader、talker/EOC 与地图系统，必须端到端
验证。

### 基础定义

```jsonc
{
  "type": "mission_definition",
  "id": "MISSION_CCB_EXAMPLE",
  "name": { "str": "Find an example part" },
  "description": "Bring an example part back to the mission giver.",
  "goal": "MGOAL_FIND_ITEM",
  "item": "ccb_example_part",
  "count": 1,
  "difficulty": 1,
  "value": 1000,
  "origins": [ "ORIGIN_ANY_NPC" ],
  "dialogue": {
    "describe": "I need a part.",
    "offer": "Could you find an example part?",
    "accepted": "Thank you.",
    "rejected": "Maybe later.",
    "advice": "Look nearby.",
    "inquire": "Did you find it?",
    "success": "Exactly what I needed.",
    "success_lie": "You do not have it.",
    "failure": "We will have to manage without it."
  }
}
```

当前 `mission_type::load` 要求 `name`、`difficulty`、`value` 和 `goal`。当 origins 包含
`ORIGIN_ANY_NPC`、`ORIGIN_OPENER_NPC` 或 `ORIGIN_SECONDARY` 时，上述九个 dialogue 字段
都必填。其他 origin 也必须有真实分配入口，不能仅靠定义存在。

### goal 与目标字段

不同 `MGOAL_*` 使用 item、item_group、count、monster type/species、destination 或
`goal_condition`。选择 goal 后从当前 enum/loader 和同类第一方任务确认配套字段；无关字段
不会自动变成完成条件。`MGOAL_CONDITION` 使用对话 condition，并依赖任务检查时提供的
talker/context。

`deadline`、urgent、required/remove/empty container、generic rewards 和 invisible-on-complete
会改变 UI 与结算。followup 引用另一个 mission ID，应检查循环、不可达任务和 giver 对话。

### start、end、fail

三个 phase 可引用当前注册的硬编码 mission function，也可写对象，由 `parse_funcs` 读取
effect、mission target、mapgen update 等行为：

```jsonc
"start": {
  "effect": { "u_message": "Mission started." },
  "assign_mission_target": {
    "om_terrain": "field",
    "random": true,
    "reveal_radius": 1
  }
}
```

alpha/beta 通常与玩家/任务给予者相关，但 phase 和调用来源会影响实际 talker。地图目标
搜索、special 放置、z-level 与 reveal 可能失败；必须覆盖“找不到目标”的路径，不能假定
世界生成总能满足限制。

### NPC 对话接线

NPC 模板/对话必须提供任务列表、接受、查询和完成路径。`mission_offered`、origins、followup
及 `TALK_MISSION_*` 节点要形成可达图；详见[NPC 与对话](../eoc/npcs-and-dialogue.md)。

### 验证

运行 formatter、`make -j2 json-check`、实际 Mod 集 `--check-mods` 和 `mission_test`/
`npc_talk_test` 相关用例。端到端走通分配、拒绝、接受、目标生成、完成、失败、deadline、
保存/载入与 followup；同时测试缺失 item/terrain/topic、目标不可放置和旧存档 ID。

## 历史与归属

清单中的已接受贡献者为：Maleclypse, thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `90916cbbaf2e611bfa285016f1f427a59e2ca50fa3b823d47a027a8d50cdf550`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/MISSIONS_JSON.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/MISSIONS_JSON.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/MISSIONS_JSON.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
