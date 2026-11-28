# 📜 AI Rules & Governance Standards

> **Universal standard for AI models, agents, and IDEs: maximum autonomy, token economy, deterministic execution, and zero-hallucination DevOps workflows.**  
> *Author:* Vladimir Bulantsev ([@GinCz ↗](https://github.com/GinCz)) | *Repository:* [GinCz/AI ↗](https://github.com/GinCz/AI) | *Version:* v2026-11 (v8.0 Universal)

---

## 🧭 Rules Architecture & Structure

To ensure zero-truncation loading across Antigravity IDE/CLI (which enforces a strict **24,000 bytes** per rule file limit), the master specification is maintained both as a complete monolithic document and modular sub-24KB files:

| File | Scope | Purpose | Size |
| :--- | :--- | :--- | :--- |
| **[`BASE_RULES.md ↗`](BASE_RULES.md)** | **Master Manifest** | Complete authoritative specification: Universal Core Rules 1–20 + AntiGravity Personal Directives 1–20. | ~37 KB |
| **[`01_BASE_RULES.md ↗`](01_BASE_RULES.md)** | **Universal Core Rules** | Rules 1 to 20: User addressing, root-cause intake, token economy, git sync, 10s SLA, turnkey execution, security triad. | ~18.5 KB (< 24 KB) |
| **[`02_ANTIGRAVITY_RULES.md ↗`](02_ANTIGRAVITY_RULES.md)** | **AntiGravity Directives** | Directives 1 to 20: Single workspace, zero passive skill loading, multi-server secret access, MEGA desktop delivery, chime alerts. | ~18.7 KB (< 24 KB) |
| **[`TOKEN_ECONOMY.md ↗`](TOKEN_ECONOMY.md)** | **Context Management** | Tactical heuristics and rules for minimizing token consumption by 90%+ across CLI, IDE, and chat sessions. | ~9 KB |

---

## ⚡ Core Operational Directives (Key Highlights)

1. **Owner Addressing:** Always address Vladimir by name at the beginning of EVERY response (`Владимир, ...`).
2. **Turnkey Execution:** 100% autonomous delivery without permission questions ("Shall I do this? / Делаем?").
3. **Smart Autonomous Skill Usage (Zero Passive Preloading):**
   * Skills are specialized on-demand tools ONLY (e.g., `facebook-management`, `czech-accounting-tax`).
   * **Categorical ban on eagerly loading, reading, or indexing skills at session start or during general queries.**
   * For general logic, math, system diagnostics, bash commands, date/time calculations: answer immediately without skills!
4. **Strict 10-Second Response SLA:** Direct answers must be delivered within maximum 10 seconds.
5. **No Rule Truncation:** Antigravity loads `01_BASE_RULES.md` and `02_ANTIGRAVITY_RULES.md` so that all rules are fully ingested without hitting the 24,000 byte limit.
6. **Mandatory WORKLOG Logging & Git Push:** Update `WORKLOG.md` before sending final confirmation, commit, push, and play the completion chime.
