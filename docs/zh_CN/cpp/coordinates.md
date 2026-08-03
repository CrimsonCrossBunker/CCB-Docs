---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp-coordinates
title: 旧文档迁移草稿：coordinates
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
last_human_reviewer: LYHGLYTX
source_paths:
- doc/c++/POINTS_COORDINATES.md
- src/point.h
- src/coordinates.h
- src/coordinate_conversions.cpp
- tests/coordinate_test.cpp
- tests/point_test.cpp
source_symbols:
- point
- tripoint
source_queries: []
source_fingerprint: 3f3b1575495c26b727ddb4f613ecfed93103166312c54ea30fb3669e4b8e3c0d
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: c94881a1aba488064f5e6f360d13f15cd177c100b828ce518f7ecbf3b1964699
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
risk_group: cpp
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/coordinates/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/coordinates/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/coordinates/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/coordinates/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/c++/POINTS_COORDINATES.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/c++/POINTS_COORDINATES.md
- path: src/point.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/point.h
- path: src/coordinates.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/coordinates.h
- path: src/coordinate_conversions.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/coordinate_conversions.cpp
- path: tests/coordinate_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tests/coordinate_test.cpp
- path: tests/point_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tests/point_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp-coordinates%29%3A+&body=Document+ID%3A+cpp-coordinates%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：coordinates

本页是 `cpp-coordinates` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `cpp-coordinates`
- Target: `cpp/coordinates.md`
- Replacement: cpp-coordinates
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| cpp-coordinates | doc/c++/POINTS_COORDINATES.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 当前 CCB 坐标类型

CCB 用类型同时编码维度、原点与水平尺度，避免把“现实气泡内 tile”误传为“世界绝对 OMT”。
类型别名以 `(tri)point_<origin>_<scale>[_ib]` 命名，并由 `coords_fwd.h` 和
`coordinates.h` 定义。

### 原点、尺度与轴

- `rel` 是相对偏移；`abs` 是全世界绝对原点。
- `sm`、`omt`、`om` 分别相对 submap、overmap terrain、overmap 左上角。
- `bub` 相对当前 reality bubble；它会随地图载入/角色位置变化。
- `ms`、`sm`、`omt`、`seg`、`om` 分别表示 map square 到 overmap 的单位。
- `point` 是 2D，`tripoint` 包含 z；`_ib` 表示对相应局部原点保证 in-bounds。

x 向屏幕右、y 向屏幕下、z 正值向上。水平尺度变化不会缩放 z。当前常量由
`SEEX/SEEY`、`OMAPX/OMAPY` 等源码定义，不把旧文档数字复制为永久契约。

### 选择和转换

新代码尽量使用 `tripoint_abs_ms`、`tripoint_bub_ms`、`point_abs_omt` 等 typed point；
只有真正没有游戏尺度的数学数据才用 raw `point`/`tripoint`。函数签名应公开需要的原点和
尺度，让错误在编译期出现。

```cpp
tripoint_abs_ms absolute = get_map().getglobal( local );
tripoint_bub_ms local_again = get_map().bub_from_abs( absolute );
point_abs_omt omt = project_to<coords::omt>( absolute.xy() );
```

同一原点改尺度用 `project_to`。向粗尺度投影且需要余数时用 `project_remain`，重组用
`project_combine`。绝对与 bubble 坐标转换必须经过具体 `map`；vehicle mount/rotated
坐标使用 `vehicle::coord_translate`/`mount_to_tripoint` 系列，不做手工旋转和偏移。

### 运算与 sentinel

只有语义成立的类型组合才支持加减：绝对位置加相对 offset 有意义，两个绝对位置相加没有。
distance 需要明确选 `square_dist`、`trig_dist`、`rl_dist` 或 `manhattan_dist`。
`zero` 是原点，`invalid`/`is_invalid()` 是失败 sentinel；不要把 `zero` 当“未设置”。

存档字段必须序列化能跨 reality-bubble 移动的坐标。NPC 或可中断 activity 的目标通常保存
absolute coordinate，而不是 avatar-relative bubble coordinate。

### 验证

编译受影响 translation unit，运行 `point_test`/`coordinate_test` 相关 filter，并覆盖负
坐标、submap/OMT 边界、z-level、map shift、vehicle rotation 与 serialize/deserialize
round trip。clang-tidy 的 point checks 是迁移帮助，不替代边界测试。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `3f3b1575495c26b727ddb4f613ecfed93103166312c54ea30fb3669e4b8e3c0d`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/c++/POINTS_COORDINATES.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/c%2B%2B/POINTS_COORDINATES.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/c%2B%2B/POINTS_COORDINATES.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
