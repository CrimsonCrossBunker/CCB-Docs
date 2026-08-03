---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.v5.capabilities
title: Capability 声明
language: zh_CN
status: draft
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
last_human_reviewer: Not yet reviewed (draft)
source_paths:
- data/lua/README.md
- data/lua/manifest.schema.json
- data/lua/types/ccb_api_v5.d.lua
- data/lua/reference/ccb_public_api_v5.json
- data/lua/reference/ccb_public_api_v5_coverage.json
- tools/lua_api/README.md
source_symbols:
- game.actions.dangerous
source_queries: []
source_fingerprint: 86ab8c697639288944692daea743e7470450d95825578f8964198c2bd0dbdc83
authority: api-contract
verified_commit: 501f84d20d4bf432dd7fec9b757f5af6a18dae36
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 7f006e3e9d2c5d2b02a4c2c83c46c8470ea1952d15614f277e23683c27e708e6
prerequisites:
- api.lua.v5.overview
depends_on:
- api.lua.v5.permissions
- api.lua.v5.reference.capabilities
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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/565
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/capabilities/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/capabilities/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/capabilities/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/capabilities/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/501f84d20d4bf432dd7fec9b757f5af6a18dae36
source_urls:
- path: data/lua/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/501f84d20d4bf432dd7fec9b757f5af6a18dae36/data/lua/README.md
- path: data/lua/manifest.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/501f84d20d4bf432dd7fec9b757f5af6a18dae36/data/lua/manifest.schema.json
- path: data/lua/types/ccb_api_v5.d.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/501f84d20d4bf432dd7fec9b757f5af6a18dae36/data/lua/types/ccb_api_v5.d.lua
- path: data/lua/reference/ccb_public_api_v5.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/501f84d20d4bf432dd7fec9b757f5af6a18dae36/data/lua/reference/ccb_public_api_v5.json
- path: data/lua/reference/ccb_public_api_v5_coverage.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/501f84d20d4bf432dd7fec9b757f5af6a18dae36/data/lua/reference/ccb_public_api_v5_coverage.json
- path: tools/lua_api/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/501f84d20d4bf432dd7fec9b757f5af6a18dae36/tools/lua_api/README.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28api.lua.v5.capabilities%29%3A+&body=Document+ID%3A+api.lua.v5.capabilities%0ALanguage%3A+zh_CN%0AVerified+commit%3A+501f84d20d4bf432dd7fec9b757f5af6a18dae36%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Capability 声明

每个 Lua 来源通过 `lua/manifest.json` 请求最小权限集合。未声明 capability 的调用会失败；
Callback、Hook、事件、模块或页面替换都不会借用另一个来源的权限。

## v5 Manifest 最小骨架

```json
{
  "$schema": "https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/raw/master/data/lua/manifest.schema.json",
  "id": "my_mod",
  "version": "1.0.0",
  "api_version": 5,
  "capabilities": ["events", "game.read", "ui.pages"],
  "dependencies": []
}
```

Mod 的 Manifest `id` 必须等于 Mod id。新代码应使用 API 5，并只声明真实调用所需项。

## 完整 capability 表

| Capability | 最低 API | 作用 |
| --- | ---: | --- |
| `events` | 2 | 自定义、生命周期与原生事件表面 |
| `game.actions` | 2 | 安全的游戏动作队列/当前输入动作 |
| `game.actions.dangerous` | 4 | 危险命名动作（仍需本地确认） |
| `game.callbacks` | 5 | JSON 定义 Callback Actor |
| `game.hooks` | 5 | 原生 Hook |
| `game.read` | 2 | 游戏快照、定义和查询 |
| `game.write` | 5 | 受校验的游戏写操作 |
| `modules.import` | 4 | 导入已声明依赖的源码模块 |
| `registry.read` | 4 | 分离的定义注册表查询 |
| `scheduler` | 4 | 确定性 turn 调度 |
| `services.consume` | 4 | 调用依赖提供的服务 |
| `services.provide` | 4 | 发布版本化服务 |
| `state.character` | 2 | 角色级持久状态 |
| `state.page` | 2 | 页面会话状态 |
| `state.world` | 2 | 世界级持久状态 |
| `ui.pages` | 2 | 注册和导航跨平台页面 |

## 依赖约束

- `game.actions.dangerous` → `game.actions`
- `game.write` → `game.read`
- `game.hooks` → `events`
- `game.callbacks` → `game.read`

Schema 会拒绝未知项、重复项、API 版本过低或缺少上述依赖的 Manifest。精确 Schema 和
来源见[生成 Capability 参考](reference/capabilities.md)与
[Manifest 字段](reference/manifest-fields.md)。
