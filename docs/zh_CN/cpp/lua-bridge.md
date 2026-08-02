---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.lua-bridge
title: Native Lua bridge
language: zh_CN
status: active
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
- src/catalua_bindings.cpp
- src/catalua_ui_manifest.cpp
- src/catalua_ui_registry.cpp
- data/lua/types/ccb_api_v5.d.lua
- data/lua/manifest.schema.json
source_symbols:
- binding_catalog()
source_queries: []
source_fingerprint: 59689762f3a441f601bafe6f1cb728eb9246dc87dfd7788a8002d7b95d6606a9
authority: api-contract
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 7e06bb671d6532093277a532546614dadca86a79266039f03d3e5bc7338a800f
prerequisites:
- cpp.mod-loading
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- lua-contract
- cpp-tests
api_version: '5'
deprecated: false
deprecation_replacement: null
risk_group: lua-api
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/lua-bridge/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/lua-bridge/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/lua-bridge/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/lua-bridge/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: src/catalua_bindings.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/catalua_bindings.cpp
- path: src/catalua_ui_manifest.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/catalua_ui_manifest.cpp
- path: src/catalua_ui_registry.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/catalua_ui_registry.cpp
- path: data/lua/types/ccb_api_v5.d.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/lua/types/ccb_api_v5.d.lua
- path: data/lua/manifest.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/lua/manifest.schema.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.lua-bridge%29%3A+&body=Document+ID%3A+cpp.lua-bridge%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Native Lua bridge

## 职责

bridge 嵌入 Lua 并暴露版本化 CCB Lua API：验证 manifest/capability，构建 namespace 与
强类型 value/handle，安装有界 registry snapshot，路由 event/hook/callback/service，并
执行 read/write/action 权限。

## 入口点

阅读 `src/catalua_bindings.cpp`、`src/catalua_ui_manifest.cpp`、
`src/catalua_ui_registry.cpp`，再进入各领域 `catalua_ui_*.cpp`。公共形状必须与
`data/lua/types/ccb_api_v5.d.lua`、manifest schema 和生成 native inventory 交叉一致。

## 数据所有权

引擎拥有 native object 与 Lua state。Lua 只获得脱离所有权的不可变 snapshot、value
type 或受检查 handle，绝不获得借用 native pointer。manifest 拥有脚本声明 capability，
runtime 拥有执行责任。

## 依赖

bridge 依赖 embedded Lua/sol、native registry/service、manifest JSON、API version、
LuaLS declaration、生成 inventory、event/callback registry 与 Lua contract test。

## 生命周期

runtime 创建 state，按依赖顺序读取验证 manifest，只安装获准 API surface，加载 module，
分派有界 event/callback，最后在 native owner 消失前销毁 state。

## 不变量

manifest ID/version/capability 有效；capability dependency 成立；API version 受支持；
native registration、LuaLS 与 inventory parity；handle 检查身份/生命周期；没有借用
pointer 跨入 Lua。

## 扩展点

公共 symbol 加到聚焦 registration module，在 LuaLS 声明、进入 inventory、按最小
capability gate，并添加 parity/behavior/example test。生成 reference 必须来自这些契约，
不能来自说明 prose。

## 序列化

Lua state 不是原始存档 snapshot。脚本只能通过支持的 scoped-state service 与可序列化
value 持久化；native handle/callback 读取后重新获取。

## 测试

运行 LuaLS parse、native-registration parity、coverage、manifest schema、Lua syntax、
callback/disabled-build test 和完整 example-Mod load；公开未记录 symbol 必须保持 0。

## 性能

跨语言调用、snapshot 构造和 event fan-out 都有成本。限制集合大小，不要每 frame 重建
registry，callback 保持确定且短。

## CCB 差异

Lua API v5、capability gate、typed handle、snapshot、hook 与 callback 都是 CCB 契约，
不能与 CDDA、CBN 或历史 Lua API 互换。

## 技术债务

领域 module 多，增加 parity 与审查负担。应保持单一生成契约链，并显式 deprecate 公共
symbol，而不是遗留 alias 或未记录 registration。
