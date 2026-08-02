## Mod 本地化流程

CCB JSON 的可翻译字段由 `lang/string_extractor` 规则决定，不是看到字符串就自动提取。
先使用结构化 translation object、plural 与 context，再生成 POT；不要在运行时拼接依赖
英文语序的句子。

### 提取模板

在 CCB 根目录为一个位于 `mods/demo` 的外部 Mod 建立空 reference POT，然后调用当前脚本：

```sh
mkdir -p mods/demo/lang/po
: > mods/demo/lang/po/demo.pot
python3 lang/extract_json_strings.py -i mods/demo -n demo -r mods/demo/lang/po/demo.pot
msgfmt -c -o /dev/null mods/demo/lang/po/demo.pot
```

当前脚本使用 `-r/--reference` 追加并规范模板，没有旧文档中的 `-o` 选项。每次 JSON
字段、ID、context 或 plural 变化都重新生成并审阅 diff；POT 中缺失字符串时先检查 object
type 与 extractor 规则，不要手写一份脱离源码的 msgid。

### 建立 PO 与翻译

```sh
msginit -i mods/demo/lang/po/demo.pot -o mods/demo/lang/po/zh_CN.po -l zh_CN
```

翻译必须保持 printf/fmt 参数、位置参数、颜色/markup tag、换行、gender/context 与 plural
含义。译者注释解释变量、不可翻译 ID 和 UI 限制；不要要求所有语言复制英文大小写、词序
或复数规则。更新模板时使用 gettext merge 流程保留已有翻译，不用覆盖 PO。

### 编译与安装布局

```sh
mkdir -p mods/demo/lang/mo/zh_CN/LC_MESSAGES
msgfmt -c -o mods/demo/lang/mo/zh_CN/LC_MESSAGES/demo.mo mods/demo/lang/po/zh_CN.po
```

当前 translation manager 在用户 Mod 根目录递归发现 `LC_MESSAGES`，并读取其中 `.mo`；
语言目录名必须与游戏选择的 language code 一致。发布包至少携带需要的 `.mo` 与 Mod
内容；是否同时发布 POT/PO 由项目协作和许可证策略决定，但必须保留可维护来源。

### 验证

对 POT 和每个 PO 运行 `msgfmt -c`，检查提取 diff、placeholder/tag parity 和无效 Unicode；
把 Mod 安装到真实用户 Mod 目录，在英文与目标语言分别启动、加载世界并检查 Mod name、
description、item plural、dialogue、EOC message 和 Lua UI 文本。还要验证目标语言缺失时
安全回退原文，且同 msgid 不同含义已使用 context。
