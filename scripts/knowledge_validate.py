#!/usr/bin/env python3
"""Validate required structure for a section-based project knowledge page."""

from __future__ import annotations

import argparse
from pathlib import Path

REQUIRED_FRONTMATTER = [
    "doc_id",
    "project_id",
    "title",
    "language_mode",
    "status",
    "last_updated",
    "owners",
]

REQUIRED_SECTIONS = [
    "Project Snapshot",
    "Linked Pages",
    "Sources",
    "Personas",
    "Product Requirements",
    "Feature Requirements",
    "Ideation",
    "Research Notes",
    "Notes & Decisions",
]


def parse_frontmatter_and_body(text: str) -> tuple[dict, list[str]]:
    lines = text.splitlines()
    if len(lines) >= 3 and lines[0].strip() == "---":
        fm = {}
        idx = 1
        while idx < len(lines):
            line = lines[idx]
            if line.strip() == "---":
                return fm, lines[idx + 1 :]
            if ":" in line:
                key, value = line.split(":", 1)
                fm[key.strip()] = value.strip()
            idx += 1
        return fm, []
    return {}, lines


def collect_h2_titles(body: list[str]) -> set[str]:
    titles = set()
    for line in body:
        if line.startswith("## "):
            titles.add(line[3:].strip())
    return titles


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter_and_body(text)

    for key in REQUIRED_FRONTMATTER:
        if key not in frontmatter or not frontmatter[key]:
            errors.append(f"missing frontmatter: {key}")

    titles = collect_h2_titles(body)
    for section in REQUIRED_SECTIONS:
        if section not in titles:
            errors.append(f"missing section: ## {section}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate knowledge markdown pages")
    parser.add_argument("--file", help="Single markdown file to validate")
    parser.add_argument(
        "--all-projects",
        action="store_true",
        help="Validate all Knowledge/projects/**/PROJECT_KNOWLEDGE.md files",
    )
    args = parser.parse_args()

    targets: list[Path] = []
    if args.file:
        targets.append(Path(args.file))
    if args.all_projects:
        targets.extend(Path("knowledge/projects").glob("**/PROJECT_KNOWLEDGE.md"))

    if not targets:
        print("No targets provided. Use --file or --all-projects.")
        return 1

    has_errors = False
    for target in targets:
        if not target.exists():
            print(f"[ERROR] Missing file: {target}")
            has_errors = True
            continue

        errors = validate_file(target)
        if errors:
            has_errors = True
            print(f"[ERROR] {target}")
            for err in errors:
                print(f"  - {err}")
        else:
            print(f"[OK] {target}")

    return 1 if has_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
