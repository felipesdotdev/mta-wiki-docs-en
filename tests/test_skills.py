from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_skill_files_are_complete() -> None:
    for name in ("mta-docs", "mta-lua-best-practices"):
        skill = ROOT / "skills" / name / "SKILL.md"
        text = skill.read_text(encoding="utf-8")
        assert text.startswith("---\nname: ")
        assert "\ndescription: " in text.split("\n---\n", 1)[0]
        assert "TODO" not in text


def test_agent_metadata_mentions_each_skill() -> None:
    for name in ("mta-docs", "mta-lua-best-practices"):
        metadata = (ROOT / "skills" / name / "agents" / "openai.yaml").read_text(
            encoding="utf-8"
        )
        assert f"${name}" in metadata
        assert "short_description:" in metadata
