---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: governance.security-license
title: 安全、许可证与来源
language: zh_CN
status: active
doc_type: explanation
audiences:
- new-contributor
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: LYHGLYTX
source_paths:
- SECURITY.md
- CONTRIBUTING.md
- LICENSE.txt
- OWNERSHIP.md
source_symbols: []
source_queries: []
source_fingerprint: 7cf4f8f2dfa74210240f7fd70014606f14a4aad2ba4e021a825d2c5bd5acf68b
authority: governance
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 6bc4417f2dbe99f4e09be3de5e30824afdd1c6b4208bc3ed43c8c25ca96dcc91
prerequisites:
- contributing.responsible-human
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: governance
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/governance/security-license/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/governance/security-license/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/governance/security-license/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/governance/security-license/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: SECURITY.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/SECURITY.md
- path: CONTRIBUTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/CONTRIBUTING.md
- path: LICENSE.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/LICENSE.txt
- path: OWNERSHIP.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/OWNERSHIP.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28governance.security-license%29%3A+&body=Document+ID%3A+governance.security-license%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 安全、许可证与来源

可能泄露数据、执行不可信代码、破坏构建/发布基础设施、泄露凭据或形成实际 exploit
的安全报告必须使用 CCB 私密漏洞报告渠道，不得在公开 Issue 披露。

## 准备私密报告

提供受影响版本、commit、平台、威胁模型、前提、影响、最小重现与脱敏日志。不要发送
凭据；凭据可能泄露时应轮换，不能只依赖从 Git 历史删除。

无安全影响的普通崩溃和玩法 bug 使用正常 bug 表单。第三方 Mod 和非官方包通常应报给
其所有者，但要明确说明任何 CCB 集成边界。

## 许可证与署名审查

- 复制代码、文档、图片、声音、字体、贴图或生成数据集前先确认许可证。
- 记录来源仓库/URL、精确 commit 或版本、原贡献者、修改与必须保留的 notice。
- 保留兼容 notice 与 commit 署名。公开 URL 不是许可证；AI 生成文本也不会消除训练
  或输入来源带来的溯源义务。
- 自动解析 Git 历史发现的异常贡献者字符串不得发布到站点，应隔离供人类审查。

CCB 仓库许可证文件与各资源 notice 是其覆盖材料的权威。每个 PR 的 Responsible
human 对最终来源和许可证声明负责。

## 特权修改

Workflow 权限、发布签名、Pages 部署、安全设置和分支规则必须最小授权并经人类审阅。
Bot 不能批准自己的修改；提交目标 YAML 不代表对应仓库设置已经启用。
