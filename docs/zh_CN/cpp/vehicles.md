---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.vehicles
title: Vehicle 子系统
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
- src/vehicle.h
- src/vehicle.cpp
- src/savegame_json.cpp
- tests/vehicle_test.cpp
source_symbols:
- class vehicle
source_queries: []
source_fingerprint: d74074095c884a900419468152311c7e2c9536aee794657a132b4c05f3c56edf
authority: source-and-tests
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: b0b38134e343955da3d09ca77b6e62b9819375d152b69d0d817aa460767b177d
prerequisites:
- cpp.map
- cpp.items
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
risk_group: cpp-vehicles
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/vehicles/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/vehicles/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/vehicles/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/vehicles/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: src/vehicle.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/vehicle.h
- path: src/vehicle.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/vehicle.cpp
- path: src/savegame_json.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/savegame_json.cpp
- path: tests/vehicle_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tests/vehicle_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.vehicles%29%3A+&body=Document+ID%3A+cpp.vehicles%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Vehicle

## 职责

`vehicle` 模型化由 `vehicle_part` 组成的可移动整体，包括安装点、cargo、engine、
battery、control、fault、label、zone、power network、运动、碰撞、autodrive 与交互。

## 入口点

阅读 `src/vehicle.h` 与各 `vehicle_*.cpp`。定义数据由 vehicle prototype 和 part 注册
表进入；放置与 `map` 集成；持久化在 `src/savegame_json.cpp`。

## 数据所有权

vehicle 拥有 part vector 与 part 内 item。已加载 submap 拥有 vehicle 实例；map 的
vehicle cache 索引占用点。`vehicle_part_location` 是受检查 locator，不是独立所有权。

## 依赖

vehicle 依赖 map 坐标/缓存、item pocket、part/type 注册表、fuel/energy 单位、Character、
Creature、zone、activity 与物理计算。

## 生命周期

prototype 生成或存档读取 vehicle；part 安装、移除、位移并 refresh；map 跟踪移动与
碰撞；split 创建不同 owner；卸载/保存持久化每个整体。

## 不变量

part mount 坐标与占用点缓存一致；part 引用只在文档有效期内使用；cargo 只有一个 owner；
part 变化失效 power/mass cache；split 不复制 part 或 label。

## 扩展点

优先使用 JSON vehicle part/prototype。原生行为放在聚焦组件，并同时更新 refresh/cache、
interaction、serialization 和 split 规则。

## 序列化

`vehicle::serialize` / `deserialize` 与 vehicle-part 持久化位于
`savegame_json.cpp`。派生物理与 map 缓存重建；持久 part 字段需要旧存档默认与迁移。

## 测试

按变化选择 vehicle part、split、power、efficiency、drag、ramp、turret、export、
fake-part、interaction 与 mapgen-placement 测试。

## 性能

移动会频繁重算占用 tile 与物理。保持 dirty flag，避免每个查询都全扫 part，并用大型
移动组合测量。

## CCB 差异

CCB vehicle 数据与代码经过选择性移植，不保证与上游缓存/存档语义一致。以 CCB
prototype、测试与当前序列化验证。

## 技术债务

part、cache、physics、power、UI 与 persistence 仍紧密耦合。重构应单独作为非行为修改，
并提供往返和运动证据。
