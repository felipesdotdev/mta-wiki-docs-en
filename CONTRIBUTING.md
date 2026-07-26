# Contributing

## Documentation changes

Do not hand-edit generated pages under `skills/mta-docs/references/`. Correct the source wiki or update the converter, then run:

```bash
mta-wiki-docs sync
mta-wiki-docs validate
```

Include the affected source URL and revision ID when reporting a conversion problem.

## Tooling and skill changes

Install development dependencies and run the local checks:

```bash
python -m pip install -e ".[dev]"
pytest
mta-wiki-docs validate
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/mta-docs
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/mta-lua-best-practices
```

Keep `SKILL.md` concise. Put detailed knowledge in `references/` and deterministic helpers in `scripts/`.
