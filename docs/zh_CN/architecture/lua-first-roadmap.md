---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: architecture.lua-first-roadmap
title: Lua-first Platform 路线图
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
- ai/lua-first-roadmap.yml
- ai/lua-first-roadmap.schema.json
- data/lua/LUA_FIRST_PLATFORM.md
source_symbols: []
source_queries: []
source_fingerprint: 05c4efbbb59bd9cb6550d35141c21123e5a34da7ecce125a07efc74a57ab26b9
authority: docs-explanation
verified_commit: c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd
verified_at: '2026-08-12'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 2682c28d441a435396381d5c65ad2ea8b8319135d90f924078edd1dab829ca9a
prerequisites:
- architecture.lua-first-platform
depends_on:
- architecture.lua-first-platform
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
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/lua-first-roadmap/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/lua-first-roadmap/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/architecture/lua-first-roadmap/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/lua-first-roadmap/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd
source_urls:
- path: ai/lua-first-roadmap.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/ai/lua-first-roadmap.yml
- path: ai/lua-first-roadmap.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/ai/lua-first-roadmap.schema.json
- path: data/lua/LUA_FIRST_PLATFORM.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/data/lua/LUA_FIRST_PLATFORM.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28architecture.lua-first-roadmap%29%3A+&body=Document+ID%3A+architecture.lua-first-roadmap%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Lua-first Platform 路线图

> 本页把源码仓库的受检路线图翻译成人可读说明。唯一机器状态源是
> `ai/lua-first-roadmap.yml`；某项写着 `planned`、`absent` 或 `partial` 时，不能把目标
> 接口当作当前游戏功能。

## 怎样读状态

里程碑状态描述一整段交付：

- `planned`：方向已列出，尚未开始形成可验收实现；
- `in_progress`：有工作证据，但退出条件还没全部满足；
- `complete`：退出条件已满足并列出源码、测试或文档证据；
- `blocked`：存在明确阻塞条件，不等于“工作很难”。

能力状态描述一个具体表面：

- `absent`：Platform 目标表面不存在；
- `legacy_only`：旧运行时有相关能力，但 Platform 合同没有；
- `partial`：存在可复用基础或部分覆盖，仍不能承诺完整目标；
- `available`：目标表面、验证和文档可以给开发者使用。

`legacy_dependency` 另行回答实现是否还依赖旧系统：`none`、仅内部可见的
`private_adapter`，或作者可见的 `public_legacy`。任何仍是 `public_legacy` 的能力都不能
标成 `available`。

## 当前基线

已生成的旧合同清单给迁移提供分母，而不是自动生成 775 个 Lua 函数：

| 清单 | 当前条目数 | 用途 |
| --- | ---: | --- |
| JSON 顶层 object type | 190 | 逐项归入原生内容域、内部序列化或不适用 |
| EOC condition key | 275 | 归入普通 Lua 查询、原生方法或共享 query service |
| EOC effect key | 310 | 归入原生方法、共享 mutation service、事件/Hook 或 workflow |

每次清单重新生成后，元数据检查器都会核对路线图里的计数，防止路线图悄悄落后。

## 九个里程碑

| 顺序 | 里程碑 | 当前状态 | 退出重点 |
| ---: | --- | --- | --- |
| 1 | 文档基础 | `complete` | 权威架构、Agent 路由、Schema 路线图、中英说明 |
| 2 | 零配置发现 | `complete` | 只有根 `main.lua` 的目录可发现；可选 `mod.lua` 先解析依赖 |
| 3 | 原生内容事务 | `in_progress` | finalize 前执行、staging/commit、owner/generation、私有 adapter 清单 |
| 4 | 物品+配方+使用行为 | `complete` | 第一个零 JSON/EOC Mod 完成存读档和可观察游戏结果 |
| 5 | 行为 service | `in_progress` | event、Hook、handler、持久 task/state 和共享领域 service |
| 6 | 可玩 MVP v0.1 | `complete` | 捆绑的纯 Lua Mod 完成发现、依赖选择、游戏存档、完整重载与继续游玩 |
| 7 | 静态内容域覆盖 | `in_progress` | 每个受检 JSON/EOC 条目有 disposition；受支持域有测试、声明、文档 |
| 8 | 核心与捆绑内容迁移 | `in_progress` | 保留稳定 ID，迁移工具输出惯用 Lua 骨架，按完成域冻结旧创作接口 |
| 9 | 旧接口移除窗口 | `planned` | 至少两个稳定版且至少十二个月，并通过存档迁移与捆绑内容检查 |

依赖是一条有向链：后续里程碑不能用“先删掉 EOC/JSON 逼大家迁移”的方式跳过前置
能力。机器检查会拒绝未知依赖与依赖环。

## 当前能力覆盖

| 能力 | 状态 | 旧依赖 | 下一项实质工作 |
| --- | --- | --- | --- |
| Mod 发现 | `partial` | `none` | 完成人工桌面/Android Mod 选择器交互检查 |
| 完整标准库 | `partial` | `none` | 完成桌面/Android 首次启用可信代码的交互检查 |
| 原生静态内容 | `partial` | `none` | 继续逐字段扩展 typed registrar 和 extractor，不公开旧 loader |
| 原生对象表面 | `partial` | `none` | 补齐导出根清单和不可绑定成员报告，并扩展显式 owner 模型 |
| event/Hook/callback | `partial` | `none` | 把已审计语义事件之外的 actor-kind 覆盖补齐 |
| presentation primitive | `partial` | `none` | 完成人工桌面/Android 交互检查，再按领域添加可组合表单 |
| 持久 task/state | `partial` | `none` | 扩展复制世界与稳定 ID 兼容测试 |
| 共享领域 service | `partial` | `none` | 逐项验证 primitive 和 bounded selector 的精确原生语义 |
| 开发模板 | `partial` | `none` | 只在证明新原生域时增加端到端例子 |
| 迁移 extractor | `partial` | `none` | 仅在目标 typed registrar 存在且语义有证据时增加转换 |
| 替代审计 | `partial` | `none` | 按领域审查 primitive 与 planned 条目，保持各状态计数独立 |

11 项能力已经都有可运行实现或受检基础，并且公共 Platform 表面都不依赖旧 parser；但
`partial` 仍表示覆盖不完整，不能把它解释成 JSON/EOC 已经全面等价替代。

## 不从零重写：怎样提取现有能力

完全抛弃旧实现会很慢，也容易重做多年积累的验证规则；直接公开旧 loader 又会把 Lua
锁成 JSON/EOC 的外壳。正确的提取单位是“游戏领域能力”：

1. **盘点**：从生成清单选一个 JSON type 或 EOC key，并定位注册与 parser；
2. **追踪语义**：找到它最终读取或改变的 C++ 对象、不变量、错误和存档影响；
3. **抽取 service**：把真正的查询或修改变成与语法无关的 C++ 领域方法/service；
4. **绑定原生对象**：为 Lua 提供有类型的参数、返回值、单位和 owner 检查；
5. **保留旧 adapter**：让 JSON/EOC 暂时调用同一个 service，不让旧 parser 成为公共 Lua
   API；
6. **做纵向测试**：从 Mod 发现一直测到 finalize、游戏结果、存档和重载；
7. **记录 disposition**：在替代 ledger 标明目标域、状态、证据和迁移办法；
8. **再迁移内容**：只有替代能力和工具可用后，才批量迁移核心与捆绑 Mod。

这样复用的是规则、校验、原生对象与游戏操作，而不是复用旧语言的形状。

### 已完成的第一批提取

“物品 + 配方 + Lua 使用行为”的第一批闭环已经交付：

- 零配置 Mod 发现和依赖顺序；
- item/recipe 原生 definition 与跨 ID 引用；
- 单位、翻译文本和通用 factory/registry 规则；
- 一个 definition 可引用的命名 handler；
- 角色/物品所需的最小领域 service；
- Mod state、存档、读档和 reload；
- 错误定位、LuaLS 声明、最小模板和端到端测试。

这套样板已经通过真实游戏存档、Lua runtime 关闭、完整数据重载、继续使用物品行为和
逾期任务恰好执行一次的可玩 MVP gate。下一批正在按同一原生模式扩到更多内容目录、
角色/世界操作、载具、怪物、地图、对话、任务与 UI，而不是复制旧 loader。

## replacement ledger 应记录什么

受检替代账本不是简单的“旧键 → 新函数”表。每条记录包含：

- 旧清单与 selector；
- 实际游戏语义与所属领域；
- 目标原生类型、方法或共享 service；
- `not_applicable` 理由（例如纯引擎内部序列化）；
- Platform 状态和旧依赖级别；
- 源码、测试、声明、文档和迁移工具证据；
- 稳定 ID、存档与混合 Mod 兼容说明。

检查器现在已经要求三个清单的每个条目恰好出现一次。当前 775 项分布是：

| disposition | 数量 | 能否声称完整替代 |
| --- | ---: | --- |
| 完整 selector 等价（`implemented_unverified`） | 0 | 尚无一项可以这样声称 |
| 有界形状已实现（`bounded_implemented_unverified`） | 119 | 只能用于账本列明的有限形状 |
| 原生 primitive 已有（`primitive_available_unverified`） | 440 | 有组合积木，不等于旧 selector 等价 |
| 待实现（`planned`） | 198 | 仍是迁移工作，不是已发布 API |
| 已审查为不适用（`reviewed_not_applicable`） | 18 | 有明确的原生 Lua/引擎内部理由 |

这正是“Lua-first 已可玩”与“尚未全面替代 JSON/EOC”能够同时成立的原因。完整 selector
等价为 0 并不否认原生 API 已存在；它表示我们没有把有限形状或组合 primitive 夸大成
旧语言所有用法的逐项等价。

## 每个能力的完成定义

一个域要从 `partial` 变成 `available`，至少需要：

1. 原生 API 不要求作者提供 JSON/EOC；
2. loader 生命周期、失败回滚和错误信息有测试；
3. 借用引用有 owner/generation 失效测试；
4. 保存的数据只含稳定 ID 与可序列化 payload；
5. LuaLS 声明、可运行例子和中英文档同步；
6. minimal/complete 模板能表达真实用例；
7. 旧 adapter 依赖为 `none` 或仅 `private_adapter`；
8. Windows、Linux、Android 等支持平台的差异被验证或明确说明。

## 下一阶段开发顺序

零配置扫描、Platform Lua state、第一批事务基础、物品/配方/行为样板、模板、迁移工具、
LuaLS 和 775 项账本都已经落地。接下来的顺序是：

1. 补完桌面与 Android 的 Mod 选择器、可信代码确认和 presentation 人工交互 gate；
2. 按显式 owner/generation 模式扩展剩余借用原生引用；
3. 逐字段补齐静态内容 registrar 和 extractor，并保持旧 loader 不进入公共 API；
4. 为 environment、dialogue、activity、战斗、导航和 relocation 补原生领域 service；
5. 用源码语义和转换 fixture，把有证据的 bounded/primitive 项逐步提升为完整等价；
6. 扩展复制世界、稳定 ID 与支持平台的存档兼容测试；
7. 只有一个域完整达到 `available` 后，才迁移该域的核心内容并冻结对应旧创作入口。

每个 PR 都应更新 `ai/lua-first-roadmap.yml` 的状态、证据和下一步，并填写受影响的
CCB-Docs ID。完整设计边界见 [Platform v1](lua-first-platform.md)，可运行接口见
[Platform v1 API 概览](../api/lua/platform-v1/overview.md)，术语解释见
[词汇表](lua-first-glossary.md)。
