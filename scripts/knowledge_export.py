#!/usr/bin/env python3
"""Export a section-based markdown knowledge page to JSON."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
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


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value or "untitled"


def next_revision(path_without_rev: str, ext: str) -> int:
    rev = 1
    while True:
        candidate = Path(f"{path_without_rev}__r{rev:02d}.{ext}")
        if not candidate.exists():
            return rev
        rev += 1


def build_auto_output_path(
    frontmatter: dict,
    project_id_override: str | None,
    artifact_type: str,
    title_override: str | None,
    lang_override: str | None,
) -> Path:
    project_id = slugify(project_id_override or frontmatter.get("project_id", "unknown-project"))
    artifact = slugify(artifact_type)
    title = slugify(title_override or frontmatter.get("title", "knowledge-export"))
    lang = slugify(lang_override or frontmatter.get("language_mode", "na")).upper()

    timestamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    base_dir = Path("exports") / project_id / artifact
    stem_without_rev = f"{timestamp}__{project_id}__{artifact}__{title}__{lang}"
    path_without_rev = str(base_dir / stem_without_rev)
    rev = next_revision(path_without_rev, "json")
    return Path(f"{path_without_rev}__r{rev:02d}.json")


def effective_project_id(frontmatter: dict, project_id_override: str | None) -> str:
    value = slugify(project_id_override or frontmatter.get("project_id", ""))
    return value


def write_manifest_row(manifest_path: Path, output_path: Path, payload: dict) -> None:
    entry = {
        "created_at": dt.datetime.now().isoformat(timespec="seconds"),
        "output_file": str(output_path),
        "source_file": payload.get("source_file"),
        "project_id": payload.get("frontmatter", {}).get("project_id", ""),
        "language_mode": payload.get("frontmatter", {}).get("language_mode", ""),
        "title": payload.get("frontmatter", {}).get("title", ""),
    }
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    with manifest_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Export markdown knowledge page to JSON")
    parser.add_argument("--input", required=True, help="Path to markdown file")
    parser.add_argument("--output", help="Path to output JSON (optional, auto path if omitted)")
    parser.add_argument(
        "--project-id",
        help="Optional project ID override for auto output naming",
    )
    parser.add_argument(
        "--artifact-type",
        default="json",
        help="Artifact type folder/name for auto output path (default: json)",
    )
    parser.add_argument(
        "--title",
        help="Optional title override for auto output naming",
    )
    parser.add_argument(
        "--lang",
        help="Optional language override for auto output naming",
    )
    parser.add_argument(
        "--no-manifest",
        action="store_true",
        help="Do not append a row to exports/manifest.jsonl",
    )
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
    project_id = effective_project_id(frontmatter, args.project_id)
    if not project_id:
        print("[ERROR] Missing project_id. Provide frontmatter project_id or --project-id.")
        return 1

    out_path = Path(args.output) if args.output else build_auto_output_path(
        frontmatter=frontmatter,
        project_id_override=project_id,
        artifact_type=args.artifact_type,
        title_override=args.title,
        lang_override=args.lang,
    )

    # Keep exports collected under project scope.
    required_root = (Path.cwd() / "exports" / project_id).resolve()
    abs_out = (Path.cwd() / out_path).resolve() if not out_path.is_absolute() else out_path.resolve()
    if required_root not in abs_out.parents and abs_out != required_root:
        print(
            f"[ERROR] Output must be inside exports/{project_id}/... "
            f"(got: {out_path})"
        )
        return 1

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(out + "\n", encoding="utf-8")

    if not args.no_manifest:
        write_manifest_row(Path("exports/manifest.jsonl"), out_path, payload)
        write_manifest_row(Path("exports") / project_id / "manifest.jsonl", out_path, payload)

    print(str(out_path))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
