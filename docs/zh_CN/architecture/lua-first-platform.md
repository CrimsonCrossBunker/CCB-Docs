---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: architecture.lua-first-platform
title: Lua-first Platform v1 架构
language: zh_CN
status: draft
doc_type: explanation
audiences:
- new-contributor
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
- data/lua/LUA_FIRST_PLATFORM.md
- ai/lua-first-roadmap.yml
- data/lua/AGENTS.md
source_symbols: []
source_queries: []
source_fingerprint: cd39163eea0a8d2253dcf3fae5ad5149bcc8f11fcb1c2f50b45bbf98c101f299
authority: docs-explanation
verified_commit: b2bbec1a2f4f8e41a2fece924c7c43b426ff2dc6
verified_at: '2026-08-09'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 500f27f11d7326b0271dd34b50d92bb29fca14bc1fdd9d4fb444d447c353241a
prerequisites:
- architecture.overview
depends_on:
- api.lua.v5.overview
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- agent-context
- lua-contract
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: lua-platform
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/615
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/lua-first-platform/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/lua-first-platform/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/architecture/lua-first-platform/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/lua-first-platform/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/b2bbec1a2f4f8e41a2fece924c7c43b426ff2dc6
source_urls:
- path: data/lua/LUA_FIRST_PLATFORM.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/b2bbec1a2f4f8e41a2fece924c7c43b426ff2dc6/data/lua/LUA_FIRST_PLATFORM.md
- path: ai/lua-first-roadmap.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/b2bbec1a2f4f8e41a2fece924c7c43b426ff2dc6/ai/lua-first-roadmap.yml
- path: data/lua/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/b2bbec1a2f4f8e41a2fece924c7c43b426ff2dc6/data/lua/AGENTS.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28architecture.lua-first-platform%29%3A+&body=Document+ID%3A+architecture.lua-first-platform%0ALanguage%3A+zh_CN%0AVerified+commit%3A+b2bbec1a2f4f8e41a2fece924c7c43b426ff2dc6%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Lua-first Platform v1

> 本页描述 CCB 已接受、但尚未完整实现的长期架构。当前可运行的脚本合同仍是
> [Lua API v5](../api/lua/v5/overview.md)。页面中的目标接口草图不是现有 API。

Lua-first Platform v1 的目标不是“让 Lua 调用 EOC”或“用 Lua 表格重写 JSON”，而是让
Lua 成为 CCB 核心内容与 Mod 的主要创作语言。作者最终应能只写 Lua 来定义元数据、
物品、配方、载具、怪物、地图生成、对话、任务、UI 和运行时行为。

## 三条最重要的结论

1. 最小 Mod 只有根目录 `main.lua`，不强制 `lua/` 子目录，也不要求作者维护
   `manifest.json` 或 `modinfo.json`。
2. Lua 使用原生对象、领域 service、普通控制流、模块、事件、Hook、命名任务与持久
   状态；公共接口不逐项复制 JSON 字段或 EOC 键。
3. Platform v1 是可信的进程内扩展系统。它计划开放完整 Lua 5.4 标准库、文件、进程
   和原生模块能力，因此安装来源必须像本机程序一样被信任。

## 当前合同与目标平台

| 问题 | 当前 Lua API v5 | 目标 Platform v1 |
| --- | --- | --- |
| 启动时机 | JSON finalize 后 | 静态内容 finalize 前开始，世界就绪后激活运行时 handler |
| Mod 发现 | manifest 与 capability 合同 | 根 `main.lua` 零配置发现，可选根 `mod.lua` |
| 静态内容 | 主要查询或控制已加载对象 | 创建、替换、事务编辑原生 definition |
| 行为 | 已公开的事件、Hook、回调与运行时域 | 原生方法、领域 service、类型化事件、同步 Hook、命名任务 |
| 安全模型 | capability 沙箱 | 完全可信，使用游戏进程权限 |
| 版本 | API v5 | 独立的 Platform v1，不是 v5 的改名 |

“当前 v5 有相似能力”不等于“Platform v1 已完成”。只有源码、测试、声明与路线图证据
一致时，某项 Platform 能力才能标为可用。

## 零配置 Mod

最小目录只有一个约定：Mod 根目录存在 `main.lua`。

```text
my_mod/
└── main.lua
```

引擎从目录名推导默认值：

- Mod ID 与显示名：目录名；
- 依赖：空；
- Platform 版本：1；
- 内容与运行时注册入口：`main.lua`。

`content/`、`runtime/`、`lib/`、`tests/` 都是作者自己的组织选择。完整模板可以推荐
这些目录，但 loader 不能要求它们存在。本地 `require` 默认从 Mod 根查找 `?.lua` 和
`?/init.lua`。

### 可选的 `mod.lua`

需要稳定 ID、显示名、版本、依赖、核心 Mod 标记或自定义入口时，作者可以增加根目录
`mod.lua`。它执行 Lua 并返回原生 `ccb.ModDefinition`，而不是返回一份 JSON 形状的
普通表。

```lua
-- 目标接口草图；名称和构造语法尚未成为可运行合同。
local ccb = require("ccb")

return ccb.ModDefinition {
    id = "my_stable_mod",
    name = "My Mod",
    version = "1.0.0",
    dependencies = { "dda" },
    entry = "main.lua",
}
```

入口必须留在 Mod 包根目录内。Mod 管理器在扫描已安装 Mod 时会执行 `mod.lua`，甚至
可能早于玩家启用它；因此 Mod UI 和发布文档必须醒目标注可信执行风险。

## 加载生命周期

目标加载序列是：

1. 发现根 `main.lua` 或可选 `mod.lua`；
2. 解析元数据、依赖与确定性加载顺序；
3. 开始一次数据加载事务；
4. 混合 Mod 如有旧 JSON，则先装载兼容内容；
5. 执行 Platform 入口，把原生 definition 放入 staging 区；
6. 提交 staging 内容并运行全局 finalize；
7. `world_ready` 后激活事件、Hook、handler 与 session task。

入口顶层可以定义静态内容和注册行为，但世界就绪前不能读取实时地图、玩家或世界。
事务失败时不能进入“加载了一半还能游玩”的状态。文件写入、启动进程等外部副作用不在
引擎事务内，无法回滚。

热重载先在候选 Lua state 执行入口。静态内容指纹未改变时，可以替换运行时注册；若
物品、配方等静态 definition 已变，结果应是 `requires_full_data_reload`，而不是原地
修改已经 finalize 的 registry。

## 原生对象，而不是 JSON 影子

Platform 导出的 C++ 类型公开所有可绑定的 `public` 字段、方法与运算符；它不会绕过
`private` 或 `protected`。导出从明确批准的类型根开始，JSON loader、EOC parser 等
旧实现不是默认导出根。

借用的原生引用携带 `owner + generation`：owner 被销毁、世界替换、内容重新提交或
runtime 替换后，旧引用访问应抛 Lua 错误，而不是解引用悬空指针。Mod 自己加载的原生
模块可以绕过此保护，因此不属于兼容保证。

静态 definition 是真实原生 staging 对象。目标内容层提供明确的 `add`、`replace` 和
事务性 `edit` 语义；重复 ID 默认报错。Lua 的构造函数、普通函数、循环、模块和组合
承担 JSON `copy-from` 以前的复用工作。

下面只展示编程模型，不锁定最终拼写：

```lua
-- 目标伪代码：当前版本不能运行。
local item = ItemDefinition("vibe_lamp")
item:name("氛围灯")
item:weight(350 * units.gram)

content.items:add(item)
content.recipes:add(make_lamp_recipe(item:id()))

handlers:define("use_vibe_lamp", function(context)
    context.user:add_morale(morale.vibe, 10)
end)
```

这里的重点是对象、函数、单位类型和组合，而不是把 JSON 的每个键变成
`item:set_json_field(...)`。

## 用 Lua 行为取代 EOC

Platform 只需要少量正交原语：

- 原生对象方法和领域 service：进行验证过的查询与修改；
- 普通 Lua 表达式：编写条件；
- 类型化 event：观察已经发生的事情；
- 同步 Hook：在决定发生前变换、否决或选择；
- 命名 handler：由 definition 引用的稳定行为；
- 命名持久 task：安排延迟或重复工作；
- 可序列化角色/世界 state：保存耐久数据；
- 普通 Lua 库：在这些原语上实现 workflow 与状态机。

迁移 EOC 时，应先追踪某个 condition/effect 背后的游戏操作，再把操作抽成 C++ 领域
service，让旧 EOC adapter 与 Lua binding 共用。禁止把 `run_eoc`、alpha/beta talker
别名、每个 EOC 键一个函数或另一套 recurrence DSL 当成 Platform 公共接口。

## 持久任务与存档

闭包、协程调用栈、userdata 和原生引用不能直接写入存档。持久任务只保存稳定数据：

```text
mod_id + handler_id + due + owner + payload + payload_version
```

读档时，新 Lua state 用 `handler_id` 重新找到函数。缺失 handler、无效 owner、过期
task 与 payload 版本变化必须产生有界诊断，并走明确的丢弃或迁移规则。协程仍适合
当前 session 的流程，但不跨越存档/读档。

“用 Lua 取代 JSON”只针对作者面对的内容合同。存档、设置、缓存、翻译产物和生成清单
仍可由引擎内部使用 JSON；把这些内部格式改成 Lua 不会增加 Mod 创作能力。

## 开发者扩展与模板

未来工具提供两种脚手架：

- `minimal`：只生成可执行的根 `main.lua`；
- `complete`：提供 `content/`、`runtime/`、`tests/` 等推荐结构和演示代码，但仍无 JSON，
  也不强制 `lua/` 目录。

脚手架不得覆盖非空目标目录，模板升级也不得改写作者文件。其他开发者可以用普通 Lua
模块发布库，在稳定 Platform 原语上建立更高层 DSL；这些库属于生态层，不应迫使引擎
把某一种 DSL 固化为核心接口。

## 首个纵向样板

首个实现样板固定为一个零 JSON/EOC Mod：定义物品、配方和 Lua 使用行为。它必须同时
验证发现、依赖顺序、原生内容、跨 ID 引用、命名 handler、持久 state、存档/读档、
重载和游戏内可观察结果。只完成“能运行一段 Lua”不算完成此样板。

后续工作与真实状态见 [Lua-first 路线图](lua-first-roadmap.md)；阅读术语时可配合
[Lua-first 词汇表](lua-first-glossary.md)。
