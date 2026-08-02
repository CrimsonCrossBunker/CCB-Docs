---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.object-types
title: 旧文档迁移草稿：json
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
- doc/JSON/JSON_INFO.md
- src/init.cpp
- src/json.cpp
- src/generic_factory.cpp
- tests/json_load_test.cpp
- tests/json_test.cpp
source_symbols:
- DynamicDataLoader::initialize
- DynamicDataLoader::load_object
- DynamicDataLoader::load_data_from_path
source_queries: []
source_fingerprint: a6d1bae5a02166a5dfd7f540f84eb347c4c5af10d6f7a8c48aa42e33457ddb09
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: fce3e759a192d6a9760124f5c91c4ec26f223747878851d916ad673085fadef7
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: LunaGlaze, MrDraMaster, OromisElf, zihanZheng, Fris0uman, Maleclypse,
  Mihály Verhás, Tektolnes, ehughsbaird, Anton Simakov, RenechCDDA; accepted inventory identities only.
  Source paths and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/JSON/JSON_INFO.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/JSON_INFO.md
- path: src/init.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/init.cpp
- path: src/json.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/json.cpp
- path: src/generic_factory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/generic_factory.cpp
- path: tests/json_load_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/tests/json_load_test.cpp
- path: tests/json_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/tests/json_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.object-types%29%3A+&body=Document+ID%3A+json.object-types%0ALanguage%3A+zh_CN%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：json

本页是 `json.object-types` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.object-types`
- Target: `reference/json/index.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.object-types | doc/JSON/JSON_INFO.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## CCB JSON object type 注册表

`DynamicDataLoader` 的 native `add(type, handler)` 调用决定可识别的 object type。
`data/reference/json/ccb_json_object_types.json` 是由
`tools/json_api/generate_contracts.py` 生成的检查清单，当前覆盖 191 个注册调用、190 个唯一
type。它证明“发现并索引”，不证明每个 handler 已有完整字段 Schema。

### 如何使用清单

每项记录 type、handler、source symbol/line、可证实的 mandatory/optional 字段、first-party
example 和 documentation status。`schema_status`/`documentation_status` 必须按原值解释；
`unclassified` 或 lexical-only 不能提升为必填、默认或完整支持。

生成清单禁止手改。新增/删除注册、修改 handler 或示例后运行 generator、仓库 JSON formatter、
`--check` 与 `tools/json_api` 单测。若提取器无法证明复杂 reader，应扩展可审核提取或加入
非行为性 registration metadata，而不是猜测。

### 从 type 到权威契约

1. 在 inventory 找 handler 和 source。
2. 阅读 loader 的 `mandatory`、`optional`、custom reader、finalize/check。
3. 找相邻第一方 JSON 与 focused test。
4. 检查 ID、copy-from、deferred load、单位、translation、migration 和 Mod 边界。
5. 用 formatter、`make -j2 json-check`、`--check-mods` 验证真实组合。

Editor Schema 可以提供补全，但 loader 和测试胜出。Occurrence count 只说明样本中出现频率，
不能证明 requiredness；成功解析也不证明 cross-ID finalize、平衡或存档兼容。

## 历史与归属

清单中的已接受贡献者为：LunaGlaze, MrDraMaster, OromisElf, zihanZheng, Fris0uman, Maleclypse, Mihály Verhás, Tektolnes, ehughsbaird, Anton Simakov, RenechCDDA。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `a6d1bae5a02166a5dfd7f540f84eb347c4c5af10d6f7a8c48aa42e33457ddb09`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/JSON_INFO.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/JSON_INFO.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/JSON_INFO.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
