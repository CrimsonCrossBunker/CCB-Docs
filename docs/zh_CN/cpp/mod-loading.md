---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.mod-loading
title: Mod 加载子系统
language: zh_CN
status: stale
doc_type: reference
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
last_human_reviewer: Pending human review
source_paths:
- src/mod_manager.h
- src/mod_manager.cpp
- src/worldfactory.cpp
- tests/worldfactory_test.cpp
source_symbols:
- class mod_manager
source_queries: []
source_fingerprint: ff3eec7e585a12184cf37c37516cf7763596e38751f9ae58ff38a67f7106a9a7
authority: source-and-tests
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 6a5379b1d791d0685dd13a81b84bff6f036d60fd00f92f78e1e3b782671038b8
prerequisites:
- compatibility.mods
depends_on:
- cpp.save
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
- json-load
- lua-contract
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: mod-loading
risk_level: high
pending_source_pr: null
stale_reason: 'Source paths changed after d32b9cc880a8: src/mod_manager.cpp'
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/mod-loading/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/mod-loading/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/mod-loading/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/mod-loading/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: src/mod_manager.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/mod_manager.h
- path: src/mod_manager.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/mod_manager.cpp
- path: src/worldfactory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/worldfactory.cpp
- path: tests/worldfactory_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/worldfactory_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.mod-loading%29%3A+&body=Document+ID%3A+cpp.mod-loading%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Mod 加载

## 职责

`mod_manager` 发现 `MOD_INFO`、构建依赖图、选择可用/默认 Mod、记录各 world 的有序
active list、应用声明的 Mod migration/removal，并向数据 loader 提供有序 source set。

## 入口点

阅读 `src/mod_manager.h`、`src/mod_manager.cpp`。`refresh_mod_list`、`load_modfile`、
`load_mods_list`、`check_mods_list` 与 `worldfactory` 的创建/读取是主要入口。

## 数据所有权

manager 拥有发现的 `MOD_INFORMATION`、dependency state 与 migration map；`WORLD` 拥有
active Mod ID 顺序；各 factory 拥有从这些 Mod path 加载的具体对象。

## 依赖

Mod 加载依赖 filesystem path、`modinfo.json`、dependency-tree 规则、worldfactory、JSON
dispatch、稳定 ID、obsoletion/migration data、localization 与可选 Lua manifest。

## 生命周期

启动时发现 core/user Mod 目录，验证 metadata/dependency；world 选择有序集合；协调缺失/
重命名 Mod；随后按顺序加载数据和脚本；列表随 world 持久化。

## 不变量

Mod ID 唯一有效；不能依赖自身；dependency 位于 dependent 前；world order 无重复；
缺失 Mod 需明确 migration 或用户决定；source attribution 保留 Mod origin。

## 扩展点

metadata、dependency、conflict、obsoletion 与 migration 用数据表达。新 loader phase 必须
保持确定顺序、失败诊断、来源归属和 world 检查。

## 序列化

`mods.json` 保存 world 的有序 Mod ID，manager registry 重新发现。重命名/移除需提供
migration，不能静默重写或破坏已有 world。

## 测试

使用 `tests/worldfactory_test.cpp`、JSON loading、dependency error、duplicate ID、missing
Mod、migration、conflict 和完整 example-Mod load；含 Lua 时加入 manifest 验证。

## 性能

发现与 JSON load 是启动成本。避免重复遍历目录、不稳定排序，以及为一个 metadata
查询重载全部 registry。

## CCB 差异

CCB bundled Mod、migration table、Lua v5 manifest 与接受的上游内容构成自己的兼容集。
不能替换成其他项目的默认 Mod list 或加载政策。

## 技术债务

发现、用户决定、依赖解析和数据加载通过启动流程耦合。未来拆分必须先保持准确顺序与
诊断，再讨论行为变化。
