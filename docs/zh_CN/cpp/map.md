---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.map
title: Map 子系统
language: zh_CN
status: stale
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
- src/map.h
- src/map.cpp
- src/map_iterator.h
- tests/map_test.cpp
source_symbols:
- class map
source_queries: []
source_fingerprint: 549d7bfce1e4851b318b0573ee58374c0dc970e02d66474472a06e33bd986d52
authority: source-and-tests
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 5a939fd0b50343c778cfd2e4cef27495b0cf33d2b38843ff5b0f21bf450f1639
prerequisites:
- architecture.overview
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: cpp-map
risk_level: normal
pending_source_pr: null
stale_reason: 'Source paths changed after d32b9cc880a8: src/map.cpp'
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/map/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/map/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/map/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/map/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: src/map.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/map.h
- path: src/map.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/map.cpp
- path: src/map_iterator.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/map_iterator.h
- path: tests/map_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/map_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.map%29%3A+&body=Document+ID%3A+cpp.map%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Map

## 职责

`map` 是已加载 reality bubble 的 submap 视图，协调 terrain、furniture、field、trap、
item、vehicle、面向 creature 的查询、寻路、视线、缓存，以及附近世界状态的加载/
保存边界。

## 入口点

从 `src/map.h` 的 `class map` 和对应 `map_*.cpp` 开始。`map::load`、`map::save`、
`shift`、item/field mutator、vehicle cache 维护和 `map_iterator` 是主要边界。

## 数据所有权

已加载 submap 拥有 tile 内容与 vehicle 实例，`map` 提供视图和缓存；creature 另行
索引。调用方拿到的引用/iterator 有效期受 map 变化和 bubble shift 限制。

## 依赖

map 依赖 submap、坐标、terrain/furniture 注册表、field、trap、item、vehicle、
creature tracker、overmap 坐标、光照、寻路和 mapgen。

## 生命周期

submap 围绕绝对位置加载；缓存按需或加载时建立；变更把缓存标脏；bubble shift 保留/
替换区域；脏 submap 最终保存回世界存储。

## 不变量

坐标类型必须匹配 API；缓存反映 tile/vehicle 状态；item/vehicle 只有一个拥有 submap；
变化必须通过 map 方法，以失效透明度、寻路、outside、floor 与 vehicle 缓存。

## 扩展点

tile 行为优先通过 terrain/furniture/field/trap 数据增加。原生操作放入聚焦 map 组件，
并使用强类型坐标和集中 mutator。

## 序列化

`map::load` / `save` 把持久 tile 状态交给 submap/world 序列化。bubble 相对坐标与派生
缓存不持久化，绝对位置和 submap 内容才持久化。

## 测试

使用 map、iterator、path、memory、bash、field、vehicle 与 map-helper 测试。缓存变化
需覆盖 mutation 前后查询，必要时还要覆盖 load/shift。

## 性能

渲染、AI 与移动循环都会调用 map 查询。避免宽泛失效、重复坐标投影和全 bubble 扫描；
使用真实规模 reality bubble 测量。

## CCB 差异

CCB 可能保留与上游移植不同的 map 行为和缓存。同名函数不代表失效规则或存档布局
相同，应以 CCB 测试为契约。

## 技术债务

`map` 仍是覆盖存储、模拟、渲染查询和缓存的大型 facade。新工作应进入聚焦组件，不要
把缓存重构与玩法变化混合。
