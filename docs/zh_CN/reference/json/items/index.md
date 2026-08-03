---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.items
title: 旧文档迁移草稿：items
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
last_human_reviewer: LYHGLYTX
source_paths:
- doc/JSON/ITEM.md
- src/item_factory.cpp
- src/item_factory.h
- data/json/items/generic.json
- data/json/items/classes/gun.json
- tests/item_test.cpp
source_symbols:
- itype::load
- items::load
- islot_comestible::deserialize
source_queries: []
source_fingerprint: 8c6c2be386b3355ef5417fc38ec2aec753b5e70c63f0c5ed32d1276368406906
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: cba127e56f71350f0eed28cf4cae7557fd01aa8cd32cef2e60d57d16dc5e40f9
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: LunaGlaze, Standing-Storm, zihanZheng, Anton Simakov, EArias, RenechCDDA,
  dumb-kevin, thaelina; accepted inventory identities only. Source paths and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/items/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/items/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/items/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/items/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/JSON/ITEM.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/ITEM.md
- path: src/item_factory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/item_factory.cpp
- path: src/item_factory.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/item_factory.h
- path: data/json/items/generic.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/json/items/generic.json
- path: data/json/items/classes/gun.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/json/items/classes/gun.json
- path: tests/item_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/item_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.items%29%3A+&body=Document+ID%3A+json.items%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：items

本页是 `json.items` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.items`
- Target: `reference/json/items/index.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/items/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.items | doc/JSON/ITEM.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 当前 CCB 物品 JSON 模型

CCB 把可拾取实体统一加载为 `"type": "ITEM"`。通用字段由 `itype::load` 读取，
`subtypes` 再决定是否读取护甲、工具、枪械、弹药等 slot。旧文档中的字段表只能作为
定位入口；字段是否必需、默认值、取值范围和组合限制以当前 loader、注册表、测试及
[JSON object type 索引](../index.md)为准。

### 最小定义与稳定 ID

```jsonc
{
  "type": "ITEM",
  "id": "ccb_example_part",
  "name": { "str": "example part" },
  "description": "A component used by the documentation example.",
  "symbol": ";",
  "color": "light_gray",
  "weight": "100 g",
  "volume": "250 ml",
  "price": "1 USD",
  "price_postapoc": "10 cent",
  "material": [ "steel" ]
}
```

`id` 是存档、配方、item group、EOC 与 Mod 间的长期引用。已发布 ID 不应仅为了更整齐
而重命名；确需替换时，要先检查迁移/obsoletion 机制和存档兼容性。面向玩家的
`name`、`description` 应可翻译，不要把 ID 当显示文本。

### subtype 与 slot

当前 `itype::load_slots` 识别 `ARMOR`、`TOOL`、`PET_ARMOR`、`GUN`、`GUNMOD`、
`AMMO`、`MAGAZINE`、`COMESTIBLE`、`BOOK`、`BIONIC_ITEM`、`TOOLMOD`、`ENGINE`、
`WHEEL`、`SEED`、`BREWABLE`、`COMPOSTABLE`、`MILLING` 与 `ARTIFACT`。例如弹药定义
需要显式声明：

```jsonc
{
  "type": "ITEM",
  "id": "ccb_example_round",
  "copy-from": "223",
  "subtypes": [ "AMMO" ],
  "name": { "str_sp": "example round" },
  "ammo_type": "223"
}
```

- `subtypes` 控制本次定义读取哪些 slot 字段；不要因为父项拥有某个 slot 就省略子项意图。
- `PET_ARMOR` 与 `ARMOR` 不能同时声明；`GUNMOD` 已包含 tool-mod slot，不能再与
  `TOOLMOD` 同时声明。
- 同一物品可组合其他兼容 subtype，但每个 slot 都可能有自己的 mandatory 字段和
  finalize 检查。

### 通用字段与继承

常见通用字段包括尺寸/质量、价格、材质、显示、近战/投掷数据、flags、qualities、
`use_action`、pocket、variant 与变量。不要从一份示例推断所有字段：部分字段使用单位
字符串，部分读取稳定 ID，部分由专用 reader 校验。

`copy-from` 先复制父定义；顶层直接字段替换对应值，容器字段可在实现支持时用
`extend`/`delete`，数值或专用对象可能支持 `relative`/`proportional`。这些操作不是
所有字段的通用 Schema；详见[继承](../inheritance.md)，并从同一 subtype 的当前数据中
选择相邻样例。

### 修改与验证顺序

1. 在相邻第一方定义中确认 `type`、`subtypes`、字段形状和 ID 引用。
2. 对照 `itype::load` 与对应 slot 的 `deserialize`，确认 required/default/范围。
3. 只格式化本次改动文件，检查 formatter 没有扩大 diff。
4. 运行 `make -j2 json-check`；涉及 pocket、use action、配方或存档 ID 时再运行对应测试。
5. Mod 还应以实际 Mod 集执行 `--check-mods`，并记录未覆盖的平台或交互。

格式通过不代表 loader、ID 或玩法关系正确。Schema 覆盖不完整时，源码加载器和测试
始终优先。

## 历史与归属

清单中的已接受贡献者为：LunaGlaze, Standing-Storm, zihanZheng, Anton Simakov, EArias, RenechCDDA, dumb-kevin, thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `d32b9cc880a85480840d82cfa05d256c78a16615`；聚合源指纹为 `8c6c2be386b3355ef5417fc38ec2aec753b5e70c63f0c5ed32d1276368406906`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/ITEM.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/ITEM.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/ITEM.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
