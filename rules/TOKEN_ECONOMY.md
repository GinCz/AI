# ⚡ AI Token Economy: Universal Zero-Waste Rules

> **Production engineering rules and heuristics to achieve 90%+ context window optimization across autonomous coding agents.**
> 
> *Repository:* [GitHub: AI/rules ↗](https://github.com/GinCz/AI/tree/main/rules) | *Author:* [Vladimir Bulantsev (GinCz) ↗](https://github.com/GinCz)

---

## 🎯 Core Principles

Context window exhaustion is the single largest cause of degraded AI reasoning, hallucination, latency spikes, and exorbitant API costs. These rules guarantee zero-waste token management.

---

## 🛑 Rule 1: The "One Task, One Session" Doctrine (`Ctrl+N`)
* **Context Bleed Prevention:** Never reuse an existing long chat thread for an unrelated problem.
* When a task is resolved, commit changes and start fresh (`Ctrl+N`).
* Each session starts with **95%+ free context**, maximizing the LLM’s attention mechanism on the immediate problem.

---

## 🔍 Rule 2: Targeted Slice Reading vs. Whole-File Dumps
* **The 100-Line Limit:** Never read or request entire source code files exceeding 100 lines into the prompt context.
* **Grep First:** Use pattern matching (`ripgrep`, `grep_search`, `Select-String`) to locate the exact function or block.
* **Line-Slice Extraction:** Read only the relevant line range (e.g., lines 140–190) rather than the 2,000-line file.
* **Direct Disk Writes:** Always persist generated code, configs, and scripts directly to disk rather than printing hundreds of lines into the chat window.

---

## 🏛️ Rule 3: Cache-First Knowledge Retrieval
* External enterprise systems (Jira, Confluence, GitHub issues) produce massive JSON payloads (often 5,000–15,000 tokens per call).
* **Fetch Once, Cache Locally:** Save responses locally in Markdown/JSON (`C:\AI\BASE\cache\`).
* Subsequent searches are performed locally against the cache via SQLite FTS5 or ripgrep at ~100 tokens instead of repeating remote API calls.

---

## 📦 Rule 4: Task Knowledge Packs (`task.md`)
* For multi-step tasks, distill only the critical parameters, architectural constraints, and identifiers into a compact `task.md` file (< 50 lines).
* Reference `task.md` instead of the raw conversation history.

---

## ⏱️ Rule 5: Turn-Based Context Watchdog
* Monitor context utilization continuously.
* When a session exceeds 10–15 turns or 50% of the active context limit, trigger compaction:
  1. Summarize accomplishments and current state into `WORKLOG.md`.
  2. Spawn a new fresh session picking up directly from `WORKLOG.md`.

---

## 🧩 Rule 6: MCP Tool Schema Token Budgeting
* **Tool Schema Overhead:** Every registered MCP tool injects its complete JSON schema into the system prompt of every turn, consuming 300–1,500 tokens permanently.
* **Rule:** Enable only active toolsets required for the immediate task. Avoid running 10+ MCP servers concurrently if only file and shell tools are needed.
* Use heavy MCPs (Jira, Confluence, GitHub API) strictly for **cache population scripts**, and lightweight local tools for reasoning.

---

## 🚫 Rule 7: Output Discipline & Relevance Filtering
* Prohibit streaming large Base64 blobs, binary outputs, or multi-megabyte terminal logs into the conversation stream.
* Filter shell command output using pipes (`Select-Object -First 20`, `grep`, `head -n 30`).
* If full output is needed for auditing, redirect to a log file (`> output.log`) and output only the exit code and error summary to the AI.

---

## 🔄 Rule 8: Never Re-Read Unchanged Files
* Within a single task session, do not re-read files that have already been inspected unless an edit or external modification took place.
* Rely on internal memory of the file structure or maintain line-number bookmarks.

---

## ⏳ Rule 9: Freshness TTL over Deletion TTL
* Do not delete cached API records or documentation after an arbitrary period.
* Use lightweight ETag or `Last-Modified` checks against remote APIs. If unchanged, reuse the cached local Markdown file at zero token expense.