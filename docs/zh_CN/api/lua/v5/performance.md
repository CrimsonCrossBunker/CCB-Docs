---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.v5.performance
title: Lua 性能与资源边界
language: zh_CN
status: stale
doc_type: explanation
audiences:
- mod-author
- api-user
- experienced-contributor
- maintainer
owners:
- CCB Lua API maintainers
reviewers:
- Documentation reviewers
- Lua API reviewers
review_interval_days: 60
last_human_reviewer: LYHGLYTX
source_paths:
- data/lua/README.md
- data/lua/manifest.schema.json
- data/lua/types/ccb_api_v5.d.lua
- data/lua/reference/ccb_public_api_v5.json
- data/lua/reference/ccb_public_api_v5_coverage.json
- tools/lua_api/README.md
source_symbols:
- callback_time_total_us
source_queries: []
source_fingerprint: 30a19e6cbd8c6709ac5ccda80fe349e9459ddaccd8d3dc96507ee282c17f48cb
authority: api-contract
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 8eac9b8b799105af96a709f068d936b1590c6986f0c735b31d9fa53323d4e233
prerequisites:
- api.lua.v5.ui
- api.lua.v5.lifecycle
depends_on:
- api.lua.v5.debugging
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; generated contract and source paths at the verified commit.
example_validation_ids: []
api_version: '5'
deprecated: false
deprecation_replacement: null
risk_group: lua-api
risk_level: high
pending_source_pr: null
stale_reason: 'Source paths changed after d32b9cc880a8: data/lua/README.md, data/lua/manifest.schema.json,
  data/lua/reference/ccb_public_api_v5.json, …'
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/performance/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/performance/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/performance/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/performance/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: data/lua/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/README.md
- path: data/lua/manifest.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/manifest.schema.json
- path: data/lua/types/ccb_api_v5.d.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/types/ccb_api_v5.d.lua
- path: data/lua/reference/ccb_public_api_v5.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/reference/ccb_public_api_v5.json
- path: data/lua/reference/ccb_public_api_v5_coverage.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/reference/ccb_public_api_v5_coverage.json
- path: tools/lua_api/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tools/lua_api/README.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28api.lua.v5.performance%29%3A+&body=Document+ID%3A+api.lua.v5.performance%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Lua 性能与资源边界

Lua 页面可能每帧调用，事件和 Hook 可能位于高频路径。API 的有界结果不是建议值，而是
保护运行时和游戏线程的契约。

## 主要边界

- 每个 runtime 有 32 MiB Lua 内存上限。
- 入口与页面、事件、scheduler、service、Hook、Callback 都有指令预算。
- 超预算或报错的回调独立禁用/移除；不能用 `pcall`/`xpcall` 吞掉预算终止。
- registry、inventory、creature、map、事件 payload、service 参数/结果和导航队列均有
  明确数量/字节/深度上限。
- scheduler 使用游戏 turn，不使用墙钟；到期回调数量和任务总数有界。

精确限制属于源契约；查看对应[函数](reference/functions.md)、[方法](reference/methods.md)
及 `data/lua/README.md`，不要把文档中的旧数字当成永久常量。

## 页面热路径

1. 每次查询都传入满足当前 UI 的最小 `limit`。
2. 长列表用 `virtual_list`/`virtual_list_rows`，只绘制可见半开区间。
3. 把翻译/定义标签缓存绑定到 `language_revision()` 或 registry revision。
4. 不在 draw 中反复注册页面、订阅、Hook、Callback、action-menu 或 sidebar。
5. 不在每帧创建大型表、序列化完整世界状态或扫描所有定义。
6. 用 `state.page` 保存编辑草稿，不保存 `ctx` 或实时对象。

## 测量

`game.runtime_status()` 中的 `callback_count`、`callback_time_total_us`、
`callback_time_max_us`、`slow_callback_count` 和 `last_slow_callback` 可用于定位累计成本。
先复现并记录回调/页面、数据规模、平台和固定 CCB commit，再优化查询次数与返回范围。

不要用关闭 capability 检查、扩大生成上限或缓存跨代次句柄作为“优化”。这会破坏安全与
兼容契约，而不是解决热路径。
