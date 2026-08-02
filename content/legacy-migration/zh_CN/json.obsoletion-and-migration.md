## Obsoletion 与 migration 选择

不存在覆盖所有 JSON type 的通用 migration。先确定旧 ID 属于 item、trait、terrain/
furniture、overmap terrain、vehicle part、effect、spell、Mod 等哪一个 registry，再使用该
loader 已注册的 migration object。没有对应 loader 时必须保留旧 ID、兼容 shim 或实现并测试
非行为性迁移支持，不能伪造 Schema。

### Item `MIGRATION`

当前 item migration 接受一个或多个旧 `id`，可设置 `replace`、`variant`、`from_variant`、
flags、charges、contents、sealed 与 `reset_item_vars`。`replace` 不得等于旧 ID。
Variant migration 只匹配对应旧 variant；contents 放不进正常 container 时进入专用 migration
pocket，避免静默丢失。

```jsonc
{
  "type": "MIGRATION",
  "id": "old_item_id",
  "replace": "new_item_id"
}
```

替换类型必须真实存在且在 load/finalize 时可用。数量、charges、pockets、item vars、damage、
ownership 和 sealed state 都可能需要额外 fixture，不是改一个 ID 就完成。

### 其他 registry 与 Mod

CCB 当前注册了 trait、bionic、proficiency、terrain/furniture、field、vehicle part、trap、
effect、overmap terrain/special、camp、spell、global variable 与 Mod migrations 等。字段名和
能力各不相同。`mod_migration` 使用旧 `id` 加 `new_id`，或在移除时提供可翻译
`removal_reason`；目标 Mod 必须有效。

`obsolete: true` 通常控制新内容选择，不自动重写存档中的所有引用。保留期、replacement、
release note 和 removed-ID 测试仍是必要的。

### 验证

为每个真实旧 fixture 加载当前代码，检查 migration 后对象、嵌套 contents、地图/角色/world
state，再保存并第二次加载，确认 migration 幂等且不重复生成资源。运行 formatter、
`make -j2 json-check`、`--check-mods` 和 owning subsystem tests。还要验证缺失 target、
migration chain/cycle、同时启用旧 Mod 与新 Mod、以及移除 migration 后的 release boundary。
