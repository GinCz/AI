# 📜 AI Rules & Governance Standards

> **Operational guardrails, context economy protocols, and agent orchestration patterns.**

---

## 🧭 Directory Overview

This directory houses the foundational operational standards required for autonomous AI coding agents and LLM-assisted engineering workflows.

| File | Scope | Purpose |
| :--- | :--- | :--- |
| **[`AI_RULES.md ↗`](AI_RULES.md)** | **Global Mandatory** | Core rules covering agent autonomy, sandbox isolation, monolithic execution, timeouts, notification protocols, fact-based pushback (no blind agreement), and skills adoption. |
| **[`ALL_AI_RULES/RULES.md ↗`](../ALL_AI_RULES/RULES.md)** | **Master Multi-AI Manifest** | Full Russian-language master manifest: Two-Step Pipeline, Token Economy, Auto-Routing, Zero Dangling Tasks, Zero Blind Agreement, and Version Bump Mandate. |
| **[`TOKEN_ECONOMY.md ↗`](TOKEN_ECONOMY.md)** | **Context Management** | Tactical rules for minimizing token consumption by 90%+ across CLI, IDE, and chat sessions. |

---

## ⚡ Loading Priority for Agents

1. **Step 1 (Root/Universal):** Load [`AI_RULES.md ↗`](AI_RULES.md) once during bootstrap.
2. **Step 2 (Local Cache):** Cache rules locally in `C:\AI\<AI_NAME>\RULES.md` or `/root/AI_157/RULES.md`.
3. **Step 3 (Specialized Modules):** Load domain configurations from [`../context-economy/ ↗`](../context-economy/) and [`../vscode/ ↗`](../vscode/).
4. **Step 4 (Expert Skills Framework):** Navigate to [`../skills/ ↗`](../skills/) (or [`../skills/ALL_SKILLS.md ↗`](../skills/ALL_SKILLS.md)) and activate all domain skills into model capabilities.