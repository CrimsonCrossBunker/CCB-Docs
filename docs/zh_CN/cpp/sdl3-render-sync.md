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
- src/CMakeLists.txt
- tools/agent/test_shader_cmake_graph.py
source_symbols: []
source_queries: []
source_fingerprint: b6c9fb6600de97d5f52c1ceb26a11e7b1600e5bfb16dcc237b1591e91b8b71ed
authority: api-contract
verified_commit: eb8bfeabd8748176cc33aa2329b634d17bb61885
verified_at: '2026-10-14'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: a376cdd4479fcfbe8bec83cde870e045bd0e0178d79ff408bc63b358b25d1e89
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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/1000
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/sdl3-render-sync/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/sdl3-render-sync/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/sdl3-render-sync/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/sdl3-render-sync/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/eb8bfeabd8748176cc33aa2329b634d17bb61885
source_urls:
- path: src/cata_tiles.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/cata_tiles.cpp
- path: src/cata_shader.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/cata_shader.cpp
- path: src/pixel_minimap.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/pixel_minimap.cpp
- path: src/sdl_font.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/sdl_font.cpp
- path: src/sdltiles.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/sdltiles.cpp
- path: src/level_cache.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/level_cache.h
- path: src/smooth_lighting.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/smooth_lighting.cpp
- path: data/shaders/lit_sample.glsl
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/data/shaders/lit_sample.glsl
- path: src/CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/CMakeLists.txt
- path: tools/agent/test_shader_cmake_graph.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/tools/agent/test_shader_cmake_graph.py
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.sdl3-render-sync%29%3A+&body=Document+ID%3A+cpp.sdl3-render-sync%0ALanguage%3A+zh_CN%0AVerified+commit%3A+eb8bfeabd8748176cc33aa2329b634d17bb61885%0A%0ADescribe+the+documentation+problem%3A%0A
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

Clang 23、Release、C++17、SDL3、图块、声音、zh_CN 和唯一 Lua Platform v1 配置下，组合分支 #1000 的匹配游戏和测试程序编译成功。有效测试范围共 992 个案例：宽范围运行通过 991 个，另一个可见 NPC 案例暴露测试初始化的视距缓存假设；修正后 Lua 与视距组合的 528 个案例、86,021 条断言通过。六个集成回归的 2,567 条断言通过。这是分范围证据，不能表述为同一次进程通过全部 992 个案例。

新程序对基础游戏及全部 18 个受影响且未废弃 Mod 的独立加载检查全部通过（共 19 个身份），包括 MoM 新维度和流亡族数据。加载检查不能证明全部新增玩法、旧存档、真实 GPU、所有桌面平台或 Android 设备已通过。

软件路径和模拟 GPU 恢复测试已进入组合回归范围。DXIL、MSL、真实 GPU、移动设备和性能基准场景尚未验证，本页不承诺帧率提升。

Windows 的 vcpkg 构建使用包内的 glslangValidator 和 shadercross；公共 GLSL 文件变化会触发重新编译。该路径按请求的 spv、dxil、msl 格式生成，并保留片元和顶点阶段。CMake 命令图的四个测试通过，覆盖带空格工具路径、SPIR-V 前置依赖、格式选择与非 vcpkg 构建；这不表示本机执行了 Windows 的 DXIL/MSL 编译。

Responsible human: LYHGLYTX.
