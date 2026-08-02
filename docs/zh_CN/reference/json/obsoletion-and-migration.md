---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.obsoletion-and-migration
title: 旧文档迁移草稿：obsoletion and migration
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
- doc/JSON/OBSOLETION_AND_MIGRATION.md
- src/item_factory.cpp
- src/effect.cpp
- src/savegame_json.cpp
- data/json/obsoletion_and_migration_0.J/migration_items.json
- data/json/obsoletion_and_migration_0.J/eocs.json
- src/init.cpp
- src/magic.cpp
- src/proficiency.cpp
source_symbols:
- effect_migration::load
- ter_furn_migrations::load
- spell_migration::load
- proficiency_migration::load
source_queries: []
source_fingerprint: 4061a49a916458a30b17a18ae14969ab456a694b47ee87fef9ac0d7a08a6d979
authority: docs-explanation
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 43ff7712534c3fc4fd748e2083641e9f9cd8731984a185aa212bf918c945389d
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/obsoletion-and-migration/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/obsoletion-and-migration/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/obsoletion-and-migration/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/obsoletion-and-migration/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: doc/JSON/OBSOLETION_AND_MIGRATION.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/JSON/OBSOLETION_AND_MIGRATION.md
- path: src/item_factory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/item_factory.cpp
- path: src/effect.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/effect.cpp
- path: src/savegame_json.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/savegame_json.cpp
- path: data/json/obsoletion_and_migration_0.J/migration_items.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/json/obsoletion_and_migration_0.J/migration_items.json
- path: data/json/obsoletion_and_migration_0.J/eocs.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/json/obsoletion_and_migration_0.J/eocs.json
- path: src/init.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/init.cpp
- path: src/magic.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/magic.cpp
- path: src/proficiency.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/proficiency.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.obsoletion-and-migration%29%3A+&body=Document+ID%3A+json.obsoletion-and-migration%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：obsoletion and migration

本页是 `json.obsoletion-and-migration` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.obsoletion-and-migration`
- Target: `reference/json/obsoletion-and-migration.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/obsoletion-and-migration/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.obsoletion-and-migration | doc/JSON/OBSOLETION_AND_MIGRATION.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## Obsoletion 与 migration 选择

不存在覆盖所有 JSON type 的通用 migration。先确定旧 ID 属于 item、trait、terrain/
furniture、overmap terrain、vehicle part、effect、spell、Mod 等哪一个 registry，再使用该
loader 已注册的 migration object。没有对应 loader 时必须保留旧 ID、兼容 shim 或实现并测试
非行为性迁移支持，不能伪造 Schema。

### Item `MIGRATION`

当前 item migration 接受一个或多个旧 `id`，可设置 `replace`、`variant`、`from_variant`、
flags、charges、contents、sealed 与 `reset_item_vars`。`replace` 不得等于旧 ID。
Variant migration 只匹配对应旧 variant；contents 放不进正常 container 时进入专用 migration
pocket，避免静默丢失。

```jsonc
{
  "type": "MIGRATION",
  "id": "old_item_id",
  "replace": "new_item_id"
}
```

替换类型必须真实存在且在 load/finalize 时可用。数量、charges、pockets、item vars、damage、
ownership 和 sealed state 都可能需要额外 fixture，不是改一个 ID 就完成。

### 其他 registry 与 Mod

CCB 当前注册了 trait、bionic、proficiency、terrain/furniture、field、vehicle part、trap、
effect、overmap terrain/special、camp、spell、global variable 与 Mod migrations 等。字段名和
能力各不相同。`mod_migration` 使用旧 `id` 加 `new_id`，或在移除时提供可翻译
`removal_reason`；目标 Mod 必须有效。

`obsolete: true` 通常控制新内容选择，不自动重写存档中的所有引用。保留期、replacement、
release note 和 removed-ID 测试仍是必要的。

### 验证

为每个真实旧 fixture 加载当前代码，检查 migration 后对象、嵌套 contents、地图/角色/world
state，再保存并第二次加载，确认 migration 幂等且不重复生成资源。运行 formatter、
`make -j2 json-check`、`--check-mods` 和 owning subsystem tests。还要验证缺失 target、
migration chain/cycle、同时启用旧 Mod 与新 Mod、以及移除 migration 后的 release boundary。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `4061a49a916458a30b17a18ae14969ab456a694b47ee87fef9ac0d7a08a6d979`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/OBSOLETION_AND_MIGRATION.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/OBSOLETION_AND_MIGRATION.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/OBSOLETION_AND_MIGRATION.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
