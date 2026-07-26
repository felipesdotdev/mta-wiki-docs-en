---
name: mta-docs
description: Search and apply the bundled English Multi Theft Auto documentation for MTA:SA scripting, Lua APIs, client/server events, resources, meta.xml, ACL, mapping, CEF, GUI, server administration, and engine development. Use when answering MTA technical questions, implementing or debugging MTA resources, checking function signatures or event behavior, or grounding MTA code changes in the official wiki mirror.
---

# MTA Documentation

Use the bundled corpus as the source of truth for MTA-specific APIs and behavior. Load only the pages needed for the current task.

## Retrieval workflow

1. Identify the relevant domain: function, event, class, resource, tutorial, mapping, server setup, or development.
2. Search before reading:

   ```bash
   python scripts/search_docs.py "trigger client event"
   ```

3. Open the strongest matching Markdown pages under `references/`.
4. Verify the function side (`client`, `server`, or `shared`), syntax, required arguments, return values, and version notes.
5. Apply the documentation to the task. Do not invent undocumented parameters or guarantees.
6. When uncertainty remains, state it and include the `source_url` from frontmatter.

## Corpus routing

- `references/scripting/client/`: client functions, events, and classes
- `references/scripting/server/`: server functions, events, and classes
- `references/scripting/shared/`: APIs available on both sides
- `references/resources/`: packaged resources and resource-specific APIs
- `references/mapping/`: map editor, maps, and gamemode material
- `references/getting-started/`: installation, manuals, and troubleshooting
- `references/development/`: building MTA and engine development
- `references/tutorials/`: longer guided material
- `references/reference/misc/`: concepts and uncategorized reference
- `references/index/all-pages.jsonl`: machine-readable catalog

## Evidence rules

- Prefer exact API reference pages over tutorials for signatures and return values.
- Treat examples as illustrative, not as broader guarantees than the prose.
- Distinguish client and server execution explicitly in code.
- Preserve wiki revision metadata when reporting stale or contradictory documentation.
- Consult `$mta-lua-best-practices` separately for code quality, architecture, performance, or security review.
