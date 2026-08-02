## 当前 CCB mapgen 模型

Mapgen 把一个或多个 overmap terrain（OMT）转换为实际地图格、家具、物品、生物和其他
内容。`mapgen` 负责首次生成，`nested_mapgen` 生成可复用片段，`update_mapgen` 修改已有
地图。三者共享 palette/placing 语法，但尺寸、背景和执行时机不同。

### standalone mapgen

```jsonc
{
  "type": "mapgen",
  "om_terrain": "ccb_example_oter",
  "weight": 1000,
  "object": {
    "fill_ter": "t_grass",
    "rows": [
      "                        "
    ]
  }
}
```

实际普通 OMT 通常是 24×24；示例省略了剩余行，不能直接加载。`om_terrain` 可以指向一个
ID、多个 ID 或多 OMT 网格；网格形式的 rows 尺寸也要按 24 扩展。相同 OMT 的多个 mapgen
按 `weight` 参与选择，0 会禁用该变体。

`mapgen_function_json::setup_internal` 允许 `fill_ter`、`predecessor_mapgen` 或
`fallback_predecessor_mapgen` 提供背景。没有背景时，rows 中每个字符必须由本地或引用的
palette 定义。不要用空格掩盖未定义 terrain。

### rows、palette 与 placing

`terrain`、`furniture`、fields、items、monsters、vehicles、traps、computers、zones 等映射
把字符连接到 placing。具名 `palette` 必须有 ID，可以引用其他 palette；循环引用会报告。
`parameters` 和动态 mapgen value 扩大了可能结果，修改时要验证每个可能 ID，而不仅是默认值。

坐标 placing 和字符 rows 可以同时使用。多 OMT mapgen 中随机坐标范围不能错误跨越 OMT
边界。rotation、镜像、线性 terrain 后缀和多 z-level 组合会改变方向语义，应使用结构测试。

### nested 与 update

`nested_mapgen` 必须提供正方形 `mapgensize`，可覆盖父 mapgen 的一个区域并复用 palette。
`update_mapgen` 不要求 fill/rows 背景，它载入已经存在的地图后应用 placing，可能用于任务、
EOC 或后处理。更新不是幂等的：重复运行可能重复生成物品/NPC、删除结构或改变存档地图。

`update_mapgen` 目标 OMT、offset、rotation 与 verify 失败都要显式处理；不要把首次 worldgen
成功当作 update 对旧存档也安全的证明。

### 验证

1. 对照 overmap terrain ID、mapgen ID、special 旋转和连接关系。
2. 运行 formatter、`make -j2 json-check` 与实际 Mod 集 `--check-mods`。
3. 运行 `mapgen_function_test`，后处理变化再跑 `mapgen_post_process_test`。
4. 检查全部变体、旋转、邻接、z-level、palette 参数和边界字符。
5. 对 update 测试首次、重复、旧存档、目标缺失与部分占用地图。

初学者可先看[mapgen 入门教程](../../tutorials/json-mapgen/beginner.md)；本页负责当前 loader
边界，不替代源码字段检查。
