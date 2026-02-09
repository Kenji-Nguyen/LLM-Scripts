#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <project_markdown>"
  exit 1
fi

python3 scripts/knowledge_validate.py --file "$1"
