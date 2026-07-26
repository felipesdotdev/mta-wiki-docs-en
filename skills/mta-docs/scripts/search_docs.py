#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def tokens(value: str) -> set[str]:
    return {token for token in re.findall(r"[a-z0-9_]+", value.lower()) if len(token) > 1}


def main() -> int:
    parser = argparse.ArgumentParser(description="Search the bundled MTA documentation")
    parser.add_argument("query")
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    skill = Path(__file__).resolve().parents[1]
    references = skill / "references"
    manifest = references / "index" / "all-pages.jsonl"
    query_tokens = tokens(args.query)
    results = []
    for line in manifest.read_text(encoding="utf-8").splitlines():
        item = json.loads(line)
        title_tokens = tokens(item.get("title", ""))
        category_tokens = tokens(" ".join(item.get("categories", [])))
        path_tokens = tokens(item["path"])
        if not query_tokens & (title_tokens | category_tokens | path_tokens):
            continue
        score = (
            8 * len(query_tokens & title_tokens)
            + 4 * len(query_tokens & category_tokens)
            + 2 * len(query_tokens & path_tokens)
        )
        results.append({
            "score": score,
            "title": item["title"],
            "path": str(references / item["path"]),
            "source_url": item.get("source_url"),
            "categories": item.get("categories", []),
        })
    results.sort(key=lambda item: (-item["score"], item["title"].lower()))
    results = results[:args.limit]
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for item in results:
            print(f"{item['score']:>3}  {item['title']}\n     {item['path']}")
    return 0 if results else 1


if __name__ == "__main__":
    raise SystemExit(main())
