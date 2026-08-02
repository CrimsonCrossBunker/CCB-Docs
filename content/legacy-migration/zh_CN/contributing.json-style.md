## 当前 JSON 风格与验证

两空格缩进、稳定字段布局、短数组内联和长结构换行仍由仓库 formatter 决定。不要手工
模仿旧示例来猜格式，也不要使用通用 formatter 重排整个文件；CCB 的 formatter 会读取
项目 JSON 方言并输出项目风格。

### 格式化入口

CI 对全部 JSON 运行：

```sh
make style-all-json-parallel RELEASE=1
```

本地修改少量已纳入检查的文件可运行：

```sh
make style-json
```

formatter 产物由 Makefile 的 `JSON_FORMATTER_BIN` 选择；不同平台可能是
`tools/format/json_formatter.cgi` 或 `.exe`。不要依赖旧的外部网页 formatter。

### 语义验证

```sh
make -j2 json-check
```

格式通过只说明排版正确；`json-check` 还会覆盖加载阶段。修改稳定 ID、`copy-from`、
EOC、item group、mapgen 或 Mod 依赖时，还要运行对应 ID/loader/focused test。Schema 不
完整的 object type 不能因为编辑器不报错就视为有效。

### 编辑原则

- 只格式化本 PR 需要的文件；formatter 产生额外 diff 时逐项检查。
- 从相邻第一方定义确认字段顺序与实际用法，但 required/default 仍以 loader 为准。
- `//` 注释和项目扩展不是标准 JSON；不要用会删除它们的工具。
- 修改生成清单中的文件时运行 generator，不要手改输出。
- PR 记录 formatter、加载检查、Mod 集和任何跳过项。

更完整的数据契约见[JSON 概览](../json/overview.md)与
[继承和 copy-from](../json/inheritance-copy-from.md)。
