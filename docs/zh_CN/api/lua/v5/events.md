---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.v5.events
title: 事件、Hook 与 Callback
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
- game.native_events
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
translation_source_fingerprint: c5889f704d092b0f46fdbdd8d00c81ebf6e80985b50a1fcb935f1a4814f2ca12
prerequisites:
- api.lua.v5.lifecycle
depends_on:
- api.lua.v5.reference.events
- api.lua.v5.reference.hooks
- api.lua.v5.reference.callbacks
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/events/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/events/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/events/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/events/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28api.lua.v5.events%29%3A+&body=Document+ID%3A+api.lua.v5.events%0ALanguage%3A+zh_CN%0AVerified+commit%3A+501f84d20d4bf432dd7fec9b757f5af6a18dae36%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 事件、Hook 与 Callback

Lua v5 有四种容易混淆的通知/扩展面。先按所有权和调用方向选择，再查生成契约。

| 表面 | 注册入口 | 用途 | 返回值是否影响原生流程 |
| --- | --- | --- | --- |
| 自定义/生命周期事件 | `events.on` | 来源内消息和 CCB 生命周期 | 返回 `false` 可停止本次传播 |
| 原生事件总线 | `game.native_events.on` | 113 种带 Schema 的游戏事件 | 观察；发送另有严格入口 |
| 原生 Hook | `game.hooks.on` | 52 个明确原生边界 | intercept Hook 可返回声明字段 |
| 定义 Callback | `game.callbacks.register` | 为 11 类 JSON 定义附加方法 | decision/consuming 由方法契约决定 |

## 自定义事件

普通事件名默认只在来源内可见。观察依赖来源要先声明依赖，再使用 `events.on_from`。
payload 只接受受限的字符串键和复制的标量值；不要用事件传递表、函数、userdata 或句柄。

```lua
events.on("quest_updated", function(event)
    game.add_msg(event.data.quest_id .. ":" .. tostring(event.data.stage))
end)
events.emit("quest_updated", { quest_id = "intro", stage = 2 })
```

## 原生事件

用 `game.native_events.list()`/`describe(name)` 发现名称和字段，而不是猜字段。订阅 payload
含事件类型、turn 和类型化字段。`emit` 只允许在活跃回调内使用，并要求精确字段集合、
正确 Lua 类型及 `events` + `game.read` + `game.write`。

## Hook

Hook 描述含 mode、payload、returns 和 capability。observe Hook 忽略返回值；intercept Hook
只接受声明的结果字段。优先级高者先执行，同优先级保持注册顺序。错误或超预算处理器只
禁用自身。

## Callback Actor

支持 `iuse`、`iwieldable`、`iwearable`、`iequippable`、`istate`、`imelee`、`iranged`、
`bionic`、`mutation`、`trap` 和 `monster`。注册与目标 id、来源和热重载事务绑定；原生
C++ 回调 Lua 时会恢复注册来源的权限身份。

完整名称、字段、decision/consuming 标志和来源见[原生事件](reference/events.md)、
[Hook](reference/hooks.md)与[Callback](reference/callbacks.md)。
