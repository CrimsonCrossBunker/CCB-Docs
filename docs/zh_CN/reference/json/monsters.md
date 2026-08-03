---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.monsters
title: 旧文档迁移草稿：monsters
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
- doc/JSON/MONSTERS.md
- src/monstergenerator.cpp
- src/monstergenerator.h
- data/json/monsters/zed-classic.json
- tests/monster_test.cpp
source_symbols:
- MonsterGenerator::load_monster
- mtype::load
- species_type::load
- mon_flag::load
source_queries: []
source_fingerprint: 9d69264687ff03d74f53d9ef417e4d15e8e797b45e100aa8c52209022a738d43
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: f9304afa2dbefb3c066e174917caca8ae8761bdc8c0b4c13e65b0123a2d5d88b
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/monsters/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/monsters/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/monsters/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/monsters/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/JSON/MONSTERS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/MONSTERS.md
- path: src/monstergenerator.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/monstergenerator.cpp
- path: src/monstergenerator.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/monstergenerator.h
- path: data/json/monsters/zed-classic.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/json/monsters/zed-classic.json
- path: tests/monster_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/monster_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.monsters%29%3A+&body=Document+ID%3A+json.monsters%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：monsters

本页是 `json.monsters` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.monsters`
- Target: `reference/json/monsters.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/monsters/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.monsters | doc/JSON/MONSTERS.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 当前 CCB Monster 契约

`MONSTER` 由 `MonsterGenerator::load_monster` 交给 generic factory，再由 `mtype::load`
解释字段、继承和范围。旧字段表只能作为历史线索；当前 loader、first-party JSON 和
`tests/monster_test.cpp` 才是契约。

### 最小定义与身份

```jsonc
{
  "type": "MONSTER",
  "id": "mon_ccb_example",
  "name": { "str": "example creature" },
  "description": "A creature used by documentation.",
  "default_faction": "wildlife",
  "symbol": "e",
  "color": "light_green",
  "material": [ "flesh" ],
  "species": [ "MAMMAL" ],
  "volume": "62500 ml",
  "weight": "80 kg",
  "hp": 40,
  "speed": 90
}
```

`id` 是 spawn group、mapgen、任务、EOC 和存档引用的稳定标识。`name`、
`default_faction` 与 `symbol` 由当前 loader 强制读取；数值边界、单位和默认值应直接查
`mtype::load`，不要把示例值当成推荐平衡值。

定义 monster 并不会让它出现。自然生成通常还需要 monster group、mapgen/static spawn、
事件或 EOC。`species`、faction、material、harvest、death drops 和 item group 都必须指向
真实注册 ID。

### 行为组合

- `flags`、anger/fear/placate trigger、vision、path settings 和 move skills 控制通用 AI。
- `special_attacks` 可以引用已注册 native attack，也可使用当前 actor 对象；同 subtype
  多次出现需要不同 `id`，否则 loader 会报告覆盖。
- `weakpoint_sets` 先合并具名集合，inline `weakpoints` 最后覆盖同名项；删除也有专门语义。
- `armor`、`melee_damage`、`attack_effs`、`emit_fields` 和 death function 使用各自子契约。
- upgrades、reproduction、revive/zombify/fungalize 与 corpse/egg/baby ID 会影响长生命周期。

`copy-from` 只继承 factory 支持的内容。`extend`、`delete`、`relative` 与 `proportional`
并非对每个字段等价；特别是 armor、weakpoints 和 special attacks 有专门 reader。

### 验证

运行 formatter、`make -j2 json-check` 和真实 Mod 集的 `--check-mods`。再运行
`monster_test` 的相关 filter，并在多 seed 世界检查 spawn、faction、路径、攻击 cooldown、
掉落、死亡、升级/繁殖和保存重载。性能审阅应覆盖高频 special attack、pathfinding、
field emission 和大量群体生成。

字段存在不代表组合可玩；HP、speed、armor、damage、spawn weight 和 loot 必须作为一个
整体做平衡与回归测试。

## 历史与归属

清单中的已接受贡献者为：Maleclypse, thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `d32b9cc880a85480840d82cfa05d256c78a16615`；聚合源指纹为 `9d69264687ff03d74f53d9ef417e4d15e8e797b45e100aa8c52209022a738d43`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/MONSTERS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/MONSTERS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/MONSTERS.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
