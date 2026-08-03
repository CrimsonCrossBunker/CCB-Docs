---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: tilesets
title: 旧文档迁移草稿：tilesets
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
- doc/TILESET.md
- tools/gfx_tools/compose.py
- tools/gfx_tools/decompose.py
- .github/workflows/compose-tilesets.yml
source_symbols: []
source_queries: []
source_fingerprint: 60752d04ad6e528c8eafada2d0bf4f559f838591a7a555c1f59a07efa2427b9f
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 027254a6cebb2e08e28ce207cd2c8087a9ea409cbc6d88349a9c215f399070ee
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
risk_group: resources
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/resources/tilesets/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/resources/tilesets/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/resources/tilesets/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/resources/tilesets/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/TILESET.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/TILESET.md
- path: tools/gfx_tools/compose.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tools/gfx_tools/compose.py
- path: tools/gfx_tools/decompose.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tools/gfx_tools/decompose.py
- path: .github/workflows/compose-tilesets.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/.github/workflows/compose-tilesets.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28tilesets%29%3A+&body=Document+ID%3A+tilesets%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：tilesets

本页是 `tilesets` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `tilesets`
- Target: `resources/tilesets.md`
- Replacement: tilesets
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| tilesets | doc/TILESET.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## Tileset 制作与组合

CCB distribution 使用 compositing tileset：独立 PNG sprite、tile-entry JSON、`tile_info.json` 与
`tileset.txt` 经 `tools/gfx_tools/compose.py` 生成 tilesheet 和 `tile_config.json`。运行时实际可读
字段仍以 tiles loader 为准；compose 只验证/转换它理解的 source format。

### Source layout 与 tile entry

Tile entry 用 `id` 把游戏实体映射到 `fg`/`bg` sprite root。可使用 rotations、weighted
variants、`multitile`/`additional_tiles`、season/gender/item variant 命名和 contextual layering。
terrain/furniture 的连接与旋转还依赖游戏 JSON 中的 `connect_groups`、`connects_to`、
`rotates_to`；tileset 不能自行创造这些 runtime 关系。Hardcoded overlay/animation ID 应从当前
`cata_tiles.cpp` 和调用点清点，旧手工列表可能遗漏。

`tile_info.json` 描述默认和各 tilesheet 的 sprite 尺寸、offset、pixelscale、sheet width，以及
filler/fallback/exclude。相同 sprite root、filler 顺序和跨目录引用会影响结果；保持名字唯一并
审查 compose warning。`layering.json` 的 context、item/field variant、offset 与 layer 是单独的
runtime contract。

### Compose、发布与验证

当前 CI 使用类似以下命令：

```sh
python3 tools/gfx_tools/compose.py --use-all --obsolete-fillers \
  --feedback CONCISE --format-json --loglevel INFO SOURCE DEST
```

实际 flags 以 `compose.py --help` 为准；`--only-json`、`--fail-fast`、palette 等选项改变输出或
诊断。先在临时输出目录运行，审查 unused/missing/duplicate sprite、生成 JSON 和图片尺寸，再用
Tiles build 加载并测试旋转、multitile、fallback、zoom、季节、overlay 和 layering。需要回转旧
index tileset 时才用 `decompose.py`，其自动文件名/目录必须人工整理。

所有 artwork 必须有可分发许可证与可追溯 attribution；CI 能 compose 不代表素材许可合格。当前
打包矩阵在 `.github/workflows/compose-tilesets.yml`，外部 tileset 仓库内容不是 CCB runtime
契约，版本与来源必须固定并审阅。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `d32b9cc880a85480840d82cfa05d256c78a16615`；聚合源指纹为 `60752d04ad6e528c8eafada2d0bf4f559f838591a7a555c1f59a07efa2427b9f`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/TILESET.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/TILESET.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/TILESET.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
