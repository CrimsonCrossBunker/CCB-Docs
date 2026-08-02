## Mod 条件兼容数据

`mod_interactions/` 允许一个 Mod 只在另一个指定 Mod 已启用时加载补丁。它适合跨 Mod
引用、兼容 EOC、联合配方或定向覆盖，不等于一般依赖：interaction 缺席时基础 Mod 仍应
能够独立加载。

### 目录约定

假设当前 Mod ID 为 `xedra_evolved`，只在 `mindovermatter` 启用时需要加载兼容文件：

```text
Xedra_Evolved/
├── modinfo.json
├── ordinary-content.json
└── mod_interactions/
    └── mindovermatter/
        └── mom-compat-data.json
```

目录名必须与目标 Mod 的 ID 大小写精确一致。普通加载会递归排除整个
`mod_interactions`；所有活跃 Mod 的普通内容结束后，loader 再按活跃 Mod 顺序处理交互
目录。当前实现只检查第一层目标 ID，不支持用 `a/b/` 表达“两个 Mod 同时存在”。

### 来源与覆盖边界

交互文件的 source 标记为 `base_mod#target_mod`，例如
`xedra_evolved#mindovermatter`。`#` 因此保留给组合来源，普通 Mod ID 禁止包含该字符。
错误日志和对象 provenance 应保留这个组合来源。

交互内容在普通数据之后加载，允许 loader 支持的覆盖/扩展，但不能假定每种 object type
具有相同 merge 语义。对 `copy-from`、`extend`、重复 ID 或 delete/obsolete，必须检查
具体 factory/loader；后加载也不能修复 finalize 前已被强制解析的无效引用。

### 多 Mod 条件

需要 A 与 B 同时存在时，不要构造嵌套目录。可选择由其中一个 interaction 加载一个
兼容 EOC，再在当前注册表允许的条件中检查另一个功能；或者建立显式兼容 Mod，并声明
`dependencies`。选择取决于“缺一方时是否仍应可用”和已发布 ID 的归属。

### 验证矩阵

至少验证：仅基础 Mod、仅目标 Mod、两者同时启用、顺序/依赖被解析后的组合，以及含相关
旧存档的加载。运行 formatter、`make -j2 json-check` 和每个组合的 `--check-mods`；同时
检查重复 ID、source 诊断、EOC talker/context、保存/重载和移除任一 Mod 后的行为。

只测试“两者同时启用”会漏掉 interaction 内容意外进入基础加载或基础文件偷偷依赖目标
Mod 的问题。
