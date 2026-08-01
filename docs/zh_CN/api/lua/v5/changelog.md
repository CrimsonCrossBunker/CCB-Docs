---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.v5.changelog
title: Lua API 变更记录
language: zh_CN
status: draft
doc_type: reference
audiences:
- mod-author
- api-user
- experienced-contributor
- maintainer
owners:
- CCB Lua API maintainers
reviewers:
- Documentation reviewers
- Lua API reviewers
review_interval_days: 60
last_human_reviewer: Not yet reviewed (draft)
source_paths:
- data/lua/README.md
- data/lua/manifest.schema.json
- data/lua/types/ccb_api_v5.d.lua
- data/lua/reference/ccb_public_api_v5.json
- data/lua/reference/ccb_public_api_v5_coverage.json
- tools/lua_api/README.md
source_symbols:
- native_luals_callable_parity
source_queries: []
source_fingerprint: 86ab8c697639288944692daea743e7470450d95825578f8964198c2bd0dbdc83
authority: api-contract
verified_commit: 3ac0bd7f356b30b880dc655f3006ebf1cbda9cfd
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 39c073b18b6732436210edee27a6ab51c66015ee4864fd7f0c7173416ec41363
prerequisites:
- api.lua.v5.overview
depends_on:
- api.lua.v5.migration
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; generated contract and source paths at the verified commit.
example_validation_ids: []
api_version: '5'
deprecated: false
deprecation_replacement: null
risk_group: lua-api
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/565
stale_reason: null
search:
  exclude: true
---

# Lua API 变更记录

本页只记录可由仓库提交和生成契约证明的 API 变化。当前生成契约把历史无法精确追溯的
公开 callable 标为 `since: untracked-before-or-at-v5`；这不是具体发布日期，不能推测。

## API v5 契约基线（待合并）

| 字段 | 值 |
| --- | --- |
| 固定提交 | `3ac0bd7f356b30b880dc655f3006ebf1cbda9cfd` |
| 源 PR | [CCB #565](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/565) |
| API 版本 | 5 |
| 唯一公开符号 | 2,806 |
| 未文档化 | 0 |
| 原生/LuaLS callable parity | 100% |
| Manifest Schema/runtime/LuaLS parity | true |

该基线首次把 modules、namespaces、classes/fields、functions、methods、properties、
operators、enums、events/fields、hooks、callbacks、capabilities、permission model 和
Manifest fields 合入统一公开清单，并为每条记录生成文档 id 与来源。

## 后续如何更新

公开 API 变化必须同时更新权威注册/声明/Schema、测试、生成 contract/coverage、示例（如
适用）和本变更记录。新增项写入真实 `since`；弃用项设置 `deprecated: true` 并给出
`deprecation_replacement`。禁止仅改生成 JSON 或生成页面。

源提交合并后，本页和所有 Lua 页面必须刷新为最终 master commit，重新生成并通过
[调试与验证](debugging.md)中的检查，才能从 draft 升为 active。
