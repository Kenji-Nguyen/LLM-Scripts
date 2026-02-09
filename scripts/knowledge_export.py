#!/usr/bin/env python3
"""Export a section-based markdown knowledge page to JSON."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def parse_frontmatter(text: str) -> tuple[dict, list[str]]:
    lines = text.splitlines()
    if len(lines) >= 3 and lines[0].strip() == "---":
        frontmatter = {}
        idx = 1
        while idx < len(lines):
            line = lines[idx]
            if line.strip() == "---":
                return frontmatter, lines[idx + 1 :]
            if ":" in line:
                key, value = line.split(":", 1)
                frontmatter[key.strip()] = value.strip()
            idx += 1
    return {}, lines


def parse_sections(body_lines: list[str]) -> list[dict]:
    sections: list[dict] = []
    current = None

    for line in body_lines:
        if line.startswith("## "):
            if current:
                current["content"] = "\n".join(current["content"]).strip()
                for sub in current["subsections"]:
                    sub["content"] = "\n".join(sub["content"]).strip()
                sections.append(current)
            current = {
                "title": line[3:].strip(),
                "content": [],
                "subsections": [],
            }
            continue

        if current and line.startswith("### "):
            current["subsections"].append({"title": line[4:].strip(), "content": []})
            continue

        if current:
            if current["subsections"]:
                current["subsections"][-1]["content"].append(line)
            else:
                current["content"].append(line)

    if current:
        current["content"] = "\n".join(current["content"]).strip()
        for sub in current["subsections"]:
            sub["content"] = "\n".join(sub["content"]).strip()
        sections.append(current)

    return sections


def main() -> int:
    parser = argparse.ArgumentParser(description="Export markdown knowledge page to JSON")
    parser.add_argument("--input", required=True, help="Path to markdown file")
    parser.add_argument("--output", help="Path to output JSON (optional, stdout if omitted)")
    args = parser.parse_args()

    path = Path(args.input)
    text = path.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(text)
    sections = parse_sections(body)

    payload = {
        "source_file": str(path),
        "frontmatter": frontmatter,
        "sections": sections,
    }

    out = json.dumps(payload, ensure_ascii=False, indent=2)
    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(out + "\n", encoding="utf-8")
    else:
        print(out)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
