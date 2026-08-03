---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: architecture.subsystem-map
title: 子系统地图
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
review_interval_days: 90
last_human_reviewer: LYHGLYTX
source_paths:
- AGENTS.md
- ai/project-map.yml
- src/AGENTS.md
- data/AGENTS.md
- tests/AGENTS.md
- android/AGENTS.md
source_symbols: []
source_queries: []
source_fingerprint: a98974327840d4768d631e096b5e00042003c0e7a60e10d7d9a5ecc967584fa7
authority: docs-explanation
verified_commit: d6aa4576178a1a6ff21ffede7f282a994fcbc4b3
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: ee57553c6d74fba8898eb506d3d41920225363885c18c2f865ed2e92bd6b4875
prerequisites:
- architecture.overview
depends_on:
- architecture.project-map
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- agent-context
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: architecture
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/560
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/subsystem-map/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/subsystem-map/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/architecture/subsystem-map/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/subsystem-map/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d6aa4576178a1a6ff21ffede7f282a994fcbc4b3
source_urls:
- path: AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d6aa4576178a1a6ff21ffede7f282a994fcbc4b3/AGENTS.md
- path: ai/project-map.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d6aa4576178a1a6ff21ffede7f282a994fcbc4b3/ai/project-map.yml
- path: src/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d6aa4576178a1a6ff21ffede7f282a994fcbc4b3/src/AGENTS.md
- path: data/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d6aa4576178a1a6ff21ffede7f282a994fcbc4b3/data/AGENTS.md
- path: tests/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d6aa4576178a1a6ff21ffede7f282a994fcbc4b3/tests/AGENTS.md
- path: android/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d6aa4576178a1a6ff21ffede7f282a994fcbc4b3/android/AGENTS.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28architecture.subsystem-map%29%3A+&body=Document+ID%3A+architecture.subsystem-map%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d6aa4576178a1a6ff21ffede7f282a994fcbc4b3%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 子系统地图

这张地图用于找到入口，不替代源码阅读。修改前继续读取目标路径最近的 `AGENTS.md`。

| 子系统 | 主要路径 | 常见相邻契约 |
| --- | --- | --- |
| Character / Avatar | `src/character*`、`src/avatar*` | effect、activity、mutation、save |
| Items / Inventory / Pockets | `src/item*`、`src/inventory*`、`src/item_pocket*` | JSON item type、crafting、vehicle |
| Creatures / Monsters | `src/creature*`、`src/monster*` | monster JSON、effects、map |
| Map / Mapgen | `src/map*`、`src/mapgen*` | terrain/furniture、overmap、save |
| Overmap | `src/overmap*` | overmap terrain/special、mapgen |
| Vehicles | `src/vehicle*` | vehicle part JSON、map、activity |
| Crafting | `src/crafting*`、`src/recipe*` | item IDs、requirements、inventory |
| Mutation / Effects | `src/mutation*`、`src/effect*` | JSON factories、Character、EOC |
| Activities | `src/activity*`、`src/player_activity*` | actors、Character、serialization |
| UI / Input | `src/*ui*`、`src/input*` | SDL/curses、translation、platform |
| Save | `src/savegame*`、`src/save_snapshot*` | every serialized owner、migration |
| Mod loading | `src/mod_manager*`、`data/mods/` | dependencies、JSON load order |
| Lua bridge | `src/catalua*`、`data/lua/` | manifest、LuaLS、registrations |
| Localization | `lang/`、`src/translations*` | extraction、PO/MO、UI |
| Android | `android/` | Gradle、JNI/native build、SDL3 |

测试通常按行为而不是按源码目录一一对应。先用 `rg` 查找类型、注册名或稳定 ID，再在
`tests/` 中查找相同符号和用户可见行为。跨子系统修改应明确对象所有权、生命周期、
序列化和性能热点。
