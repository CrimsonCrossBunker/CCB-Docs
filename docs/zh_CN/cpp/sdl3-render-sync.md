---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.sdl3-render-sync
title: SDL3 渲染同步草稿
language: zh_CN
status: draft
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
review_interval_days: 90
last_human_reviewer: Pending human review
source_paths:
- src/cata_tiles.cpp
- src/cata_shader.cpp
- src/pixel_minimap.cpp
- src/sdl_font.cpp
- src/sdltiles.cpp
- src/level_cache.h
- src/smooth_lighting.cpp
- data/shaders/lit_sample.glsl
source_symbols: []
source_queries: []
source_fingerprint: 4de63a674cc4587ddef63bf9fcf379e1d65b46d42b793a428eaddfad1410890a
authority: api-contract
verified_commit: 7c964d3c9047216fffbefc602218da86c2781049
verified_at: '2026-10-14'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 19f4ab0c610d25f7944c6ffd8b630695478361e2c082212b00a96d16f471f002
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- lua-contract
api_version: '1'
deprecated: false
deprecation_replacement: null
risk_group: lua-api
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/sdl3-render-sync/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/sdl3-render-sync/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/sdl3-render-sync/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/sdl3-render-sync/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/7c964d3c9047216fffbefc602218da86c2781049
source_urls:
- path: src/cata_tiles.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7c964d3c9047216fffbefc602218da86c2781049/src/cata_tiles.cpp
- path: src/cata_shader.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7c964d3c9047216fffbefc602218da86c2781049/src/cata_shader.cpp
- path: src/pixel_minimap.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7c964d3c9047216fffbefc602218da86c2781049/src/pixel_minimap.cpp
- path: src/sdl_font.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7c964d3c9047216fffbefc602218da86c2781049/src/sdl_font.cpp
- path: src/sdltiles.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7c964d3c9047216fffbefc602218da86c2781049/src/sdltiles.cpp
- path: src/level_cache.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7c964d3c9047216fffbefc602218da86c2781049/src/level_cache.h
- path: src/smooth_lighting.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7c964d3c9047216fffbefc602218da86c2781049/src/smooth_lighting.cpp
- path: data/shaders/lit_sample.glsl
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7c964d3c9047216fffbefc602218da86c2781049/data/shaders/lit_sample.glsl
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.sdl3-render-sync%29%3A+&body=Document+ID%3A+cpp.sdl3-render-sync%0ALanguage%3A+zh_CN%0AVerified+commit%3A+7c964d3c9047216fffbefc602218da86c2781049%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# SDL3 渲染同步草稿

本页对应尚未合并的渲染同步分支，依赖 CCB #987 的 SDL3 后端。同步保留上游作者和 #88716、#88880、#88720、#88318、#88754、#88873、#88888 的来源。

## 保留的 CCB 行为

地图记忆仍由模拟侧更新，渲染只读取；没有恢复逐帧记忆扫描。RenderPrep 仍使用稀疏行缓存、图层侧表和合并动态刷新。图集重载包含 Lua 图块生成版本；Android 的输入唤醒和缩放边界保留。

小地图把变化区块像素与生物标记组成批量几何，保留 CCB 区块缓存和组合纹理缓存。文字使用共享字形页、货架分配与四边形批次，同时保留软件位图回退。着色与平滑光照接入 SDL3 着色器，并保留恢复和呈现修复边界。

喷涂或对角方向的载具图块暂时沿用经典几何路径，避免覆盖 CCB 喷涂显示。这是兼容性限制；不能声称所有图块都走新的光照路径。

## 验证范围

10 个 SPIR-V 着色器由生成器编译通过；39 个受影响源码/测试编译单元的语法检查通过。avatar 与 level_cache 布局已改变，不能用新文件链接旧引擎对象冒充匹配构建。

完整组合构建与软件渲染回归仍在进行。DXIL、MSL、实际 GPU、移动设备和性能场景尚未验证。这里不提供帧率提升承诺。

Responsible human: LYHGLYTX.
