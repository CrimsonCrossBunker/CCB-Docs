---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.proficiencies
title: 旧文档迁移草稿：proficiencies
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
- doc/JSON/PROFICIENCY.md
- src/proficiency.cpp
- src/proficiency.h
- data/json/proficiencies/misc.json
- tests/crafting_test.cpp
source_symbols:
- proficiency::load
- proficiency_category::load
- proficiency_migration::load
source_queries: []
source_fingerprint: f5656b361798c328b6a002d40cc8abf6e325f847c7da9380c240b26c721e0f8f
authority: docs-explanation
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: e63972f9bf023b243740b8b83aad9b26355e9f12d6d5803406e042a7beedfa9c
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/proficiencies/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/proficiencies/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/proficiencies/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/proficiencies/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: doc/JSON/PROFICIENCY.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/JSON/PROFICIENCY.md
- path: src/proficiency.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/proficiency.cpp
- path: src/proficiency.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/proficiency.h
- path: data/json/proficiencies/misc.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/json/proficiencies/misc.json
- path: tests/crafting_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tests/crafting_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.proficiencies%29%3A+&body=Document+ID%3A+json.proficiencies%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：proficiencies

本页是 `json.proficiencies` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.proficiencies`
- Target: `reference/json/proficiencies.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/proficiencies/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.proficiencies | doc/JSON/PROFICIENCY.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## Proficiency、category 与 migration

Proficiency 是独立于 skill 的知识图。recipe/activity 决定何时学习或使用它；JSON definition
提供 identity、前置、默认 penalty、学习属性和 consumer-specific bonuses。依赖可以形成任意有向
图，不要假设只是一棵树。

### 三种 object

`proficiency` 必须有 name、description、can_learn、category。可选字段包括 teachable（默认 true）、
time_to_learn、required_proficiencies、ignore_focus、default time/skill/weakpoint modifiers 和
bonuses。旧 `default_fail_multiplier` 仍被转换但会报告，新的数据使用
`default_skill_penalty`。

`proficiency_category` 要求 name/description，ID 由 factory 提供。`proficiency_migration` 要求
from，可选 to；缺少 to 表示移除旧 proficiency，给出 to 则必须引用有效 ID。删除/重命名公开 ID
时 migration 是存档兼容的一部分。

### Bonuses 与 consumers

bonus entry 要求 type/value，但 bonus key 的含义由具体 activity/attack consumer 定义；JSON 中
可解析不表示有代码使用。新增 key/type 必须同时实现 consumer、文档和测试。recipe 可覆盖默认
time/skill/learning/max-experience，最终效果要查 recipe 展开结果。

### 验证

检查 category、所有 prerequisites、循环/不可达节点、learnable/teachable 组合、migration 和引用
它的 recipes/books/activities。运行 formatter、`make -j2 json-check`、Mod `--check-mods`，再用
focused crafting/learning/save migration tests 覆盖无 proficiency、部分学习、已掌握和旧 ID。
生成 proficiency index 用于发现，不替代 loader 与 consumer 审核。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `f5656b361798c328b6a002d40cc8abf6e325f847c7da9380c240b26c721e0f8f`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/PROFICIENCY.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/PROFICIENCY.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/PROFICIENCY.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
