---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: how-to.common-tasks
title: 旧文档迁移草稿：common tasks
language: zh_CN
status: draft
doc_type: explanation
audiences:
- new-contributor
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 365
last_human_reviewer: Pending human review
source_paths:
- doc/DEVELOPER_FAQ.md
- src/monstergenerator.cpp
- src/overmap_terrain.cpp
- src/item_factory.cpp
- src/item_armor.cpp
- tests/monster_test.cpp
source_symbols:
- MonsterGenerator::load_monster
- overmap_terrains::load
- itype::load
source_queries: []
source_fingerprint: 51bcfbc2885b30088566d8c5623f1c4b35f924e720d8d11b5c2b3858a7bab9fa
authority: docs-explanation
verified_commit: 02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 0118e577510ae885c0bdb09fea6ec0f0cc8cfd0b7863024c9f1cddcaf0bf5bc1
prerequisites: []
depends_on: []
redirect_from: []
supersedes:
- contributing.developer-faq
license: CC-BY-SA-3.0
attribution: 'CCB contributors: thaelina; accepted inventory identities only. Source paths and Git history
  remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: architecture
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/how-to/common-tasks/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/how-to/common-tasks/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/how-to/common-tasks/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/how-to/common-tasks/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
source_urls:
- path: doc/DEVELOPER_FAQ.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/DEVELOPER_FAQ.md
- path: src/monstergenerator.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/monstergenerator.cpp
- path: src/overmap_terrain.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/overmap_terrain.cpp
- path: src/item_factory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/item_factory.cpp
- path: src/item_armor.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/item_armor.cpp
- path: tests/monster_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/tests/monster_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28how-to.common-tasks%29%3A+&body=Document+ID%3A+how-to.common-tasks%0ALanguage%3A+zh_CN%0AVerified+commit%3A+02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：common tasks

本页是 `how-to.common-tasks` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `contributing.developer-faq`
- Target: `how-to/common-tasks.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/how-to/common-tasks/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| contributing.developer-faq | doc/DEVELOPER_FAQ.md | merge_into | stubbed | b1ee97987589450da70f30ee2feed12c9d18f479 | how-to.common-tasks |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 当前贡献任务路线

旧 FAQ 中关于 `omdata.h`、大型 `switch`、`player::activate_bionic` 和直接注册
`iuse` 的步骤已经不能当成当前流程。现在先找数据类型的加载器、相邻的第一方
JSON 例子和对应测试，再决定是否真的需要 C++ 扩展。

### 添加或修改怪物

1. 在 `data/json/` 或目标 Mod 中找到同类 `MONSTER` 定义，复制最小可工作的例子。
2. 使用全局唯一 ID；若要自然生成，再修改对应 monster group，而不是只添加类型。
3. 掉落物使用已有 item group；特殊攻击优先使用已有 JSON actor/EOC 能力，只有公开
   数据契约无法表达时才修改 native 注册。
4. 运行 JSON 格式与加载检查，再运行 `tests/monster_test.cpp` 中最接近改动的过滤测试。

`MonsterGenerator::load_monster` 把定义交给 monster factory；一致性检查还会验证物种、
harvest、ammo 与相关 ID。因此“JSON 能解析”不等于“定义完整”。

### 添加 overmap 地形或建筑

1. 先确认目标是 overmap terrain、overmap special 还是 mapgen；三者不是同一个层级。
2. 从 `data/json/overmap/`、目标 Mod 和相邻 mapgen 定义中选择当前例子。
3. 为需要的方向、连接规则、城市放置或 wilderness special 明确数据关系。
4. 运行 JSON 加载和 mapgen/overmap 相关测试；不要照搬旧文档中的硬编码 enum 与
   `draw_map` switch 流程。

`overmap_terrains::load` 使用 factory 载入数据，随后的一致性检查会解析 mapgen ID 和
spawn group。新增建筑时必须同时验证 overmap 放置与实际 mapgen。

### 添加物品、护甲或可使用动作

1. 从当前同类 object type 和相邻数据定义开始，确认 `copy-from`、必需字段与默认值。
2. 护甲要同时检查 pocket、coverage、material、layer 和受击部位语义；不要把旧 FAQ
   的保护计算步骤视为稳定公式。
3. 优先复用已有 use action、EOC 或 Lua API。只有新行为不能由公开契约表达时，才添加
   native action，并同步注册、测试和文档影响字段。
4. 运行 JSON 格式、加载、ID 检查和受影响的 focused test。

`itype::load` 直接读取重量、体积、长度、价格及各 subtype slot，随后还有 factory
finalize/check 阶段；修改者应追踪完整加载生命周期，不能只看一个 JSON 样例。

### 提交前最小闭环

- 从最近的 `AGENTS.md` 与 `ai/test-matrix.yml` 选择最窄验证。
- 在 PR 中填写 Documentation impact、Related CCB-Docs PR、Affected documentation IDs、
  Generated reference impact 与 Responsible human。
- 记录实际运行的命令、平台和结果；未运行项写明原因，不用全量测试掩盖 focused 失败。
- 若改动公开 Schema、LuaLS 声明、注册或生成清单，重新生成引用并检查 diff。

进一步入口见[常见任务](../getting-started/common-tasks.md)、
[JSON 概览](../json/overview.md)、[EOC 概览](../eoc/overview.md)与
[测试策略](../validation/testing.md)。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b`；聚合源指纹为 `51bcfbc2885b30088566d8c5623f1c4b35f924e720d8d11b5c2b3858a7bab9fa`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/DEVELOPER_FAQ.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/DEVELOPER_FAQ.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/DEVELOPER_FAQ.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
