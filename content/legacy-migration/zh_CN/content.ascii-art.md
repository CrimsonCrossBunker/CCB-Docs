## ASCII art 数据契约

第一方 ASCII art 使用 JSON `ascii_art` 对象，至少包含稳定 `id` 和字符串数组 `picture`。当前
`ascii_art::load` 会去除颜色标签后按终端显示宽度计算每一行；超过 `41` 个显示列的行会被截断并产生
debug message。这里的“列”不是 UTF-8 字节数，宽字符、组合字符和颜色标签都需要用实际 loader 验证。

```json
{
  "type": "ascii_art",
  "id": "example_art",
  "picture": [ "<color_white>+---+</color>", "<color_white>|   |</color>" ]
}
```

上例只展示结构，不是待提交资源。使用现有有效 color name，并正确闭合标签。空行、前导空格和 Unicode
线框字符是画面的一部分；通用 JSON formatter 之外的文本处理可能破坏对齐。Body-part graph 位于另一
类数据和显示路径，不能仅因为外观相似就假定尺寸与字段完全相同。

## 制作与审查

任何能保留 UTF-8、空格和逐行文本的编辑器都可使用；REXPaint 只是可选工具，不是项目契约。外部 palette、
字体或模板必须确认来源和许可证，不能直接把来源不明的图案带入仓库。

提交前运行项目 JSON formatting/loading，检查重复 ID、无效颜色标签和 debug 输出，并在实际目标界面测试
curses/tiles、默认及 fallback 字体、窄窗口、缩放和中英文环境。检查每行去标签后的显示宽度，而不是只看
编辑器画布。ASCII art 不能成为识别物品或身体部位状态的唯一信息；无障碍路径仍需文字或结构替代。
