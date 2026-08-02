---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.monster-special-attacks
title: 旧文档迁移草稿：monster special attacks
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
- doc/JSON/MONSTER_SPECIAL_ATTACKS.md
- src/monstergenerator.cpp
- src/monstergenerator.h
- data/json/monster_special_attacks/monster_attacks.json
- tests/monster_attack_test.cpp
source_symbols:
- MonsterGenerator::load_monster_attack
- mattack_actor::load
source_queries: []
source_fingerprint: b4670a309a41ffe2bd452359a1f19f61ab7653d62acbb8582b4a245c78736492
authority: docs-explanation
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 37ea54fc1bc8b70dbdf6102f2ba706cfa53de70b2836f8f1fcc5d9bfc6a82beb
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
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/monster-special-attacks/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/monster-special-attacks/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/monster-special-attacks/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/monster-special-attacks/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: doc/JSON/MONSTER_SPECIAL_ATTACKS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/JSON/MONSTER_SPECIAL_ATTACKS.md
- path: src/monstergenerator.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/monstergenerator.cpp
- path: src/monstergenerator.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/monstergenerator.h
- path: data/json/monster_special_attacks/monster_attacks.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/json/monster_special_attacks/monster_attacks.json
- path: tests/monster_attack_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tests/monster_attack_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.monster-special-attacks%29%3A+&body=Document+ID%3A+json.monster-special-attacks%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：monster special attacks

本页是 `json.monster-special-attacks` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.monster-special-attacks`
- Target: `reference/json/monster-special-attacks.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/monster-special-attacks/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.monster-special-attacks | doc/JSON/MONSTER_SPECIAL_ATTACKS.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## Monster special attack 契约

`special_attacks` 是 `MONSTER` 的有序能力集合。条目可用旧式
`[ native_name, cooldown ]` 引用注册的 C++ attack，也可使用带 `type`/`id` 的 actor object。
Actor type、字段与运行时行为以 `MonsterGenerator::init_attack`、`mattack_actors.cpp` 和测试为准。

### 身份、cooldown 与条件

同一 monster 上重复 actor subtype 必须提供不同 `id`，否则 loader 会报告重复并只保留最后
定义。Cooldown reader 可以是固定值或当前支持的表达式；条件失败、没有目标或资源不足时，
是否消耗 cooldown 取决于 actor call path，必须按实现测试。

Leap、melee/bite、gun、spell、grab、summon 等 actor 的必填字段不同。例如 leap 强制
`max_range`，gun 读取 `gun_type`、range/mode、targeting 和 ammo 数据。不要把一个 actor 的
字段表套给另一个。`condition` 的 alpha 通常是 monster，beta 是否存在由 actor 构造 dialogue
的方式决定。

### 继承和副作用

Monster `copy-from` 的 special attack reader 支持替换/删除，但同名项和 `id` 决定结果。
Self/target effect、field、spawn、sound、message、ammo、item 和 spell ID 都要存在。
攻击可能改变地图、跨 z-level、抓取 bodypart 或建立 targeting state；失败路径必须清理状态。

### 验证

运行 formatter、`make -j2 json-check`、实际 Mod `--check-mods`，以及
`monster_attack_test`/`mondefense_test` 和相关 actor tests。覆盖无目标、不可见目标、最小/
最大距离、障碍、cooldown、ammo 空、condition false、NPC/player/monster target、保存重载和
重复 actor ID。高频 path search、AoE、spawn 与 field actor 需要 profile。

## 历史与归属

清单中的已接受贡献者为：Maleclypse, thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `b4670a309a41ffe2bd452359a1f19f61ab7653d62acbb8582b4a245c78736492`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/MONSTER_SPECIAL_ATTACKS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/MONSTER_SPECIAL_ATTACKS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/MONSTER_SPECIAL_ATTACKS.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
