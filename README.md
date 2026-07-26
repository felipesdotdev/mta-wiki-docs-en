# Multi Theft Auto Wiki — English Markdown Mirror

This corpus is an English-only Markdown mirror of the public Multi Theft Auto wiki, structured for agent and RAG use.

- `scripting/` — client, server and shared functions, events, classes and concepts
- `resources/` — resource documentation, `meta.xml`, ACL, CEF and editor material
- `mapping/` — map editor, maps and gamemode material
- `getting-started/` — manuals, installation and troubleshooting
- `development/` — compiling, builds, branches and coding guidelines
- `tutorials/` and `reference/` — learning material and uncategorised reference
- `index/all-pages.jsonl` — one JSON record per emitted page
- `index/inventory.json` — source inventory used for the crawl

Every page preserves source metadata in YAML frontmatter. Internal resolved wiki links use `mta://` paths into this corpus.

## Source and licence

Content is derived from the public [Multi Theft Auto Wiki](https://wiki.multitheftauto.com/wiki/Main_Page), which declares the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). See [LICENSE.md](LICENSE.md) for attribution and reuse information.
