## Tiles build 字体配置

Tiles build 从用户配置 `fonts.json` 读取四个 fallback chain：`typeface`、`gui_typeface`、
`map_typeface` 与 `overmap_typeface`。每项可为 path 字符串、含 `path` 的对象，或这些项的数组。
数组顺序就是 glyph fallback 顺序；loader 会确保 `data/font/unifont.ttf` 作为最终 fallback。

对象可设置 `hinting` 与 `antialiasing`。当前接受的 hinting 字符串是 `Auto`、`NoAuto`、
`Default`、`Light`、`None`、`Bitmap`。未知值会报告 debug message 后回到 default；不要复制旧文档
中不一致的枚举。关闭 antialiasing 会设置 monochrome/mono-hinting flags。字体 path 相对于当前
运行环境解析，发布包必须实际携带文件并满足字体许可证。

### 迁移与验证

`font_loader::load` 会读取当前配置；不存在时从 legacy/default 路径加载并由
`font_loader::save` 写成规范对象数组。这个写回可能改变用户文件的表示但应保持选择语义。

验证时使用含拉丁、简繁中文、组合字符、宽字符、emoji fallback 和缺失 glyph 的样例；覆盖
四种 screen、不同 DPI/缩放、Bitmap/Light/None、antialiasing on/off 和找不到文件。还要检查
ImGui atlas、地图格子宽高、终端对齐、内存/启动时间和许可证归属。不要只凭配置 JSON 成功解析
就认为字体可用。
