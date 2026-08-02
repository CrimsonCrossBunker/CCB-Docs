---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.climbing-aids
title: 旧文档迁移草稿：climbing aids
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
- doc/JSON/CLIMBING.md
- src/climbing.cpp
- src/climbing.h
- data/json/climbing.json
source_symbols:
- climbing_aid::load
source_queries: []
source_fingerprint: 997faf1bea95578f5e2960f8dc83e65303b4e20c8d8c8d4c01ebe1e383e235b4
authority: docs-explanation
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 82caf79146dc39a70e66a4544ac8900fb85fed8d9375975476731840dd3706cd
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: Killa-bite, thaelina; accepted inventory identities only. Source paths
  and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/climbing-aids/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/climbing-aids/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/climbing-aids/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/climbing-aids/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: doc/JSON/CLIMBING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/JSON/CLIMBING.md
- path: src/climbing.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/climbing.cpp
- path: src/climbing.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/climbing.h
- path: data/json/climbing.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/json/climbing.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.climbing-aids%29%3A+&body=Document+ID%3A+json.climbing-aids%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：climbing aids

本页是 `json.climbing-aids` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.climbing-aids`
- Target: `reference/json/climbing-aids.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/climbing-aids/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.climbing-aids | doc/JSON/CLIMBING.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## Climbing aid 契约

`climbing_aid` generic factory 按 condition category + flag 建立 lookup。顶层 `down` 与
`condition` 必填，`slip_chance_mod` 可选。项目还要求有效 `default` entry；缺失时运行时虽会构造
fallback，但 consistency check 会报告。

### Condition

type 必须是 special、ter_furn、veh、item、character 或 trait，flag 必填。item condition 还要求
uses；ter_furn 可设置 range（默认 1）；其他 category 不读取这些专用字段。uses 表示使用时消耗的
item 数量，condition 检测和 route scan 决定 aid 是否可用。

### Down rules

max_height 默认 1，设为 0 禁止向下；allow_remaining_height 默认 true，easy_climb_back_up 默认 0。
启用时 menu_text 与 confirm_text 必填。设置 deploy_furn 后，menu_cant 和单字节 menu_hotkey 也
必填；否则二者可选且 hotkey 最多一个字节。cost 的 kcal、thirst、damage、pain 按下降层数应用。

部署 furniture 必须验证开放空气、已有 furniture/vehicle/creature、max height 和部分下降行为。
当前 menu 通常列出全部 deployable aids 与最安全的 non-deploy aid；slip modifier 会影响选择，不是
孤立显示数字。

### 验证

运行 formatter、`make -j2 json-check`、Mod `--check-mods`。在多 Z-level fixture 覆盖向下高度、
部分下降、item 消耗、部署碰撞、veh part length、terrain flag、trait/character condition、滑落、
体力/伤害 cost 与返回难度。新增边界需要 climbing focused tests 和存档 reload 检查。

## 历史与归属

清单中的已接受贡献者为：Killa-bite, thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `997faf1bea95578f5e2960f8dc83e65303b4e20c8d8c8d4c01ebe1e383e235b4`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/CLIMBING.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/CLIMBING.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/CLIMBING.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
