---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp-json-interface
title: 旧文档迁移草稿：json interface
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
- doc/c++/JSON_INTERFACE.md
- src/flexbuffer_json.h
- src/flexbuffer_json.cpp
- src/generic_factory.h
- tests/generic_factory_test.cpp
source_symbols:
- JsonObject
- JsonArray
- generic_factory
source_queries: []
source_fingerprint: c63af9e125cbee7cbed69fcdde222171233e52ab5c6bdc2661d41903fa1b0bd7
authority: docs-explanation
verified_commit: 02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 7a264178f15e4e29a98637b03b4743edc3c4b807861345e277d9fb010fe9efc2
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: ehughsbaird; accepted inventory identities only. Source paths and Git
  history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: cpp
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/json-interface/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/json-interface/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/json-interface/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/json-interface/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
source_urls:
- path: doc/c++/JSON_INTERFACE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/c++/JSON_INTERFACE.md
- path: src/flexbuffer_json.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/flexbuffer_json.h
- path: src/flexbuffer_json.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/flexbuffer_json.cpp
- path: src/generic_factory.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/generic_factory.h
- path: tests/generic_factory_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/tests/generic_factory_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp-json-interface%29%3A+&body=Document+ID%3A+cpp-json-interface%0ALanguage%3A+zh_CN%0AVerified+commit%3A+02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：json interface

本页是 `cpp-json-interface` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `cpp-json-interface`
- Target: `cpp/json-interface.md`
- Replacement: cpp-json-interface
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| cpp-json-interface | doc/c++/JSON_INTERFACE.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## CCB C++ JSON 接口

先区分三种任务：载入人写的 game data、读取程序写的旧存档、写出新的存档。它们共享
`JsonValue`、`JsonArray`、`JsonObject`、`JsonMember` 和 `JsonOut`，但兼容策略不同。
Game data 支持 factory 继承；save data 必须能识别旧格式，不能把 `copy-from` 当存档机制。

### 读写基础

`JsonValue` 可测试并读取 scalar 或转成 object/array；`JsonObject` 按 member 名访问，
`JsonArray` 迭代或按位置读取，`JsonMember` 同时保留 key 和 value。优先用 `read` 以及
项目已有 deserialize/reader，不重复手写类型分支。

实现 `T::serialize( JsonOut & ) const` 或自由 `serialize` 后，`JsonOut::write/member` 可
组合该类型。读取对应实现 `deserialize`。写出格式是兼容契约：字段改名、删除或改变类型前
必须保留旧格式 reader 和 round-trip/旧 fixture 测试。

### Game data loader

generic factory 管理 ID、`copy-from`、deferred load、finalize 和 consistency check。对象
`load` 通常使用：

- `mandatory( jo, was_loaded, name, member[, reader] )`：首次对象必须提供；
- `optional( jo, was_loaded, name, member[, reader], default )`：首次缺失时使用明确 default；
- typed reader：解析 shorthand、单位、ID、容器和该字段允许的继承操作。

Default 必须出现在 `optional` 调用中，而不是只依赖 header 初始化。`was_loaded` 让子对象
缺失字段时保留父值；错误传 false 会抹掉继承值，错误传 true 会跳过首定义要求。

`extend`/`delete`、`relative`、`proportional` 都是 opt-in。容器 reader 常支持前两者，
数值操作依赖类型和 reader；字段看起来“像 vector/int”不证明它自动支持相应 patch。

### 错误和严格性

让 `JsonObject`/reader 在具体 member 抛出错误，以保留文件、行列和 member context。
不要为“兼容”广泛调用 `allow_omitted_members`；只在明确转发或忽略对象的边界使用。
加载成功后仍要运行 finalize/consistency checks，因为 cross-ID 和循环往往到该阶段才发现。

### 验证

Game data 运行 formatter、`make -j2 json-check`、真实 Mod 集 `--check-mods` 和 object
focused tests。Save data 用当前写出→读回、冻结旧 fixture→当前读取、缺失/新增字段与损坏
输入测试。C++ 改动还要编译所有使用公开 header 的 target，并确认错误消息仍指向来源。

## 历史与归属

清单中的已接受贡献者为：ehughsbaird。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b`；聚合源指纹为 `c63af9e125cbee7cbed69fcdde222171233e52ab5c6bdc2661d41903fa1b0bd7`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/c++/JSON_INTERFACE.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/c%2B%2B/JSON_INTERFACE.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/c%2B%2B/JSON_INTERFACE.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
