---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.v5.lifecycle
title: Lua 来源与生命周期
language: zh_CN
status: active
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
- ccb.lifecycle.reload
source_queries: []
source_fingerprint: 30a19e6cbd8c6709ac5ccda80fe349e9459ddaccd8d3dc96507ee282c17f48cb
authority: api-contract
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: ac95dbf6b61cdeb4e9f921e901cce7c75c662e5162301423b88843b2b1176b0b
prerequisites:
- api.lua.v5.overview
depends_on:
- api.lua.v5.capabilities
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
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/lifecycle/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/lifecycle/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/lifecycle/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/lifecycle/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28api.lua.v5.lifecycle%29%3A+&body=Document+ID%3A+api.lua.v5.lifecycle%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Lua 来源与生命周期

## 加载事务

运行时按以下顺序加载入口：内置 `data/lua/main.lua`、启用 Mod 的 `lua/main.lua`
（按 Mod 顺序）、最后是 `config/lua/main.lua`。每个来源拥有独立环境、Manifest 身份、
capability 集合和模块缓存。

热重载先创建候选 Lua state。全部入口成功后才整体替换当前运行时；任一入口失败都会
丢弃候选状态并保留旧状态。注册的页面、事件、任务、Hook 和 Callback 因此不会留下
“加载一半”的组合。

## 模块边界

- `require("foo.bar")` 在 API v4/v5 中只搜索调用来源的根目录。
- `modules.import(provider_id, "foo.bar")` 只允许 `builtin`、当前来源或 Manifest 中更早
  加载的依赖。
- 跨 Mod 保留提供者权限身份时使用版本化 `services`，不要把源码当服务导入。
- 绝对路径、目录穿越、动态库和任意文件加载不可用。

## 生命周期信号

| 名称 | 时机 |
| --- | --- |
| `ccb.lifecycle.reload` | 新候选运行时成功提交后 |
| `ccb.lifecycle.world_ready` | 新游戏或存档运行时加载完成后 |
| `ccb.lifecycle.before_save` | 写 Lua sidecar 前 |
| `ccb.lifecycle.after_save` | 保存结束，payload 含 `success`/`error` |
| `ccb.lifecycle.shutdown` | 世界或运行时被释放前 |

生命周期事件通过 `events.on` 订阅。原生生命周期 Hook 则通过 `game.hooks`，两者名称、
payload 和返回约束不同，必须查各自的[生成参考](reference/hooks.md)。

## 状态与代次

- `state.character`：按来源和角色隔离，随存档持久化。
- `state.world`：按来源隔离，在当前世界的角色间共享并持久化。
- `state.page`：按来源和页面隔离，仅当前世界运行会话；只能在页面 draw 回调中访问。
- 普通 Lua 全局/局部变量：成功重载后被替换。

`GameHandle`、任务 id、订阅 id 和 Callback 注册都由创建来源拥有。世界切换或成功重载
会改变代次；长期保存句柄前应调用 `is_valid()`/`status()`，不要保存 `ctx`。页面 `ctx`
只在当前 draw 回调内有效。

## 安全的初始化形态

入口只声明模块、服务和注册项；需要读取或修改实时游戏状态的工作应放入明确的页面、
事件、调度器、Hook 或 Callback 回调。许多交互/写操作会拒绝顶层加载阶段调用。
