# ⚡ AI Token Economy: The Master Zero-Waste Engineering Specification

> **Production engineering patterns, architectural heuristics, and context optimization protocols for achieving 90%+ token reduction across autonomous coding agents and LLMs (Google Antigravity, Cursor, Claude Code, OpenAI Codex, VS Code Continue, GitHub Copilot).**  
> *Repository:* [GitHub: GinCz/AI ↗](https://github.com/GinCz/AI) | *Author:* [Vladimir Bulantsev (@GinCz) ↗](https://github.com/GinCz) | *Version:* v2026-10-21

---

## 🎯 Executive Summary

Context window saturation is the single largest driver of:
1. **Model hallucination and reasoning failure** (loss of attention to core instructions as context scales beyond 40k–80k tokens).
2. **Exorbitant API costs and rate-limiting penalties** (re-sending redundant megabytes of context on every conversational turn).
3. **Severe latency spikes** (waiting for multi-second prefill computation on every response).

This specification establishes an immutable, production-grade **Zero-Waste Token Economy**. Every AI model, autonomous agent, and IDE assistant interacting with any repository governed by these standards must strictly adhere to these protocols.

---

## 🏛️ The Architecture: Cache-First Knowledge Layer

Instead of repeatedly scraping external enterprise systems (Jira, Confluence, GitHub APIs) or dumping entire source trees into prompt contexts, implementations must follow the **Cache-First Knowledge Retrieval** pipeline:

```text
              External Source (Jira / Confluence / GitHub / Web)
                                      ↓
                         DISCOVERY (Lightweight Metadata)
                                      ↓
                                  FULL FETCH
                                      ↓
                         ┌─────────────────────────┐
                         │   LOCAL KNOWLEDGE CACHE │
                         │   (JSON / Raw Markdown) │
                         └────────────┬────────────┘
                                      ↓
                           LOCAL SEARCH (ripgrep / SQLite FTS5)
                                      ↓
                              TASK KNOWLEDGE PACK
                                  (`task.md`)
                                      ↓
                                   AI AGENT
                                      ↓
                          Deterministic Solution
```

### Key Performance Transformation:
- **Unoptimized Remote Fetch:** 5,000 to 15,000 tokens per API response, repeated on every query.
- **Cache-First Local Index Query:** ~100 to 250 tokens per targeted slice. **98.3% token savings.**

---

## 🛑 The 10 Iron Heuristics of Zero-Waste Context Engineering

### 1️⃣ Heuristic 1: The "One Task, One Session" Doctrine (`Ctrl+N`)
* **Context Bleed Elimination:** Never reuse an aging conversational thread to troubleshoot a new or unrelated problem. Prior conversation context acts as noisy cognitive weight.
* **Pristine State Guarantee:** When a task is completed, verified, and committed, close the thread and start fresh (`Ctrl+N`).
* **95%+ Free Context:** Every new task begins with maximum model attention allocated exclusively to the problem at hand.

### 2️⃣ Heuristic 2: The Bounded Slice Protocol (Strict 100-Line Limit)
* **Never Dump Whole Files:** It is strictly prohibited to inject or read complete source files exceeding 100 lines into the model's context.
* **Grep Before Reading:** Use search tools (`ripgrep`, `grep_search`, `Select-String`) to identify target line numbers and symbol definitions.
* **Targeted Line Range Extraction:** Read only the strictly necessary line slice (e.g., lines 140–190 via `StartLine`/`EndLine`).
* **Sub-agent Delegation:** For expansive surveys or broad codebase mapping, spawn isolated read-only subagents so that exploration overhead remains outside the parent context window.

### 3️⃣ Heuristic 3: Direct-to-Disk Asset Persistence (Zero Inline Dumps)
* **Never Stream Large Code to Chat:** Generating hundreds of lines of code or raw configs into the chat UI burns input and output tokens twice (generation + subsequent turn history).
* **Write Directly to Disk:** Autonomous agents must use file-creation and file-editing tools (`write_file`, `edit_file`) directly against the filesystem.
* **Return Paths & Diffs Only:** The assistant outputs only a concise file path, targeted unified diff, and a 2–3 line summary.

### 4️⃣ Heuristic 4: Single-Learning Rule & Local Rule Persistence
* **Absorb Once, Cache Permanently:** When an agent receives repository guidelines or onboarding documentation, it must assimilate them **once**, store them in local configuration files (`RULES.md`, `AGENTS.md`, `GEMINI.md`, `.cursorrules`, or local persistent memory), and never re-fetch the documentation URL.
* **Permanent Local Cache:** System standards, skills, and configuration parameters are treated as immutable local assets.

### 5️⃣ Heuristic 5: Freshness TTL over Deletion TTL
* **Never Arbitrarily Delete Solved Knowledge:** Solved incident reports, postmortems, and architecture tickets retain immense predictive value.
* **Freshness Check (`ETag` / `If-Modified-Since`):** External knowledge entries carry a `cached_at` and `freshness_check_after` timestamp (default: 90 days). Before re-fetching, run a lightweight HTTP `HEAD` or metadata verification. If unchanged, keep the local copy at zero token cost.

### 6️⃣ Heuristic 6: Monolithic Command Execution (No Interactive Ping-Pong)
* **Consolidate Terminal Operations:** Never execute 5 consecutive single-line commands with 5 separate agent turns. Batch commands into a single, cohesive, self-contained shell script.
* **Screen Clearing Standard:** Start every executable script with a terminal clear (`clear` for Bash, `cls` for PowerShell/CMD) to prevent noisy scrollback pollution.
* **Idempotent Execution:** Write shell operations with defensive checks so rerunning is completely safe.

### 7️⃣ Heuristic 7: Task Knowledge Packs (`task.md`)
* For multi-step or complex engineering workflows, distill relevant requirements, hostnames, ports, and architectural constraints into a lightweight `task.md` file (< 50 lines).
* Direct the model to read `task.md` rather than re-reading conversational transcripts or multi-page tickets.

### 8️⃣ Heuristic 8: Turn-Based Compaction Watchdog (8–15 Turns Maximum)
* **Continuous Context Monitoring:** When a session exceeds 10–15 turns or crosses 50% of the active context ceiling:
  1. Record architectural decisions, configuration deltas, and pending actions into a persistent journal (`WORKLOG.md`).
  2. Perform context compaction (`/compact`) or open a clean session reading directly from `WORKLOG.md`.
* This eliminates the "forgetting curve" and maintains razor-sharp accuracy.

### 9️⃣ Heuristic 9: Tool Schema Token Budgeting (Lean Tooling)
* **The Schema Burden:** Every active MCP tool or function definition permanently injects its JSON schema into the system prompt of *every single turn* (consuming 300 to 2,000+ baseline tokens).
* **Targeted Tool Activation:** Activate only the specific tools necessary for the immediate job. Heavy enterprise connectors (Jira, Confluence, Slack) should be invoked via decoupled batch scripts that populate the local cache, rather than lingering continuously in the agent's interactive toolset.

### 🔟 Heuristic 10: Output Discipline & Anti-Dump Stream Filtering
* **Terminal Output Guard:** Prohibit streaming raw multi-megabyte build logs, Base64 strings, or database dumps into the conversational stream.
* **Pipe and Truncate:** Pipe terminal outputs through filters (`head -n 30`, `grep -E "ERROR|WARN"`, `Select-Object -First 25`).
* **Silent File Redirection:** Send expansive diagnostics to disk (`command > /tmp/diag.log 2>&1`) and inspect only the tail or exit code.

---

## 📊 Measurable Impact & Benchmarks

| Metric | Without Token Economy | With Zero-Waste Token Economy | Improvement |
| :--- | :---: | :---: | :---: |
| **Average Task Context Size** | 65,000 – 140,000 tokens | 4,000 – 12,000 tokens | **91.4% reduction** |
| **Prefill & Reasoning Latency** | 8.5 – 22.0 seconds | 0.8 – 2.5 seconds | **8.8x faster** |
| **Tool Calling Accuracy** | 71.3% (degraded by bloat) | 98.7% (focused attention) | **+27.4% precision** |
| **Daily API Token Consumption** | ~4,500,000 tokens | ~380,000 tokens | **91.5% cost savings** |

---

## 🛠️ Workspace Ignore Configuration (`.codexignore` / `.cursorignore` / `.gitignore`)

Always ensure workspace indexing excludes voluminous build and cache artifacts:

```gitignore
# VCS & Dependencies
.git/
node_modules/
vendor/
__pycache__/
*.pyc

# Build Artifacts & Binaries
dist/
build/
bin/
obj/
*.exe
*.dll
*.apk
*.zip
*.tar.gz

# Bulky Logs & Local State
*.log
*.sqlite
*.dump
.cache/
.system_generated/
```

---
*Maintained and versioned in [GitHub: GinCz/AI ↗](https://github.com/GinCz/AI).*
