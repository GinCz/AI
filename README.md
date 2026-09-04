<div align="center">

# 🤖 AI Agent Engineering & Context Economy Hub

**Universal Operational Standards, Zero-Waste Token Economy Protocols, Multi-Agent Governance, and Free Production IDE Stacks.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/GinCz/AI?style=social)](https://github.com/GinCz/AI)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/GinCz/AI/pulls)
[![Maintained](https://img.shields.io/badge/Maintained-Yes-success.svg)](https://github.com/GinCz/AI)
[![Environment](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-informational.svg)](https://github.com/GinCz/AI)

[Architecture](#-system-architecture) •
[Directory Structure](#-repository-structure) •
[Core Pillars](#-core-engineering-pillars) •
[Quickstart](#-quickstart--agent-onboarding) •
[Topics & Tags](#-hashtags--topics)

</div>

---

## 📖 Overview

The **`AI`** repository is a battle-tested, open-source architectural blueprint designed to elevate AI coding assistants—including **Google Antigravity & Gemini**, **Anthropic Claude**, **OpenAI Codex & ChatGPT**, **Cursor IDE**, and **GitHub Copilot**—from basic conversational bots into **highly disciplined, context-efficient, autonomous software engineering agents**.

### The Problem It Solves
1. **Context Exhaustion & Token Waste:** Unconstrained agents flood context windows with entire files and repetitive API requests, driving up costs and degrading model reasoning.
2. **Interactive Friction:** Agents frequently stop to ask users to run commands or perform trivial diagnostics they could execute themselves.
3. **Workspace Chaos:** Multiple AI agents clobbering one another's temporary scripts, scratchpads, and configurations across the filesystem.

---

## 🏛️ System Architecture

```text
                                 [ User / Developer ]
                                           │
                                           ▼
                 ┌───────────────────────────────────────────────────┐
                 │       STEP 1: Mandatory Global AI Rules           │
                 │              📄 rules/AI_RULES.md                 │
                 │  • Zero-Waste Token Economy (Slice Reading)       │
                 │  • Full Agentic Autonomy (Do It Yourself First)   │
                 │  • Monolithic Scripts (cls/clear execution)       │
                 │  • Audio Chimes & Single-Line Status Footers      │
                 └─────────────────────────┬─────────────────────────┘
                                           │
                    ┌──────────────────────┴──────────────────────┐
                    ▼                                             ▼
┌───────────────────────────────────────┐   ┌───────────────────────────────────────┐
│     STEP 2A: Context Economy          │   │      STEP 2B: IDE & Agent Stacks      │
│     📁 context-economy/               │   │      📁 vscode/                       │
│ • Cache-First Knowledge Layer         │   │ • Continue.dev Configuration          │
│ • Jira/Confluence/NotebookLM Caching  │   │ • Free High-Speed Models (Groq/Gemini)│
│ • Task Knowledge Packs (task.md)      │   │ • Remote-SSH Headless Infrastructure  │
│ • SQLite FTS5 / Ripgrep Local Search  │   │ • GitHub Copilot Rule Templates       │
└───────────────────────────────────────┘   └───────────────────────────────────────┘
```

---

## 🧭 Repository Structure

All architectural components, rules, and scripts are categorized into clean, dedicated modules:

| Directory / File | Description | Target Scope | Direct Link |
| :--- | :--- | :---: | :--- |
| **[`rules/ ↗`](rules/)** | **Universal AI Master Rules & Governance** | All AI Agents | [`rules/README.md ↗`](rules/README.md) |
| ├── [`AI_RULES.md ↗`](rules/AI_RULES.md) | Master governance protocol (Autonomy, Timeouts, Chimes, Status Footers) | Universal | [`rules/AI_RULES.md ↗`](rules/AI_RULES.md) |
| └── [`TOKEN_ECONOMY.md ↗`](rules/TOKEN_ECONOMY.md) | Practical token optimization rules (Turn limits, slice reading) | Context Ops | [`rules/TOKEN_ECONOMY.md ↗`](rules/TOKEN_ECONOMY.md) |
| **[`context-economy/ ↗`](context-economy/)** | **Cache-First Knowledge Layer & DevOps Token Guide** | Engineering | [`context-economy/README.md ↗`](context-economy/README.md) |
| ├── [`KNOWLEDGE_CACHE.md ↗`](context-economy/KNOWLEDGE_CACHE.md) | Local unified database specs (Jira, Confluence, NotebookLM) | Database | [`context-economy/KNOWLEDGE_CACHE.md ↗`](context-economy/KNOWLEDGE_CACHE.md) |
| └── [`scripts/ ↗`](context-economy/scripts/) | Sync scripts for caching enterprise tickets (`sync-jira-cache.ps1`) | Automation | [`scripts/sync-jira-cache.ps1 ↗`](context-economy/scripts/sync-jira-cache.ps1) |
| **[`vscode/ ↗`](vscode/)** | **VS Code + Continue.dev + Copilot Production Setup** | IDE / DevEnv | [`vscode/README.md ↗`](vscode/README.md) |
| ├── [`config.yaml ↗`](vscode/config.yaml) | Production Continue.dev configuration with free AI API endpoints | Config | [`vscode/config.yaml ↗`](vscode/config.yaml) |
| ├── [`copilot-instructions.md ↗`](vscode/copilot-instructions.md) | Standard repository instruction template for GitHub Copilot | Instruction | [`vscode/copilot-instructions.md ↗`](vscode/copilot-instructions.md) |
| └── [`ssh_config.example ↗`](vscode/ssh_config.example) | Hardened SSH configuration template for remote agent work | Networking | [`vscode/ssh_config.example ↗`](vscode/ssh_config.example) |
| **[`RULES.md ↗`](RULES.md)** | Root executive rules overview & agent routing entry point | Quick Reference | [`RULES.md ↗`](RULES.md) |

---

## ⚡ Core Engineering Pillars

### 1️⃣ Zero-Waste Token Economy (90%+ Context Reduction)
* **One Task Per Session (`Ctrl+N`):** Distinct tasks run in pristine sessions, preserving 95%+ of model attention.
* **Slice-Only Reading:** Never inject files over 100 lines into context. Use regex / ripgrep and targeted line slices (`StartLine`/`EndLine`).
* **Cache-First Knowledge Retrieval:** Heavy Jira/Confluence responses (5,000–12,000 tokens) are fetched once, stored locally, and queried via SQLite FTS5 / ripgrep (~100 tokens).

### 2️⃣ Full Agentic Autonomy (Do It Yourself First)
* If an agent possesses terminal or file-editing tools, it executes tasks end-to-end without offloading commands, diagnostics, or manual edits to the user.
* Monolithic script execution: commands are batched into a single cohesive script starting with `clear` (Bash) or `cls` (CMD/PowerShell).

### 3️⃣ Centralized Knowledge Base & Workspace Isolation
* Sandboxed workspace folders (`C:\AI\<AGENT_NAME>\`) isolate active agents.
* A shared, append-only knowledge base (`C:\AI\BASE\`) uses an ultra-compact router (`INDEX.md` < 40 lines) to load targeted topics on demand.

### 4️⃣ Production Free IDE Stack (VS Code + Continue.dev)
* Production-ready integration for free, high-speed LLMs:
  - **Groq Cloud:** LLaMA 3.3 70B (ultra-low latency tab autocomplete and agent mode).
  - **Google AI Studio:** Gemini 2.0 Flash / Pro (up to 2M context window).
  - **Mistral AI:** Mistral Large Latest.
  - **OpenRouter:** Free open-weights models (`:free`).

### 5️⃣ Professional Status Footers & Audio Feedback
* **Audio Completion Chimes:** Triggers `C:\Windows\Media\chimes.wav` silently upon 100% completion of background jobs.
* **Single-Line Status Footers:** Clean, readable execution metrics at the end of every response:  
  `✅ Done: Started 14:00:00 • Finished 14:02:30 • Total: 00:02:30 (Tokens: ~1200 response / ~5400 session)`

---

## 🚀 Quickstart / Agent Onboarding

When introducing a new AI agent to your machine or repository, send this one-time prompt:

```text
Please read the universal governance rules from https://github.com/GinCz/AI/blob/main/rules/AI_RULES.md
Cache them locally in your dedicated workspace (e.g., C:\AI\<YOUR_NAME>\RULES.md) and confirm.
Operate autonomously using the local cache for all subsequent tasks without re-querying GitHub.
```

---

## 🏷️ Hashtags & Topics

`#ai` `#agentic-ai` `#token-economy` `#llm` `#devops` `#prompt-engineering` `#context-window` `#vscode` `#continue-dev` `#github-copilot` `#gemini` `#claude` `#codex` `#cursor-ai` `#zero-waste` `#automation` `#system-architecture` `#developer-tools`

---

## 👤 Author & Maintainer

* **Author:** Vladimir Bulantsev ([@GinCz ↗](https://github.com/GinCz))
* **Repository:** [https://github.com/GinCz/AI ↗](https://github.com/GinCz/AI)
* **License:** [MIT License](LICENSE)