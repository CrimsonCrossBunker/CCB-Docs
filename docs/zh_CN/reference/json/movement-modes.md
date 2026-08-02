---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.movement-modes
title: 旧文档迁移草稿：movement modes
language: zh_CN
status: active
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
- doc/JSON/MOVE_MODE.md
- src/move_mode.cpp
- src/move_mode.h
- data/json/move_modes.json
source_symbols:
- move_mode::load
source_queries: []
source_fingerprint: 3a00588b939b053ee86e7754623a56ab4ca546f9304e4230da35cde8e69a7a3d
authority: docs-explanation
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: e6197c06a274977e3dd88120bfd657678164cdb2f0cdbe6c88bcf65006aad593
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: thaelina; accepted inventory identities only. Source paths and Git history
  remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/movement-modes/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/movement-modes/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/movement-modes/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/movement-modes/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: doc/JSON/MOVE_MODE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/JSON/MOVE_MODE.md
- path: src/move_mode.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/move_mode.cpp
- path: src/move_mode.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/move_mode.h
- path: data/json/move_modes.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/json/move_modes.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.movement-modes%29%3A+&body=Document+ID%3A+json.movement-modes%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：movement modes

本页是 `json.movement-modes` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.movement-modes`
- Target: `reference/json/movement-modes.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/movement-modes/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.movement-modes | doc/JSON/MOVE_MODE.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## Movement mode 契约

`move_mode` 是 generic factory 对象。当前 loader 强制读取显示字符/名称、panel character、
`exertion_level`、步行/骑乘/机甲的 prepare 与成功消息，以及 `move_type`。`move_type` 只接受
当前注册的 prone、crouching、walking、running 语义；显示名称不是行为类型。

### 速度、体力和循环

`move_speed_multiplier`、`stamina_multiplier`、`sound_multiplier`、`swim_speed_mod`、
`mech_power_use` 和 `stop_hauling` 影响不同子系统。倍率不是独立平衡旋钮：terrain move cost、
encumbrance、mount、stamina、noise 和 effect 会继续参与最终结果。

Finalize 按 move-speed multiplier 排序并建立正向/反向 cycle。新增模式可能改变所有玩家的
循环顺序，即使没有修改现有 ID；相同 multiplier 的稳定顺序也不应当作 UI 契约。

### 文本和载具

prepare/change message 分别覆盖徒步、animal 和 mech；失败消息有默认值但不应依赖占位的
“bugs”文本发布。字符和 panel symbol 必须是合法 Unicode；颜色由当前 color reader 解析。
骑乘 exertion 可独立设置，不能用步行测试推断。

### 验证

运行 formatter、`make -j2 json-check`、`--check-mods` 和 movement/stamina/sound/vehicle
focused tests。覆盖 cycle 两个方向、UI symbol、prone/crouch/run 切换失败、hauling、swim、
animal/mech power、负重/terrain、保存重载与翻译。记录实际 move、stamina 和 sound，而不只
检查 JSON 能加载。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `3a00588b939b053ee86e7754623a56ab4ca546f9304e4230da35cde8e69a7a3d`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/MOVE_MODE.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/MOVE_MODE.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/MOVE_MODE.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
