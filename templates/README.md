# CCB-Docs page templates

Copy the appropriate authored-body template into both `docs/zh_CN/` and
`docs/en/`, then register the pair once in `docs-catalog.yml`. The catalog is
the only authority for front matter, navigation, indexes, redirects, search,
and AI inclusion; do not hand-write those generated blocks.

Generated API bodies are emitted by their declared generator and must not be
edited by hand. Archive pages stay public but are excluded from navigation,
search, and AI indexes.
