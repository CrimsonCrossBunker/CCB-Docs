---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.loading-order
title: 旧文档迁移草稿：loading order
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
- data/json/LOADING_ORDER.md
- doc/JSON/JSON_LOADING_ORDER.md
- src/filesystem.cpp
- src/init.cpp
- src/game_io.cpp
source_symbols:
- DynamicDataLoader::load_data_from_path
- DynamicDataLoader::load_all_from_json
- DynamicDataLoader::finalize_loaded_data
source_queries: []
source_fingerprint: f0979275d95b5694a34e200e0c493b395e64c987686d4ae7488c44253f01d92e
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: a8f29676da84cf0f6bc70e5741efc62e26fc2961cba06d4ba15b9ef0e3ecab84
prerequisites: []
depends_on: []
redirect_from: []
supersedes:
- legacy.data-json-loading-order
- legacy.doc-json-json-loading-order
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/loading-order/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/loading-order/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/loading-order/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/loading-order/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: data/json/LOADING_ORDER.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/LOADING_ORDER.md
- path: doc/JSON/JSON_LOADING_ORDER.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/JSON_LOADING_ORDER.md
- path: src/filesystem.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/filesystem.cpp
- path: src/init.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/init.cpp
- path: src/game_io.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/game_io.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.loading-order%29%3A+&body=Document+ID%3A+json.loading-order%0ALanguage%3A+zh_CN%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：loading order

本页是 `json.loading-order` 的迁移草稿页面。它记录 **2** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `legacy.data-json-loading-order, legacy.doc-json-json-loading-order`
- Target: `reference/json/loading-order.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/loading-order/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| legacy.data-json-loading-order | data/json/LOADING_ORDER.md | merge_into | stubbed | 5f23722ff28c5cc552baa0422b32b1f10fd890fa | json.loading-order |
| legacy.doc-json-json-loading-order | doc/JSON/JSON_LOADING_ORDER.md | merge_into | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | json.loading-order |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## JSON 加载阶段与顺序

CCB 对每个 active Mod 按 world 已解析的依赖顺序调用 loader。单个路径内
`get_files_from_path(..., recursive=true)` 以 breadth-first 发现 JSON，同一目录按当前 filesystem
排序；普通 Mod 数据排除 `mod_interactions`，所有普通数据完成后再加载命中的 interaction。

### 可以依赖什么

可以依赖明确的 Mod dependency、generic factory deferred loading，以及 owning loader 文档化
的 finalize 解析。不要把文件名或目录深度当成通用 forward-reference API。某些 object 在
parse 时强制目标已存在，另一些只存 string ID 到 consistency check；必须检查具体 handler。

Core `data/json` 的历史目录布局曾用深度表达 skills→professions→scenarios 等顺序，但新代码
应优先让 factory/loader 明确处理关系。把文件移动到子目录可能改变 parse 次序，并影响依赖
旧偶然顺序的内容；这种变化属于高风险 JSON 修改。

### Mod 与 interaction

`dependencies` 决定 active Mod 顺序。普通内容必须在声明依赖之后可解析。
`mod_interactions/<target-id>/` 在普通 pass 后加载，source 记录为 `base#target`；它不能解决
普通文件在之前已经抛出的错误，也不支持嵌套多目标目录。

### 验证

运行 formatter、`make -j2 json-check` 和完整依赖组合 `--check-mods`。对顺序敏感修改，
加入最小 fixture，分别测试父/子先后、缺失 dependency、两个 Mod 覆盖、interaction 和
finalize。不要只在开发 checkout 测试；打包后的 path/case 行为也要由目标平台 CI 覆盖。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `f0979275d95b5694a34e200e0c493b395e64c987686d4ae7488c44253f01d92e`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`data/json/LOADING_ORDER.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/LOADING_ORDER.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/LOADING_ORDER.md)
- [`doc/JSON/JSON_LOADING_ORDER.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/JSON_LOADING_ORDER.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/JSON_LOADING_ORDER.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
