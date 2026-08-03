---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: resources.fonts
title: 字体
language: zh_CN
status: active
doc_type: reference
audiences:
- experienced-contributor
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- doc/user-guides/FONT_OPTIONS.md
- src/font_loader.cpp
- src/sdl_font.h
source_symbols:
- class Font
source_queries:
- gui_typeface
source_fingerprint: 79981d08415e94a2469b032cd78f03d8ad9b3e66810ecd39e5524ea2d329f1c1
authority: source-and-tests
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 8922eb552ca0384525d024eece39f14ecebad1dd58fdc11c423803d33708d1e1
prerequisites:
- platforms.ui
depends_on:
- resources.translation
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: resources-fonts
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/resources/fonts/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/resources/fonts/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/resources/fonts/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/resources/fonts/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/user-guides/FONT_OPTIONS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/user-guides/FONT_OPTIONS.md
- path: src/font_loader.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/font_loader.cpp
- path: src/sdl_font.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/sdl_font.h
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28resources.fonts%29%3A+&body=Document+ID%3A+resources.fonts%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 字体

font 覆盖四种不同显示角色：terminal/native typeface、ImGui GUI、map 与 overmap，同时
处理有序 fallback、glyph coverage、metric、hinting、antialiasing 与 GPU resource recovery。

## 权威路径

`doc/user-guides/FONT_OPTIONS.md` 解释用户配置；`src/font_loader.cpp` 定义可接受的
string/object/array、hinting 值、migration 与强制 Unifont fallback；`src/sdl_font.*`
拥有运行时 font instance 与 glyph/texture cache；bundled 文件位于 `data/font/`。

## 配置契约

`typeface`、`gui_typeface`、`map_typeface`、`overmap_typeface` 可为单一路径或有序 fallback
列表。object entry 可声明 `path`、`hinting`、`antialiasing`。必须保留能提供缺失 Unicode
glyph 的 fallback；只检查 Latin 不充分。

## 贡献流程

添加 binary 前确认 font 的 redistribution/embedding license，记录 source、version、
author/foundry、license、subset/transformation 与预期角色。不能在同名下替换文件而不审查
metric、coverage、package size 与 attribution。

## 验证

测试拉丁、简繁中文、combining mark、wide character、symbol、fallback、line drawing、
窄 UI、map/overmap alignment、DPI/scaling、hinting mode 与 renderer reset。texture lifecycle
不同处要覆盖 SDL2/SDL3。

## 性能与所有权

font object 拥有 glyph texture cache；renderer recovery 会 release/rebuild 或按需重新填充。
无界 glyph/color cache 会消耗 GPU memory。font path/metadata 可进用户配置，GPU resource
绝不持久化。

## 生成数据

不要提交 local font cache/atlas。刻意生成 subset 只有连同可复现 generator、source
license、Unicode coverage input 与验证时才可跟踪。
