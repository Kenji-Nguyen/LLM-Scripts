#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <input_markdown> <output_json>"
  exit 1
fi

python3 scripts/knowledge_export.py --input "$1" --output "$2"
