---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: mods.complete-json-eoc-mod
title: 完整 JSON/EOC Mod 教程
language: zh_CN
status: active
doc_type: tutorial
audiences:
- new-contributor
- experienced-contributor
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: LYHGLYTX
source_paths:
- data/AGENTS.md
- data/mods/AGENTS.md
- doc/MODDING.md
- data/mods/TEST_DATA/modinfo.json
- data/mods/TEST_DATA/effect_on_condition.json
- Makefile
- data/reference/json/ccb_json_object_types.json
- data/reference/json/ccb_eoc_conditions.json
- data/reference/json/ccb_eoc_effects.json
source_symbols: []
source_queries: []
source_fingerprint: 07702c94c6abf44a4ce57494f396a161ccbd4e8a072625d8731c2d659ddd75b6
authority: source-and-tests
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 9bfbec4adf55ce95bbad4bf3b6d1b8755882c8d3c10366a7450446fd8f96feee
prerequisites:
- json.overview
- eoc.overview
depends_on:
- json.validation
- eoc.nesting
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; tutorial example is maintained in CCB-Docs.
example_validation_ids:
- docs-json-eoc-example
- json-load
- json-mod-load
api_version: contract-inventory-v1
deprecated: false
deprecation_replacement: null
risk_group: mods
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/968
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/mods/complete-json-eoc-mod/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/mods/complete-json-eoc-mod/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/mods/complete-json-eoc-mod/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/mods/complete-json-eoc-mod/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: data/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/AGENTS.md
- path: data/mods/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/mods/AGENTS.md
- path: doc/MODDING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/MODDING.md
- path: data/mods/TEST_DATA/modinfo.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/mods/TEST_DATA/modinfo.json
- path: data/mods/TEST_DATA/effect_on_condition.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/mods/TEST_DATA/effect_on_condition.json
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/Makefile
- path: data/reference/json/ccb_json_object_types.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/reference/json/ccb_json_object_types.json
- path: data/reference/json/ccb_eoc_conditions.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/reference/json/ccb_eoc_conditions.json
- path: data/reference/json/ccb_eoc_effects.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/reference/json/ccb_eoc_effects.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28mods.complete-json-eoc-mod%29%3A+&body=Document+ID%3A+mods.complete-json-eoc-mod%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 完整 JSON/EOC Mod 教程

本教程的维护样例位于 CCB-Docs 的 `examples/complete-json-eoc-mod/`，包含两个文件：

```text
complete-json-eoc-mod/
├── modinfo.json
└── eocs.json
```

## 1. 声明 Mod

`modinfo.json` 是完整 JSON 数组；ID 使用项目专用前缀，并明确依赖 core `dda`：

```json
[
  {
    "type": "MOD_INFO",
    "id": "ccb_docs_json_eoc_example",
    "name": "CCB Docs JSON/EOC Example",
    "authors": [ "CCB contributors" ],
    "description": "A minimal contract-tested EOC mod used by the bilingual developer documentation.",
    "category": "misc_additions",
    "dependencies": [ "dda" ]
  }
]
```

## 2. 添加 EOC

`eocs.json` 定义一个不会自动触发的 activation EOC，因此加载样例不会改变正常游戏流程：

```json
[
  {
    "type": "effect_on_condition",
    "id": "EOC_CCB_DOCS_HELLO",
    "eoc_type": "ACTIVATION",
    "condition": { "math": [ "1 == 1" ] },
    "effect": [ { "u_message": "The CCB Docs example EOC ran." } ]
  }
]
```

## 3. 验证维护样例

在 CCB-Docs 根目录运行；把路径替换为包含 PR #566 提交的 CCB clone：

```sh
# validation: docs-json-eoc-example
python3 scripts/check_json_eoc_example_mod.py --source-repo /path/to/Cataclysm-Cleanwater-Bomb
```

该检查真实解析两个 JSON 文件，并确认 `MOD_INFO`、`effect_on_condition`、`math`、
`u_message` 都存在于固定提交的生成清单。它刻意不声称执行了游戏 loader。

在 CCB 根目录运行基础仓库检查：

```sh
# validation: json-load
make -j2 json-check
```

当前 `json-check` 不扫描 CCB-Docs 外部样例。最终发布前还必须把目录放入 CCB 支持的
第三方 Mod 位置，并调用真实 loader：

```sh
# validation: json-mod-load
ccb_source=/path/to/Cataclysm-Cleanwater-Bomb
ccb_example_user=/tmp/ccb-docs-example-user
mkdir -p "$ccb_example_user/mods"
cp -R examples/complete-json-eoc-mod "$ccb_example_user/mods/ccb_docs_json_eoc_example"
"$ccb_source/cataclysm" --basepath "$ccb_source/" --userdir "$ccb_example_user/" --check-mods ccb_docs_json_eoc_example
```

`--check-mods` 成功后，再在测试世界中启用 `dda` + 本 Mod，验证实际触发行为并保存日志。

## 4. 扩展时保持可验证

- 每个顶层 `type` 先在[对象类型注册表](../reference/json-object-types.md)中确认。
- 每个条件/效果键分别在[条件](../reference/eoc-conditions.md)和
  [效果](../reference/eoc-effects.md)注册表中确认。
- 不把 `lexical_only` 样例当作最小有效契约。
- ID 保持稳定并加 Mod 前缀；依赖必须显式声明。
- 添加行为前先复制最小 EOC，逐层增加嵌套、变量和 talker，并在真实 loader 中测试。

## 5. 声明式地图连接：Railroads 示例

铁路地图、车辆原型和车站入口可以使用静态 JSON。新增玩法行为遵循 Lua Platform v1（`require("ccb")`）；本节不引入另一个行为运行时。

[CCB PR #968](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/968) 尚未合并。以下字段已经在该 PR 的源码和原生回归中验证，发布前应再次核对最终合并提交。固定 `city_building` 与固定 `overmap_special` 的 `connections` 使用相同格式：

```json
"connections": [
  { "point": [ 0, 0, 0 ], "terrain": "railroad", "connection": "local_railroad", "from": [ 0, 1, 0 ] },
  { "point": [ 0, 5, 0 ], "terrain": "railroad", "connection": "local_railroad", "from": [ 0, 4, 0 ] }
]
```

`point` 位于站房占地之外；相邻的 `from` 指出站房一侧，连接方向随特殊建筑旋转。使用区域 `rail_connection` 的入口寻找可达的既有铁路；早于区域路网生成的车站入口参与后续路网生成。没有可达线路时仅留下朝向车站的短轨，不保证联网。普通公路仍连接原有城市目标。

检查应同时包含真实加载、大地图双向连接及局部钢轨和车辆通行；生成清单中的内容指纹刷新不代表新增 JSON 类型或 EOC 能力，也不证明车辆能通过站口。旧存档中的已生成车站不会自动重建。具体数据和验收边界见源码仓库的 `data/mods/railroads/README.md`。

后续内容与验收分别见 [PR #964](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/964)、[PR #969](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/969)、[PR #970](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/970) 和 [PR #971](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/971)。组合批次在固定种子 3404 下通过 12 个原生测试、29,865 条断言，覆盖车辆实际生成、进出站、曲线与道岔、桥梁和平交道、发动机启动与耗油及磁盘读档后继续行驶。验收复用了兼容的 Curses/Lua Platform v1 原生缓存；完整构建 CI 和人工 UI 驾驶仍待完成。这些源码 PR 合并前，文档保持草稿，发布前应同步最终提交及验收结果。
