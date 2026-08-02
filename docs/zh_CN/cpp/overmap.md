---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.overmap
title: Overmap 子系统
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
- src/overmap.h
- src/overmap.cpp
- src/overmapbuffer.cpp
- tests/overmap_test.cpp
source_symbols:
- class overmap
source_queries: []
source_fingerprint: 4f1c926269074f731ddaf35e690803968df3af0b87142ae1d011333e858511ef
authority: source-and-tests
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: ee342328cb87cb48e7d7df8792b3ad573fb8d7b4a9057e89b21dd743436eb6d0
prerequisites:
- architecture.overview
depends_on:
- cpp.map
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: cpp-overmap
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/overmap/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/overmap/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/overmap/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/overmap/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: src/overmap.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/overmap.h
- path: src/overmap.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/overmap.cpp
- path: src/overmapbuffer.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/overmapbuffer.cpp
- path: tests/overmap_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tests/overmap_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.overmap%29%3A+&body=Document+ID%3A+cpp.overmap%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Overmap

## 职责

`overmap` 保存一个大尺度世界区域：overmap terrain、城市、道路/连接、special 放置、
monster group、NPC/camp 引用、note、可见性与区域 worldgen 状态；`overmapbuffer` 协调
多个区域。

## 入口点

阅读 `src/overmap.h` 和各 `overmap_*.cpp`。区域获取与跨边界查询进入
`overmapbuffer`；`overmap::save`、`serialize`、`unserialize` 定义持久边界。

## 数据所有权

overmap 拥有区域 terrain layer 与延迟的世界尺度记录；buffer 拥有或缓存加载的
overmap 对象。已加载 reality-bubble monster 与 overmap monster-group 记录不是同一
所有权形态。

## 依赖

overmap 依赖绝对 overmap 坐标、terrain/special/connection 注册表、region settings、
mapgen 放置、monster group、城市、天气、NPC 与世界存储。

## 生命周期

区域被生成或读取，与邻区连接，世界运行时被查询和更新，最后按 buffer 政策序列化并
逐出。

## 不变量

绝对坐标必须定位正确区域与局部 cell；连接在区域边界一致；unique special 遵守放置
状态；creature 加载/卸载不能复制 population。

## 扩展点

优先使用 JSON overmap terrain、special、location 和 connection。原生生成放在聚焦
模块，提供确定性放置测试并明确邻区行为。

## 序列化

`src/savegame.cpp` 保存 terrain layer、group、NPC/camp、note 和全局 overmap 状态。
缓存和生成摘要可重建；新持久字段必须有旧存档默认值。

## 测试

使用 overmap、noise、connection、cache、special-placement 与 worldfactory 测试。
生成回归要记录 seed，并测试区域边界。

## 性能

世界旅行与生成可能接触许多区域。只读查询应避免强制加载，并限制 map-data summary
与路径搜索范围。

## CCB 差异

CCB 的 overmap 生成与 POI 处理包含项目专属修复和选择性上游移植。删除、放置与持久
行为必须按当前 CCB 测试和数据验证。

## 技术债务

生成、运行时查询、UI 数据与持久化仍集中在宽区域对象中。应保持 buffer 所有权，并
按职责拆分工作，避免新增全局扫描。
