---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.character
title: Character 子系统
language: zh_CN
status: stale
doc_type: reference
audiences:
- experienced-contributor
- maintainer
- api-user
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- src/character.h
- src/character.cpp
- src/savegame_json.cpp
- tests/character_modifier_test.cpp
source_symbols:
- 'class Character : public Creature, public visitable'
source_queries: []
source_fingerprint: 26cdc71d8491575caf3196c2b7b47e83000f229c404aebf0c82f4ffd742a013a
authority: source-and-tests
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 18981a2c728ee2086cc0f845397786036da299f213159c1a0587ff087c5379b4
prerequisites:
- architecture.overview
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
risk_group: cpp-character
risk_level: normal
pending_source_pr: null
stale_reason: 'Source paths changed after d32b9cc880a8: src/character.cpp'
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/character/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/character/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/character/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/character/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: src/character.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/character.h
- path: src/character.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/character.cpp
- path: src/savegame_json.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/savegame_json.cpp
- path: tests/character_modifier_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/character_modifier_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.character%29%3A+&body=Document+ID%3A+cpp.character%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Character

## 职责

`Character` 是人形行动者的共享原生模型：它在 `Creature` 之上组织属性、身体状态、
特质、技能、需求、装备、物品访问、制作知识和活动；`avatar` 与 NPC 实现提供具体的
存档边界。

## 入口点

先读 `src/character.h` 中的 `class Character`，再按修改内容进入对应的
`character_*.cpp`。`initialize`、每回合处理、物品遍历、效果处理、活动，以及纯虚的
`serialize` / `deserialize` 是主要集成点。

## 数据所有权

实例拥有角色专属的可变状态和持久 ID。它访问地图与载具，但不全局拥有它们；物品
所有权由穿戴、持用和 inventory 容器协调。特质、职业等静态定义由 ID 注册数据拥有。

## 依赖

`Character` 依赖 `Creature`、item/pocket 遍历、effect、activity、recipe、mutation、
地图坐标和存档 JSON。调用方不能绕开这些所有者各自的不变量。

## 生命周期

构造得到尚未完整初始化的行动者，`initialize` 填充默认值，游戏循环更新派生状态与
活动，具体子类负责保存和读取。行动者转换或接管 NPC 时必须保持身份与所有权一致。

## 不变量

Character ID 一经分配就应稳定；基础属性、身体部位与派生缓存必须一致；物品变化应
失效对应缓存；依赖位置的操作必须使用正确坐标系和当前 `map`。

## 扩展点

把行为放到对应的 `character_*.cpp`，新数据复用 ID 注册表；只有在 avatar 与 NPC
语义都明确时才新增虚函数。纯内容扩展优先使用 JSON、EOC 或受支持的 Lua 接口。

## 序列化

`Character` 声明契约，具体子类执行序列化。持久字段变更必须追踪
`src/savegame_json.cpp`、旧值/默认值处理和存档兼容；临时缓存应明确保持不序列化。

## 测试

运行聚焦的 character、crafting、effect、inventory、mutation 与 save/world 测试。
派生值变更既要验证失效前后，也不能只验证构造结果。

## 性能

每回合处理属于热路径。避免重复遍历完整 inventory、重复注册表查询和宽泛缓存重建；
保持现有失效边界，并用大型物品集合测量。

## CCB 差异

本页不宣称 CCB 的 `Character` 与任一上游版本完全等价。CCB 仍保留 `kill_xp` 等旧
EOC/Mod 可见状态；移植时必须逐项核对当前存档、活动和 Lua 边界。

## 技术债务

头文件明确记录了 player 逻辑逐步上移到 `Character` 的历史，因此仍有大量 getter、
setter 和宽依赖。新修改应局部降低耦合，不要把大范围清理和行为变化混在一起。
