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

# Keep .agents/skills and ~/.gemini/config/skills in sync with skills (only directories)
if [ -d "/AI/GitHub/BASE/SKILLS" ]; then
  mkdir -p /AI/.agents/skills /root/.gemini/config/skills
  find /AI/GitHub/BASE/SKILLS -mindepth 1 -maxdepth 1 -type d ! -name PROMPTS -exec cp -ru {} /AI/.agents/skills/ \; 2>/dev/null || true
  find /AI/GitHub/BASE/SKILLS -mindepth 1 -maxdepth 1 -type d ! -name PROMPTS -exec cp -ru {} /root/.gemini/config/skills/ \; 2>/dev/null || true
elif [ -d "/AI/skills" ] && [ -d "/AI/.agents/skills" ]; then
  find /AI/skills -mindepth 1 -maxdepth 1 -type d ! -name PROMPTS -exec cp -ru {} /AI/.agents/skills/ \; 2>/dev/null || true
fi

# Keep rules synchronized across ~/.gemini/config
if [ -d "/AI/GitHub/AI/rules" ]; then
  mkdir -p /root/.gemini/config/rules
  # Copy only active modular rule files (<24KB) to avoid Antigravity truncation and duplicates
  if [ -f "/AI/GitHub/AI/rules/01_BASE_RULES.md" ] && [ -f "/AI/GitHub/AI/rules/02_ANTIGRAVITY_RULES.md" ]; then
    cp -u /AI/GitHub/AI/rules/01_BASE_RULES.md /root/.gemini/config/rules/ 2>/dev/null || true
    cp -u /AI/GitHub/AI/rules/02_ANTIGRAVITY_RULES.md /root/.gemini/config/rules/ 2>/dev/null || true
    # Remove oversized or legacy files that cause prompt truncation
    rm -f /root/.gemini/config/rules/BASE_RULES.md /root/.gemini/config/rules/AI_RULES.md /root/.gemini/config/rules/ALL_AI_RULES.md 2>/dev/null || true
  fi
  if [ -f "/AI/GitHub/AI/rules/BASE_RULES.md" ]; then
    cp -u /AI/GitHub/AI/rules/BASE_RULES.md /AI/AGENTS.md 2>/dev/null || true
    ln -sfn /AI/AGENTS.md /AI/RULES.md 2>/dev/null || true
  fi
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
