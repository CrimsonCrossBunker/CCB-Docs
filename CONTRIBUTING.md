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
3. Update the Chinese body fingerprint and source fingerprint when their
   authoritative inputs change; mark English `translation-stale` if it is not
   updated in the same PR.
4. Run `uv run python scripts/generate_catalog.py`. Do not hand-edit generated
   front matter, indexes, allowlists, redirects, or sitemap metadata.
   For JSON/EOC reference changes, first run
   `scripts/generate_json_eoc_reference.py` against the catalog's exact CCB
   `verified_commit`; do not edit the generated registry bodies.
5. Run the validation commands in `AGENTS.md`.
6. If the page depends on an unmerged CCB PR, keep it `draft`. After source
   merge, replace `verified_commit` with the final commit and regenerate before
   requesting docs merge.

Use the matching file in `templates/` when starting a tutorial, how-to,
reference, explanation, generated API page, or archive page. A generated page
must identify its generator and must never be edited as prose.

CCB governance is authoritative at
https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/master/GOVERNANCE.md.
