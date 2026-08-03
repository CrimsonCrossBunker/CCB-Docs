---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: compatibility.mods
title: Mod 兼容
language: zh_CN
status: active
doc_type: explanation
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
last_human_reviewer: LYHGLYTX
source_paths:
- CONTRIBUTING.md
- doc/MOD_COMPATIBILITY.md
- src/mod_manager.cpp
- src/worldfactory.cpp
- tests/worldfactory_test.cpp
source_symbols: []
source_queries: []
source_fingerprint: a3359e19ec5de3957becfbf9495cc25aeaeac01a15c37e3dc816578f476103d1
authority: source-and-tests
verified_commit: 2c899a3db790e11a6ff44d91f319064b1ee65d2a
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: cdc0443d43962c6fa7df2cf31aed0552423177b56a0132432e40c272a494f66a
prerequisites:
- architecture.overview
depends_on:
- compatibility.save
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- json-load
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: compatibility
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/560
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/compatibility/mods/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/compatibility/mods/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/compatibility/mods/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/compatibility/mods/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/2c899a3db790e11a6ff44d91f319064b1ee65d2a
source_urls:
- path: CONTRIBUTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/CONTRIBUTING.md
- path: doc/MOD_COMPATIBILITY.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/doc/MOD_COMPATIBILITY.md
- path: src/mod_manager.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/src/mod_manager.cpp
- path: src/worldfactory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/src/worldfactory.cpp
- path: tests/worldfactory_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/tests/worldfactory_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28compatibility.mods%29%3A+&body=Document+ID%3A+compatibility.mods%0ALanguage%3A+zh_CN%0AVerified+commit%3A+2c899a3db790e11a6ff44d91f319064b1ee65d2a%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Mod 兼容

Mod 兼容包含标识符、依赖、加载顺序、可选交互、存档数据和公共脚本契约，不只是
“JSON 能解析一次”。

## 稳定边界

- 已发布 type/object ID 应保持稳定，否则提供受支持的 migration/obsoletion 数据。
- 在 Mod 元数据中声明依赖，不依赖文件名字母顺序或另一个 Mod 偶然存在。
- 针对另一已加载 Mod 的条件内容放在
  `mod_interactions/<other-mod-id>/`。交互内容在普通内容之后加载；目录 ID 区分
  大小写，verified 实现不支持嵌套的多 Mod 组合。
- EOC talker、变量和 context 属于行为契约。
- Lua manifest 版本、capability、permission 与公开 v5 符号属于 API 契约。

## 验证

先用声明的依赖单独加载 Mod，再测试每个受支持交互组合。创建世界、执行变更内容、
保存、重载并检查第一个 loader error。完整示例 Mod 应由 CI 加载，不能只逐个解析
孤立 JSON 文件。

兼容性结论必须注明 CCB commit、Mod 版本、依赖集合与平台。注册、数据和 Lua 表面
可能分歧，因此上游兼容不自动等于 CCB 兼容。
