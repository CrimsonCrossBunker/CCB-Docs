---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.npcs-dialogue
title: 旧文档迁移草稿：npcs and dialogue
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
- doc/JSON/NPCs.md
- src/npc.cpp
- src/npc_class.cpp
- src/npctalk.cpp
- data/json/npcs/missiondef.json
- tests/npc_talk_test.cpp
source_symbols:
- npc_template::load
- npc_class::load
- json_talk_topic::load
source_queries: []
source_fingerprint: 9e6515c57f4bec96e397fe7ce1624895b165ed1c1d32cceae8e1a50a6cadf6cc
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 1289a5265e763b710d9234f1b68f8c803d9279a01473b66d2dafd8572ba14d7b
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: Killa-bite, Standing-Storm, Maleclypse, LunaGlaze, 李诗琪, Anton Simakov,
  Tektolnes, RenechCDDA, thaelina; accepted inventory identities only. Source paths and Git history remain
  authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: eoc
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/eoc/npcs-and-dialogue/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/eoc/npcs-and-dialogue/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/eoc/npcs-and-dialogue/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/eoc/npcs-and-dialogue/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/JSON/NPCs.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/NPCs.md
- path: src/npc.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/npc.cpp
- path: src/npc_class.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/npc_class.cpp
- path: src/npctalk.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/npctalk.cpp
- path: data/json/npcs/missiondef.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/json/npcs/missiondef.json
- path: tests/npc_talk_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/npc_talk_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.npcs-dialogue%29%3A+&body=Document+ID%3A+json.npcs-dialogue%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：npcs and dialogue

本页是 `json.npcs-dialogue` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.npcs-dialogue`
- Target: `reference/eoc/npcs-and-dialogue.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/eoc/npcs-and-dialogue/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.npcs-dialogue | doc/JSON/NPCs.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 当前 CCB NPC 与对话结构

NPC 内容通常跨三个独立对象：`npc` 定义具体模板和初始关系，`npc_class` 定义生成属性与
装备分布，`talk_topic` 定义对话图。mission、faction、item group、skill、trait、effect
与 topic 均通过稳定 ID 连接；只让单个 JSON 文件可加载并不能证明整条对话可达。

### NPC 模板

```jsonc
{
  "type": "npc",
  "id": "ccb_example_npc",
  "name_unique": "Example Keeper",
  "gender": "female",
  "class": "NC_CCB_EXAMPLE",
  "faction": "your_followers",
  "attitude": 0,
  "mission": "GUARD",
  "chat": "TALK_CCB_EXAMPLE"
}
```

`npc_template::load` 读取模板并由 class、faction、mission 和 chat ID 组合行为。新模板应
确认出生位置/调用者会实际生成它，不要只在 Debug 菜单中手动 spawn 后认为流程完成。
随机 NPC 属性属于 `npc_class`；具名 NPC 的专有内容留在模板或对话中。

### talk topic 与 response

```jsonc
{
  "type": "talk_topic",
  "id": "TALK_CCB_EXAMPLE",
  "dynamic_line": "Welcome.",
  "responses": [
    { "text": "Goodbye.", "topic": "TALK_DONE" }
  ]
}
```

`json_talk_topic::load` 可读取 dynamic line、speaker effects、responses 和 repeat
responses。最终 response 列表为空会报错。已有同 ID topic 的 response 可能按加载顺序
追加，`replace_built_in_responses` 和 `insert_before_standard_exits` 会改变组合位置；Mod
patch 必须声明依赖并测试最终图。

response 的 condition 控制是否出现，success/failure effect 决定副作用和下一个 topic。
每条可见分支都应有退出或可到达的后续节点，避免无条件环、空页面与无法返回的任务对话。

### talker 与 EOC 语义

传统对话中 alpha 通常是玩家、beta 通常是 NPC，因此 condition/effect 使用 `u_` 与
`npc_` 前缀。相同 topic/EOC 被怪物、物品或其他系统调用时，talker 类型可能不同；应
查[条件索引](../eoc-conditions.md)、[效果索引](../eoc-effects.md)和实际调用点。

dynamic line、response text、NPC 名称和 mission dialogue 都是玩家文本，应使用 translation
对象或当前字段要求的可翻译字符串，保留 placeholder/context，并测试文本宽度与复数。

### mission 接线

NPC 提供任务时，模板的 `mission_offered`、mission_definition 的 origins/dialogue，及
通向 mission list/inquiry 的 topic 必须一致。自定义任务完成条件和 start/end/fail effect
仍使用同一 talker/EOC 系统；详见[任务](../json/missions.md)。

### 验证

运行 JSON loader、ID 检查、实际 Mod 集 `--check-mods` 和 `npc_talk_test` 相关用例。至少
走通首次见面、条件隐藏/显示、success、failure、repeat response、任务接受/完成和退出；
同时检查缺失 NPC、缺失 topic 与不同加载顺序。

## 历史与归属

清单中的已接受贡献者为：Killa-bite, Standing-Storm, Maleclypse, LunaGlaze, 李诗琪, Anton Simakov, Tektolnes, RenechCDDA, thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `d32b9cc880a85480840d82cfa05d256c78a16615`；聚合源指纹为 `9e6515c57f4bec96e397fe7ce1624895b165ed1c1d32cceae8e1a50a6cadf6cc`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/NPCs.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/NPCs.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/NPCs.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
