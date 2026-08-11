---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.platform-v1.overview
title: Lua-first Platform v1 API 概览
language: zh_CN
status: active
doc_type: reference
audiences:
- new-contributor
- experienced-contributor
- maintainer
- mod-author
- api-user
owners:
- CCB Lua API maintainers
reviewers:
- Documentation reviewers
- Lua API reviewers
review_interval_days: 60
last_human_reviewer: LYHGLYTX
source_paths:
- data/lua/types/ccb_platform_v1.d.lua
- data/lua/LUA_FIRST_PLATFORM.md
- ai/lua-first-roadmap.yml
- ai/lua-first-replacement-ledger.yml
- data/mods/Lua_First_Example/mod.lua
- data/mods/Lua_First_Example/main.lua
- data/mods/Lua_First_Example/content/cleanwater_charm.lua
- data/mods/Lua_First_Example/runtime/behaviour.lua
- tools/create_lua_mod.py
- tools/migrate_lua_first.py
source_symbols:
- CcbPlatformV1
- ModDefinition
- CcbPlatformContent
- CcbPlatformRuntime
- CcbPlatformTasks
- CcbPlatformServices
source_queries: []
source_fingerprint: 145df35fb96e317cd11ab1619fa43b3ea8eb7f94373f96c3aa32dcec7264f3da
authority: api-contract
verified_commit: c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd
verified_at: '2026-08-12'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 5de362515587d913a379f8a74fd93034e91e329ccec7215338767b05b5efcacc
prerequisites:
- architecture.lua-first-platform
depends_on:
- architecture.lua-first-roadmap
- api.lua.v5.overview
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; LuaLS declarations, native registrations, tests, and the replacement ledger
  remain authoritative.
example_validation_ids:
- agent-context
- lua-contract
api_version: platform-v1
deprecated: false
deprecation_replacement: null
risk_group: lua-platform
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/platform-v1/overview/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/platform-v1/overview/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/platform-v1/overview/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/platform-v1/overview/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd
source_urls:
- path: data/lua/types/ccb_platform_v1.d.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/data/lua/types/ccb_platform_v1.d.lua
- path: data/lua/LUA_FIRST_PLATFORM.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/data/lua/LUA_FIRST_PLATFORM.md
- path: ai/lua-first-roadmap.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/ai/lua-first-roadmap.yml
- path: ai/lua-first-replacement-ledger.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/ai/lua-first-replacement-ledger.yml
- path: data/mods/Lua_First_Example/mod.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/data/mods/Lua_First_Example/mod.lua
- path: data/mods/Lua_First_Example/main.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/data/mods/Lua_First_Example/main.lua
- path: data/mods/Lua_First_Example/content/cleanwater_charm.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/data/mods/Lua_First_Example/content/cleanwater_charm.lua
- path: data/mods/Lua_First_Example/runtime/behaviour.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/data/mods/Lua_First_Example/runtime/behaviour.lua
- path: tools/create_lua_mod.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/tools/create_lua_mod.py
- path: tools/migrate_lua_first.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/tools/migrate_lua_first.py
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28api.lua.platform-v1.overview%29%3A+&body=Document+ID%3A+api.lua.platform-v1.overview%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Lua-first Platform v1 API 概览

Lua-first Platform v1 是与 Lua API v5 分开版本化的原生创作表面。它已经能运行纯 Lua
纵向样板，但仍处于增量实现阶段；当前发布合同的总称仍是 Lua API v5。精确签名以
`data/lua/types/ccb_platform_v1.d.lua`、原生注册和测试为准。

严格替代账本目前有 775 项：0 项达到完整 selector 等价，119 项只有明确边界内的实现，
440 项只有可组合原语，198 项仍在计划中，18 项经审查无需替代。因此本页说明“现在能
写什么”，不表示 JSON/EOC 已可删除。

## 最小 Mod 与元数据

最小目录只需要根 `main.lua`：

```text
my_mod/
└── main.lua
```

目录名提供默认 ID 和显示名；不要求 `lua/` 子目录、`manifest.json` 或
`modinfo.json`。需要稳定元数据或依赖时，可选的根 `mod.lua` 返回原生
`ccb.ModDefinition`：

```lua
local ccb = require("ccb")

return ccb.ModDefinition {
    id = "my_mod",
    name = "My Lua Mod",
    version = "0.1.0",
    dependencies = { "dda" },
    entry = "main.lua",
}
```

`id`、`name`、`version`、`entry`、`dependencies` 和 `core` 都有长度、类型与路径边界。
本地 `require` 从 Mod 根目录解析 `?.lua` 与 `?/init.lua`；入口不能逃出 Mod 根目录。
每个 Platform Mod 使用独立 Lua 5.4 state，并按可信本机扩展对待。

## `ccb` 根表

| 成员 | 用途 |
| --- | --- |
| `platform_version` | 固定为 `1`，用于显式版本判断 |
| `ModDefinition` | 构造可选原生 Mod 元数据 |
| `content` | 在全局 finalize 前创建、替换或编辑原生 definition |
| `runtime` | 注册命名 handler、事件、Hook 与任务 payload 迁移 |
| `state` | 角色级和世界级可序列化状态 |
| `tasks` | 命名、可保存的延迟任务 |
| `presentation` | 通知、确认、稳定 ID 选择和文本输入 |
| `services` | 49 个游戏领域服务及少量 Platform 专用精确操作 |

## 原生内容事务

`ccb.content` 提供原生构造器以及 `add`、`replace`、`edit`。definition 先进入当前 Mod 的
staging 区，成功后统一提交和 finalize；失败会逆序回滚。重复 ID 默认报错，静态内容
改变要求完整数据重载，运行时-only 变化才允许热替换。

下面是已随游戏交付的物品与配方写法：

```lua
local charm = ccb.content.Item {
    id = "my_cleanwater_charm",
    name = "clean-water charm",
    description = "A native Lua-authored item.",
    symbol = "*",
}
charm:mass_grams(20)
charm:volume_ml(10)
charm:material("steel", 1)
charm:on_use("use_cleanwater_charm", "Listen to the charm")
ccb.content.add(charm)

local recipe = ccb.content.Recipe {
    id = "my_cleanwater_charm",
    result = "my_cleanwater_charm",
    category = "CC_OTHER",
    subcategory = "CSC_OTHER_OTHER",
    skill = "fabrication",
    difficulty = 1,
    duration_moves = 500,
    autolearn = true,
}
recipe:component_any {
    { id = "scrap", count = 1 },
    { id = "steel_chunk", count = 1 },
}
ccb.content.add(recipe)
```

声明文件还列出已绑定的 requirement、proficiency、怪物、身体图、伤口、效果、字段、
载具辅助目录、天气、活动、帮助、播放列表等构造器。每个构造器只承诺声明中列出的字段
与方法；存在同名构造器不等于旧 JSON 类型的每个合法形状都已等价。

## Handler、事件与 Hook

行为先用稳定 ID 定义，再由内容、event 或 Hook 引用：

```lua
ccb.runtime.handler("use_cleanwater_charm", function(context)
    context:message("The charm hums.")
    return 0
end, 1)

ccb.runtime.handler("my_world_ready", function(event)
    if event.new_game then
        ccb.services.message("Lua-first Mod ready")
    end
end, 1)

ccb.runtime.on("world_ready", "my_world_ready")
```

`on` 接受 `world_ready`、`before_save`、`after_save`、`shutdown` 与
`game:<native-event>`。原生事件把角色放在 `actors.character`、`actors.attacker`、
`actors.killer`、`actors.victim` 等语义字段中，不公开 EOC 的 alpha/beta 别名。
`hook` 是同步决策点，handler 的返回值会按对应 Hook 合并规则处理；它不是事后事件。

## Typed handle 与生命周期

`GameHandle` 以及任务、群体、区域等 token 都绑定到精确的 Mod runtime owner、runtime
generation、world generation 和原生对象生命期。来自另一个 Mod、旧热重载或旧世界的
handle 会被拒绝。`ItemUseContext` 在回调结束时失效。

不要把 live handle、闭包、协程栈或 userdata 写入持久数据。跨存档只保存稳定 ID、
标量和重新解析对象所需的数据。多数领域服务返回 `CcbResult`；先检查 `ok`，再读取
`value`，并把 `error.code`/`error.message` 作为有界失败处理。

## 持久状态与命名任务

状态只接受 `boolean`、`integer`、有限 `number`、`string` 或 `nil`：

```lua
local uses = ccb.state.character.get("charm_uses", 0) + 1
ccb.state.character.set("charm_uses", uses)

if not ccb.state.world.get("initialized", false) then
    ccb.state.world.set("initialized", true)
    ccb.tasks.after(10, "my_reminder", { text = "Still here" }, 1, "world")
end
```

任务存储 handler ID、到期回合、owner、payload 和 payload version，而不是函数本身。
`ccb.runtime.migrate_task_payload` 可注册逐版本迁移；缺失 handler、孤儿 owner、损坏数据
和过期任务都有受测的保留、诊断或一次性执行规则。`ccb.tasks.cancel(id)` 只取消当前
Mod 拥有的任务。

## Presentation 与领域服务

`ccb.presentation.notice`、`confirm`、`choose`、`input_text` 是 callback-only 的原生
交互原语。`choose` 返回稳定 entry ID，不返回易变的显示序号。桌面和 Android 的真实
交互体验仍需要持续人工验证。

`ccb.services` 复用 v5 的类型化查询/操作，并增加 Platform 专用能力，例如：

| 领域 | 代表能力 |
| --- | --- |
| `inventory` | 精确读取物理持有物，不用分页扫描猜测 |
| `activities` | activity snapshot、普通定时 activity、原生取消 |
| `wounds` | 精确身体部位的伤口 snapshot/add/remove |
| `bionics` | 安装数与能量容量摘要、grant/remove |
| `recipes` | 已学配方的 knows/learn/forget/category forget |
| `martial_arts` | 与 presentation 解耦的 learn/forget |
| `morale` | 类型化 morale add/remove |
| `random` | 每 Mod 确定性随机流、概率、抽样与对抗检定 |
| `gameplay` | 字符串谓词、活动 Mod、维度、室外与视线查询 |

其他服务入口包括角色、生物、物品、载具、任务、区域、魔法、地图、天气、需求、技能、
熟练度、阵营、营地、声音、变量和序列化。它们是可组合原语，不是 275+310 个 EOC 键
的同名包装。

## 模板、迁移与可玩样板

创建新 Mod：

```sh
python3 tools/create_lua_mod.py --template minimal /path/to/MyMod
python3 tools/create_lua_mod.py --template complete /path/to/MyMod
```

迁移器只输出原生 Lua 骨架与显式 TODO，不生成 JSON loader、EOC runner 或原始旧对象：

```sh
python3 tools/migrate_lua_first.py old.json --output /tmp/MyMigratedMod --mod-id my_mod
python3 tools/migrate_lua_first.py old.json --output /tmp/MyMigratedMod --check
```

`data/mods/Lua_First_Example/` 是零 JSON、EOC、manifest 和强制 `lua/` 目录的捆绑样板。
`[playable_mvp]` 门禁通过真实 Mod 选择、数据加载、物品使用、游戏存档、runtime 销毁、
完整数据重载、继续游戏以及过期任务恰好执行一次。

## 当前边界

- Platform 的 11 个路线图能力目前全部仍是 `partial`；不要把局部可用写成完整替代。
- 完整地图栈、载具定义、NPC/职业/场景/阵营、具体 mutation、bionic、武术、魔法、
  对话、任务定义等大域仍有计划项。
- 事件 actor、借用引用、复杂 activity、NPC 导航/传送、战斗伤害、湿润和复杂表单仍需
  扩展或验证。
- 旧 JSON/EOC 在覆盖、迁移和至少两个稳定版本且满十二个月的弃用窗口完成前不能移除。

架构理由见 [Platform v1 架构](../../../architecture/lua-first-platform.md)，准确进度见
[路线图](../../../architecture/lua-first-roadmap.md)，术语见
[词汇表](../../../architecture/lua-first-glossary.md)。
