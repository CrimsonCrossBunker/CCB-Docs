---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.artifacts
title: 旧文档迁移草稿：artifacts
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
- doc/JSON/ARTIFACTS.md
- src/relic.cpp
- src/relic.h
- data/json/artifact/relic_procgen_data.json
- data/json/artifact/premade_artifacts.json
source_symbols:
- relic_procgen_data::load
- relic_procgen_data::generation_rules::load
- relic_charge_template::load
source_queries: []
source_fingerprint: ad2b5a81653c650736c14c7353edf81b77620c498c521c6ccdcb628e6b7c3fc5
authority: docs-explanation
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: c5ea9a0faad65d7cd2f6686be43ccd9ae63d9c8e079dd44adfb2b0b5441c31a9
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/artifacts/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/artifacts/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/artifacts/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/artifacts/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: doc/JSON/ARTIFACTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/JSON/ARTIFACTS.md
- path: src/relic.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/relic.cpp
- path: src/relic.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/relic.h
- path: data/json/artifact/relic_procgen_data.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/json/artifact/relic_procgen_data.json
- path: data/json/artifact/premade_artifacts.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/json/artifact/premade_artifacts.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.artifacts%29%3A+&body=Document+ID%3A+json.artifacts%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：artifacts

本页是 `json.artifacts` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.artifacts`
- Target: `reference/json/artifacts.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/artifacts/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.artifacts | doc/JSON/ARTIFACTS.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## Relic 与 procedural artifact

Artifact 是 base item 加上 relic data；预制 relic 与 `relic_procgen_data` 是不同路径。procgen
dataset 提供 weighted base items、charge templates、active spells、passive enchantment values 和
type weights，generation rules 决定 power budget、attribute 上限、negative power 与 resonance。

### Procgen lists

所有 weighted entry 都要求 weight。passive entry 要求 enchantment value type，可设置 min/max、
increment、power_per_increment 和 ench_has；active entry 要求 spell_id，并可设置 level/power 与
ench_has。items entry 要求 item，type_weights 要求可用 value。dataset check 会验证 active spell，
但不能证明 power、item suitability 或所有 enchantment consumer 都合理。

### Charges

每个 charge template 包含 max_charges、charges、charges_per_use 的 range/power，另有
recharge_type 与 time。生成时初始 charges 被 clamp 到 max，time 在范围内随机选择。当前 procgen
template loader 不读取旧文档列出的 `recharge_condition`；该字段存在于生成后的 runtime charge
info，不应伪装成此 JSON 输入契约。

recharge type 与 ench_has 的有效 enum 以 `relic.cpp` 为准。active effect 有多个 spell 时共享一次
activation 的 charge cost；activation requirement 的组合行为必须用当前 generator 验证。

### Power、resonance 与验证

Power 是 generator 的选择预算，不是自动平衡证明。resonant generation rule 把最终 power 接入
当前 resonance runtime；阈值、效果和 lore 属于行为/设计契约，不能只从旧说明复制。

运行 formatter、`make -j2 json-check`、Mod `--check-mods`，固定 RNG seed 生成大量样本，检查空
weighted list、无效 spell/item、charge bounds、负面/正面预算、activation positions、存档 reload
和 resonance。变更 generator 时加入 deterministic distribution 与 consistency tests。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `ad2b5a81653c650736c14c7353edf81b77620c498c521c6ccdcb628e6b7c3fc5`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/ARTIFACTS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/ARTIFACTS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/ARTIFACTS.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
