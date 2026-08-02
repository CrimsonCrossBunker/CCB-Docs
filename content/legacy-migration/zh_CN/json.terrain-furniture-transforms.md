## 当前 CCB terrain/furniture transform

`ter_furn_transform` 是具名、可复用的格子转换表。它分别匹配 terrain、furniture、field 和
trap，然后从带权 `result` 中选择替代值。各类别互相独立；匹配 terrain 不会自动产生某个
furniture。

### 基础定义

```jsonc
{
  "type": "ter_furn_transform",
  "id": "ccb_example_transform",
  "terrain": [
    {
      "valid_terrain": [ "t_sand" ],
      "result": [ [ "t_dirt", 4 ], "t_grass" ],
      "message": "The sand shifts.",
      "message_good": true
    }
  ]
}
```

单个 result 的权重为 1；二元数组可提供权重。`message_good` 缺省为 true。terrain 与
furniture 还可用 `valid_flags` 匹配；field/trap 使用各自 valid-ID 字段。具体字段名和是否
支持 flag 以 `ter_furn_transform::load` 为准。

### 匹配与冲突

Loader 把每个 valid ID/flag 映射到转换结果。同一输入被多条规则覆盖时，容器插入顺序与
实现细节不应被当成内容优先级机制；保持匹配集合互斥，或补测试证明预期。`f_null`、
`fd_null` 等“清除”结果仍是各系统的真实 ID，不要用 JSON null 替代。

Transform 可由 mapgen placing、EOC 半径效果、spell 等调用。调用者决定位置、范围、
talker、重复次数和消息展示；transform 本身不记录“已执行”。重复调用必须是明确设计，
尤其是带随机结果或可能形成 A↔B 循环时。

### 验证

1. 检查所有 valid/result terrain、furniture、field、trap ID 与 flags。
2. 运行 formatter、`make -j2 json-check` 和实际 Mod 集 `--check-mods`。
3. 分别测试每类输入、无匹配、多个 flag、权重边界与 null/清除结果。
4. 从每个真实调用点测试范围、z-level、重复执行和消息。
5. Mapgen 调用再运行 `mapgen_function_test`，EOC/spell 调用运行对应 focused test。

Transform 适合声明同格类型替换；需要跨格、条件链或副作用时，应在 EOC/mapgen 调用层
表达，而不是依赖偶然的规则覆盖。
