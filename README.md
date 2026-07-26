# MTA Wiki Docs for Agents

An English, skill-first mirror of the [Multi Theft Auto Wiki](https://wiki.multitheftauto.com/wiki/Main_Page), plus the tooling required to keep it current.

The repository is designed for two audiences:

- AI agents install `skills/mta-docs` to search and apply the bundled MTA documentation.
- Maintainers run `mta-wiki-docs` to synchronize changed MediaWiki revisions and validate the generated corpus.

## Repository layout

```text
.
├── skills/
│   ├── mta-docs/
│   │   ├── SKILL.md
│   │   ├── scripts/search_docs.py
│   │   └── references/          # generated English documentation corpus
│   └── mta-lua-best-practices/  # optional engineering guidance
├── src/mta_wiki_docs/           # incremental sync and validation CLI
├── tests/
└── .github/workflows/update-docs.yml
```

## Use as a skill

Install the whole repository or copy the desired skill directory into your agent's skill directory.

The core skill is `skills/mta-docs`. It retrieves exact API and conceptual pages progressively instead of loading the full corpus into context. Search it directly with:

```bash
python skills/mta-docs/scripts/search_docs.py "add event handler"
```

The optional `skills/mta-lua-best-practices` skill complements the source documentation with MTA-specific review criteria for security, client/server design, lifecycle, and performance.

## Maintain the corpus

Requires Python 3.11 or newer.

```bash
python -m pip install -e ".[dev]"
mta-wiki-docs normalize
mta-wiki-docs sync
mta-wiki-docs validate
pytest
```

Synchronization is incremental: existing `revision_id` values are compared with MediaWiki, and only changed or new pages are parsed again. Generated files omit wall-clock timestamps so unchanged pages remain byte-for-byte stable.

## Automatic updates

The `update-docs` workflow runs weekly and on manual dispatch. It:

1. normalizes the current corpus;
2. fetches new and changed English pages;
3. validates metadata, language, indexes, and internal links;
4. runs tests;
5. opens or updates an `automation/update-docs` pull request when the corpus changed.

No scheduled job commits directly to `main`.

## Source and licensing

Documentation is derived from the public Multi Theft Auto Wiki, which declares the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). Every generated page preserves its source URL and revision ID.

Repository tooling is available under the MIT License. See [LICENSE.md](LICENSE.md).

This is an unofficial community mirror and is not an official Multi Theft Auto project.
