## 当前游戏文本风格

本页规范默认英文源码文本；翻译应遵循目标语言语法、标点和复数规则。文本首先要清晰、
可本地化并符合角色语气，不能为了机械套规则而破坏含义。

### 默认英文

- 通用 UI 与叙述使用 US English；角色对白可以有经过设计的方言。
- 面向玩家的动作通常用第二人称；描述使用 sentence case，并以合适标点结束。
- stat、trait/mutation、scenario、profession、background、proficiency、martial art 与
  CBM 名称按既有同类文本的 title case 规则；普通 item/entity 名通常小写，专名例外。
- 使用 serial comma；省略号使用 Unicode `…`，不要用三个句点代替。
- 对话条件标签保持一致，例如 `[PER 10]`、`[Tailoring 2]`、`[SWEET TOOTH]` 和
  `[Use Stethoscope]`；无对白动作也要写成清晰标签。

### 可本地化性

- 不拼接依赖英文词序的句子；为相同英文、不同含义提供 translation context。
- 数量变化使用 plural API，不手写 English-only singular/plural 分支。
- 保留并核对 `%s`、`%d`、位置参数、format braces、颜色/markup tag 与换行。
- 不要求翻译复制英文大小写、双空格、serial comma 或句子结构。
- 变量、ID、按键 token 与不应翻译的 marker 必须在 translator comment 中解释。

### 名称、品牌与来源

现实品牌或引用仍需符合项目 lore、许可证和内容政策；“可能属于 fair use”不是自动批准。
引用外部文字、图像或名称争议时，在 PR 中提供来源与许可，交给 Responsible human 和
维护者复核。不要复制不兼容项目的 prose。

### 验证

检查提取、translation tag、placeholder parity、invalid PO 与 MO 编译。若文本在 JSON、
C++、EOC 或 Lua 中生成，还要验证实际 UI 宽度、复数、性别/context 和错误路径，而不只
阅读源码字符串。

翻译流程见[翻译指南](../localization/translation-guide.md)。
