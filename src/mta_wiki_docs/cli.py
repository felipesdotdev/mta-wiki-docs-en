from __future__ import annotations

import argparse
import concurrent.futures as futures
import hashlib
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from bs4 import BeautifulSoup, Comment, NavigableString, Tag

API = "https://wiki.multitheftauto.com/api.php"
WIKI = "https://wiki.multitheftauto.com"
USER_AGENT = "mta-wiki-docs/0.1 (+https://github.com/felipesdotdev/mta-wiki-docs-en)"
CONTENT_DIRS = {
    "development", "getting-started", "mapping", "reference", "resources",
    "scripting", "tutorials",
}
LANG_PREFIX = re.compile(
    r"^(?:(?:Resource):)?(?:AR|AT|BE|BG|CS|DA|DE|EL|ES|FA|FI|FR|HE|HR|HU|"
    r"ID|IT|JA|KO|LT|LV|NL|NO|PL|PT|PT-BR|RO|RU|SK|SR|SV|TR|UK|VI|"
    r"ZH|ZH-CN|ZH-TW)/",
    re.IGNORECASE,
)
LANG_MARKER = re.compile(
    r"(?:^|[-_/])(?:AR|AT|BE|BG|CS|DA|DE|EL|ES|FA|FI|FR|HE|HR|HU|ID|IT|"
    r"JA|KO|LT|LV|NL|NO|PL|PT|PT-BR|RO|RU|SK|SR|SV|TR|UK|VI|ZH|ZH-CN|"
    r"ZH-TW)(?:[-_/]|$)",
    re.IGNORECASE,
)
FOREIGN_CATEGORY_MARKERS = (
    "conceitos", "funções", "funciones", "tutoriais", "tutoriales",
    "einführung", "funktionen", "событ", "функци", "教程", "脚本",
)
FOREIGN_TITLE_MARKERS = (
    "acesso ", "argumentos opcionais", "cliente deathmatch", "conceitos de ",
    "elemento ", "funciones ", "funções ",
    "funkcje ", "przydatne ", "pisania ", "skryptów", "wstęp ", "wstęp_",
    "zdarzenia ", "widoczność",
)
FOREIGN_PROSE_MARKERS = {
    "pt": (" para ", " com ", " uma ", " que ", " não ", " você ", " recursos "),
    "es": (" para ", " con ", " una ", " que ", " puedes ", " recursos "),
    "de": (" und ", " die ", " der ", " das ", " eine ", " mit ", " für "),
    "fr": (" le ", " les ", " une ", " des ", " avec ", " pour ", " vous "),
    "pl": (" jest ", " oraz ", " przez ", " można ", " skrypt ", " funkcj "),
}
EXCLUDED_TITLE_PREFIXES = (
    "Category:", "File:", "Help:", "MediaWiki:", "Multi Theft Auto: Wiki:",
    "Talk:", "Template:", "User:",
)


@dataclass(frozen=True)
class Page:
    pageid: int
    title: str
    revision_id: int


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def default_output() -> Path:
    return repo_root() / "skills" / "mta-docs" / "references"


def api(params: dict[str, Any], retries: int = 7) -> dict[str, Any]:
    query = urllib.parse.urlencode({"format": "json", "formatversion": "2", **params})
    request = urllib.request.Request(f"{API}?{query}", headers={"User-Agent": USER_AGENT})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                return json.load(response)
        except urllib.error.HTTPError as exc:
            if attempt == retries - 1 or exc.code not in {429, 500, 502, 503, 504}:
                raise
            retry_after = exc.headers.get("Retry-After")
            delay = int(retry_after) if retry_after and retry_after.isdigit() else min(60, 2 ** attempt)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
            if attempt == retries - 1:
                raise
            delay = min(60, 2 ** attempt)
        time.sleep(delay)
    raise AssertionError("unreachable")


def normalized_title(title: str) -> str:
    return title.replace("_", " ").strip()


def is_english(title: str, categories: Iterable[str], prose: str = "") -> bool:
    title = normalized_title(title)
    if title.startswith(EXCLUDED_TITLE_PREFIXES):
        return False
    if LANG_PREFIX.match(title) or LANG_MARKER.search(title):
        return False
    if any(marker in title.lower() for marker in FOREIGN_TITLE_MARKERS):
        return False
    if re.search(r"[\u0400-\u052f\u0600-\u06ff\u3040-\u30ff\u3400-\u9fff]", title):
        return False
    category_text = " ".join(categories).lower().replace("_", " ")
    if any(marker in category_text for marker in FOREIGN_CATEGORY_MARKERS):
        return False
    padded = " " + re.sub(r"\s+", " ", prose.lower()[:8000]) + " "
    return max((sum(marker in padded for marker in markers)
                for markers in FOREIGN_PROSE_MARKERS.values()), default=0) < 4


def slug(value: str) -> str:
    value = value.replace("_", " ").strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "untitled"


def classify(title: str, categories: Iterable[str]) -> Path:
    cats = " ".join(categories).lower()
    low = title.lower()
    if title.startswith("Resource:"):
        return Path("resources") / slug(title.split(":", 1)[1])
    has_client = "client" in cats or low.startswith("onclient")
    has_server = "server" in cats or low.startswith("onserver")
    side = "shared" if has_client and has_server else "client" if has_client else "server" if has_server else "shared"
    if "function" in cats:
        return Path("scripting") / side / "functions" / slug(title)
    if "event" in cats:
        return Path("scripting") / side / "events" / slug(title)
    if "class" in cats:
        return Path("scripting") / side / "classes" / slug(title)
    if any(word in low for word in ("scripting", "lua", "debugging", "security", "gui")):
        return Path("scripting") / "concepts" / slug(title)
    if any(word in low for word in ("editor", "map", "gamemode", "race")):
        return Path("mapping") / slug(title)
    if any(word in low for word in ("compiling", "building", "coding_guidelines", "branches", "roadmap", "forks")):
        return Path("development") / slug(title)
    if any(word in low for word in ("manual", "install", "download", "known_issues", "faq", "where_to_buy")):
        return Path("getting-started") / slug(title)
    if "tutorial" in cats or "tutorial" in low or "introduction" in low:
        return Path("tutorials") / slug(title)
    return Path("reference") / "misc" / slug(title)


def parse_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text
    metadata: dict[str, Any] = {}
    for line in text[4:end].splitlines():
        key, sep, raw = line.partition(":")
        if not sep:
            continue
        try:
            metadata[key.strip()] = json.loads(raw.strip())
        except json.JSONDecodeError:
            metadata[key.strip()] = raw.strip()
    return metadata, text[end + 5:]


def frontmatter(metadata: dict[str, Any]) -> str:
    order = ("doc_id", "title", "source_title", "source_url", "revision_id", "language", "categories")
    lines = [f"{key}: {json.dumps(metadata[key], ensure_ascii=False)}" for key in order if key in metadata]
    return "---\n" + "\n".join(lines) + "\n---\n"


def node_markdown(node: Any, paths: dict[str, Path]) -> str:
    if isinstance(node, Comment):
        return ""
    if isinstance(node, NavigableString):
        return str(node)
    if not isinstance(node, Tag):
        return ""
    name = node.name.lower()
    if name in {"script", "style", "noscript"}:
        return ""
    if name == "sup" and "reference" in node.get("class", []):
        return ""
    body = "".join(node_markdown(child, paths) for child in node.children)
    if name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
        return f"\n\n{'#' * int(name[1])} {body.strip()}\n\n"
    if name == "p":
        return f"\n\n{body.strip()}\n\n"
    if name == "br":
        return "  \n"
    if name in {"strong", "b"}:
        return f"**{body.strip()}**"
    if name in {"em", "i"}:
        return f"*{body.strip()}*"
    if name == "code":
        return f"`{body.strip()}`"
    if name == "pre":
        language = next((item.removeprefix("lang-") for item in node.get("class", []) if item.startswith("lang-")), "")
        return f"\n\n```{language}\n{node.get_text('', strip=False).strip()}\n```\n\n"
    if name == "a":
        label = re.sub(r"\s+", " ", body).strip()
        if not label:
            return ""
        target = normalized_title(node.get("title", ""))
        if target in paths:
            return f"[{label}](mta://{paths[target].as_posix()}.md)"
        href = node.get("href", "")
        if href.startswith("/"):
            href = WIKI + href
        return f"[{label}]({href})" if href else label
    if name == "li":
        return "\n- " + body.strip()
    if name in {"ul", "ol"}:
        return "\n" + body.strip() + "\n"
    if name == "table":
        rows: list[list[str]] = []
        for row in node.find_all("tr"):
            cells = [
                re.sub(r"\s+", " ", cell.get_text(" ", strip=True)).replace("|", "\\|")
                for cell in row.find_all(["th", "td"], recursive=False)
            ]
            if cells:
                rows.append(cells)
        if not rows:
            return ""
        width = max(map(len, rows))
        rows = [row + [""] * (width - len(row)) for row in rows]
        header = "| " + " | ".join(rows[0]) + " |"
        divider = "| " + " | ".join(["---"] * width) + " |"
        rest = "\n".join("| " + " | ".join(row) + " |" for row in rows[1:])
        return f"\n\n{header}\n{divider}\n{rest}\n\n"
    if name in {"div", "section", "main", "dl", "dd", "dt", "blockquote"}:
        return f"\n{body}\n"
    return body


def render_page(record: dict[str, Any], paths: dict[str, Path]) -> str:
    parsed = record["parse"]
    source_title = normalized_title(parsed["title"])
    soup = BeautifulSoup(parsed["text"], "html.parser")
    for unwanted in soup.select(".mw-editsection, .noprint, .navbox, .metadata, .ambox, .catlinks, .toc"):
        unwanted.decompose()
    title = BeautifulSoup(parsed.get("displaytitle", source_title), "html.parser").get_text(" ", strip=True)
    body = html.unescape(node_markdown(soup, paths))
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    if body.startswith("# "):
        body = body.split("\n", 1)[1] if "\n" in body else ""
    categories = [item.get("category", "") for item in parsed.get("categories", [])]
    metadata = {
        "doc_id": f"mta-wiki:{parsed['pageid']}",
        "title": title,
        "source_title": source_title,
        "source_url": f"{WIKI}/wiki/{urllib.parse.quote(source_title.replace(' ', '_'))}",
        "revision_id": parsed["revid"],
        "language": "en",
        "categories": categories,
    }
    return frontmatter(metadata) + f"\n# {title}\n\n{body}\n"


def list_inventory() -> list[dict[str, Any]]:
    site = api({"action": "query", "meta": "siteinfo", "siprop": "namespaces"})
    resource_ids = [
        int(key) for key, value in site["query"]["namespaces"].items()
        if value.get("canonical") == "Resource" or value.get("*") == "Resource"
    ]
    pages: list[dict[str, Any]] = []
    for namespace in [0, *resource_ids]:
        continuation: dict[str, str] = {}
        while True:
            data = api({
                "action": "query", "list": "allpages", "apnamespace": namespace,
                "aplimit": "max", "apfilterredir": "nonredirects", **continuation,
            })
            pages.extend(
                page for page in data.get("query", {}).get("allpages", [])
                if is_english(page["title"], ())
            )
            continuation = data.get("continue", {})
            if not continuation:
                break
    return pages


def attach_revisions(pages: list[dict[str, Any]]) -> list[Page]:
    revisions: dict[int, int] = {}
    for start in range(0, len(pages), 50):
        batch = pages[start:start + 50]
        data = api({
            "action": "query", "prop": "info",
            "pageids": "|".join(str(page["pageid"]) for page in batch),
        })
        for page in data.get("query", {}).get("pages", []):
            if not page.get("missing") and page.get("lastrevid"):
                revisions[page["pageid"]] = page["lastrevid"]
    return [
        Page(page["pageid"], normalized_title(page["title"]), revisions[page["pageid"]])
        for page in pages if page["pageid"] in revisions
    ]


def fetch_page(page: Page) -> dict[str, Any]:
    data = api({
        "action": "parse", "pageid": page.pageid,
        "prop": "text|categories|links|revid|displaytitle",
        "redirects": "1",
    })
    if "parse" not in data:
        raise RuntimeError(f"{page.title}: {data.get('error', 'missing parse payload')}")
    return {"parse": data["parse"]}


def markdown_files(output: Path) -> Iterable[Path]:
    for directory in sorted(CONTENT_DIRS):
        root = output / directory
        if root.exists():
            yield from root.rglob("*.md")


def existing_documents(output: Path) -> dict[str, tuple[Path, dict[str, Any]]]:
    result = {}
    for path in markdown_files(output):
        metadata, _ = parse_frontmatter(path)
        title = normalized_title(str(metadata.get("source_title", "")))
        if title:
            result[title] = (path, metadata)
    return result


def load_exclusions(output: Path) -> dict[str, int | None]:
    path = output / "index" / "excluded-non-english.json"
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    result: dict[str, int | None] = {}
    for item in data:
        if isinstance(item, str):
            result[normalized_title(item)] = None
        elif isinstance(item, dict) and item.get("title"):
            result[normalized_title(item["title"])] = item.get("revision_id")
    return result


def write_exclusions(output: Path, exclusions: dict[str, int | None]) -> None:
    index = output / "index"
    index.mkdir(parents=True, exist_ok=True)
    records = [
        {"title": title, "revision_id": revision}
        for title, revision in sorted(exclusions.items())
    ]
    (index / "excluded-non-english.json").write_text(
        json.dumps(records, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8", newline="\n",
    )


def unique_paths(candidates: dict[str, Path]) -> dict[str, Path]:
    used: dict[Path, str] = {}
    result: dict[str, Path] = {}
    for title in sorted(candidates):
        path = candidates[title]
        if path in used and used[path] != title:
            path = path.with_name(path.name + "--" + hashlib.sha1(title.encode()).hexdigest()[:8])
        used[path] = title
        result[title] = path
    return result


def write_indexes(
    output: Path,
    errors: list[dict[str, str]] | None = None,
    extra_report: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    documents = existing_documents(output)
    manifest = []
    for title, (path, metadata) in sorted(documents.items()):
        manifest.append({
            "doc_id": metadata.get("doc_id"),
            "title": title,
            "path": path.relative_to(output).as_posix(),
            "revision_id": metadata.get("revision_id"),
            "categories": metadata.get("categories", []),
            "source_url": metadata.get("source_url"),
        })
    index = output / "index"
    index.mkdir(parents=True, exist_ok=True)
    (index / "all-pages.jsonl").write_text(
        "".join(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n" for item in manifest),
        encoding="utf-8", newline="\n",
    )
    report = {
        "source": f"{WIKI}/wiki/Main_Page",
        "language": "en",
        "markdown_pages": len(manifest),
        "errors": errors or [],
    }
    report.update(extra_report or {})
    (index / "crawl-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8", newline="\n",
    )
    return manifest


def normalize(output: Path, remove_foreign: bool = True) -> dict[str, int]:
    removed = rewritten = repaired_links = deduplicated = 0
    exclusions = load_exclusions(output)
    for path in list(markdown_files(output)):
        if not path.exists():
            continue
        metadata, body = parse_frontmatter(path)
        if not metadata:
            continue
        title = str(metadata.get("source_title", metadata.get("title", "")))
        categories = metadata.get("categories", [])
        if remove_foreign and not is_english(title, categories, body):
            exclusions[normalized_title(title)] = metadata.get("revision_id")
            path.unlink(missing_ok=True)
            removed += 1
            continue
        changed = False
        if "generated_at" in metadata:
            metadata.pop("generated_at")
            changed = True
        if metadata.get("language") != "en":
            metadata["language"] = "en"
            changed = True
        if changed:
            path.write_text(frontmatter(metadata) + body, encoding="utf-8", newline="\n")
            rewritten += 1
    by_title: dict[str, list[Path]] = {}
    for path in markdown_files(output):
        metadata, _ = parse_frontmatter(path)
        title = normalized_title(str(metadata.get("source_title", "")))
        if title:
            by_title.setdefault(title, []).append(path)
    aliases: dict[str, str] = {}
    for paths in by_title.values():
        if len(paths) < 2:
            continue
        paths.sort(key=lambda item: ("--" in item.stem, len(item.as_posix()), item.as_posix()))
        kept = paths[0].relative_to(output).as_posix()
        for duplicate in paths[1:]:
            aliases[duplicate.relative_to(output).as_posix()] = kept
            duplicate.unlink(missing_ok=True)
            deduplicated += 1
    existing_paths = {
        path.relative_to(output).as_posix() for path in markdown_files(output)
    }
    missing_pattern = re.compile(r"\[([^\]]+)\]\(mta://([^)#]+)\)")
    for path in list(markdown_files(output)):
        metadata, body = parse_frontmatter(path)
        changed_count = 0

        def repair(match: re.Match[str]) -> str:
            nonlocal changed_count
            if match.group(2) in existing_paths:
                return match.group(0)
            if match.group(2) in aliases:
                changed_count += 1
                return f"[{match.group(1)}](mta://{aliases[match.group(2)]})"
            changed_count += 1
            query = urllib.parse.quote(match.group(1).strip())
            return f"[{match.group(1)}]({WIKI}/index.php?search={query})"

        repaired = missing_pattern.sub(repair, body)
        if changed_count:
            path.write_text(frontmatter(metadata) + repaired, encoding="utf-8", newline="\n")
            repaired_links += changed_count
    manifest = write_indexes(output)
    write_exclusions(output, exclusions)
    return {
        "removed": removed, "rewritten": rewritten, "deduplicated": deduplicated,
        "repaired_links": repaired_links, "indexed": len(manifest),
    }


def sync(output: Path, workers: int, limit: int | None, full: bool) -> dict[str, Any]:
    output.mkdir(parents=True, exist_ok=True)
    inventory = list_inventory()
    if limit:
        inventory = inventory[:limit]
    pages = attach_revisions(inventory)
    current = existing_documents(output)
    exclusions = load_exclusions(output)
    remote_titles = {page.title for page in pages}
    stale = [title for title in current if title not in remote_titles]
    for title in stale:
        current[title][0].unlink()
    changed = [
        page for page in pages
        if full or page.title not in current
        and exclusions.get(page.title) != page.revision_id
        or page.title in current
        and current[page.title][1].get("revision_id") != page.revision_id
    ]
    errors: list[dict[str, str]] = []
    fetched: dict[str, dict[str, Any]] = {}
    with futures.ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
        jobs = {pool.submit(fetch_page, page): page for page in changed}
        for job in futures.as_completed(jobs):
            page = jobs[job]
            try:
                record = job.result()
                categories = [item.get("category", "") for item in record["parse"].get("categories", [])]
                prose = BeautifulSoup(record["parse"]["text"], "html.parser").get_text(" ", strip=True)
                if is_english(page.title, categories, prose):
                    fetched[page.title] = record
                    exclusions.pop(page.title, None)
                elif page.title in current:
                    current[page.title][0].unlink()
                    exclusions[page.title] = page.revision_id
                else:
                    exclusions[page.title] = page.revision_id
            except Exception as exc:  # keep the remaining corpus usable and report exact failures
                errors.append({"title": page.title, "error": str(exc)})
    candidates = {
        title: path.relative_to(output).with_suffix("")
        for title, (path, _) in existing_documents(output).items()
    }
    for title, record in fetched.items():
        categories = [item.get("category", "") for item in record["parse"].get("categories", [])]
        candidates[title] = classify(title, categories)
    paths = unique_paths(candidates)
    for title, record in fetched.items():
        destination = output / paths[title].with_suffix(".md")
        destination.parent.mkdir(parents=True, exist_ok=True)
        old = current.get(title)
        if old and old[0] != destination and old[0].exists():
            old[0].unlink()
        destination.write_text(render_page(record, paths), encoding="utf-8", newline="\n")
    revisions_by_title = {page.title: page.revision_id for page in pages}
    exclusions = {
        title: revision for title, revision in exclusions.items()
        if title in revisions_by_title and revision == revisions_by_title[title]
    }
    write_exclusions(output, exclusions)
    normalization = normalize(output)
    result = {
        "inventory": len(pages), "changed": len(changed), "written": len(fetched),
        "removed": len(stale), "error_count": len(errors),
        "normalized": normalization,
    }
    manifest = write_indexes(output, errors, result)
    result["indexed"] = len(manifest)
    return result


def validate(output: Path) -> list[str]:
    errors: list[str] = []
    documents = existing_documents(output)
    paths = {path.relative_to(output).as_posix() for path, _ in documents.values()}
    for title, (path, metadata) in documents.items():
        relative = path.relative_to(output).as_posix()
        if metadata.get("language") != "en":
            errors.append(f"{relative}: language is not en")
        if "generated_at" in metadata:
            errors.append(f"{relative}: contains non-deterministic generated_at")
        _, body = parse_frontmatter(path)
        if not is_english(title, metadata.get("categories", []), body):
            errors.append(f"{relative}: appears non-English")
        for target in re.findall(r"\]\(mta://([^)#]+)", body):
            if target not in paths:
                errors.append(f"{relative}: broken mta link -> {target}")
    manifest_path = output / "index" / "all-pages.jsonl"
    if not manifest_path.exists():
        errors.append("index/all-pages.jsonl is missing")
    else:
        manifest_paths = {
            json.loads(line)["path"] for line in manifest_path.read_text(encoding="utf-8").splitlines() if line
        }
        if manifest_paths != paths:
            errors.append(
                f"manifest mismatch: {len(paths)} documents vs {len(manifest_paths)} indexed paths"
            )
    return errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="mta-wiki-docs")
    parser.add_argument("--output", type=Path, default=default_output())
    commands = parser.add_subparsers(dest="command", required=True)
    sync_parser = commands.add_parser("sync", help="incrementally synchronize the MTA wiki")
    sync_parser.add_argument("--workers", type=int, default=2)
    sync_parser.add_argument("--limit", type=int)
    sync_parser.add_argument("--full", action="store_true")
    commands.add_parser("normalize", help="make the existing corpus deterministic and English-only")
    commands.add_parser("validate", help="validate metadata, language, index, and internal links")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    output = args.output.resolve()
    if args.command == "sync":
        result = sync(output, args.workers, args.limit, args.full)
        print(json.dumps(result, indent=2))
        return 1 if result["error_count"] else 0
    if args.command == "normalize":
        print(json.dumps(normalize(output), indent=2))
        return 0
    errors = validate(output)
    if errors:
        print("\n".join(errors))
        print(f"\nValidation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1
    print(f"Validation passed: {len(existing_documents(output))} documents.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
