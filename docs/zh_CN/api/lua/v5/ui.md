---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.v5.ui
title: 跨平台 Lua UI
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
- ctx:environment()
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
translation_source_fingerprint: 782c93e819b86b219cd3df29162a540afad030ae56da6d60f6d4bb207357f970
prerequisites:
- api.lua.v5.lifecycle
- api.lua.v5.capabilities
depends_on:
- api.lua.v5.reference.classes
- api.lua.v5.reference.methods
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/ui/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/ui/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/ui/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/ui/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28api.lua.v5.ui%29%3A+&body=Document+ID%3A+api.lua.v5.ui%0ALanguage%3A+zh_CN%0AVerified+commit%3A+501f84d20d4bf432dd7fec9b757f5af6a18dae36%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 跨平台 Lua UI

`ui.page` 注册语义页面，不注册像素位置。一个页面实现由 Android/桌面 Tiles 的 ImGui
host 或终端 ImTui fallback 渲染；Mod 不应导入渲染后端。

## 页面与 slot

descriptor 形式可声明 `title`、`category`、`order` 与以下 slot：

- `main.extensions`
- `ingame.extensions`
- `settings.mods`
- `debug.tools`

字符串标题形式保留兼容性，默认进入主菜单和游戏内 Extensions。稳定页面 id 可在热重载
后保留选择；`ui.open`、`ui.back`、`ui.close` 的导航请求在回调返回后处理。

```lua
ui.page("my_mod.settings", {
    title = i18n.gettext("My Mod"),
    category = "settings",
    order = 50,
    slots = { "main.extensions", "ingame.extensions", "settings.mods" },
}, function(ctx)
    ctx:heading(i18n.gettext("Settings"))
    local env = ctx:environment()
    ctx:text(env.profile .. " / " .. env.input)
end)
```

## `ctx` 生命周期与稳定 id

`ctx` 只在当前 draw 回调中有效，不得保存到全局、闭包、事件或调度任务。持久数据放入
合适的 `state` scope。翻译标签、动态标签和重复控件必须用 `_id` 形式，把稳定 id 与
显示文字分开。

`ctx:environment()` 提供 profile、input、density、breakpoint、touch、hover 和键盘导航
能力。布局应根据这些语义信息降级，不要用旧 `ctx:platform()` 判断触摸/桌面。

## 大列表与每帧成本

页面回调可能每帧运行。使用有界查询，只渲染需要的字段；大列表使用 `virtual_list`/
`virtual_list_rows`，缓存仅依赖 `language_revision()`、registry revision 等明确代次的数据。

## 与原生 HUD/sidebar 的边界

Lua 没有 `ui.hud`。Android schema-6 HUD 是独立的 Java/原生扩展面，不调用 Lua。
API v5 的 `sidebar` widget 只挂载到 PC 原生 Widget sidebar。跨平台信息入口应使用
`ui.page`。完整控件、类和方法见[类](reference/classes.md)与[方法](reference/methods.md)。
