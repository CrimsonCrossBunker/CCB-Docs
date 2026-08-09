---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: architecture.lua-first-roadmap
title: Lua-first Platform 路线图
language: zh_CN
status: draft
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
source_fingerprint: e8cd2ca29e3d1c735f3d5e460f5224b9bd96b723e91b9f1d509db504c762c21f
authority: docs-explanation
verified_commit: b2bbec1a2f4f8e41a2fece924c7c43b426ff2dc6
verified_at: '2026-08-09'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 18cd86df4ccf4d50b87415b40ed310c10249b716e624934ec3771301466c5c81
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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/615
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/lua-first-roadmap/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/lua-first-roadmap/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/architecture/lua-first-roadmap/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/lua-first-roadmap/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/b2bbec1a2f4f8e41a2fece924c7c43b426ff2dc6
source_urls:
- path: ai/lua-first-roadmap.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/b2bbec1a2f4f8e41a2fece924c7c43b426ff2dc6/ai/lua-first-roadmap.yml
- path: ai/lua-first-roadmap.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/b2bbec1a2f4f8e41a2fece924c7c43b426ff2dc6/ai/lua-first-roadmap.schema.json
- path: data/lua/LUA_FIRST_PLATFORM.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/b2bbec1a2f4f8e41a2fece924c7c43b426ff2dc6/data/lua/LUA_FIRST_PLATFORM.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28architecture.lua-first-roadmap%29%3A+&body=Document+ID%3A+architecture.lua-first-roadmap%0ALanguage%3A+zh_CN%0AVerified+commit%3A+b2bbec1a2f4f8e41a2fece924c7c43b426ff2dc6%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
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

## 八个里程碑

| 顺序 | 里程碑 | 当前状态 | 退出重点 |
| ---: | --- | --- | --- |
| 1 | 文档基础 | `complete` | 权威架构、Agent 路由、Schema 路线图、中英说明 |
| 2 | 零配置发现 | `planned` | 只有根 `main.lua` 的目录可发现；可选 `mod.lua` 先解析依赖 |
| 3 | 原生内容事务 | `planned` | finalize 前执行、staging/commit、owner/generation、私有 adapter 清单 |
| 4 | 物品+配方+使用行为 | `planned` | 第一个零 JSON/EOC Mod 完成存读档和可观察游戏结果 |
| 5 | 行为 service | `planned` | event、Hook、handler、持久 task/state 和共享领域 service |
| 6 | 静态内容域覆盖 | `planned` | 每个受检 JSON/EOC 条目有 disposition；受支持域有测试、声明、文档 |
| 7 | 核心与捆绑内容迁移 | `planned` | 保留稳定 ID，迁移工具输出惯用 Lua 骨架，按完成域冻结旧创作接口 |
| 8 | 旧接口移除窗口 | `planned` | 至少两个稳定版且至少十二个月，并通过存档迁移与捆绑内容检查 |

依赖是一条有向链：后续里程碑不能用“先删掉 EOC/JSON 逼大家迁移”的方式跳过前置
能力。机器检查会拒绝未知依赖与依赖环。

## 当前能力覆盖

| 能力 | 状态 | 旧依赖 | 下一项实质工作 |
| --- | --- | --- | --- |
| Mod 发现 | `absent` | `public_legacy` | 在旧 `modinfo.json` 扫描旁加入 Platform 发现和冲突诊断 |
| 完整标准库 | `legacy_only` | `none` | 建立独立版本的可信 Platform Lua state 和显式安全警告 |
| 原生静态内容 | `absent` | `public_legacy` | 增加 pre-finalize 执行、staging registry 与提交语义 |
| 原生对象表面 | `partial` | `none` | 导出根清单、不可绑定成员报告、owner/generation 检查 |
| event/Hook/callback | `partial` | `none` | 用原生参数替代 snapshot/talker 别名，稳定 handler ID |
| 持久 task/state | `partial` | `none` | 保存 handler、到期时间、owner、payload 与版本并定义异常结果 |
| 共享领域 service | `absent` | `public_legacy` | 分类 EOC handler，先抽取样板所需的物品、配方、角色等操作 |
| 开发模板 | `absent` | `none` | 交付 minimal/complete 和安全的 `create_lua_mod.py` |
| 替代审计 | `absent` | `private_adapter` | 建立覆盖每个清单条目恰好一次的 selector ledger |

这里的 `partial` 多数表示现有 v5 或 C++ 已有可复用基础，不表示 Platform 作者现在可以
使用页面里的目标写法。

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

### 第一批提取范围

第一个样板只提取完成“物品 + 配方 + Lua 使用行为”所需的最小闭环：

- 零配置 Mod 发现和依赖顺序；
- item/recipe 原生 definition 与跨 ID 引用；
- 单位、翻译文本和通用 factory/registry 规则；
- 一个 definition 可引用的命名 handler；
- 角色/物品所需的最小领域 service；
- Mod state、存档、读档和 reload；
- 错误定位、LuaLS 声明、最小模板和端到端测试。

这个范围够小，能尽快得到可玩的样板；又够完整，能暴露生命周期、所有权和持久化中
最难的问题。第二批再按样板经验扩到载具、怪物、地图生成、对话、任务与 UI。

## replacement ledger 应记录什么

未来替代账本不是简单的“旧键 → 新函数”表。每条记录至少需要：

- 旧清单与 selector；
- 实际游戏语义与所属领域；
- 目标原生类型、方法或共享 service；
- `not_applicable` 理由（例如纯引擎内部序列化）；
- Platform 状态和旧依赖级别；
- 源码、测试、声明、文档和迁移工具证据；
- 稳定 ID、存档与混合 Mod 兼容说明。

检查器最终要求三个清单的每个条目恰好出现一次，防止遗漏、重复认领或用模糊的
“其他”桶掩盖未解决工作。

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

## 近期开发顺序

近期最合理的 PR 拆分是：

1. 实现零配置扫描和可信执行警告，但先只加载一个无内容入口；
2. 建立 Platform Lua state、错误边界、依赖排序和候选 reload；
3. 建立 definition staging、事务与 owner/generation 基础设施；
4. 逐步抽取 item、recipe 和 use behaviour 所需 service；
5. 交付样板 Mod、模板、LuaLS 和端到端测试；
6. 用第一批经验设计 replacement ledger 生成/校验工具；
7. 再按领域扩覆盖，而不是一次导出全部 C++。

每个 PR 都应更新 `ai/lua-first-roadmap.yml` 的状态、证据和下一步，并填写受影响的
CCB-Docs ID。完整设计边界见 [Platform v1](lua-first-platform.md)，术语解释见
[词汇表](lua-first-glossary.md)。
