---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: home
title: CCB 开发文档
language: zh_CN
status: draft
source_paths:
- AGENTS.md
- GOVERNANCE.md
authority: docs-explanation
verified_commit: 11748581a0df8651380cfb8ae37ae91baafe054d
verified_at: '2026-08-01'
generated: false
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
risk_group: project-context
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/551
stale_reason: null
search:
  exclude: true
---

# CCB 开发文档

这里是 Cataclysm: Cleanwater Bomb 的正式开发者解释、教程、架构与导航站。

!!! warning "当前为 Phase 0/1 草稿"
    这些示范页依赖 CCB 主仓库 PR #551。该 PR 经人类审核合并并刷新最终
    commit 后，页面才会从草稿转为正式内容。

## 先理解权威边界

- 游戏实际怎样运行，以 CCB 主仓库源码和测试为准。
- JSON、Lua 与 API 契约，以 Schema、LuaLS 声明、注册信息和生成清单为准。
- 构建与验证，以 CI、CMake、Makefile、Gradle 和验证脚本为准。
- 贡献政策，以主仓库 `AGENTS.md`、`CONTRIBUTING.md`、`GOVERNANCE.md` 为准。
- 本站负责把这些事实组织成可以学习、查阅和被 Agent 导航的文档。

如果本站与契约冲突，页面必须标记为 stale 并修复；本站不能覆盖契约。

## 选择入口

- [第一次贡献](getting-started/first-contribution.md)：完成从定位到 PR 的最短路线。
- [项目地图](architecture/project-map.md)：按子系统寻找源码、规则和测试。
- [Responsible human](contributing/responsible-human.md)：理解 AI 辅助贡献的责任。
- [构建与验证](validation/quickstart.md)：选择最小但充分的验证命令。

CCB 玩家主页和物品查询站保持独立：主页提供玩家简明入口，CCB-GUIDE 提供
游戏数据查询。
