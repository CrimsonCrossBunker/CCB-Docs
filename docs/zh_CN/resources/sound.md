---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: resources.sound
title: Sound 与 soundpack
language: zh_CN
status: draft
doc_type: reference
audiences:
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
- doc/SOUNDPACKS.md
- src/sound_backend.h
- src/sdlsound.h
- src/sounds.h
- tests/sound_backend_test.cpp
source_symbols:
- namespace sounds
source_queries:
- soundpack
source_fingerprint: 9f1e5ea8a80d6091a01ff14d6ff874263d556de42bc5ea84ea11c76fda51ef24
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 42715b3663d7e72ab93813b14b8d1d37b2126d3889b073c471ed6d67477145c0
prerequisites:
- platforms.ui
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
- json-load
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: resources-sound
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/resources/sound/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/resources/sound/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/resources/sound/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/resources/sound/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/dbaedf8357408ae6f96309732d6e087e9b878e18
source_urls:
- path: doc/SOUNDPACKS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/doc/SOUNDPACKS.md
- path: src/sound_backend.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/sound_backend.h
- path: src/sdlsound.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/sdlsound.h
- path: src/sounds.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/sounds.h
- path: tests/sound_backend_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/tests/sound_backend_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28resources.sound%29%3A+&body=Document+ID%3A+resources.sound%0ALanguage%3A+zh_CN%0AVerified+commit%3A+dbaedf8357408ae6f96309732d6e087e9b878e18%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Sound 与 soundpack

CCB 区分玩法 sound event 与音频 sample playback。`sounds` namespace 记录用于 hearing、AI
与 marker 的 simulation event；`sfx`/backend 把 ID/variant 映射到 file、playlist、channel、
attenuation 与 SDL playback。

## 权威路径

- `src/sounds.*` 定义玩法 sound category 与 event processing；
- `src/sound_backend.h` 和 SDL2/SDL3 backend 实现定义 device/sample 行为；
- `src/sdlsound.*` 协调初始化、soundset load、music 与 shutdown；
- `doc/SOUNDPACKS.md` 解释 pack metadata/JSON，`data/sound/Menu_Sound_Test/` 是小型 checked
  example/fixture。

## ID、variant 与所有权

code/data 发出稳定 sound ID、variant 与 context，soundpack 将其映射到有许可证音频。即使
关闭 `SOUND` 或 device init 失败，玩法 event 仍须工作；audio playback 不能成为 simulation
权威。

## 贡献流程

每个 sample 记录原始 source、creator、license、edit、loop 状态、format 与 attribution。
normalize 只能使用已记录流程。更新 mapping/fallback variant，绝不硬编码本地绝对路径。

## 验证

验证 soundpack JSON/引用 file、exact/fallback variant、playlist、loop/fade、channel/group、
indoor/night/season、angle/volume、missing sample diagnostic、device init failure、SDL2/SDL3
与 no-sound build；适用时运行 sound backend test。

## 性能与打包

preload policy、decoded sample size、同时 channel 数和重复 variant resolution 影响内存/
frame time。只打包可分发 asset 并保持大小写路径。大型第三方 soundpack 除非政策/license
明确允许，应独立分发。

## CCB 边界

CCB 可能与上游共享历史 ID，但当前发出的 context 与 bundled mapping 才是契约。移植要
按 CCB event 验证，不能假设上游 soundpack 已完整覆盖。
