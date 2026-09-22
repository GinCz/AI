# 🌟 Master AI Rules & Zero Dangling Tasks Mandate

> **Personalized Profile & Universal Directives for AI Systems**  
> *Owner:* Vladimir Bulantsev ([GinCz ↗](https://github.com/GinCz)) | *Version:* v2026-09-22

---

## 🛑 Ironclad Zero Dangling Tasks & Immediate Cleanup Mandate

1. **Strict Task Lifecycle Control:**
   - Background tasks must NEVER be left running or dangling unmanaged.
   - Any tool call that sends a process to the background must be tracked, checked, and immediately terminated upon completion using explicit task management.
2. **Synchronous Execution Preference (`WaitMsBeforeAsync: 10000`):**
   - Use maximum synchronous wait (`10000` ms) for all standard commands so execution completes in-line without unneeded background task generation.
3. **Mandatory Pre-Response Audit:**
   - Prior to sending any final response, the agent MUST verify that the active background task count is exactly 0.
   - Any idle, completed, or dangling task MUST be immediately terminated (`manage_task kill`).
4. **SSH Anti-Hang Flags:**
   - Always run non-interactive SSH with timeout safeguards:
     `ssh -o BatchMode=yes -o ConnectTimeout=5 -o ServerAliveInterval=5 -o ServerAliveCountMax=1 -i ~/.ssh/id_ed25519 root@<IP> "<command>"`.

---

## 👑 Core Interaction Rules

- **User Addressing:** Always address the user by name: **Владимир**.
- **Default Language:** Always respond in **Russian** (unless English or Czech is explicitly requested).
- **Single-Line Status Footer:** Single concise footer on English:
  `✅ Start: HH:MM:SS | Stop: HH:MM:SS | Total: XXm YYs (tokens: ~X.Xk)`
- **External Links:** Format all web/repo links with trailing arrow `↗` (e.g. `[GitHub: GinCz ↗](https://github.com/GinCz)`).
- **Directory Isolation:** Workspace is isolated to `C:\UTIL\Antigravity_AI\` (Desktop strictly prohibited).