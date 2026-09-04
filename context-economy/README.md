# ⚡ AI Token Economy: Practical DevOps Engineering Guide

> **Production engineering patterns for context optimization and 90%+ token reduction across autonomous AI coding agents and LLMs (Cursor, Google Antigravity, Claude Code, OpenAI Codex, GitHub Copilot, Google Gemini).**  
> 🔗 Repository: [GitHub: AI/context-economy ↗](https://github.com/GinCz/AI/tree/main/context-economy) | Author: [GinCz ↗](https://github.com/GinCz)

---

## 🏛️ 1. Architecture: Cache-First Knowledge Access

The foundational solution for optimal token usage and AI context management is the **Cache-First Knowledge Access** architecture. Instead of constantly scraping external enterprise systems (Confluence, Jira) or dumping entire project structures into the AI context, we implement a lazy-loading caching mechanism.

### The Cache-First Workflow

```text
              Jira / Confluence
                     ↓
              FIRST DISCOVERY
                     ↓
              FULL FETCH
                     ↓
            ┌─────────────────┐
            │ LOCAL KNOWLEDGE │
            │     CACHE       │
            └────────┬────────┘
                     ↓
                LOCAL SEARCH
                     ↓
             TASK KNOWLEDGE PACK
                     ↓
                    AI
                     ↓
          Remote API only if needed
```

1. **First Discovery:** Use tools/MCP for a lightweight metadata search.
2. **Full Fetch:** Identify relevant tickets/pages and fetch them completely.
3. **Local Knowledge Cache:** Save the complete raw response locally (JSON + Markdown) into a unified local database (combining Jira, Confluence, and custom knowledge notes).
4. **Local Search:** For all subsequent inquiries, perform a local SQLite FTS5 or ripgrep search against the cache.
5. **Task Knowledge Pack:** Assemble only the necessary fragments into a small task-specific context bundle (`task.md`).

This transforms heavy operations (e.g., 5,000–12,000 tokens per MCP fetch) into lightweight local reads (~100–200 tokens).

---

## 🚨 2. Operational Guard: Intelligent Context Limits

To enforce task isolation and prevent silent context bloat, the AI assistant evaluates session weight continuously:

* **Context Threshold Warnings:** Warn when context utilization approaches high watermarks of the model's active window.
* **Turn Thresholds:** Use 8–15 turns as a rule of thumb for task isolation, and compress key state into persistent summaries (`WORKLOG.md`) before resetting the session.

---

## ⚡ 3. 10 DevOps Engineering Guidelines for Token Efficiency

1. **"Fetch Once, Reuse Many":**
   * If an external system returns a relevant record, fetch it completely, save it locally, and never call the remote system for that record again unless freshness verification is required.
2. **Persistent Git Worklog (`WORKLOG.md`):**
   * Maintain a running Markdown journal of architectural changes, configurations, and fixes. New sessions re-hydrate technical context efficiently.
3. **Task Knowledge Packs (`task.md`):**
   * Group related cached tickets and current hypotheses into a tiny task-specific directory rather than feeding the AI a monolithic database.
4. **Freshness TTL, Not Deletion TTL:**
   * Do not delete cached tickets after 90 days. Instead, use a `freshness_check_after` date. Historical solved tickets provide immense problem-solving context.
5. **Zero-Bloat Chat Discipline:**
   * Prohibit streaming large source code files, Base64 dumps, or raw terminal logs into the conversation stream. Write assets directly to disk and return concise diffs and target paths.
6. **Slice-Only File Reading:**
   * Avoid full-file reads on files exceeding 100 lines. Enforce bounded line slices (`StartLine`/`EndLine` in 50–100 line blocks) or targeted `ripgrep` queries.
7. **Monolithic Command Execution:**
   * Combine multi-command shell routines into a single consolidated script starting with terminal clearing (`clear` / `cls`). Avoid interactive one-by-one round-trips.
8. **Anti-Hang and Decoupled Background Daemons:**
   * Ban continuous polling loops in the chat interface. For operations exceeding 60 seconds, decouple execution into standalone background services with asynchronous notifications.
9. **Strict Workspace Ignore Filters:**
   * Exclude `.git/`, `node_modules/`, `vendor/`, `dist/`, `build/`, `*.log`, `*.zip`, and binary dumps from AI indexing and search scopes.
10. **Targeted MCP Strategy:**
    * Use Heavy Enterprise MCPs (Jira/Confluence) strictly for **cache population**, and local tools (`grep_search`, `view_file`) for **reasoning**.

---

## 📁 4. Engine Navigation

| AI Engine / Environment | Relevant Document | Primary Focus |
| :--- | :--- | :--- |
| **Universal Standards** | [`../rules/AI_RULES.md ↗`](../rules/AI_RULES.md) | Universal Agent Master Rules, Autonomy, Sandbox Isolation |
| **Token Economy Rules** | [`../rules/TOKEN_ECONOMY.md ↗`](../rules/TOKEN_ECONOMY.md) | Turn Limits, Slice Reading, Zero-Waste Protocols |
| **Knowledge Cache Spec** | [`KNOWLEDGE_CACHE.md ↗`](KNOWLEDGE_CACHE.md) | Local Database Layout, Schema, and Sync Tooling |
| **VS Code & Copilot** | [`../vscode/README.md ↗`](../vscode/README.md) | Extension setup, Continue.dev config, free AI models |

---
*Maintained and versioned in [GitHub: AI ↗](https://github.com/GinCz/AI).*