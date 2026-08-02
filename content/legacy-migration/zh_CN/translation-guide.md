## CCB 本地化流程

CCB 使用 gettext、source extraction、PO 与编译后的 MO。运行时行为以 `translations.cpp` 为准，
JSON extraction 以 `lang/` scripts 为准，远端同步以当前 translation workflows 和 Transifex CCB
project 为准。旧 `cataclysm-dda` resource 名或论坛说明不能覆盖当前 `.tx/config`。

### 开发者

简单 C++ literal 用 `_()`；有歧义时用 context；数量使用 plural API。需要延迟翻译、JSON context
或 plural 的数据用 `translation`/`to_translation`/`pl_translation`，在展示时调用 `translated()`。
不要在 global/local static 初始化时缓存已翻译字符串，否则初始化顺序或运行时换语言会出错。
Debug/error 文本保持可复制的原文，除非其明确属于 player-facing contract。

JSON translator comment 使用 loader 支持的 `//~`/translation object 形式。占位符、位置参数、
markup、gender context、key tags 和换行必须保持等价；不要拼接依赖英语词序的句子。新增 extraction
形态时同时更新 extractor 与测试。

### 构建与验证

当前本地 MO 入口是：

```sh
make -C lang LANGUAGES=zh_CN
```

或使用仓库脚本生成 POT、验证/合并 PO、更新 stats 和编译 MO；具体名称从当前 `lang/` 与 CI
读取。CI 的 build-translations workflow 有 TX token 时拉取、丢弃无效 PO、更新统计并编译；无
token 时复用可信 master artifact。Experimental Release 成功后另一个 workflow 生成 POT 并向
Transifex 推送 source template。

验证 extraction diff、POT/PO 格式、placeholder/plural/context parity、`msgfmt`、语言切换、fallback、
UI 宽度和目标平台字体。不要手改生成 MO；Transifex 写操作需要维护者凭据和人工审查。
