#!/usr/bin/env python3
"""Validate required structure for a section-based project knowledge page."""

from __future__ import annotations

import argparse
import re
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


def extract_h2_section(body: list[str], section_title: str) -> list[str]:
    """Return lines that belong to one H2 section."""
    in_section = False
    captured: list[str] = []
    needle = f"## {section_title}"

    for line in body:
        if line.startswith("## "):
            if line.strip() == needle:
                in_section = True
                continue
            if in_section:
                break
        if in_section:
            captured.append(line)
    return captured


def find_duplicates(ids: list[str]) -> list[str]:
    counts: dict[str, int] = {}
    for item in ids:
        counts[item] = counts.get(item, 0) + 1
    return sorted([item for item, count in counts.items() if count > 1])


def check_block_has_evidence(text: str, prefix: str) -> list[str]:
    """
    For each ### <PREFIX>-### block, ensure an Evidence refs line exists.
    """
    errors: list[str] = []
    lines = text.splitlines()
    header_re = re.compile(rf"^###\s+({prefix}-\d{{3}})\b")

    idx = 0
    while idx < len(lines):
        match = header_re.match(lines[idx])
        if not match:
            idx += 1
            continue

        item_id = match.group(1)
        block_has_evidence = False
        j = idx + 1
        while j < len(lines):
            if lines[j].startswith("## ") or lines[j].startswith("### "):
                break
            if "Evidence refs" in lines[j]:
                block_has_evidence = True
            j += 1

        if not block_has_evidence:
            errors.append(f"{item_id} is missing an 'Evidence refs' line")
        idx = j

    return errors


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

    # Integrity checks for IDs and evidence links.
    sources_lines = extract_h2_section(body, "Sources")
    sources_text = "\n".join(sources_lines)
    source_ids = re.findall(r"\bSRC-\d{3}\b", sources_text)
    source_id_set = set(source_ids)

    if not source_ids:
        errors.append("sources section has no SRC-### IDs")

    for dup in find_duplicates(source_ids):
        errors.append(f"duplicate source ID in Sources: {dup}")

    prd_ids = re.findall(r"^###\s+(PRD-\d{3})\b", text, flags=re.MULTILINE)
    for dup in find_duplicates(prd_ids):
        errors.append(f"duplicate PRD ID: {dup}")

    frd_ids = re.findall(r"^###\s+(FRD-\d{3})\b", text, flags=re.MULTILINE)
    for dup in find_duplicates(frd_ids):
        errors.append(f"duplicate FRD ID: {dup}")

    ideation_text = "\n".join(extract_h2_section(body, "Ideation"))
    idea_ids = re.findall(r"\bIDEA-\d{3}\b", ideation_text)
    for dup in find_duplicates(idea_ids):
        errors.append(f"duplicate IDEA ID in Ideation: {dup}")

    for err in check_block_has_evidence(text, "PRD"):
        errors.append(err)
    for err in check_block_has_evidence(text, "FRD"):
        errors.append(err)

    for line in body:
        if "Evidence refs" not in line:
            continue
        refs = re.findall(r"\bSRC-\d{3}\b", line)
        if not refs:
            errors.append("evidence refs line has no SRC-### ID")
            continue
        for src_id in refs:
            if src_id not in source_id_set:
                errors.append(f"missing source definition for referenced ID: {src_id}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate knowledge markdown pages")
    parser.add_argument("--file", help="Single markdown file to validate")
    parser.add_argument(
        "--all-projects",
        action="store_true",
        help="Validate all knowledge/projects/**/PROJECT_KNOWLEDGE.md files",
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
