---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.effects
title: 旧文档迁移草稿：effects
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
- doc/JSON/EFFECTS_JSON.md
- src/effect.cpp
- src/effect.h
- data/json/effects.json
- tests/effect_test.cpp
- tests/creature_effect_test.cpp
source_symbols:
- load_effect_type
- effect_type::load_mod_data
- effect_migration::load
source_queries: []
source_fingerprint: 8ec137d6fe7ecf424e3b8578ae092348222e0e81343604637980c88dca9d208c
authority: docs-explanation
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 65911ff8b34e34ed2a9fb30b4415f300d00738c358f26a3b1348b381759d99e9
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/effects/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/effects/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/effects/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/effects/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: doc/JSON/EFFECTS_JSON.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/JSON/EFFECTS_JSON.md
- path: src/effect.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/effect.cpp
- path: src/effect.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/effect.h
- path: data/json/effects.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/json/effects.json
- path: tests/effect_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tests/effect_test.cpp
- path: tests/creature_effect_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tests/creature_effect_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.effects%29%3A+&body=Document+ID%3A+json.effects%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：effects

本页是 `json.effects` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.effects`
- Target: `reference/json/effects.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/effects/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.effects | doc/JSON/EFFECTS_JSON.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 当前 CCB effect_type 数据

`effect_type` 定义附着在角色/生物上的持续状态，例如名称、描述、强度、持续时间、免疫、
数值修饰和周期行为。它与 Effect on Condition 的“effect command”不是同一对象：EOC 可以
添加/移除某个 effect_type，但 `effect_type` 本身不是可执行脚本。

### 基础定义

```jsonc
{
  "type": "effect_type",
  "id": "ccb_example_status",
  "name": [ "Example status" ],
  "desc": [ "You are affected by the documentation example." ],
  "max_intensity": 3,
  "max_duration": "1 hour",
  "show_in_info": true
}
```

`load_effect_type` 要求稳定 `id`，并读取多强度 name/desc、显示字段、resist/immune/block/
remove 关系、duration/intensity 演化、消息、flags、enchantment 和 modifier data。数组索引
与 intensity 的对应、缺省回退和 hardcoded 行为要以 `effect.cpp` 与测试为准。

### 实例生命周期

运行时 `effect` 实例保存 effect type、duration、body part、permanent、intensity、开始时间
与来源，并进入存档。因此删除或重命名已发布 effect ID 是存档兼容变化；需要使用
`effect_migration`：

```jsonc
{
  "type": "effect_migration",
  "from": "old_effect_id",
  "to": "ccb_example_status"
}
```

省略 `to` 是否代表移除、以及迁移触发时机，应由当前 loader/反序列化测试确认。目标 ID
不存在会在一致性检查中报告。

### 强度、持续时间与 modifier

`max_intensity`、`int_add_val`、decay 字段与 `int_dur_factor` 共同决定叠加和衰减。`base_mods`
和 `scaling_mods` 下的 STR/DEX/PER/INT、速度、疼痛、伤害、睡眠等条目由
`effect_type::load_mod_data` 的固定映射解释，并不是自由命名属性。错误的 chance/tick/min/
max 组合可能制造每回合高成本或极端数值。

身体部位限制、resist trait/effect、immune flag、blocks/removes 关系会改变能否施加和共存。
循环关系和强度边界需要 focused test，不应只看状态栏文本。

### 验证

1. 从 `load_effect_type` 和相邻第一方 effect 确认字段形状与强度数组。
2. 运行 formatter、`make -j2 json-check` 和实际 Mod 集 `--check-mods`。
3. 运行 `effect_test`/`creature_effect_test` 相关用例，覆盖施加、叠加、衰减、免疫与移除。
4. 对已发布 ID 测试旧存档/`effect_migration`，不要静默改名。
5. 对周期 modifier 测试强度 1、上限、超时和不同 body part。

若目标是执行条件逻辑，请使用[EOC](../eoc/index.md)；不要把脚本副作用塞进状态数据。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `8ec137d6fe7ecf424e3b8578ae092348222e0e81343604637980c88dca9d208c`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/EFFECTS_JSON.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/EFFECTS_JSON.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/EFFECTS_JSON.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
