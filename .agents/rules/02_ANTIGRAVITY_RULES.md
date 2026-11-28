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
* **Public GitHub Repositories Release Standard & Designated Targets:**
  - For ANY project with a public GitHub repository (e.g. `GIN-PDF-RW`, `GIN-DNS-Switch`, `GIN-Dock-Wallpaper`), EVERY version increment MUST publish an official **GitHub Release** with compiled binary assets (`gh release create vXXX <Setup.exe>`) so users can download it directly from GitHub.
  - Deliver compiled Windows installers to **BOTH**:
    1. Desktop in MEGA: `/MEGA/DOCS/desktop/<AppName>_vXXX_Setup.exe` (maps to `D:\MEGA\DOCS\desktop\`)
    2. Designated Flash Category in MEGA:
       - `GIN-PDF-RW`: `/MEGA/WIN-FLASH/Util-WINDOWS/Graphics/PDF/` (maps to `D:\MEGA\WIN-FLASH\Util-WINDOWS\Graphics\PDF\`)
       - `GIN-DNS-Switch`: `/MEGA/WIN-FLASH/Util-WINDOWS/N E T/` (maps to `D:\MEGA\WIN-FLASH\Util-WINDOWS\N E T\`)
       - `GIN-Dock-Wallpaper`: `/MEGA/WIN-FLASH/Util-WINDOWS/Graphics/` (maps to `D:\MEGA\WIN-FLASH\Util-WINDOWS\Graphics\`)
  - Retain strictly 2 latest versions in deployment targets (purge older releases via `mega-rm`).
* **Delivery Strictly to Desktop in MEGA & Designated Targets:** All new Windows binaries and installers are written **EXCLUSIVELY to Vladimir's Desktop in MEGA** (`D:\MEGA\DOCS\desktop\` via `mega-put`) AND their designated utility target folders (specifically for `GIN-DNS-Switch`: `D:\MEGA\WIN-FLASH\Util-WINDOWS\N E T\GIN-DNS-Switch_vXXX_Setup.exe` / `/MEGA/WIN-FLASH/Util-WINDOWS/N E T/`). Purge older releases via `mega-rm` (retain strictly 2 latest versions).
* **Strict MEGA Cloud Sync Root Standard (`/MEGA/` Prefix):**
  - Vladimir's synchronized root folder on local drive `D:\` is mapped **EXCLUSIVELY to `/MEGA/` in the cloud**.
  - **Categorical Ban on Unprefixed Cloud Uploads:** Uploading directly to root `/DOCS/`, `/WIN-FLASH/`, or `/desktop/` is strictly prohibited because those unprefixed cloud folders do NOT sync with Vladimir's PC.
  - **Canonical Cloud Sync Paths (Always prefix with `/MEGA/`):**
    - Desktop: `/MEGA/DOCS/desktop/<FileName>` (maps to `D:\MEGA\DOCS\desktop\<FileName>`)
    - Flash Root: `/MEGA/WIN-FLASH/Util-WINDOWS/<FileName>` (maps to `D:\MEGA\WIN-FLASH\Util-WINDOWS\<FileName>`)
    - Flash NET: `/MEGA/WIN-FLASH/Util-WINDOWS/N E T/<FileName>` (maps to `D:\MEGA\WIN-FLASH\Util-WINDOWS\N E T\<FileName>`)
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

### 1️⃣1️⃣ ANDROID TV & TV-BOX REMOTE OPERATIONS (ZERO AUTO-REBOOT & MANDATORY LIVE SCREEN LOG)
* **Mandatory Pre-Flight Device Profile Inspection (Strict Invariant):**
  BEFORE running any command (`adb`, `pm`, `settings`, `am`) against ANY TV device, the agent MUST read that device's passport file in `Android/GIN-Remote/DEVICES/<Device_ID>.md` (e.g. `Vestel_Android_TV.md`, `Hisilicon_TVBOX.md`). It is CATEGORICALLY FORBIDDEN to execute blind commands without verifying the target device's quirks, platform hazards, and hardware invariants!
* **Mandatory Live TV OSD Screen Logging:** Every update, APK deployment, configuration change, diagnostic check, or maintenance task executed on an Android TV or TV-Box (via GIN-Remote, ADB, or automation scripts) MUST transmit every action in real time to the TV screen log (`log_tv` via GIN-Bridge TCP socket `127.0.0.1:17001` format: `CMD <DEVICE_ID> KEY <MSG>\n`). The user on the TV must see live progress.
* **Categorical Ban on Autonomous Device Reboot:** Agents, LLMs, and automated scripts are CATEGORICALLY FORBIDDEN from executing automatic reboots (`adb reboot`, `su -c reboot`, broadcast intents, or shell commands).
* **Mandatory Final Status & Explicit Manual Reboot Notice:** Any update or configuration session on an Android TV/Box MUST conclude with an explicit final status message displayed in the TV screen log AND in the chat:
  - If a system reboot is REQUIRED to apply changes: state clearly: `⚠️ Все готово! Требуется вручную перезагрузить устройство пультом.` (leaving the reboot strictly to the user via remote control).
  - If a system reboot is NOT required: state clearly: `✅ Все готово! Перезагрузка не требуется.`
* **Mandatory Default Debloat on ALL TV Devices (Ironclad Rule):**
  Whenever configuring or optimizing ANY Smart TV, TV-Box, or TV-Stick, the agent MUST unconditionally execute:
  1. **Stock Launcher & Chromecast Built-in Safety Invariant (Never Freeze on Smart TVs):**
     - On Smart TVs (especially Vestel, Hyundai, Philips, Sony), **NEVER disable or freeze** `com.google.android.tvlauncher` or `com.google.android.apps.tv.launcherx`.
     - Freezing stock launcher breaks Chromecast built-in (`com.google.android.apps.mediashell`) and leads to critical `system_server` crashes or bootloops (`FallbackHome` grey/black screen).
     - Set default launcher strictly via standard system APIs: `cmd package set-home-activity com.gincz.ginlauncher/.MainActivity` & `cmd role add-role-holder android.app.role.HOME com.gincz.ginlauncher`.
  2. **Purge Commercial Bloatware (Uninstall/Disable):**
     - Netflix: `com.netflix.ninja`, `com.netflix.mediaclient`
     - Prime Video: `com.amazon.amazonvideo.livingroom`, `com.amazon.avod.thirdpartyclient`
     - YouTube Music: `com.google.android.youtube.tvmusic`
     - Google Play Movies: `com.google.android.videos`
  3. **Disable-Only Bloatware (Disable via `pm disable-user --user 0`):**
     - Live Channels: `com.google.android.tv`, `com.android.tv`
     - PatchWall & Xiaomi Feeds: `com.mitv.tvhome`, `com.xiaomi.mitv.tvhome`, `com.xiaomi.mitv.upgrade`, `com.mitv.videoplayer`
  4. **Disable Google Play Store, Protect, Antivirus & Automatic App Updates:**
     - On Vladimir's TVs, all apps are installed manually. To block ads, unrequested app modifications, and background downloads:
     - `pm disable-user --user 0 com.android.vending` (Google Play Store daemon disabled to stop auto-updates completely).
     - `pm disable-user --user 0 com.google.android.play.games`
     - `settings put global package_verifier_enable 0`
     - `settings put global package_verifier_user_consent -1`
     - `settings put global upload_apk_enable 0`
     - `settings put global auto_update 0`
     - `pm disable-user --user 0 com.google.android.gms/.update.SystemUpdateService`
     - `pm disable-user --user 0 com.google.android.gsf/.update.SystemUpdateService`
  5. **Strict Chromecast Immunity (Never Touch):**
     - `com.google.android.apps.mediashell` (Chromecast Built-in) MUST ALWAYS be preserved and enabled (`pm enable com.google.android.apps.mediashell`). Screen casting from phones, Google Chrome, and Cent Browser must never be impaired.
  6. **Mandatory First-Run Low-RAM (≤ 1.5GB) & Stick Emergency Thermal Profile:**
     Whenever connecting to, configuring, or optimizing ANY Android TV stick or low-RAM TV-Box (≤ 1.5GB RAM, e.g. Xiaomi Mi TV Stick S805Y, Realme TV Stick, Chromecast HD, etc.), the agent MUST unconditionally execute the emergency thermal & RAM optimization FIRST, BEFORE any other commands, installations, or app launches:
     - **Reduce UI Resolution to 720p:** `wm size 1280x720` and `wm density 213` (cuts GPU memory allocation, texture cache, and fillrate load on weak Mali GPUs in half; drops SoC temperature by 15–20°C, eliminating thermal shutdown/reboot loops while hardware video decoding in media players retains 1080p).
     - **Disable All System Animations:**
       - `settings put global window_animation_scale 0.0`
       - `settings put global transition_animation_scale 0.0`
       - `settings put global animator_duration_scale 0.0`
     - **Strict Background Process Limit:** `settings put global background_process_limit 2`
     - **Disable Heavy Recommendation Feeds & Telemetry:** `pm disable-user --user 0 com.google.android.tvrecommendations`
     - **Mandatory Power Supply Verification Notice:** Immediately alert the user if a stick is powered from a TV's USB port (0.5A). Sticks MUST be powered strictly from an external dedicated 5V ≥ 1.5A–2.0A power adapter to prevent severe voltage drop reboots under load.

### 1️⃣2️⃣ MANDATORY TELEGRAM NOTIFICATIONS ON BUILD & DEPLOYMENT COMPLETION
* **Universal Telegram Notification:** Every project build script, compilation pipeline (Windows EXE, Android APK, Linux daemon/service builds) and long-running asynchronous preparation task MUST integrate automated Telegram notification to Vladimir.
* **Credentials & Endpoint:**
  - Bot Token: `1226649515:AAFzU7Rkq-kGGRDbPCEf-Zkzb9smT7mWTUU` (My_WWW_bot)
  - Target Chat: `261784949` (Vladimir / @GinCz)
  - Standard Scripts: `bash /root/.AI/GitHub/Secret_Privat/scripts/notify_telegram.sh "<Project>" "<SUCCESS|ERROR>" "<vXXX>" "<Details>" "<Download_URL>"` (Linux) or `notify_telegram.ps1` (Windows).
* **Mandatory Trigger:**
  - Upon successful build and publication of ANY APK or EXE installer, send an immediate notification with app name, version, changelog summary, and direct download URL.
  - Upon any catastrophic build or verification failure, immediately alert with error details.
  - When the agent finishes a long-running background build, it must ensure Vladimir receives this Telegram ping without needing to check the IDE chat manually.

### 1️⃣4️⃣ GIN-AGENT STANDALONE ARCHITECTURE & ZERO-LATENCY FAST-PATH
* **Strict Single Polyglot File:** `GIN-Agent` for Windows MUST ALWAYS be implemented, distributed, and maintained as **strictly ONE standalone `.cmd` file** (`GIN-Agent_Windows_vXXX.cmd`).
* **Categorical Ban on External PS1 Files:** Categorically forbidden to create, distribute, generate, or execute separate `.ps1` files (e.g. `GIN-Agent-Core.ps1`, `agent.ps1`) anywhere in the repository, deployment mirrors, or client `%ProgramData%\GIN-Agent` directories.
* **Dual-Mode Self-Contained Execution:**
  - **Installer Mode (Interactive / Double-Click):** Checks UAC elevation, halts existing agent processes, purges any obsolete `.ps1` files, copies itself to `%ProgramData%\GIN-Agent\GIN-Agent.cmd`, registers the Windows scheduled service `GIN-Agent-Service` (`cmd.exe /c ""%ProgramData%\GIN-Agent\GIN-Agent.cmd" /service"`), starts it silently in the background, and displays an auto-closing countdown.
  - **Service Worker Mode (`/service`):** Runs headless in the background via hidden PowerShell block executed directly from the `.cmd` file, handles singleton mutex (`Global\GIN_Agent_Core_Mutex`), gateway polling, hardware 9-digit GIN-PIN calculation, and strict numeric RustDesk ID detection.
* **Zero-Latency Remote Update Fast-Path (Strict Ban on Discovery Searching & Blocking Verification):**
  - **Zero Pre-Search:** When requested to update an agent on a connected Windows host, the agent MUST NEVER run broad `find`, `grep`, or multi-file research to figure out how to update. The update pipeline is strictly canonical: download `http://152.53.182.222:9876/GIN-Agent_Windows_v<NEW>.cmd` to `%ProgramData%\GIN-Agent\`, overwrite `GIN-Agent.cmd`, and restart `GIN-Agent-Service` in a detached process.
  - **Hard Timeout on `/exec` Calls (Max 15s):** Any HTTP POST `/exec` call sent through the remote bridge (`http://152.53.182.222:9876/exec`) MUST have an explicit hard command timeout of maximum 15 seconds (`--max-time 15` in curl). Categorically forbidden to wait indefinitely on hanging remote command sockets.
  - **Non-Blocking Status Verification via Heartbeat:** When an agent service is restarted, NEVER query status through `/exec` (which blocks up to 180s while the service is cycling). Verify online presence and version exclusively through the central registry heartbeat in `rd.gincz.com` / `clients.json` (`agent_version` and `agent_last_seen`), which updates within 15–30 seconds.

### 2️⃣0️⃣ RULE 20: MANDATORY `versions/` DIRECTORY & COMPANION ZIP ARCHIVES FOR ALL CMD/BAT PROJECTS
* **Root Directory Cleanliness:** In any Windows script or CMD project repository or subfolder, the root directory MUST contain ONLY `README.md` and clean subfolders (`versions/`, `docs/`, `src/`). Categorical ban on littering root directories with loose `.cmd` or `.bat` files.
* **Dedicated `versions/` Directory:** All release versions of Windows scripts (`.cmd`, `.bat`) must reside strictly in a dedicated `versions/` subfolder. Retain strictly the 2 latest versions (`vXXX` and `vYYY`), purging older obsolete versions.
* **Mandatory Companion ZIP Archive for EVERY Version:**
  Because GitHub Web UI right-click ("Save link as...") downloads the HTML preview page instead of the script, strips CRLF line endings, or triggers browser `.txt` extension renaming and Windows SmartScreen blocks, **EVERY versioned `.cmd` file in `versions/` (`<AppName>_vXXX.cmd`) MUST have a corresponding companion ZIP archive (`<AppName>_vXXX.zip`)** containing that exact script in pristine Windows CRLF (`\r\n`) encoding.
* **Mandatory ZIP Download Link in `README.md`:** The root `README.md` of every CMD project must explicitly document:
  1. Safe ZIP download link: `[Скачать ZIP-архив vXXX](versions/<AppName>_vXXX.zip)` as the primary safe download method to avoid HTML corruption.
  2. 1-click PowerShell launcher: `powershell -ep bypass -c "iwr -useb <url> -OutFile <file>; .\<file>"`.
