## 当前 CCB Mod 模型

CCB Mod 是一个带 `MOD_INFO` 的数据包。运行时先解析可用 Mod、依赖与冲突，再按世界保存的
顺序加载 JSON；普通数据全部加载后，才加载命中的 `mod_interactions/`。JSON、EOC 与 Lua
可以并存，但各自仍受 loader、Schema、注册表和 Lua v5 契约约束。

### 最小目录

```text
ccb_example/
├── modinfo.json
├── items.json
└── lua/
    └── manifest.json   # 仅在使用 Lua 时需要
```

```jsonc
[
  {
    "type": "MOD_INFO",
    "id": "ccb_example",
    "name": "CCB Example",
    "authors": [ "Example author" ],
    "maintainers": [ "github-account" ],
    "description": "A small example Mod.",
    "category": "content",
    "dependencies": [ "dda" ]
  }
]
```

`id` 是世界 Mod 列表、依赖、交互目录与来源追踪使用的稳定标识，不能把改名当成显示文本
清理。当前 `MOD_INFORMATION` 还读取 `path`、`version`、`conflicts`、`core`、`obsolete`、
`loading_images` 与 `disable_other_loading_screens`。不要从旧表猜字段；以
`mod_manager::load_modfile` 和相邻第一方 `modinfo.json` 为准。Mod 不得依赖自身，`#` 也不是
合法 Mod ID 字符。

### 数据、依赖和加载顺序

普通 JSON 在 Mod 路径下递归发现，`mod_interactions` 延后处理，`lua/manifest.json` 不交给
JSON object loader。`dependencies` 表示必须先加载的 Mod；`conflicts` 用于阻止不兼容组合。
依赖只决定可用性和顺序，不会自动为被引用 ID 提供迁移，也不会替代显式兼容文件。

把对象按领域拆文件，而不是按加载顺序拆文件。Forward reference 只在相应 loader 明确支持
时成立。已发布 item、terrain、EOC、Lua service 等 ID 可能进入存档或其他 Mod；删除或
改名时必须检查 obsoletion/migration 机制与旧世界加载。

### 选择表达层

- 静态内容、配方、地图和注册对象优先用 JSON。
- 条件、效果、事件链与对话流程优先考虑 EOC。
- Lua 用于公开 Lua v5 契约允许的动态逻辑，并声明精确 capability。
- 只有公开数据契约无法表达且项目愿意维护该能力时才改 C++。

### 最小验证闭环

1. 用仓库 formatter 格式化改动 JSON，并运行 `make -j2 json-check`。
2. 用已构建游戏执行 `./cataclysm-tiles --check-mods ccb_example`（实际二进制名随构建而异）。
3. EOC 覆盖 true/false、talker、context 与重复执行；Lua 运行 manifest、语法、coverage 和示例检查。
4. 创建世界、保存、重新加载，并测试与声明依赖/冲突的真实组合。
5. PR 记录命令、平台、Mod 集、失败和未运行项；加载成功不等于玩法平衡或存档兼容。

配套阅读：[Mod 兼容](compatibility.md)、[Mod 本地化](localization.md)与
[仓库内 Mod 政策](../mods/in-repository-policy.md)。
