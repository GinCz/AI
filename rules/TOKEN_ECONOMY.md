# ⚡ AI Token Economy: Universal Zero-Waste Rules

> **Production engineering rules and heuristics to achieve 90%+ context window optimization across autonomous coding agents.**

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