---
name: mta-lua-best-practices
description: Review, design, and improve Lua code for Multi Theft Auto resources with practical guidance for client/server boundaries, event security, resource lifecycle, performance, element data, timers, handlers, exports, and maintainability. Use when writing an MTA resource, reviewing MTA Lua code, diagnosing architectural or performance problems, or asking for MTA-specific coding and security best practices.
---

# MTA Lua Best Practices

Apply MTA-specific engineering guidance while grounding API details in `$mta-docs`. Treat the bundled practices as review criteria, not as replacements for exact function documentation.

## Review workflow

1. Identify the execution side of every file and event.
2. Search `$mta-docs` for every unfamiliar MTA API used by the code.
3. Read [references/practices.md](references/practices.md).
4. Review correctness and trust boundaries before style.
5. Report concrete findings with file/line references when code is available.
6. Suggest the smallest safe change and show MTA-appropriate Lua where useful.

## Priority order

- Remote-event security and server authority
- Client/server API misuse
- Handler, timer, and resource cleanup
- Hot-path performance and network traffic
- Data ownership and maintainability
- Naming and formatting
