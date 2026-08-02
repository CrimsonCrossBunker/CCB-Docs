---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.monsters
title: Monster 子系统
language: zh_CN
status: draft
doc_type: reference
audiences:
- experienced-contributor
- maintainer
- mod-author
- api-user
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- src/monster.h
- src/monster.cpp
- src/monstergenerator.cpp
- tests/monster_test.cpp
source_symbols:
- 'class monster : public Creature'
source_queries: []
source_fingerprint: d32869f17e7e85b671a83a09a3b196638df5130c32eba07b8ced8fccce8118b1
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 2b25c242a79a9761e70ba5092154a44fbbb3694bf164138f53376c512c37ca5b
prerequisites:
- cpp.creatures
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
risk_group: cpp-monsters
risk_level: normal
pending_source_pr: null
stale_reason: null
search:
  exclude: true
---

# Monster

## 职责

`monster` 是非 Character 的具体 creature，把 `mtype` 定义与运行时生命、移动计划、
faction/态度、特殊攻击、物品状态、目的地和死亡行为组合起来。

## 入口点

从 `src/monster.h`、`src/monster.cpp` 开始。静态 monster 定义和攻击进入
`monstergenerator`，AI helper 与特殊攻击位于各自文件，活跃实例由
`creature_tracker` 索引。

## 数据所有权

实例拥有可变 monster 状态并引用不可变 `mtype` 数据。tracker 只索引它，map 拥有
地形；overmap group 可能拥有延迟 population 记录，而不是当前加载实例。

## 依赖

monster 依赖 `Creature`、monster type 注册表、faction、path、map field、effect、
特殊攻击 actor、item、overmap population 与存档 JSON。

## 生命周期

monster 被生成或读取，放入 tracker，每回合规划和行动，可能在 reality bubble 与
overmap 表示之间移动，最后死亡或卸载回世界所有状态。

## 不变量

`mtype_id` 可解析；计划使用正确坐标系；tracker 位置同步；特殊攻击已注册；加载/
卸载不能复制实例或其 inventory。

## 扩展点

优先使用 monster JSON 和已注册 attack actor。原生 AI 放在聚焦 helper 中并添加确定
性测试；仅当数据无法表达时才新增虚函数或硬编码类型判断。

## 序列化

`monster::serialize` / `deserialize` 位于 `savegame_json.cpp`；overmap 序列化覆盖延迟
group 和存放的 monster。新字段要同时为加载与卸载形态提供安全默认值。

## 测试

使用 monster behavior、attack、vision、stairs、deterministic AI、overmap 与存档相关
测试。计划/攻击回归必须固定 RNG seed。

## 性能

寻路、目标选择、可见性和特殊攻击评估随活跃数量增长。缓存要确定且有范围，避免每个
monster 都扫描全部 creature。

## CCB 差异

monster 数据、AI 和 overmap 处理是常见上游移植热点。必须用 CCB 自身 JSON 与测试
验证；同名 ID 不能证明语义相同。

## 技术债务

运行时 AI、类型数据与持久化仍跨文件耦合。新修改应建立可测量的政策边界，不要继续
增加临时状态 flag。
