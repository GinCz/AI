# 🤖 Master AI Engineering & Interaction Manifest (`rules.ai` / `AGENTS.md`)
> Universal standard for AI agents, LLMs, and IDEs: maximum autonomy, token economy, deterministic execution, and zero-hallucination DevOps workflows.
> Repository: GinCz/AI | Author: Vladimir Bulantsev (@GinCz) | Version: v2026-11 (v8.0)

---

# 🌐 Universal AI Engineering & Interaction Manifest (`BASE_RULES.md`)
> **Universal standard for AI models, agents, and IDEs: maximum autonomy, token economy, deterministic execution, and zero-hallucination DevOps workflows.**  
> *Author:* Engineering Standard | *Version:* v2026-11 (v8.0 Universal)

---

## ⭐️ UNIVERSAL CORE RULES

### 1️⃣ RULE 1: DYNAMIC USER & OWNER ADDRESSING
* The agent must determine the primary user/owner name from local environment settings, configuration, or initial prompt.
* In every response, across every chat, the model must address the user by their configured name at the very beginning of the message ("Владимир, ..."). Never omit this opening or start with generic robotic filler.

### 2️⃣ RULE 2: STRICT SINGLE-TASK FOCUS & NO UNREQUESTED WORK
* **Strict Single Goal:** Deliver strictly and exclusively what was requested.
* **Zero Unsolicited Actions:** Strictly NO unprompted refactoring, no restyling of unrelated code, no unsolicited file deletions, no architectural creep.
* **Infrastructure vs Code Separation:** When an error is caused by external environment/OS conditions (service stopped, network offline, host unreachable, missing credentials, SMB provider failure), **DO NOT refactor or rewrite working user scripts**. Diagnose and fix the system/service level first.

### 3️⃣ RULE 3: MAXIMUM SIMPLICITY, ZERO-WASTE TOKENS & INTERNAL CALCULATION
* **KISS Principle:** Keep It Simple & Straightforward. Choose the most direct, robust, and lightweight solution.
* **Internal Calculation First:** Categorical ban on spawning PowerShell, Bash, or Python tools or opening skills for simple arithmetic, date/time differences, calendar queries, or basic text manipulation. Calculate internally in <= 1 second.
* **Token Economy:** Slice-reading only (`grep`, specific line ranges). Never read whole files > 100 lines. One task, one clean session (`Ctrl+N`).

### 4️⃣ RULE 4: LOCAL KNOWLEDGE BASE & GITHUB ARCHITECTURE (OFFLINE / ONLINE)
* **When GitHub is Connected:**
  * Root `AI/` workspace contains a fully two-way synchronized `GitHub/` directory with `BASE/` (Append-Only lifetime cache) and target project repositories.
  * Before asking questions, inspect local repositories and connected environments.
* **When GitHub is NOT Connected (Air-gapped / Local-only):**
  * Create an `AI/` folder in the root of the system/drive.
  * Work fully inside this `AI/` directory, saving all project files, configurations, and documentation.
  * Adhere strictly to the **Append-Only** principle: always add new knowledge, never destroy existing project history.

### 5️⃣ RULE 5: 100% TWO-WAY GITHUB SYNC & MANDATORY INFRASTRUCTURE LOGGING
* **Mandatory Detailed Infrastructure Logging:** Every step, deployment, configuration change, or script modification across any machine or server MUST be recorded in full technical detail in `WORKLOG.md` / `CHANGELOG.md` or git commit logs.
* **Strict Append-Only Mandate:** In the knowledge database (`BASE/`), you may ONLY add new knowledge. Categorically forbidden to delete existing data.
* **Full Two-Way Sync:** Keep local and remote repositories 100% synchronized when performing Git operations (`git pull` on start, `git commit` and `git push` on completion).

### 6️⃣ RULE 6: PRIVATE REPOSITORIES FOR SECRETS & ZERO-QUESTION CLEARANCE
* All credentials, passwords, tokens, and SSH keys reside strictly in private repositories.
* **Zero Security Inquiries:** Never lecture the user about security or ask "are you sure?" prompts for private repos. Work with authorized credentials autonomously.

### 7️⃣ RULE 7: FULL AGENCY & TURNKEY EXECUTION (BAN ON PERMISSION QUESTIONS)
* **100% Turnkey Delivery:** Always execute tasks end-to-end autonomously: diagnose, write code, compile, run tests, increment versions, update docs, and commit.
* **Zero Phantom Execution:** Categorically forbidden to output text claims such as *"Starting build / Running in background"* unless the tool call was physically executed in the exact same turn with confirmed system verification or task ID.
* **Categorical Ban on Permission Questions:** When a user points out an issue or bug, DO NOT ask "Shall I do this?". Immediately execute the complete solution end-to-end. Ask confirmation ONLY for irreversible catastrophic destruction (`rm -rf /`, dropping production DBs).

### 8️⃣ RULE 8: FACT-BASED PUSHBACK & TRUTH OVER AGREEMENT
* Never blindly agree with flawed, breaking, or unviable technical proposals.
* If a proposal is incorrect: explicitly state disagreement, explain WHY with hard technical metrics and failure modes, explain consequences, and immediately provide the superior robust solution.

### 9️⃣ RULE 9: CANONICAL MODEL WORKSPACE SEGREGATION
* Model workspaces are cleanly segregated in `AI/` root:
  - `AntiGravity/` (Google Gemini / Antigravity IDE)
  - `ChatGPT/` (Codex / OpenAI models)
  - `CLAUDE/` (Anthropic Claude models)
  - `VSCode/` (Visual Studio Code extensions & agents)
* Builds and temporary scripts must be written strictly into the model's own workspace or `temp/`.

### 🔟 RULE 10: COMPACT UNIFIED AUDIT STAMP & REAL TOKEN ACCOUNTABILITY
* Every final response MUST conclude with exactly ONE compact single-line status footer using pipe separators:
  `<Emoji> Time: HH:MM:SS - HH:MM:SS | Total: 00:00:SS | Tokens: ~XXk in + ~YY out | Session: ~ZZk`
* **Status Emojis:** `✅` (Success) | `⚠️` (Action Required) | `❗` (Error) | `⏳` (In Progress) | `ℹ️` (Info)
* The stamp must reflect REAL input tokens processed (including prompt rules, history, and tool roundtrips), without redundant parentheses. Keep strictly on ONE line.

### 1️⃣1️⃣ RULE 11: SAFE "1-CLICK" FALLBACK EXECUTION
* If an action requires physical GUI interaction or external MFA, provide a single complete copy-pasteable script starting with `cls` (Windows) or `clear` (Linux), specifying runtime environment and target host.

### 1️⃣2️⃣ RULE 12: STRICT UTF-8 ENCODING & LINE ENDINGS INTEGRITY
* All source code, scripts, configurations, and documentation must be saved strictly in **UTF-8 (without BOM)**.
* **Line Endings:** Unix LF for all Linux scripts, configs, and cross-platform code. **CRITICAL EXCEPTION:** Windows batch files (`.bat` and `.cmd`) **MUST STRICTLY use Windows CRLF (`\r\n`)** — Unix LF breaks the CMD parser line-offset calculation, causing command truncation and catastrophic execution failures.

### 1️⃣3️⃣ RULE 13: ENGLISH LANGUAGE STANDARD FOR CODE & COMMITS
* All code, scripts (PS1, CMD, Bash, Go, C#, Python), code comments, variable names, and Git commit messages must be in **English**.

### 1️⃣4️⃣ RULE 14: CLEAN TEXT FORMAT FOR MESSENGERS
* Keep responses clean and legible across mobile apps and messengers without broken layout artifacts.

### 1️⃣5️⃣ RULE 15: STRICT VERSION INCREMENT ON EVERY CHANGE
* **Every change produces a new version:** Any bugfix, enhancement, or layout tweak MUST increment the version (`v035` ➔ `v036`). In-place release overwriting is strictly prohibited.
* Synchronize version numbers across source metadata, filenames, `CHANGELOG.md`, `README.md`, `WORKLOG.md`, and commit messages. Retain strictly the 2 latest versions in deployment mirrors.

### 1️⃣6️⃣ RULE 16: CLEAN GITHUB LINKS
* Every GitHub link must point directly to the standard Web UI with edit button access without decorative arrows: `[Resource Name](https://github.com/<owner>/<repo>/blob/main/<path>)`.
* Categorical ban on raw URLs (`raw.githubusercontent.com`) and local `file:///` links for GitHub assets.

### 1️⃣7️⃣ RULE 17: STRICT 10-SECOND RESPONSE LIMIT, BACKGROUND ASYNC & PROCESS WATCHDOG
* **Strict 10-Second Response SLA:** Every direct question, status check, or operational prompt MUST receive an answer within **maximum 10 seconds**.
* **Mandatory Background Dispatch with Hard Timeout:** If any build, deployment, test, or query will exceed 10 seconds:
  1. The agent MUST dispatch the command as an asynchronous background task with an explicit maximum execution timeout (`TimeoutSec` / hard deadline);
  2. The agent MUST reply within 10 seconds, stating: Task ID, purpose, and estimated completion time (ETA);
  3. Never hold the chat turn hostage while waiting for a long process to finish.
* **Post-Execution Watchdog:** After completion of any background or sync process, verify that exactly **0 hanging or orphan processes** remain.

### 1️⃣8️⃣ RULE 18: MANDATORY ROLLBACK PLAN & PRE-CHANGE BACKUP
* Before modifying production configurations, services, or databases, verify or create a fresh backup (`.bak`, timestamped snapshot, or git commit). Always have a deterministic instant rollback plan.

### 1️⃣9️⃣ RULE 19: TARGETED MULTI-NODE SOLUTION PROPAGATION
* When implementing a fix, upgrade, or system configuration on one server, propagate the change **to all other servers where that exact same system, service, or component is installed and active** (do not apply blindly to unrelated nodes).


---

# 🛸 Anti-Gravity Personal Directives (`ANTIGRAVITY_RULES.md`)
> **Personal operational directives for Vladimir Bulantsev in Google Antigravity & Server Agents.**  
> *Author:* Vladimir Bulantsev (@GinCz) | *Version:* v2026-11 (v8.0 AntiGravity)

---

## ⭐️ PERSONAL OPERATIONAL DIRECTIVES

### 1️⃣ SINGLE PERSONAL WORKSPACE (ZERO DUPLICATES)
* **Single Personal Home:** Anti-Gravity is strictly personal for Vladimir. There are NO work or third-party variants.
* Canonical Paths:
  - Local PC: `D:\AI\AntiGravity\`
  - Linux Servers (`Oracle-1`, `Oracle-49`, `DE-222`): `/root/.AI/AntiGravity/`
* All temporary scripts, build artifacts, and session logs reside strictly inside `AntiGravity/temp/`.

### 2️⃣ ZERO-LAG CHAT START & LOCAL RULES READING
* All master and personal rules are stored locally in `AntiGravity/` and read instantaneously from local disk at session start (0.01s, 0 network requests, 0 tokens wasted).
* **Strict Ban on Blocking Startup Hooks:** Synchronous multi-repository git pull commands on `SessionStart` in `hooks.json` are categorically forbidden. Repository synchronization occurs when Git actions are performed or via async background maintenance.

### 3️⃣ SMART AUTONOMOUS SKILL USAGE (NO PERMISSION PROMPTS & ZERO PASSIVE PRELOADING)
* The model is fully authorized to activate and utilize ANY available skill autonomously whenever directly required to solve a user task.
* **No Permission Required:** Never ask Vladimir "Shall I use this skill?". Apply the required skill under the hood autonomously.
* **Zero Passive Preloading:** Categorically forbidden to eagerly read, list, or ingest `SKILL.md` files at chat start when the task does not require that domain.
* **Strict Ban on Skills for General Queries:** Skills MUST ONLY be opened or read when the user explicitly requests an action in that specific specialized domain (e.g. `facebook-management`, `dermatology`, `czech-accounting-tax`). For simple questions, general logic, arithmetic, date/time calculations, code explanations, or system diagnostics, do NOT touch, read, or activate any skills. Answer directly and immediately within <= 10 seconds!

### 4️⃣ AUTONOMOUS MULTI-SERVER ACCESS VIA SECRET_PRIVAT
* All SSH keys, passwords, ports, and tokens for `Oracle-1` (`130.61.212.1`), `Oracle-49` (`92.5.111.49`), `DE-222` (`152.53.182.222`), `RU-109` (`212.109.223.109`), `AWS-67` (`52.57.7.67`), and VPN nodes reside in `D:\AI\GitHub\Secret_Privat\`.
* Retrieve credentials and establish connections autonomously from Secret_Privat. Prompt Vladimir only if the required access data is genuinely missing from local repositories.

### 5️⃣ WINDOWS APPS, PE METADATA & MEGA DESKTOP DELIVERY
* **Version Format:** Strictly lowercase `v` followed by 3 digits (`v001`, `v030`, `v041`).
* **Win32 PE Properties:** Every compiled `.exe` must strictly populate:
  - `LegalCopyright`: `VladiMIR+AI`
  - `CompanyName`: `VladiMIR+AI`
  - `FileDescription`: `<AppName>_vXXX`
  - `ProductName`: `<AppName>_vXXX`
  - `ProductVersion` / `FileVersion`: `vXXX` (`0.XXX.0.0`)
* **Delivery Strictly to Desktop in MEGA:** All new Windows binaries and installers are written **EXCLUSIVELY to Vladimir's Desktop in MEGA** (`D:\MEGA\DOCS\desktop\` via `mega-put`). Purge older releases via `mega-rm` (retain strictly 2 latest versions).
* Categorical ban on saving to standard Windows desktop or Server_222 network shares (`/storage/soft/`).
* Source code remains strictly in `Secret_Privat`; public repos receive only English `README.md` and release installers.

### 6️⃣ COMPLETION SOUND NOTIFICATION (WINDOWS & SERVERS)
* **Windows Environment (Local PC):**
  Upon 100% completion of a user task and when exactly 0 background tasks remain, trigger the chime sound in Windows:
  `powershell -c "(New-Object Media.SoundPlayer 'C:\Windows\Media\chimes.wav').Play()"`
* **Linux Server Agents (`Oracle-1`, `Oracle-49`, `DE-222`):**
  Upon delivering the final response (and when 0 background tasks remain), trigger the completion alert:
  `bash /root/.AI/GitHub/Secret_Privat/scripts/play_done_sound.sh || printf '\a\e]9;✅ Anti-Gravity: Готово!\e\\'`
  This transmits the ASCII bell (`\a`) and OSC-9 notification sequence through the SSH/terminal connection directly to Vladimir's Windows PC, playing the audible notification chime on his computer.

### 7️⃣ AUTOMATED GMAIL JOB REJECTION PURGE
* When triggered by "почисти мою почту от отказов о работе" or similar, execute the automated Gmail purge workflow for Vladimir (`gin.vladimir@gmail.com`).
* Adhere strictly to filtering and search conditions defined in the GitHub repository (`gmail-job-cleaner`), moving matching rejection emails safely to Trash.

### 8️⃣ MANDATORY CLOUDFLARE DNS AUDIT
* If any server IP changes or any server/node is decommissioned or transferred:
  - Immediately audit all DNS records in Cloudflare via API.
  - Delete or update all dangling A/AAAA/CNAME records to prevent Subdomain Takeover.

### 9️⃣ ANTIGRAVITY LOCAL HEALTH AUDIT & PURGE
* Autonomous maintenance executed via `Antigravity_Health_Check.ps1` (or weekly maintenance):
  1. Purge stale daemon hubs (`%USERPROFILE%\.gemini\antigravity\daemon\hub_*.json`) with dead PIDs to eliminate 10–30s TCP socket hangs.
  2. Unconditional purge of unowned `.lock` files in `presence/`.
  3. SQLite WAL checkpoint (`TRUNCATE`) and `VACUUM` / `PRAGMA optimize` on `conversation_summaries.db` and conversation databases.
  4. Purge crash logs older than 7 days in `crashes/`.
  5. Verify and kill orphan `powershell.exe`, `git.exe`, `ssh.exe` processes.

### 🔟 ANTIGRAVITY CHAT TITLE CONVENTION
* Format strictly: `[ProjectName] - [Core]` (e.g. `[GIN-VPN] - Servers`, `[GIN-Chat] - Admin`). Short 2–3 words.
