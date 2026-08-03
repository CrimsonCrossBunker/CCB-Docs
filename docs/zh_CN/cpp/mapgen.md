---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.mapgen
title: Mapgen 子系统
language: zh_CN
status: active
doc_type: reference
audiences:
- experienced-contributor
- maintainer
- mod-author
- api-user
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- src/mapgen.h
- src/mapgen.cpp
- src/mapgendata.h
- tests/mapgen_function_test.cpp
source_symbols:
- class mapgen_function
- class mapgendata
source_queries: []
source_fingerprint: 0b3c8ae0393e04b93c3f693b6ff48eff6c2b478d5e88afd88c806b8d4afc08bb
authority: source-and-tests
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 7dd843b71a513b99479857a00e50c756f7716a3ae595bfd1ce01960c03946165
prerequisites:
- cpp.map
- cpp.overmap
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
- json-load
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: cpp-mapgen
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/mapgen/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/mapgen/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/mapgen/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/mapgen/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: src/mapgen.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/mapgen.h
- path: src/mapgen.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/mapgen.cpp
- path: src/mapgendata.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/mapgendata.h
- path: tests/mapgen_function_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/mapgen_function_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.mapgen%29%3A+&body=Document+ID%3A+cpp.mapgen%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 地图生成

## 职责

mapgen 把 overmap terrain 与区域上下文转换为 submap 内容，通过 `mapgendata` 分派
内置/JSON mapgen function、palette、nested chunk、parameter、join、rotation、放置和
后处理。

## 入口点

从 `src/mapgen.h`、`src/mapgen.cpp`、`src/mapgendata.h` 开始。JSON 实现继承
`mapgen_function_json_base`；primitive 与 post-process 位于聚焦模块；异步编排隔离在
`mapgen_async`。

## 数据所有权

注册表拥有 mapgen 定义与 palette；一个 `mapgendata` 实例携带一次生成上下文并写入
目标 `map`；生成的 terrain、furniture、item、field 和 vehicle 随后归 submap 所有。

## 依赖

mapgen 依赖 overmap terrain/special、region settings、map data 注册表、RNG、坐标、
JSON loader、palette 与生成实体的 validator。

## 生命周期

定义加载并 finalize；请求选择实现和上下文；生成放置、变换内容；后处理执行区域规则；
完成的 submap 进入常规 map 持久化。

## 不变量

mapgen ID 与 nested 引用可解析；join/rotation 使用预期朝向；坐标留在目标内；unique
放置规则成立；需要确定性时固定 seed 能复现相同契约。

## 扩展点

优先使用 JSON mapgen、palette、nested mapgen 与 parameter。仅在数据无法表达算法时
增加内置生成器，并集中注册、提供带 seed 的测试。

## 序列化

mapgen 定义是源数据，不是存档记录。延迟请求需要持久化时 `mapgen_arguments` 可序列化；
生成 submap 通过常规 map 保存。

## 测试

使用 function、vehicle placement、post-process、remove-NPC/vehicle、rotation、special
与 JSON load 测试。记录 seed，并检查每个受影响朝向。

## 性能

探索时可能触发生成并阻塞游戏。避免重复扫描注册表与无界拒绝循环；测量大型/nested
generator 与异步交接。

## CCB 差异

CCB 数据集与选择性 worldgen 移植定义实际 mapgen 行为。上游 JSON 可能依赖这里没有
的 loader、parameter 或后处理，必须验证而不是直接复制。

## 技术债务

内置与 JSON 生成器共享可变 map 上下文，但验证程度不同。应把共同不变量移到 validator，
同时防止意外改变生成结果。
