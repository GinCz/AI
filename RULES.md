# 📜 Universal AI Master Rules (`RULES.md`)

> **Executive summary and routing manifest for autonomous AI agents and coding assistants.**
> 
> *Full Specification:* [`rules/AI_RULES.md ↗`](rules/AI_RULES.md) | *Repository:* [GitHub: AI ↗](https://github.com/GinCz/AI) | *Author:* [Vladimir Bulantsev (GinCz) ↗](https://github.com/GinCz)

---

## 🧭 Multi-Agent Rules Hierarchy

Upon session startup, any autonomous AI coding assistant (Gemini, Claude, Codex/ChatGPT, VS Code AI, Cursor, Copilot) follows this two-step architecture:

1. **Step 1 (Mandatory Base):** Read and cache [`rules/AI_RULES.md ↗`](rules/AI_RULES.md) locally.
2. **Step 2 (Domain Modules):** Access domain guides in [`context-economy/ ↗`](context-economy/) and [`vscode/ ↗`](vscode/).

---

## ⚡ Core Pillars at a Glance

* **Token Economy & Zero Waste:** One task per session (`Ctrl+N`). Read targeted line slices (< 100 lines) instead of whole files. Write assets directly to disk.
* **Full Agentic Autonomy:** When equipped with tools (terminal, filesystem, search), complete tasks end-to-end without offloading routine actions to the user.
* **Epistemic Honesty & Real Verification:** Never hallucinate certainty. Distinguish verified facts from working assumptions. Validate functionality through actual execution, never file creation alone.
* **Monolithic Shell Scripts:** Consolidate multi-command routines into a single script starting with `clear` (Linux/macOS) or `cls` (Windows).
* **Anti-Hang Protection:** Use strict network and SSH timeouts (`ConnectTimeout=5`). Decouple jobs exceeding 60 seconds into background tasks with async notifications.
* **Audio Completion Chimes:** Trigger `C:\Windows\Media\chimes.wav` silently in background only when the entire workload is 100% complete.
* **Single-Line Status Footer:** Conclude each message with:  
  `✅ Done: Started HH:MM:SS • Finished HH:MM:SS • Total: HH:MM:SS (Tokens: ~XXXX response / ~YYYY session)`
* **Continuous Worklog (`WORKLOG.md`):** Maintain an append-only engineering worklog for instant, token-efficient context rehydration across sessions.
* **One-Time Onboarding:** Read rules from GitHub once, cache locally (`C:\AI\<AI_NAME>\RULES.md`), and operate offline from local cache.

---
*For the exhaustive specification, see [`rules/AI_RULES.md ↗`](rules/AI_RULES.md).*