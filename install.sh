#!/usr/bin/env bash
# Installs all skills in this repo to ~/.claude/skills/

set -euo pipefail

SKILLS_DIR="${HOME}/.claude/skills"
REPO_DIR="$(cd "$(dirname "$0")" && pwd)"

installed=0
skipped=0

while IFS= read -r skill_md; do
  rel="${skill_md#"$REPO_DIR/"}"   # e.g. ux-writing/SKILL.md
  parts_count=$(echo "$rel" | tr '/' '\n' | wc -l)

  if [ "$parts_count" -ne 2 ]; then
    echo "⚠ skipped (unexpected depth): $rel"
    skipped=$((skipped + 1))
    continue
  fi

  skill_name=$(dirname "$rel")
  dest="$SKILLS_DIR/$skill_name"
  mkdir -p "$dest"
  cp "$skill_md" "$dest/SKILL.md"
  echo "✓ $skill_name"
  installed=$((installed + 1))
done < <(find "$REPO_DIR" -name "SKILL.md" -not -path "*/.git/*")

echo ""
echo "Done: $installed installed, $skipped skipped → $SKILLS_DIR"
