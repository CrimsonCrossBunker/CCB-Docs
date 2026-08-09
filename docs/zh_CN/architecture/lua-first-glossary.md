---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: architecture.lua-first-glossary
title: Lua-first 学习词汇表
language: zh_CN
status: draft
doc_type: reference
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
review_interval_days: 180
last_human_reviewer: LYHGLYTX
source_paths:
- data/lua/LUA_FIRST_PLATFORM.md
- ai/lua-first-roadmap.yml
- data/lua/types/ccb_api_v5.d.lua
source_symbols: []
source_queries: []
source_fingerprint: 83295e7405ceb3d25e667560f81370be8f5180b5e039c8f559cad409b2865a3f
authority: docs-explanation
verified_commit: b2bbec1a2f4f8e41a2fece924c7c43b426ff2dc6
verified_at: '2026-08-09'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 553074fb818e8229c2a2da4d9ad3a0ba8f997cac6df6f23be0314647c88ee0f1
prerequisites:
- architecture.lua-first-platform
depends_on:
- architecture.lua-first-platform
- architecture.lua-first-roadmap
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/lua-first-glossary/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/lua-first-glossary/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/architecture/lua-first-glossary/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/lua-first-glossary/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/b2bbec1a2f4f8e41a2fece924c7c43b426ff2dc6
source_urls:
- path: data/lua/LUA_FIRST_PLATFORM.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/b2bbec1a2f4f8e41a2fece924c7c43b426ff2dc6/data/lua/LUA_FIRST_PLATFORM.md
- path: ai/lua-first-roadmap.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/b2bbec1a2f4f8e41a2fece924c7c43b426ff2dc6/ai/lua-first-roadmap.yml
- path: data/lua/types/ccb_api_v5.d.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/b2bbec1a2f4f8e41a2fece924c7c43b426ff2dc6/data/lua/types/ccb_api_v5.d.lua
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28architecture.lua-first-glossary%29%3A+&body=Document+ID%3A+architecture.lua-first-glossary%0ALanguage%3A+zh_CN%0AVerified+commit%3A+b2bbec1a2f4f8e41a2fece924c7c43b426ff2dc6%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Lua-first 学习词汇表

这份词汇表面向一边学习、一边 vibe coding 的开发者。你不需要先背完全部名词；遇到
一个对象时先问四件事：**谁拥有它、什么时候有效、能否存档、哪份源码/测试证明它
已经实现**。

> Platform v1 仍在规划和实现过程中。词条中的“目标”描述设计方向，不代表当前 Lua
> API v5 已经提供同名对象或函数。

## Lua 与 Mod 装载

| 名词 | 含义 |
| --- | --- |
| Lua | 一门轻量、动态类型、可嵌入的编程语言。CCB 把解释器放进游戏进程，让 Mod 调用受支持的游戏能力。 |
| Lua 5.4 | Platform v1 选定的语言语义基线。具体捆绑小版本、平台构建选项和 C 模块兼容仍以源码/构建合同为准。 |
| Lua state | 一套独立 Lua 运行环境，包含全局变量、模块缓存、堆、协程和注册函数。重新装载可能创建新 state，因此旧函数和引用不能默认继续有效。 |
| chunk | Lua 一次加载/执行的代码单元，例如一个 `.lua` 文件。Mod 入口也是 chunk。 |
| entry point / 入口 | 引擎开始加载一个 Mod 时执行的文件。Platform 默认是根 `main.lua`，高级元数据可在根 `mod.lua` 改写入口。 |
| zero-configuration / 零配置 | 只靠稳定目录约定即可发现 Mod；最小 Mod 不要求额外 manifest。它不等于“没有默认值或验证”。 |
| `main.lua` | Platform Mod 的默认内容与运行时注册入口。它是目标约定，不是当前 v5 Mod 的替代事实。 |
| `mod.lua` | 可选高级元数据入口，目标是返回原生 `ccb.ModDefinition`。扫描时会执行，因此有可信代码风险。 |
| manifest | 描述 Mod ID、版本、依赖、能力等的元数据文件。当前 v5 使用 manifest；Platform 最小 Mod 不要求作者维护它。 |
| Mod ID | 跨依赖、存档和迁移识别 Mod 的稳定标识。零配置时默认取目录名；发布后不应随意改变。 |
| dependency / 依赖 | 一个 Mod 在另一个 Mod 之后加载并使用其内容/API 的声明关系。必须在执行静态内容前确定顺序并拒绝依赖环。 |
| module / 模块 | 一个 `.lua` 文件或原生库导出的可复用值。通常由 `require` 加载，并在当前 Lua state 的 `package.loaded` 中缓存。 |
| `require` | Lua 的模块加载函数。Platform 默认从 Mod 根的 `?.lua` 与 `?/init.lua` 开始搜索，可信代码还可改变 `package.path`。 |
| standard library / 标准库 | Lua 自带的表、字符串、数学、协程、I/O、操作系统、调试和 package 等库。Platform 计划完整开放。 |
| trusted execution / 可信执行 | Mod 与游戏进程拥有相同权限，可能读写文件、启动进程或加载原生代码；它不是隔离的不可信脚本。 |
| sandbox / 沙箱 | 限制脚本能看到的库与操作的安全边界。当前 v5 capability 模型使用限制；Platform v1 明确不复用它。 |
| capability / 能力声明 | 当前 v5 用来声明和授予某类 API 的权限单位。它不是 Platform v1 的目标发现/信任模型。 |

## 绑定与原生对象

| 名词 | 含义 |
| --- | --- |
| embedding / 嵌入 | C++ 程序创建 Lua state、装载脚本并在两种语言之间传值/调用函数。Lua 不需要成为独立进程。 |
| binding / 绑定 | 把 C++ 函数、类型、字段或枚举安全地暴露给 Lua 的桥接代码。好的绑定表达游戏领域，而不是 parser 内部细节。 |
| sol2 | CCB 可用于连接 C++ 与 Lua 的 C++ 库。它简化注册函数和类型，但不会自动解决生命周期、线程、存档或 API 设计。 |
| Lua C API | Lua 官方的栈式 C 接口。sol2 等绑定层最终建立在它上面；错误的栈/所有权操作可能导致难调试问题。 |
| usertype | sol2 对“把一个 C++ 类型注册为 Lua 可用类型”的称呼。它可以暴露构造、方法、属性和运算符。 |
| userdata | Lua 用来承载 C/C++ 对象或句柄的值。它不是普通 table，也不能默认序列化。 |
| native object / 原生对象 | 由 C++ 定义语义和存储的对象，通过 binding 给 Lua 使用。Platform 静态 definition 目标是真实原生对象，不是 JSON 影子 table。 |
| public/private/protected | C++ 访问控制。Platform 只暴露明确导出类型中可绑定的 `public` 成员，不绕过 `private`/`protected`。 |
| handle / 句柄 | 间接指向对象的稳定或受检引用。它可以保存 ID、owner、generation，而不是裸指针。 |
| owner / 所有者 | 决定某个借用对象何时存在的对象或系统，例如 world、map、registry、Lua state。owner 消失后借用引用失效。 |
| generation / 代次 | owner 每次整体替换时增加的版本号。引用保存创建时的 generation，用来发现“地址看似还在但已属于新世界”的陈旧引用。 |
| stale reference / 陈旧引用 | owner 已销毁或 generation 已变化的旧引用。Platform 要求访问时抛 Lua 错误，而不是产生悬空指针。 |
| ABI | Application Binary Interface，编译后二进制之间的调用、布局和符号约定。Lua 源码 API 稳定不代表任意 C 模块 ABI 跨编译器/平台稳定。 |
| LuaLS | Lua Language Server，为编辑器提供补全、类型提示和诊断。`.d.lua` 声明描述公共接口，但不能代替运行时测试。 |

## 静态内容与加载生命周期

| 名词 | 含义 |
| --- | --- |
| definition / 定义对象 | 描述某类静态游戏内容的对象，例如 item、recipe、vehicle。它通常在数据加载期创建，finalize 后只读或受严格控制。 |
| factory | 按类型创建、查找和校验 definition 的通用机制。历史 C++ `generic_factory` 是实现背景；Platform 公共 API 不必照搬其内部模板形状。 |
| registry | 按稳定 ID 保存某一类 definition 的集合。它负责重复 ID、查找、迭代和最终化边界。 |
| staging | 提交前暂存新 definition 的区域。失败时可以丢弃，避免污染已经可玩的全局 registry。 |
| transaction / 事务 | 一组变更要么全部提交、要么全部不进入游戏状态。它能回滚引擎内 staging，不能回滚 Mod 已做的文件/进程副作用。 |
| `add` | 新增 definition；ID 重复默认报错。 |
| `replace` | 明确用新 definition 替换已有 ID；需要兼容和所有权检查，不能由重复 ID 暗中触发。 |
| `edit` | 在事务里受控修改现有 definition，失败则不提交。它不同于拿到裸指针随时改 finalized 数据。 |
| finalize / 最终化 | 所有数据加载后解析跨 ID 引用、生成缓存、验证不变量并封闭 registry 的阶段。执行顺序决定 Lua 静态内容能否参与正常校验。 |
| cross-ID reference / 跨 ID 引用 | 一个 definition 用稳定 ID 指向另一个，例如 recipe 指向 item。通常在 finalize 解析并报告缺失目标。 |
| stable ID / 稳定 ID | 存档、引用和迁移长期使用的字符串身份。改变显示名没关系，随意改变稳定 ID 会破坏世界和依赖。 |
| fingerprint / 指纹 | 对静态内容或源文件做的确定性摘要。热重载用它判断静态 definition 是否变化；文档用它检查证据漂移。 |
| hot reload / 热重载 | 不重启整个游戏地替换运行时脚本。静态内容改变时必须升级为完整数据重载，不能绕过 finalize。 |

## 运行时行为

| 名词 | 含义 |
| --- | --- |
| event / 事件 | “某事已经发生”的类型化通知，适合观察和异步反应。监听者通常不应改变事件本身的决定。 |
| Hook | 引擎在决定前同步调用的扩展点，可变换、选择或否决。因为它影响主流程，需要严格的顺序、返回类型和错误策略。 |
| callback / 回调 | 引擎稍后调用的函数总称。event listener、Hook 和 definition 行为都可算 callback，但语义不同。 |
| handler | 有稳定名字、可由 definition 或 task 引用的 callback。名字让 reload 和存档后重新绑定成为可能。 |
| context / 上下文 | 某次调用所需对象与信息的有类型集合，例如 user、item、位置和原因；它的有效期通常只到 callback 返回。 |
| service / 领域服务 | 与 JSON/EOC/Lua 语法无关的游戏操作，例如“给角色增加经过校验的 morale”。旧 adapter 和新 binding 可以共用它。 |
| query / 查询 | 读取状态、不产生持久副作用的操作。Lua 条件通常组合 query 和普通表达式。 |
| mutation / 修改 | 改变游戏状态的操作，必须定义验证、所有权、事件、失败和存档影响。 |
| task / 任务 | 安排在未来或重复执行的命名工作。持久 task 保存 handler ID 与数据，不保存函数调用栈。 |
| workflow / 工作流 | 用普通 Lua 函数、task、event 和 state 组合出的多步骤过程。它是库层模式，不需要引擎再造 EOC DSL。 |
| state machine / 状态机 | 把流程表示为有限状态和显式转移。状态可序列化时，读档后可以重新驱动，而无需保存协程栈。 |
| coroutine / 协程 | Lua 可暂停和恢复的函数执行。适合当前 session 的顺序流程，但调用栈不跨存读档。 |
| scheduler / 调度器 | 按时间或游戏事件决定 task 何时运行的系统。它还负责取消、过期、owner 失效和诊断。 |

## 持久化与兼容

| 名词 | 含义 |
| --- | --- |
| serialization / 序列化 | 把内存状态转换成可保存数据。函数、线程、userdata 和裸原生引用通常不能直接序列化。 |
| payload | task 或 state 保存的普通数据，例如数字、字符串、布尔、数组和受限 table。它需要明确大小与类型边界。 |
| payload version | Mod 自己的数据版本。handler 变化时可用它选择迁移、拒绝或安全丢弃旧 payload。 |
| persistent state / 持久状态 | 与 Mod、角色或世界关联并写入存档的稳定数据，不等于 Lua 全局变量。 |
| session state / 会话状态 | 只活到当前运行或 Lua state 被替换的数据，可以包含函数和协程，但不承诺读档恢复。 |
| save compatibility / 存档兼容 | 新版本仍能加载旧世界并维持稳定 ID 和预期意义。API 漂亮但破坏存档的迁移不是成功迁移。 |
| hybrid Mod / 混合 Mod | 迁移期同时含旧 JSON/EOC 和 Platform Lua 的 Mod。它允许小步迁移，但冲突顺序必须明确。 |
| adapter / 适配层 | 把一种接口转换到另一种接口的薄层。允许旧 EOC/JSON 私有适配到共享 service；禁止把 adapter 当新公共模型。 |
| deprecation / 弃用 | 接口仍可用但计划移除，并提供替代、警告和时间窗口。Platform 规定至少两个稳定版且十二个月，两者都满足。 |
| migration / 迁移 | 在保留稳定 ID、存档和行为的前提下把内容/调用转到新接口。自动工具应输出惯用 Lua 骨架和明确 TODO。 |
| IR | Intermediate Representation，中间表示。它可以帮助工具分析旧内容，但不应成为作者必须手写的新 JSON/EOC 式公共语言。 |

## JSON 与 EOC 旧概念

| 名词 | 含义 |
| --- | --- |
| JSON | 当前大量静态内容使用的数据格式。Platform 替代的是作者侧 JSON 合同，不要求存档、设置或生成清单放弃 JSON。 |
| JSON loader | 读取 JSON、按 `type` 分派并构造 C++ definition 的旧入口。早期实现可以私有复用，不能公开为 Lua API。 |
| `copy-from` | JSON 内容的继承/复制语法。Lua 用函数、构造、clone 和组合获得复用，不需要复制这个关键字。 |
| EOC | Effect on Condition，CCB/CDDA 数据驱动的条件与效果机制。它有自己的 parser、上下文、变量和递归执行模型。 |
| condition | EOC 中返回真假的判断。Platform 通常用原生 query 和普通 Lua 表达式表达，而不是每个 key 一个 wrapper。 |
| effect | EOC 中改变状态或触发动作的步骤。Platform 将底层操作抽成原生方法或共享领域 service。 |
| talker | EOC/对话系统把角色、物品、怪物等包装成统一访问接口的历史抽象，常见 `alpha`/`beta`。Platform 应传有类型原生对象。 |
| EOC context | EOC 执行时携带 talker、变量、位置等的旧上下文模型。Platform callback context 可以吸收真正需要的信息，但不复制旧别名。 |
| variable scope / 变量作用域 | EOC 的 `u_val`、`npc_val`、`global_val`、`context_val` 等查找规则。Platform 用明确的 Mod/角色/世界 state 代替隐式字符串作用域。 |
| recurrence | EOC 自我重复或延迟执行的机制。Platform 使用命名 task 与 scheduler，不再发布另一套递归 DSL。 |
| replacement ledger | 逐项记录旧清单条目去向的受检账本：目标域、service、状态、证据或不适用理由，而不是“旧 key 到新 key”的别名表。 |

## Vibe coding 时的实用检查法

Vibe coding 是借助 AI 快速探索和迭代的工作方式，不是跳过合同与验证。每次让 Agent 写
一小段时，可以固定追问：

1. 这是当前 v5 API，还是尚未实现的 Platform 目标？
2. 这个对象的 owner 和 generation 是什么，什么时候失效？
3. 它发生在 discover、staging、finalize、`world_ready` 还是 runtime？
4. 需要存档的是稳定 ID/payload，还是误把函数、协程、userdata 当成数据？
5. 这是领域 service，还是把旧 JSON/EOC parser 包了一层？
6. 对应的源码、LuaLS、测试、路线图状态和中英文档是否一起更新？

这六问能让“凭感觉快速写”仍然落在可维护的工程边界里。整体设计见
[Platform v1](lua-first-platform.md)，开发顺序见[路线图](lua-first-roadmap.md)。
