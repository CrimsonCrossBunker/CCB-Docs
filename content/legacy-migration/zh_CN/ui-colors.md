## CCB 颜色系统

颜色名、配对与 invert/highlight 映射由 `color_manager::load_default` 建立，基础 RGB 默认值来自
`data/raw/colors.json`。常用名为 `c_foreground`，`h_` 表示 highlight，`i_` 表示 invert；部分
foreground/background 组合也有具名 pair。有效名称应从当前 color manager 查询，不能通过任意
拼接两个颜色名来推断。

Player-facing 字符串可用 `<color_name>…</color>`，并允许正确闭合的嵌套。颜色不能作为唯一
语义：禁用、危险、选中等状态还应有文字、符号或结构提示，以满足 screen reader 和不同主题。
地图、item 与其他 JSON 字段对 `color`/`bgcolor` 的支持由各自 loader 决定，不是所有对象都接受
相同组合。

### 用户配置与验证

基础 RGB 可在用户配置中覆盖，color manager 还会序列化具名 custom/invert mapping；ImGui
style 是另一条配置路径，RGBA 范围与 curses pair 不同。主题文件可以改变 highlight/invert
规则，因此代码不能依赖某个默认主题的实际 RGB。

修改颜色契约时运行 JSON loading、color consistency 和相关 UI/light tests。检查默认与自定义
主题、curses 与 tiles、ImGui、低对比和色觉差异、嵌套 tag、无效名 fallback 及 screen reader。
文档中的 RGB 只是固定 source commit 的默认值，不是永久视觉 ABI。
