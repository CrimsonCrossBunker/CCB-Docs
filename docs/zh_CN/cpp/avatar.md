---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.avatar
title: Avatar 子系统
language: zh_CN
status: draft
doc_type: reference
audiences:
- experienced-contributor
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- src/avatar.h
- src/avatar.cpp
- src/savegame_json.cpp
- tests/new_character_test.cpp
source_symbols:
- 'class avatar : public Character'
source_queries: []
source_fingerprint: baff9146ea4183f1cf2e0de2ace20b9a1fbd1c5d6f5ea61d8fb9247021285d12
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: bb72d2a0ebdb8ba5fbd91491ebc59b2d83acd5be495cbf92ce2e24cf4e10897a
prerequisites:
- cpp.character
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: cpp-avatar
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/avatar/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/avatar/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/avatar/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/avatar/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/dbaedf8357408ae6f96309732d6e087e9b878e18
source_urls:
- path: src/avatar.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/avatar.h
- path: src/avatar.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/avatar.cpp
- path: src/savegame_json.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/savegame_json.cpp
- path: tests/new_character_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/tests/new_character_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.avatar%29%3A+&body=Document+ID%3A+cpp.avatar%0ALanguage%3A+zh_CN%0AVerified+commit%3A+dbaedf8357408ae6f96309732d6e087e9b878e18%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Avatar

## 职责

`avatar` 是玩家控制的具体 `Character`，增加角色创建、模板、玩家身份、地图记忆、
控制权转移、面向 UI 的状态，以及世界存档中的顶层玩家序列化。

## 入口点

先读 `src/avatar.h` 与 `src/avatar.cpp`；创建和玩家命令继续进入
`newcharacter.cpp`、`avatar_action.cpp`。`avatar::serialize`、`avatar::deserialize`、
`save_map_memory` 和 `control_npc` 是高风险边界。

## 数据所有权

avatar 拥有玩家专属状态和稳定 save ID，并通过 memory 对象拥有地图记忆；当前 map、
world、creature 与 UI 服务仍由各自系统管理，avatar 只引用它们。

## 依赖

它依赖 `Character`、world/save 服务、map memory、input/UI 状态、mission、faction 和
角色创建注册表。玩家动作应通过常规 map 与 activity 接口，不能直接改远端状态。

## 生命周期

avatar 被创建或读取，按 character type 初始化，接入世界，然后作为受控行动者更新。
`control_npc` 会有意转移控制权，同时把原行动者保留为 NPC。

## 不变量

同一上下文只有一个受控 avatar；save ID 必须稳定；地图记忆使用绝对坐标；转移控制
不能复制 character ID 或物品所有权。

## 扩展点

玩家专属命令放在 `avatar_action.cpp`，创建政策放在创建流程；只有不能用局部 adaptor
表达时才保存 UI 状态。共享行动者行为属于 `Character`，不应塞入 `avatar`。

## 序列化

`src/savegame_json.cpp` 实现具体玩家记录。明确不序列化的 UI 状态（例如区域整理视口
锁）必须能在读取后重建。

## 测试

使用 new-character 测试，再运行被修改共享子系统的聚焦测试。存档字段需要覆盖旧值/
缺失值读取和往返，不能只比一份 JSON 快照。

## 性能

不要在玩家每回合或 redraw 路径执行全世界查询或反复扫描 map memory。任何缓存都需
要明确的失效事件。

## CCB 差异

CCB 的玩家 UI 与 Lua 集成可能与上游缺失或不同。移植 avatar 修改时应比较行为和
存档字段，不能仅凭同名类判断等价。

## 技术债务

玩家专属状态仍分散于创建、game、UI 和 save 单元。应以小而可测的步骤改成显式服务，
不要继续扩大全局 avatar 访问。
