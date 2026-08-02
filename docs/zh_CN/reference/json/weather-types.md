---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.weather-types
title: 旧文档迁移草稿：weather types
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
- doc/JSON/WEATHER_TYPE.md
- src/weather_type.cpp
- src/weather_type.h
- src/weather_gen.cpp
- data/json/weather_type.json
- tests/weather_test.cpp
source_symbols:
- weather_type::load
- weather_types::load
- weather_generator::load
source_queries: []
source_fingerprint: 99ab7d48f3e59f2838601af2918c484918825859f5a9d6591ff856ccc0d483de
authority: docs-explanation
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: a74043661e0c7a5ba454667e429006fd2870ffe4e389116ea1a1eaf881a0c36b
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: Anton Simakov, thaelina; accepted inventory identities only. Source paths
  and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/weather-types/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/weather-types/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/weather-types/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/weather-types/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: doc/JSON/WEATHER_TYPE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/JSON/WEATHER_TYPE.md
- path: src/weather_type.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/weather_type.cpp
- path: src/weather_type.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/weather_type.h
- path: src/weather_gen.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/weather_gen.cpp
- path: data/json/weather_type.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/json/weather_type.json
- path: tests/weather_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tests/weather_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.weather-types%29%3A+&body=Document+ID%3A+json.weather-types%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：weather types

本页是 `json.weather-types` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.weather-types`
- Target: `reference/json/weather-types.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/weather-types/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.weather-types | doc/JSON/WEATHER_TYPE.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## Weather type 与 generator

`weather_type` 描述一种天气的显示和运行时影响，`weather_generator` 决定候选集合与基础气象。
二者是独立 object type。全局 consistency 要求 `null` 与 `clear` 两个 weather ID 有效。

### Weather type loader

name、id、sym、ranged_penalty、sight_penalty、light_modifier、priority、sound_attn、dangerous、
precip 和 rains 必填。可选字段包括 UI colors/sun symbol、temperature/light/sun modifier、音效/
tiles animation、duration、passive field effects、debug EOCs、required_weathers 与 condition。
duration_min/max 默认 5 minutes，且 min 不得大于 max。

condition 在 `weather_location` 等 dialogue context 中求值；候选按 priority 排序，required
weathers 必须引用有效 ID。不要把 JSON 文件顺序当稳定优先级，也不要把旧文档中的 sound/precip
枚举当完整列表，应查当前 enum registration。

### Weather generator

generator 要求 base temperature、humidity、pressure、wind；可配置季节修正、wind distribution
以及 weather whitelist 或 blacklist。白名单和黑名单互斥，finalize 会过滤并按 priority 排序；
白名单路径仍保留 clear。

### 验证

运行 formatter、`make -j2 json-check`、Mod `--check-mods` 和 focused weather tests。用固定 seed
覆盖四季、多坐标、condition/priority tie、required chain、duration bounds、indoors/vehicle passive
effects、debug EOC、light/sight/sound 与 whitelist。天气变化可能影响存档中当前 weather 和长期
世界生成，PR 要标记兼容/平衡影响。

## 历史与归属

清单中的已接受贡献者为：Anton Simakov, thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `99ab7d48f3e59f2838601af2918c484918825859f5a9d6591ff856ccc0d483de`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/WEATHER_TYPE.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/WEATHER_TYPE.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/WEATHER_TYPE.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
