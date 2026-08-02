---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: resources.tiles
title: Tileset
language: zh_CN
status: active
doc_type: reference
audiences:
- new-contributor
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- doc/TILESET.md
- gfx/tile_config_template.json
- src/sdltiles.h
- .github/workflows/compose-tilesets.yml
source_symbols:
- void load_tileset()
source_queries:
- TILESETS
source_fingerprint: 548f727df0a5e71280243013c4da40bb2aa4e81cbcd4b78459286334a318b5c9
authority: source-and-tests
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 61061f9df4b9952d28240b82ab556c77960a44966a74848a439c9063fb89270b
prerequisites:
- platforms.ui
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- json-load
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: resources-tiles
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/resources/tiles/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/resources/tiles/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/resources/tiles/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/resources/tiles/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: doc/TILESET.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/TILESET.md
- path: gfx/tile_config_template.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/gfx/tile_config_template.json
- path: src/sdltiles.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/sdltiles.h
- path: .github/workflows/compose-tilesets.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/.github/workflows/compose-tilesets.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28resources.tiles%29%3A+&body=Document+ID%3A+resources.tiles%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Tileset

tileset 把游戏 ID/variant 映射到 sprite/tilesheet。运行时加载、composition、package
metadata、ID fallback、rotation、multitile/connect rule、overlay 与许可证都属于契约。

## 权威路径

- `doc/TILESET.md` 解释受支持 tile JSON 概念与 composition 模型；
- `gfx/` 包含 bundled tileset metadata/asset，`gfx/tile_config_template.json` 是起始形状，
  不能替代真实 load；
- `src/sdltiles.*` 与 tile loader 定义运行时行为；
- `.github/workflows/compose-tilesets.yml` 定义受检查 composition 与可分发 asset。

## 所有权与 ID

游戏 JSON 拥有 entity ID；tile entry 引用 ID，并可增加 variant、rotation、multitile、
seasonal/gender form、overlay 或 fallback。重命名游戏 ID 未同步 tile 时，即使 JSON 加载
成功也可能静默退回 fallback art。

## 贡献流程

source sprite、tile entry JSON、tilesheet metadata 与 license/attribution 放在一起。使用
仓库 workflow/tool compose，审查 warning，再在 tiles build 启动结果。若 compositing
source 才是维护输入，不要手改 generated tilesheet。

## 验证

验证 JSON/composition、缺失/重复 ID、sprite bound、fallback、rotation/connection、overlay、
zoom/scaling、map/overmap view 与干净 package load。在游戏中抽查变化 ID；composition
成功不能证明视觉正确。

## 性能与打包

atlas 尺寸、texture 数、fallback chain 与重复 variant lookup 会影响启动、内存与 redraw。
明确 generated sheet 与 source art 的角色；仓库 workflow 视作 generated 时，大型输出可
作为 release/CI artifact。

## 许可证

每个导入 sprite 都需要兼容 license/attribution。“来自上游 tileset”不是充分来源；记录
source repository/path、可得作者、license 与转换。
