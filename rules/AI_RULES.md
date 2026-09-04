# 📜 Universal AI Master Rules & Governance (`AI_RULES.md`)
> **Unified operational standards, token economy protocols, and agent autonomy guidelines for LLMs and autonomous coding assistants.**
> 
> *Repository:* [GitHub: AI ↗](https://github.com/GinCz/AI) | *Author:* [Vladimir Bulantsev (GinCz) ↗](https://github.com/GinCz) | *Version:* v2026-09-04

---

## 🏗️ 1. Two-Step Architecture (Rules Chain)

Every AI coding agent (Google Antigravity/Gemini, Anthropic Claude, OpenAI Codex/ChatGPT, VS Code AI, Cursor, GitHub Copilot) follows a strict two-step execution model upon session initialization:

```text
[AI Session Initialized]
           │
           ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 1: Global Mandatory Rules (This Document)                  │
│ 📄 rules/AI_RULES.md                                            │
│ • Token Economy & Zero Waste                                    │
│ • Full Agentic Autonomy                                         │
│ • Local Sandbox Isolation                                       │
│ • Single-Line Status Footer & Chimes Notification               │
└─────────────────────────────────────────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 2: Domain-Specific Modules                                 │
│ 📁 context-economy/ → Cache-First Knowledge Layer & Token Reduction │
│ 📁 vscode/          → VS Code, Continue.dev, and Copilot Configs   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🚀 2. One-Time Onboarding & Local Caching Protocol

> **CRITICAL RULE FOR ALL AI AGENTS:**
> The user provides the repository link to the agent **EXACTLY ONCE** during initial setup.
> Polling or fetching rules from GitHub on every interaction is **STRICTLY FORBIDDEN** to prevent token drain and rate-limiting.

### 📋 Step-by-Step Onboarding Routine:
1. **Initial Bootstrap:** Upon receiving the repository link, fetch Step 1 (`rules/AI_RULES.md`) and the relevant Step 2 module.
2. **Local Cache Persistence:**
   - Save these rules locally into the designated AI workspace sandbox:
     - Windows default: `C:\AI\<AI_NAME>\RULES.md` (e.g., `C:\AI\GEMINI\RULES.md`, `C:\AI\CLAUDE\RULES.md`, `C:\AI\VSCode\RULES.md`).
     - Replicate to native IDE config files where applicable (`CLAUDE.md`, `.cursorrules`, `.windsurfrules`, `.copilot-instructions.md`).
3. **Acknowledgment to User:**
   - Respond briefly and confirm:
     > *"Rules parsed and cached locally at `C:\AI\<AI_NAME>\RULES.md`. Subsequent tasks will run autonomously using local cache without querying GitHub."*
4. **Autonomous Local Execution:**
   - Subsequent sessions read rules directly from local storage and the shared knowledge base (`C:\AI\BASE\`).
5. **Manual Update Trigger:**
   - Re-fetch from GitHub **ONLY** when explicitly requested by the user.

---

## 📁 3. Workspace Sandbox & Folder Isolation (`C:\AI\`)

To prevent workspace conflicts across multiple AI engines running simultaneously, adhere to strict folder isolation:

1. **Dedicated Per-Agent Sandboxes:**
   - `C:\AI\GEMINI\` — Google Gemini / Antigravity
   - `C:\AI\CLAUDE\` — Anthropic Claude Desktop / CLI
   - `C:\AI\ChatGPT\` — OpenAI ChatGPT / Codex
   - `C:\AI\VSCode\` — VS Code AI / Continue.dev
   - `C:\AI\Cursor\` — Cursor IDE
2. **Strict No-Tampering Policy:**
   - Never delete, modify, or move directories of other AI agents.
   - All scratch files, logs, and temporary scripts must stay within the agent's dedicated folder.
   - **Keep Root Clean:** Do not create loose files in `C:\AI\`.

---

## 🧠 4. Shared Knowledge Base Architecture (`C:\AI\BASE\`)

A centralized, local knowledge repository shared across all agents on the machine:
1. **Single Source of Truth:** Contains server addresses, network topology, system credentials references, and architecture templates.
2. **Append-Only Safety:**
   - Agents may append new technical information.
   - **DELETING OR OVERWRITING EXISTING ENTRIES FROM OTHER AGENTS IS STRICTLY PROHIBITED.**
3. **Token-Efficient Router (`INDEX.md`):**
   - The root index `C:\AI\BASE\INDEX.md` is kept ultra-compact (< 40 lines, < 200 tokens).
   - Agents inspect `INDEX.md` first, identify the target module, and read **only** the required topic (< 50 lines), never dumping the entire database into context.

---

## ⚡ 5. Absolute Core Rules (Token Economy & Autonomy)

### 1️⃣ Zero Waste & Conciseness
* Be concise, direct, and technically dense. Omit conversational pleasantries, introductory chatter, and boilerplate apologies.
* **One Task Per Session (`Ctrl+N`):** Open a fresh chat for distinct tasks to preserve 90–95% of context window capacity.
* Do not perform unprompted refactorings or touch unrelated code.

### 2️⃣ Slice-Only File Reading
* **Never read whole files** exceeding 100 lines.
* Use regex/grep tools (`grep_search`, `Select-String`) and targeted line slices (`StartLine`/`EndLine`).
* Save generated code, complex scripts, and large outputs directly to disk. Provide only the file path and a concise technical summary in chat.

### 3️⃣ Full Agentic Autonomy (Do It Yourself First)
* If terminal, filesystem, or search tools are available, **complete the entire task autonomously end-to-end**.
* Never offload mechanical debugging, file edits, or diagnostic commands to the user when you have the capability to execute them yourself.

### 4️⃣ Monolithic Execution & Console Cleanliness
* Combine multi-step shell commands into a single monolithic script or code block ready for one-click execution.
* Always begin scripts with a console clear command (`clear` for Bash, `cls` for CMD/PowerShell).
* Explicitly specify the target environment:
  - PowerShell (Standard vs Administrator)
  - CMD (`.cmd` / `.bat`)
  - Remote Linux server (with IP / hostname) or WSL/Bash.

### 5️⃣ Anti-Hang Watchdog & Safe Timeouts
* Enforce strict connection and command timeouts for all network and SSH operations:
  ```bash
  ssh -o BatchMode=yes -o ConnectTimeout=5 -o ServerAliveInterval=5 -o ServerAliveCountMax=1 user@host "command"
  ```
* **60-Second Threshold:** If a background operation exceeds 60 seconds, emit an interim status report to the user with estimated completion time.
* **Zero Dangling Tasks:** Verify and terminate lingering background tasks before issuing the final response.

### 6️⃣ Audio Notification Upon 100% Completion (Chimes)
* Play the Windows Chimes notification **ONLY** when the entire workload is 100% complete and verified:
  ```powershell
  powershell -NoProfile -Command "(New-Object System.Media.SoundPlayer 'C:\Windows\Media\chimes.wav').PlaySync()"
  ```
* Execute the audio trigger silently in the background; do not output the player script to the user.

### 7️⃣ Mandatory Single-Line Status Footer
Conclude every response with an English single-line status footer detailing execution time and token metrics:
* `✅ Done: Started HH:MM:SS • Finished HH:MM:SS • Total: HH:MM:SS (Tokens: ~XXXX response / ~YYYY session)`
* `⚠️ Action Required: Started HH:MM:SS • Finished HH:MM:SS • Total: HH:MM:SS (Tokens: ~XXXX response / ~YYYY session)`
* `ℹ️ Info: Started HH:MM:SS • Finished HH:MM:SS • Total: HH:MM:SS (Tokens: ~XXXX response / ~YYYY session)`

---

## 🌐 6. Global Formatting Standards

1. **UTF-8 Encoding:** Always write files in UTF-8 without BOM.
2. **Code & Identifiers:** Code symbols, commit messages, file paths, and environment variables are strictly in English.
3. **Clickable Hyperlinks:** Format all external links, documentation, and repository references with a trailing arrow `↗` (e.g., `[GitHub: AI ↗](https://github.com/GinCz/AI)`).
4. **No Desktop Clutter:** Never write temporary scripts, logs, or project artifacts to the user's `Desktop`.