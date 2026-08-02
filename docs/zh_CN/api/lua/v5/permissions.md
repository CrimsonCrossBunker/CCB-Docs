---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.v5.permissions
title: 权限与信任模型
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
- capability-gating
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
translation_source_fingerprint: 97e992a62f3f105811f0d23a9fdbeac395bb0c6d73ff166b944e26578916a06f
prerequisites:
- api.lua.v5.capabilities
depends_on:
- api.lua.v5.reference.permissions
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
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/permissions/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/permissions/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/permissions/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/permissions/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28api.lua.v5.permissions%29%3A+&body=Document+ID%3A+api.lua.v5.permissions%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 权限与信任模型

Lua v5 使用 capability gating；没有独立 `permissions` Manifest 字段，`capabilities` 就是
权限声明。权限绑定“来源身份”，不是当前函数、页面 id 或调用栈。

## 身份传播

- `require` 在当前来源环境执行。
- `modules.import` 导入提供者源码，但代码以消费者 capability 执行。
- `services.call` 在提供者身份和预算下执行服务，再复制结果给消费者。
- 事件、调度任务、Hook、Callback、action-menu 和 sidebar 回调恢复注册来源身份。
- 用相同 id 替换页面不会取得原页面来源权限。

因此跨 Mod 共享能力时，源码复用用 `modules.import`，需要权限隔离的操作用 `services`。

## 写与交互边界

`game.write` 不是任意内存访问。每个操作仍会验证 id、坐标空间、对象代次、范围、调用
阶段和结果上限。危险当前输入动作还需要 `game.actions.dangerous`，并由原生界面显示
来源与动作的一次性确认。许多交互、移动和写操作只允许在活跃回调内调用。

Lua 标准库环境不提供 `io`、`os`、`debug`、原生 C 模块或任意动态代码/文件加载。
不过这仍是应用脚本隔离，不是执行不受信任下载代码的安全沙箱：安装 Lua Mod 应采用
与安装普通游戏 Mod 相同的信任判断。

## 审查清单

1. Manifest 是否只请求代码实际使用的 capability？
2. 写操作是否能改为只读快照或安全动作队列？
3. 跨来源调用是否应由 service 保留提供者身份？
4. 是否在日志或 UI 中泄露本地路径、存档内容或不必要的状态？
5. 是否假定 capability 能绕过参数、生命周期或代次验证？（不能。）

机器契约见[权限模型参考](reference/permissions.md)。
