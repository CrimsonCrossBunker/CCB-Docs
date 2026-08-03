---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.magic-spells-enchantments
title: 旧文档迁移草稿：magic spells enchantments
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
- doc/JSON/MAGIC.md
- src/magic.cpp
- src/magic_enchantment.cpp
- src/magic_type.cpp
- data/json/enchantments.json
- tests/magic_spell_test.cpp
source_symbols:
- spell_type::load
- enchantment::load
- magic_type::load
- spell_migration::load
source_queries: []
source_fingerprint: 05865897c5c912a033dde17275cb850056b9b8ce3a46b2917abea7071cf484bf
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: a02fd8ec925348ff537b65439d3350068d758994bc36f5af17f0209a990847fc
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: LYHGLYTX, Standing-Storm, LunaGlaze, thaelina; accepted inventory identities
  only. Source paths and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/magic-spells-enchantments/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/magic-spells-enchantments/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/magic-spells-enchantments/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/magic-spells-enchantments/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/JSON/MAGIC.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/MAGIC.md
- path: src/magic.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/magic.cpp
- path: src/magic_enchantment.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/magic_enchantment.cpp
- path: src/magic_type.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/magic_type.cpp
- path: data/json/enchantments.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/json/enchantments.json
- path: tests/magic_spell_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/magic_spell_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.magic-spells-enchantments%29%3A+&body=Document+ID%3A+json.magic-spells-enchantments%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：magic spells enchantments

本页是 `json.magic-spells-enchantments` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.magic-spells-enchantments`
- Target: `reference/json/magic-spells-enchantments.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/magic-spells-enchantments/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.magic-spells-enchantments | doc/JSON/MAGIC.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 当前 CCB Magic、Spell 与 Enchantment 契约

这组契约包含 `SPELL`、`magic_type`、`enchantment` 和在其他对象中使用的 inline
`fake_spell`。它们共享部分 ID 和条件，但 lifecycle 不同：spell 被施放，magic type
提供系统默认规则，enchantment 按持有者/载体状态持续求值。

### Spell 最小骨架

```jsonc
{
  "type": "SPELL",
  "id": "spell_ccb_example",
  "name": "Example pulse",
  "description": "A documentation-only spell.",
  "effect": "attack",
  "shape": "blast",
  "valid_targets": [ "hostile" ],
  "min_damage": 1,
  "damage_increment": 1,
  "max_damage": 5,
  "min_range": 3,
  "max_range": 3,
  "energy_source": "MANA",
  "base_energy_cost": 10,
  "base_casting_time": 100
}
```

当前 `spell_type::load` 强制读取 `name`、`description`、`effect`、`shape` 与
`valid_targets`。Effect 和 shape 必须在 native registry 中存在。damage、range、AoE、
duration、pierce、accuracy、energy 和 casting time 通常使用 min/increment/max；表达式和
单位由对应 reader 决定，不能假定全是普通整数。

`caster_condition`、`target_condition`、target species/monster、body parts 和 flags 共同
限制合法目标。`extra_effects`/`fake_spell` 可以连锁施法，consistency check 会检查循环；
WONDER、permanent summon、vitamin energy、touch/no-hands 与 formula 参数也有专门约束。

### Magic type、学习与 channel

`magic_type` 可集中声明 energy、level/XP/failure formula、cannot-cast flags、failure cost
和 failure EOC。level 与 XP formula 必须成对且参数数目正确。Spell 可以覆盖 magic type，
并通过 book、profession/NPC、`learn_spells` 或其他当前入口学习。

Channeled spell 需要 max turns、channel spell 与 end spell；interrupt、每回合耗能和重复
effect 必须覆盖取消、移动、受击、资源耗尽和保存边界。多 projectile 与重复/随机
extra spell 需要性能和递归上限审阅。

### Enchantment

Enchantment 可以是具名 ID，也可以在调用者能提供稳定 inline ID 时内联。`has` 与
`condition` 决定 HELD/WIELD/WORN、ACTIVE/INACTIVE/ALWAYS 或 dialogue condition。
`values`、skills、custom、encumbrance、melee/incoming damage 支持 add/multiply；
mutations、effects、bodypart changes、special vision、emitter、hit effects 和 intermittent
spell 各有独立语义。

Character、monster 与 vehicle 只处理其实现认为 relevant 的子集。不要因为字段能加载就
假设对所有载体生效；用 `is_monster_relevant`/`is_vehicle_relevant` 和调用点查证。

### 验证

运行 formatter、`make -j2 json-check`、实际 Mod 集 `--check-mods`，以及
`magic_spell_test`、`magic_spell_effect_test`、`enchantments_test` 的相关 filter。
覆盖每个 level 边界、失败率/资源、target/shape、extra-effect cycle、channel 中断、
enchantment 开关与 add/multiply 顺序，并保存重载。玩家/NPC/monster/vehicle 和 inline
载体分别测试；高频 intermittent/area spell 需要 profile。

## 历史与归属

清单中的已接受贡献者为：LYHGLYTX, Standing-Storm, LunaGlaze, thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `d32b9cc880a85480840d82cfa05d256c78a16615`；聚合源指纹为 `05865897c5c912a033dde17275cb850056b9b8ce3a46b2917abea7071cf484bf`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/MAGIC.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/MAGIC.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/MAGIC.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
