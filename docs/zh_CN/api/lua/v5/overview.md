---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.v5.overview
title: Lua API v5 总览
language: zh_CN
status: active
doc_type: explanation
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
- Lua Mod API v5
source_queries: []
source_fingerprint: 86ab8c697639288944692daea743e7470450d95825578f8964198c2bd0dbdc83
authority: api-contract
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: dfef84a47a5a3b5ced5529956431c598a4dc1b404dd6461699079e9076e1fc94
prerequisites:
- architecture.overview
depends_on: []
redirect_from: []
supersedes:
- lua.v5.overview
license: CC-BY-SA-3.0
attribution: CCB contributors; generated contract and source paths at the verified commit.
example_validation_ids: []
api_version: '5'
deprecated: false
deprecation_replacement: null
risk_group: lua-api
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/overview/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/overview/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/overview/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/overview/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: data/lua/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/lua/README.md
- path: data/lua/manifest.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/lua/manifest.schema.json
- path: data/lua/types/ccb_api_v5.d.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/lua/types/ccb_api_v5.d.lua
- path: data/lua/reference/ccb_public_api_v5.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/lua/reference/ccb_public_api_v5.json
- path: data/lua/reference/ccb_public_api_v5_coverage.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/lua/reference/ccb_public_api_v5_coverage.json
- path: tools/lua_api/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tools/lua_api/README.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28api.lua.v5.overview%29%3A+&body=Document+ID%3A+api.lua.v5.overview%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Lua API v5 总览

!!! warning "草案契约"
    本页验证于 CCB 提交 `3ac0bd7f356b30b880dc655f3006ebf1cbda9cfd`，对应待合并的
    [CCB #565](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/565)。
    合并前不进入正式导航、搜索或 AI 索引。

Lua API v5 是 CCB 的版本化 Mod 脚本接口。它提供模块、服务、事件、调度、持久状态、
跨平台页面、类型化值与句柄、只读定义/快照查询，以及受 capability 约束的写操作。
Lua 不获得裸 C++ 指针；实时对象通过带运行时/世界代次的句柄访问，查询结果通常是有界、
分离的快照。

## 权威来源

文档不能自行定义 API。冲突时按以下顺序检查并修正文档：

1. `data/lua/manifest.schema.json`：Manifest 字段与 capability 组合。
2. `data/lua/types/ccb_api_v5.d.lua`：LuaLS 类型、参数与返回值。
3. 原生注册、事件/Hook/Callback 注册表：实际可调用表面。
4. `data/lua/reference/ccb_public_api_v5.json`：上述来源生成的统一公开契约。
5. `data/lua/reference/ccb_public_api_v5_coverage.json` 与测试：分母、对等性和覆盖证明。

## 当前可证明覆盖

| 指标 | 值 |
| --- | ---: |
| 唯一公开符号 | 2,806 |
| 已映射到生成参考的符号 | 2,806 |
| 未文档化公开符号 | 0 |
| 生成参考覆盖率 | 100% |
| 原生事件 / 字段 | 113 / 242 |
| Hook / Callback 对 | 52 / 38 |
| Capability / Manifest 字段 | 16 / 6 |

“100%”表示固定提交的公开分母都可在生成参考中定位，并不表示源 PR 已合并或页面已发布。

## 从哪里开始

- 新 Mod：先读[完整示例 Mod](example-mod.md)、[Capability](capabilities.md)与
  [生命周期](lifecycle.md)。
- 页面与输入：读[跨平台 UI](ui.md)。
- 订阅游戏状态变化：读[事件、Hook 与 Callback](events.md)。
- 出错或发生漂移：读[调试与验证](debugging.md)。
- 从旧 API 升级：读[迁移指南](migration.md)和[变更记录](changelog.md)。

## 生成参考

- [模块入口](reference/modules.md)、[命名空间](reference/namespaces.md)
- [类与记录](reference/classes.md)、[属性](reference/properties.md)
- [函数](reference/functions.md)、[方法](reference/methods.md)、
  [运算符](reference/operators.md)
- [枚举族](reference/enums.md)、[原生事件](reference/events.md)、
  [Hook](reference/hooks.md)、[Callback](reference/callbacks.md)
- [Capability](reference/capabilities.md)、[权限模型](reference/permissions.md)、
  [Manifest 字段](reference/manifest-fields.md)

生成页由 `scripts/generate_lua_reference.py` 从固定 CCB 提交重建，页内参数、返回值、
错误模式、引入版本、弃用状态、来源和示例记录禁止手改。
