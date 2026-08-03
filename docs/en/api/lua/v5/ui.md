---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.v5.ui
title: Portable Lua UI
language: en
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
last_human_reviewer: LYHGLYTX
source_paths:
- data/lua/README.md
- data/lua/manifest.schema.json
- data/lua/types/ccb_api_v5.d.lua
- data/lua/reference/ccb_public_api_v5.json
- data/lua/reference/ccb_public_api_v5_coverage.json
- tools/lua_api/README.md
source_symbols:
- ctx:environment()
source_queries: []
source_fingerprint: 30a19e6cbd8c6709ac5ccda80fe349e9459ddaccd8d3dc96507ee282c17f48cb
authority: api-contract
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 782c93e819b86b219cd3df29162a540afad030ae56da6d60f6d4bb207357f970
prerequisites:
- api.lua.v5.lifecycle
- api.lua.v5.capabilities
depends_on:
- api.lua.v5.reference.classes
- api.lua.v5.reference.methods
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/ui/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/ui/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/ui/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/ui/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: data/lua/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/README.md
- path: data/lua/manifest.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/manifest.schema.json
- path: data/lua/types/ccb_api_v5.d.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/types/ccb_api_v5.d.lua
- path: data/lua/reference/ccb_public_api_v5.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/reference/ccb_public_api_v5.json
- path: data/lua/reference/ccb_public_api_v5_coverage.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/reference/ccb_public_api_v5_coverage.json
- path: tools/lua_api/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tools/lua_api/README.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28api.lua.v5.ui%29%3A+&body=Document+ID%3A+api.lua.v5.ui%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Portable Lua UI

`ui.page` registers a semantic page, not pixel placement. One implementation is rendered by
the ImGui page host on Android/desktop Tiles or the terminal ImTui fallback. A Mod must not
import a renderer backend.

## Pages and slots

The descriptor form supports `title`, `category`, `order`, and these slots:

- `main.extensions`
- `ingame.extensions`
- `settings.mods`
- `debug.tools`

The string-title form remains compatible and defaults to main-menu and in-game Extensions.
A stable page id preserves selection across hot reload. `ui.open`, `ui.back`, and `ui.close`
queue navigation until the current callback returns.

```lua
ui.page("my_mod.settings", {
    title = i18n.gettext("My Mod"),
    category = "settings",
    order = 50,
    slots = { "main.extensions", "ingame.extensions", "settings.mods" },
}, function(ctx)
    ctx:heading(i18n.gettext("Settings"))
    local env = ctx:environment()
    ctx:text(env.profile .. " / " .. env.input)
end)
```

## `ctx` lifetime and stable ids

`ctx` is valid only in the current draw callback. Never retain it in a global, closure, event,
or task. Put persistent data in an appropriate `state` scope. Translated, dynamic, or repeated
controls must use `_id` forms that separate a stable id from visible text.

`ctx:environment()` reports profile, input, density, breakpoint, touch, hover, and keyboard
navigation semantics. Adapt or degrade through those values; do not use legacy
`ctx:platform()` to distinguish touch from desktop.

## Large lists and per-frame cost

A page callback may run each frame. Make bounded queries, render only required fields, and use
`virtual_list`/`virtual_list_rows` for large data. Cache only against explicit generations such
as `language_revision()` or a registry revision.

## Native HUD/sidebar boundary

There is no Lua `ui.hud`. Android's schema-6 HUD is a separate Java/native surface and never
calls Lua. API v5 `sidebar` widgets mount only in the native PC Widget sidebar. Use `ui.page`
for information that must be portable. See generated [classes](reference/classes.md) and
[methods](reference/methods.md) for the complete control contract.
