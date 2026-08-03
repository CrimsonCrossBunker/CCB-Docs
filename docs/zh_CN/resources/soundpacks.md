---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: soundpacks
title: 旧文档迁移草稿：soundpacks
language: zh_CN
status: draft
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
last_human_reviewer: Pending human review
source_paths:
- doc/SOUNDPACKS.md
- src/sdlsound.cpp
- src/sdlsound.h
source_symbols:
- load_soundset
- sfx::load_sound_effects
- sfx::load_playlist
source_queries: []
source_fingerprint: 0246b49b05f9e86197e17d62765a99f0194dc121017d1108d02e49e787ffa0ab
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: f0dd83e89a759e2e3948783e6dc04f8cdf50ec15ea47834bda84b38f637cb1e4
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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/resources/soundpacks/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/resources/soundpacks/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/resources/soundpacks/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/resources/soundpacks/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/SOUNDPACKS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/SOUNDPACKS.md
- path: src/sdlsound.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/sdlsound.cpp
- path: src/sdlsound.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/sdlsound.h
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28soundpacks%29%3A+&body=Document+ID%3A+soundpacks%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：soundpacks

本页是 `soundpacks` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `soundpacks`
- Target: `resources/soundpacks.md`
- Replacement: soundpacks
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| soundpacks | doc/SOUNDPACKS.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## Soundpack 契约

Soundpack 是 `data/sound/` 下带 `soundpack.txt` 的目录；`NAME` 是 option 使用的唯一 ID，
`VIEW` 是显示名。`load_soundset` 解析当前选择，找不到时回退到 `basic`，再通过
`DynamicDataLoader` 加载目录内 JSON。音频功能未成功初始化时 sound JSON loader 会提前返回。

### SFX 与 playlist

`sound_effect` 要求 `id` 和 `files`，`volume` 默认 100；`variant` 可为字符串或数组，省略时为
`default`。`season`、`is_indoors`、`is_night` 进入查找 key。多个 file 是同一 key 的随机候选，
路径相对于 soundpack。实际 fallback 由 `sfx_resources` 查找实现；某些调用点会要求 exact
variant，因此不能假定每个 ID 都回退到 `default`。

`sound_effect_preload` 只预热列出的 key，不改变播放契约。`playlist` 包含 `playlists` 数组，每项
有 ID、可选 shuffle 和 `{file, volume}` 列表；同 ID 后加载的定义会替换 map entry。音乐 ID 的
激活和优先级由当前 `music` 调用代码决定，旧文档中的四项列表不是保证完整的 registry。

### 清点与验证

SFX 的 ID/variant 没有一份永远完整的手工清单：从所有 `play_variant_sound`、ambient、vehicle、
UI 和 music 调用点生成清单，并和 soundpack JSON 比对。检查缺失文件、解码格式、空列表、重复
key、exact/default fallback、季节/室内/昼夜组合、preload、shuffle、音量叠乘、loop/channel、
距离/pan/pitch、切换 pack 和禁用声音。发布音频还必须记录作者、来源和兼容许可证；不要把测试
模式或无音频 backend 的“成功加载”当成真实播放验证。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `0246b49b05f9e86197e17d62765a99f0194dc121017d1108d02e49e787ffa0ab`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/SOUNDPACKS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/SOUNDPACKS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/SOUNDPACKS.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
