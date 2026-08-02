## Tileset 制作与组合

CCB distribution 使用 compositing tileset：独立 PNG sprite、tile-entry JSON、`tile_info.json` 与
`tileset.txt` 经 `tools/gfx_tools/compose.py` 生成 tilesheet 和 `tile_config.json`。运行时实际可读
字段仍以 tiles loader 为准；compose 只验证/转换它理解的 source format。

### Source layout 与 tile entry

Tile entry 用 `id` 把游戏实体映射到 `fg`/`bg` sprite root。可使用 rotations、weighted
variants、`multitile`/`additional_tiles`、season/gender/item variant 命名和 contextual layering。
terrain/furniture 的连接与旋转还依赖游戏 JSON 中的 `connect_groups`、`connects_to`、
`rotates_to`；tileset 不能自行创造这些 runtime 关系。Hardcoded overlay/animation ID 应从当前
`cata_tiles.cpp` 和调用点清点，旧手工列表可能遗漏。

`tile_info.json` 描述默认和各 tilesheet 的 sprite 尺寸、offset、pixelscale、sheet width，以及
filler/fallback/exclude。相同 sprite root、filler 顺序和跨目录引用会影响结果；保持名字唯一并
审查 compose warning。`layering.json` 的 context、item/field variant、offset 与 layer 是单独的
runtime contract。

### Compose、发布与验证

当前 CI 使用类似以下命令：

```sh
python3 tools/gfx_tools/compose.py --use-all --obsolete-fillers \
  --feedback CONCISE --format-json --loglevel INFO SOURCE DEST
```

实际 flags 以 `compose.py --help` 为准；`--only-json`、`--fail-fast`、palette 等选项改变输出或
诊断。先在临时输出目录运行，审查 unused/missing/duplicate sprite、生成 JSON 和图片尺寸，再用
Tiles build 加载并测试旋转、multitile、fallback、zoom、季节、overlay 和 layering。需要回转旧
index tileset 时才用 `decompose.py`，其自动文件名/目录必须人工整理。

所有 artwork 必须有可分发许可证与可追溯 attribution；CI 能 compose 不代表素材许可合格。当前
打包矩阵在 `.github/workflows/compose-tilesets.yml`，外部 tileset 仓库内容不是 CCB runtime
契约，版本与来源必须固定并审阅。
