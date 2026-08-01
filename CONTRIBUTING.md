# Contributing to CCB-Docs / 参与 CCB-Docs

All changes use pull requests. AI-tool disclosure is optional, but every pull
request names a Responsible human who understands the change, reviews the final
diff, owns test results, checks licenses and external sources, and answers
review questions.

所有修改均通过 PR。无需披露 AI 工具或模型，但必须指定 Responsible human，
由其理解修改、审查最终差异、确认测试、许可证和外部来源并回答审阅问题。

## Workflow

1. Edit prose in both language trees or mark an existing English translation
   `translation-stale` in `docs-catalog.yml`.
2. Edit catalog metadata only in `docs-catalog.yml`.
3. Run `uv run python scripts/generate_catalog.py`.
4. Run the validation commands in `AGENTS.md`.
5. If the page depends on an unmerged CCB PR, keep it `draft`. After source
   merge, replace `verified_commit` with the final commit and regenerate before
   requesting docs merge.

CCB governance is authoritative at
https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/master/GOVERNANCE.md.
