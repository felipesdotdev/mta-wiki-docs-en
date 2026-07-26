from pathlib import Path

from mta_wiki_docs.cli import (
    classify,
    frontmatter,
    is_english,
    load_exclusions,
    parse_frontmatter,
    slug,
    write_exclusions,
)


def test_language_prefix_after_resource_namespace() -> None:
    assert not is_english("Resource:RU/Admin", [])
    assert not is_english("ZH-CN/Template OOP", [])
    assert not is_english("AddCommandHandler-PT-BR", [])
    assert not is_english("BROKEN/PL/Instrukcja klienta", [])
    assert not is_english("AT/Fahrzeugfarben", [])
    assert not is_english("Multi Theft Auto: Wiki:Privacy policy", [])
    assert is_english("Resource:Admin", ["Resource"])
    assert not is_english("Funkcje po stronie klienta", [])


def test_language_content_heuristic() -> None:
    portuguese = "Este recurso é usado para criar uma interface com uma lista que você pode configurar."
    assert not is_english("Acesso web via recursos", ["Tutoriais"], portuguese)
    assert is_english("Resource Web Access", ["Tutorials"], "This resource provides web access from MTA.")
    assert is_english("Utf8.byte", ["Client_functions"], 'The example uses "Ницца!" as input.')


def test_classification_understands_execution_side() -> None:
    assert classify("AddEvent", ["Client_functions", "Server_functions"]) == Path(
        "scripting/shared/functions/addevent"
    )
    assert classify("OnClientRender", ["Client_events"]) == Path(
        "scripting/client/events/onclientrender"
    )


def test_frontmatter_round_trip(tmp_path: Path) -> None:
    metadata = {
        "doc_id": "mta-wiki:1",
        "title": "Example",
        "source_title": "Example",
        "source_url": "https://example.test",
        "revision_id": 42,
        "language": "en",
        "categories": ["Functions"],
    }
    path = tmp_path / "example.md"
    path.write_text(frontmatter(metadata) + "\n# Example\n", encoding="utf-8")
    parsed, body = parse_frontmatter(path)
    assert parsed == metadata
    assert body == "\n# Example\n"


def test_slug_is_readable_and_stable() -> None:
    assert slug("OnClientResourceStart") == "onclientresourcestart"
    assert slug("Meta.xml") == "meta-xml"


def test_exclusions_preserve_revision_ids(tmp_path: Path) -> None:
    write_exclusions(tmp_path, {"PT-BR/Página Inicial": 123})
    assert load_exclusions(tmp_path) == {"PT-BR/Página Inicial": 123}
