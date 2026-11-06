#!/usr/bin/env bash
set -e

GITHUB_DIR="/AI/GitHub"
LOG_FILE="/AI/sync.log"
DATE_STR=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$DATE_STR] Starting GitHub synchronization..." >> "$LOG_FILE"

synced_count=0
updated_count=0
error_count=0

# Include root workspace /AI as well as all repositories in /AI/GitHub
REPOS=()
if [ -d "/AI/.git" ]; then
  REPOS+=("/AI")
fi
for repo_dir in "$GITHUB_DIR"/*; do
  if [ ! -L "$repo_dir" ] && [ -d "$repo_dir/.git" ]; then
    REPOS+=("$repo_dir")
  fi
done

for repo_dir in "${REPOS[@]}"; do
  repo_name=$(basename "$repo_dir")
  cd "$repo_dir"
  
  # Configure safe directory
  git config --global --add safe.directory "$repo_dir" >/dev/null 2>&1 || true
  
  # Fetch with timeout
  if timeout 15s git fetch origin >/dev/null 2>&1; then
    current_branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "main")
    local_hash=$(git rev-parse HEAD 2>/dev/null || echo "1")
    remote_hash=$(git rev-parse "origin/$current_branch" 2>/dev/null || echo "2")
    
    if [ "$local_hash" != "$remote_hash" ]; then
      if git diff-index --quiet HEAD -- 2>/dev/null; then
        git merge --ff-only "origin/$current_branch" >/dev/null 2>&1 || git pull --rebase >/dev/null 2>&1 || true
        updated_count=$((updated_count + 1))
        echo "[$DATE_STR] Updated $repo_name ($current_branch)" >> "$LOG_FILE"
      else
        echo "[$DATE_STR] Repo $repo_name has local changes, skipping pull" >> "$LOG_FILE"
      fi
    fi
    synced_count=$((synced_count + 1))
  else
    error_count=$((error_count + 1))
    echo "[$DATE_STR] Failed to fetch $repo_name" >> "$LOG_FILE"
  fi
done

# Keep .agents/skills in sync with skills (only directories)
if [ -d "/AI/skills" ] && [ -d "/AI/.agents/skills" ]; then
  find /AI/skills -mindepth 1 -maxdepth 1 -type d ! -name PROMPTS -exec cp -ru {} /AI/.agents/skills/ \; 2>/dev/null || true
fi

echo "[$DATE_STR] Synchronization complete: $synced_count checked, $updated_count updated, $error_count errors" >> "$LOG_FILE"

# If called as hook (stdin has JSON or stdin not a terminal)
if [ ! -t 0 ]; then
  cat << JSON_OUT
{
  "injectSteps": [
    {
      "systemMessage": {
        "systemMessage": "✅ [GitHub Sync] Локальные репозитории (/AI и /AI/GitHub/) синхронизированы: $synced_count проверено, $updated_count обновлено."
      }
    }
  ]
}
JSON_OUT
else
  echo "✅ GitHub sync complete: $synced_count checked, $updated_count updated, $error_count errors."
fi
