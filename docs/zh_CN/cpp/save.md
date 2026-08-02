---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.save
title: 存档子系统
language: zh_CN
status: draft
doc_type: reference
audiences:
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: Pending human review
source_paths:
- src/savegame.cpp
- src/savegame_json.cpp
- src/savegame_legacy.cpp
- tests/worldfactory_test.cpp
source_symbols:
- const int savegame_version = 39;
source_queries: []
source_fingerprint: 50026553eb625ef2ef0861270fc41c0a232cfaa1e00e471a34e5b59055aa0cb5
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 1539fd64a9a2b9434540c1e4f16a32720c008c1fdefe17c80a5cee834eae7a3a
prerequisites:
- compatibility.save
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: save-compatibility
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/save/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/save/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/save/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/save/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/dbaedf8357408ae6f96309732d6e087e9b878e18
source_urls:
- path: src/savegame.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/savegame.cpp
- path: src/savegame_json.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/savegame_json.cpp
- path: src/savegame_legacy.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/savegame_legacy.cpp
- path: tests/worldfactory_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/tests/worldfactory_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.save%29%3A+&body=Document+ID%3A+cpp.save%0ALanguage%3A+zh_CN%0AVerified+commit%3A+dbaedf8357408ae6f96309732d6e087e9b878e18%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 存档系统

## 职责

存档系统把世界持久化为带版本 JSON 与辅助文件，包括 game/global state、avatar/NPC、
monster、overmap、submap、vehicle、item、activity、faction、mission、map memory 和 Mod
顺序，同时读取仍受支持的旧表示。

## 入口点

从 `src/savegame.cpp`、`src/savegame_json.cpp`、`src/savegame_legacy.cpp` 开始。常量
`savegame_version`、解析后的 `savegame_loading_version`、顶层 game load/store，以及各
类型 `serialize` / `deserialize` 对构成兼容边界。

## 数据所有权

每个运行时 owner 序列化自己的持久状态，world directory 拥有文件集合。save 层协调
记录，但不能成为第二运行时 owner；cache、pointer、window 与局部坐标视图读取后重建。

## 依赖

保存依赖 filesystem/path API、JSON archive、worldfactory、map/overmap 存储、每个持久
子系统的 serializer、ID、Mod order 与 migration/default 逻辑。

## 生命周期

新世界使用当前版本；保存写入版本标记与记录；读取识别 stored version，应用字段默认/
legacy 转换，重连 ID 与所有权，重建缓存，然后返回活跃世界。

## 不变量

读取受支持旧字段不能破坏数据；对象只由 owner 序列化一次；ID 与绝对坐标稳定；失败
写入不能伪装成完整存档；只有具备有意迁移支持时才提升版本。

## 扩展点

序列化放在 owning type 旁，使用命名字段和安全默认，仅在必要时增加显式版本 migration。
不能保存 raw pointer 或派生 cache。

## 序列化

本子系统本身就是序列化契约。字段变化必须说明 writer、reader、default、影响旧版本、
移除期限与往返证据；删除/重命名必须提供兼容策略。

## 测试

使用聚焦 serializer/world 测试和可用旧存档 fixture，验证当前往返、缺失字段、错误输入
处理和被触及最旧版本。

## 性能

save/load 会遍历大量世界状态并大量分配。保持 streaming 边界，避免二次复杂度 ID 重连，
用大型世界测量且不能用计时掩盖失败。

## CCB 差异

CCB 当前版本与 legacy reader 只对 CCB 权威。复制上游 serializer 前必须比较字段历史、
Mod migration 与 world layout。

## 技术债务

兼容逻辑分散在类型 serializer 与版本检查。每个新例外应局部化并记录，不能把宽格式
重写与无关修改混在一起。
