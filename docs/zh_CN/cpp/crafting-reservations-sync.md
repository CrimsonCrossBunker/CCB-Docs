---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.crafting-reservations-sync
title: 制作材料预留与临时库存同步草稿
language: zh_CN
status: draft
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
- src/crafting.cpp
- src/craft_reservation_search.cpp
- src/temp_crafting_inventory.cpp
- src/lua_platform_crafting.cpp
- src/lua_platform_items.cpp
- src/veh_interact.cpp
- src/version.cmake
source_symbols:
- Character::crafting_inventory
- veh_interact::installation_requirement_availability
source_queries:
- independent_contents
- zero_move_dispatches
- CMAKE_MATCH_1
source_fingerprint: 2b68b6f557a1b5934dd6ce9719a7776f979f0e96ac481021c9f39d680105f052
authority: api-contract
verified_commit: 0a9822532c83189bc431631fd5e2b05a632460c6
verified_at: '2026-10-14'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 16b662752793ebd42f81224f79c63633f078f476be19cf928de5097e8189e9ba
prerequisites:
- cpp.lua-bridge
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- lua-contract
api_version: '1'
deprecated: false
deprecation_replacement: null
risk_group: lua-api
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/crafting-reservations-sync/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/crafting-reservations-sync/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/crafting-reservations-sync/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/crafting-reservations-sync/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/0a9822532c83189bc431631fd5e2b05a632460c6
source_urls:
- path: src/crafting.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/0a9822532c83189bc431631fd5e2b05a632460c6/src/crafting.cpp
- path: src/craft_reservation_search.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/0a9822532c83189bc431631fd5e2b05a632460c6/src/craft_reservation_search.cpp
- path: src/temp_crafting_inventory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/0a9822532c83189bc431631fd5e2b05a632460c6/src/temp_crafting_inventory.cpp
- path: src/lua_platform_crafting.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/0a9822532c83189bc431631fd5e2b05a632460c6/src/lua_platform_crafting.cpp
- path: src/lua_platform_items.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/0a9822532c83189bc431631fd5e2b05a632460c6/src/lua_platform_items.cpp
- path: src/veh_interact.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/0a9822532c83189bc431631fd5e2b05a632460c6/src/veh_interact.cpp
- path: src/version.cmake
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/0a9822532c83189bc431631fd5e2b05a632460c6/src/version.cmake
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.crafting-reservations-sync%29%3A+&body=Document+ID%3A+cpp.crafting-reservations-sync%0ALanguage%3A+zh_CN%0AVerified+commit%3A+0a9822532c83189bc431631fd5e2b05a632460c6%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 制作材料预留与临时库存同步草稿

本页对应尚未合并的制作同步分支，保持草稿。源代码与测试是行为依据，最终组合版本的编译、Mod 加载和平台 CI 尚未验收。

## 预留工具的范围

无人值守制作步骤按实际物品身份预留工具、材料及相关供能资源，其他自动操作应跳过被预留对象。暂停后保留原因，重复检查不会重复发送相同提示。

CCB 的穿戴存储与上游旧库存结构不同：穿戴容器的独立存储物品分别作为工具单元，工具的弹匣和配件仍属于同一单元。一个预留工具不会使同背包里的独立工具全部消失。移动含预留对象的容器仍受到整体保护。

## 临时库存与 Lua

临时制作库存保存对现有物品的引用，以及必要的临时伪工具或副本。它不是可持久化的玩家库存。读取期间引用对象必须有效；不能借快照改变持有者或绕过预留。

Lua 仍通过 Platform v1 的现有制作、物品和任务服务调用行为。此次适配更新营地及 Lua 的库存查询类型，并保留材料托管、退款、身份核对和重复结算限制，没有增加第二套 Lua 接口。

## 载具和区域搬运

载具安装界面先建立一次可用材料类型快照，排除不可能满足的部件，再执行完整数量、工具品质及角色检查。新增临时库存不应使每个部件重复扫描数千件物品。

区域搬运保留 CCB 的直接交付流程和批量搬运耗时。小推车拒绝继续装载时可尝试角色携带；每回合的零移动点循环有上限，转交路线前清空计数。

## 验证边界

本组 288 个案例已有通过证据：完整运行通过 287 个，最后一个修正夹具后单独通过 26 条断言；另一次聚焦运行通过 8 个案例、89 条断言。检查包含材料预留、临时库存、有限水源、安装材料查询、区域搬运和 Lua 托管恢复。不要把这些局部证据写成新组合版本、所有平台或旧存档的完整验收。

版本头文件由 CMake 生成。版本值不变时保留其时间戳，防止相同内容反复触发编译；真实生成器的回归测试修复前失败、修复后通过。

来源及署名：[CDDA #88559](https://github.com/CleverRaven/Cataclysm-DDA/pull/88559): dobbry-vechur; [CDDA #88647](https://github.com/CleverRaven/Cataclysm-DDA/pull/88647): dobbry-vechur; [CDDA #88606](https://github.com/CleverRaven/Cataclysm-DDA/pull/88606): Curtis Merrill; [CDDA #88656](https://github.com/CleverRaven/Cataclysm-DDA/pull/88656): dobbry-vechur; [CDDA #88767](https://github.com/CleverRaven/Cataclysm-DDA/pull/88767): dobbry-vechur。Responsible human: LYHGLYTX。
