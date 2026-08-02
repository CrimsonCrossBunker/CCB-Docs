---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: architecture.design-principles
title: 设计原则
language: zh_CN
status: draft
doc_type: explanation
audiences:
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 180
last_human_reviewer: LYHGLYTX
source_paths:
- CONTRIBUTING.md
- doc/design-balance-lore/design-doc.md
- doc/design-balance-lore/design-gameplay.md
- doc/design-balance-lore/design-user-experience.md
source_symbols: []
source_queries: []
source_fingerprint: 5da90a32b5e4f26ca60b5ca3ea00782926f74b1f31dd60a1c900e01bf75d7c8d
authority: docs-explanation
verified_commit: 2c899a3db790e11a6ff44d91f319064b1ee65d2a
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 746d83cab18a1c2f87fc345bf1ee403dc978ed942e1ddac84eb77e15ef72df85
prerequisites:
- architecture.overview
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: design
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/560
stale_reason: null
search:
  exclude: true
---

# 设计原则

CCB 设计受可观察行为、兼容性、可维护性和项目自身方向约束。历史设计文档提供背景；
当前 CCB 源码、测试、治理与维护者决定哪些仍适用。

## 评估提案

1. 先说明玩家或贡献者问题，不预设实现。
2. 定义可观察成功条件、非目标、受影响人群和失败模式。
3. 增加引擎复杂度前，检查 JSON、EOC 或受支持 Lua API 是否能表达需求。
4. 明确所有权、生命周期、不变量、序列化、性能热点、UI/无障碍、本地化与平台影响。
5. 区分共同上游行为和 CCB 有意分歧。
6. 优先选择可逆、可测试并有清楚兼容政策的小步修改。

## 数据驱动不能隐藏语义

只有 loader 能验证、错误可操作且作者能理解生命周期时，把行为移入数据才有价值。
灵活 JSON 或 Lua 表面仍需要约束文档和测试。不要只为避免 C++ 修改就把不稳定内部
hook 发布成公共扩展点。

## 平衡与内容

机制和平衡提案需要示例、受影响场景与衡量目标结果的方法。技术修复中避免混入大范围
无关再平衡。尊重项目 lore 与内容政策；尚未在 CCB 确认的历史上游指导应明确标记，
不能当作当前规则。

最终决定应保留在 Issue 或经审阅 PR 中，使理由、取舍和 Responsible human 可审计。
