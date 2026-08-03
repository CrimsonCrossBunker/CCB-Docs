---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.v5.debugging
title: Lua 调试与契约验证
language: zh_CN
status: active
doc_type: how-to
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
last_human_reviewer: LYHGLYTX
source_paths:
- data/lua/README.md
- data/lua/manifest.schema.json
- data/lua/types/ccb_api_v5.d.lua
- data/lua/reference/ccb_public_api_v5.json
- data/lua/reference/ccb_public_api_v5_coverage.json
- tools/lua_api/README.md
source_symbols:
- check_public_contract.py
source_queries: []
source_fingerprint: 86ab8c697639288944692daea743e7470450d95825578f8964198c2bd0dbdc83
authority: api-contract
verified_commit: 501f84d20d4bf432dd7fec9b757f5af6a18dae36
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: f5953a3b1725321b7ef41ff313e9a5de3de53a5cd360c7322bbbb1e0cbcc8438
prerequisites:
- api.lua.v5.overview
depends_on:
- api.lua.v5.example-mod
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; generated contract and source paths at the verified commit.
example_validation_ids:
- lua-contract
- lua-docs
api_version: '5'
deprecated: false
deprecation_replacement: null
risk_group: lua-api
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/debugging/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/debugging/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/debugging/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/debugging/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/501f84d20d4bf432dd7fec9b757f5af6a18dae36
source_urls:
- path: data/lua/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/501f84d20d4bf432dd7fec9b757f5af6a18dae36/data/lua/README.md
- path: data/lua/manifest.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/501f84d20d4bf432dd7fec9b757f5af6a18dae36/data/lua/manifest.schema.json
- path: data/lua/types/ccb_api_v5.d.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/501f84d20d4bf432dd7fec9b757f5af6a18dae36/data/lua/types/ccb_api_v5.d.lua
- path: data/lua/reference/ccb_public_api_v5.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/501f84d20d4bf432dd7fec9b757f5af6a18dae36/data/lua/reference/ccb_public_api_v5.json
- path: data/lua/reference/ccb_public_api_v5_coverage.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/501f84d20d4bf432dd7fec9b757f5af6a18dae36/data/lua/reference/ccb_public_api_v5_coverage.json
- path: tools/lua_api/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/501f84d20d4bf432dd7fec9b757f5af6a18dae36/tools/lua_api/README.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28api.lua.v5.debugging%29%3A+&body=Document+ID%3A+api.lua.v5.debugging%0ALanguage%3A+zh_CN%0AVerified+commit%3A+501f84d20d4bf432dd7fec9b757f5af6a18dae36%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Lua 调试与契约验证

## 先区分失败阶段

| 阶段 | 常见证据 | 下一步 |
| --- | --- | --- |
| Manifest | 未知 capability、依赖顺序、id/version 不一致 | 对照 Schema 校验 `lua/manifest.json` |
| 候选加载 | 语法、模块路径、顶层非法调用 | 查 `debug.log`；旧运行时应继续工作 |
| 回调 | capability、参数、对象代次、超预算 | 查最新 runtime error 与对应生成条目 |
| UI | 过期 `ctx`、重复控件 id、不支持能力 | 用稳定 `_id`，每次 draw 使用新 `ctx` |
| 生成漂移 | generated diff 或 parity 失败 | 更新权威声明/注册后重新生成，禁止手改产物 |

`game.runtime_status()` 提供运行/世界代次、内存、注册数量、最新错误和回调耗时统计。
句柄问题先检查 `handle:status()`；事件、Hook、Callback 问题用各自 `list`/`describe`
发现运行时契约，不要依赖猜测的名称。

## 主仓库权威验证

在固定 CCB 源工作树运行：

```sh
# validation: lua-contract
python3 tools/lua_api/generate_public_contract.py --check
python3 tools/lua_api/check_public_contract.py
python3 tools/lua_api/check_luals_declarations.py
python3 tools/lua_api/check_examples.py --require-luac
python3 -m unittest discover -s tools/lua_api -p 'test_*.py'
```

它们分别检查可重现生成、Schema/注册对等、LuaLS 签名、完整示例 Mod 和工具回归。
`check_coverage.py` 的 CBN 能力映射不是 CCB 公开 API 文档覆盖分母；公开分母以
`ccb_public_api_v5_coverage.json` 为准。

## CCB-Docs 生成验证

```sh
# validation: lua-docs
python3 scripts/generate_lua_reference.py --source-repo /path/to/CCB --check --require-luac
python3 scripts/generate_catalog.py --check
python3 scripts/check_catalog.py --source-repo /path/to/CCB
python3 scripts/build_site.py --strict --include-drafts
python3 scripts/check_links.py --site-dir site --critical
```

任何失败都应从生成器或权威来源修复。生成页正文、catalog 派生前言和覆盖报告不得手改。
