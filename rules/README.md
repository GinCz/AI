# 📜 AI Rules & Governance Standards

> **Operational guardrails, context economy protocols, and agent orchestration patterns.**

---

## 🧭 Directory Overview

This directory houses the foundational operational standards required for autonomous AI coding agents and LLM-assisted engineering workflows.

| File | Scope | Purpose |
| :--- | :--- | :--- |
| **[`AI_RULES.md ↗`](AI_RULES.md)** | **Global Mandatory** | Core rules covering agent autonomy, sandbox isolation, monolithic execution, timeouts, and notification protocols. |
| **[`TOKEN_ECONOMY.md ↗`](TOKEN_ECONOMY.md)** | **Context Management** | Tactical rules for minimizing token consumption by 90%+ across CLI, IDE, and chat sessions. |

---

## ⚡ Loading Priority for Agents

1. **Step 1 (Root/Universal):** Load [`AI_RULES.md ↗`](AI_RULES.md) once during bootstrap.
2. **Step 2 (Local Cache):** Cache rules locally in `C:\AI\<AI_NAME>\RULES.md`.
3. **Step 3 (Specialized Modules):** Load domain configurations from [`../context-economy/ ↗`](../context-economy/) and [`../vscode/ ↗`](../vscode/).