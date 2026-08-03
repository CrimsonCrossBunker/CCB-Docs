---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.terrain-furniture-transforms
title: 旧文档迁移草稿：terrain furniture transforms
language: zh_CN
status: draft
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
- doc/JSON/TER_FURN_TRANSFORM.md
- src/magic_ter_fur_transform.cpp
- src/magic_ter_furn_transform.h
- src/mapgen.cpp
- data/json/mapgen/haunting.json
source_symbols:
- ter_furn_transform::load
- ter_furn_data<T>::load
source_queries: []
source_fingerprint: 7a7d7f8f3faec648766f1b2b622d9ba14c2f24702c6e4a2954b9b65e8ee93188
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 40f0140ddc61dc0e3297fb1827429ffca26927f499a333a9a3b3bb6ffc1e0f93
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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/terrain-furniture-transforms/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/terrain-furniture-transforms/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/terrain-furniture-transforms/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/terrain-furniture-transforms/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/JSON/TER_FURN_TRANSFORM.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/TER_FURN_TRANSFORM.md
- path: src/magic_ter_fur_transform.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/magic_ter_fur_transform.cpp
- path: src/magic_ter_furn_transform.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/magic_ter_furn_transform.h
- path: src/mapgen.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/mapgen.cpp
- path: data/json/mapgen/haunting.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/mapgen/haunting.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.terrain-furniture-transforms%29%3A+&body=Document+ID%3A+json.terrain-furniture-transforms%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：terrain furniture transforms

本页是 `json.terrain-furniture-transforms` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.terrain-furniture-transforms`
- Target: `reference/json/terrain-furniture-transforms.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/terrain-furniture-transforms/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.terrain-furniture-transforms | doc/JSON/TER_FURN_TRANSFORM.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 当前 CCB terrain/furniture transform

`ter_furn_transform` 是具名、可复用的格子转换表。它分别匹配 terrain、furniture、field 和
trap，然后从带权 `result` 中选择替代值。各类别互相独立；匹配 terrain 不会自动产生某个
furniture。

### 基础定义

```jsonc
{
  "type": "ter_furn_transform",
  "id": "ccb_example_transform",
  "terrain": [
    {
      "valid_terrain": [ "t_sand" ],
      "result": [ [ "t_dirt", 4 ], "t_grass" ],
      "message": "The sand shifts.",
      "message_good": true
    }
  ]
}
```

单个 result 的权重为 1；二元数组可提供权重。`message_good` 缺省为 true。terrain 与
furniture 还可用 `valid_flags` 匹配；field/trap 使用各自 valid-ID 字段。具体字段名和是否
支持 flag 以 `ter_furn_transform::load` 为准。

### 匹配与冲突

Loader 把每个 valid ID/flag 映射到转换结果。同一输入被多条规则覆盖时，容器插入顺序与
实现细节不应被当成内容优先级机制；保持匹配集合互斥，或补测试证明预期。`f_null`、
`fd_null` 等“清除”结果仍是各系统的真实 ID，不要用 JSON null 替代。

Transform 可由 mapgen placing、EOC 半径效果、spell 等调用。调用者决定位置、范围、
talker、重复次数和消息展示；transform 本身不记录“已执行”。重复调用必须是明确设计，
尤其是带随机结果或可能形成 A↔B 循环时。

### 验证

1. 检查所有 valid/result terrain、furniture、field、trap ID 与 flags。
2. 运行 formatter、`make -j2 json-check` 和实际 Mod 集 `--check-mods`。
3. 分别测试每类输入、无匹配、多个 flag、权重边界与 null/清除结果。
4. 从每个真实调用点测试范围、z-level、重复执行和消息。
5. Mapgen 调用再运行 `mapgen_function_test`，EOC/spell 调用运行对应 focused test。

Transform 适合声明同格类型替换；需要跨格、条件链或副作用时，应在 EOC/mapgen 调用层
表达，而不是依赖偶然的规则覆盖。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `7a7d7f8f3faec648766f1b2b622d9ba14c2f24702c6e4a2954b9b65e8ee93188`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/TER_FURN_TRANSFORM.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/TER_FURN_TRANSFORM.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/TER_FURN_TRANSFORM.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
