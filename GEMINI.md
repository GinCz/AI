# 🤖 Gemini / Antigravity Model Directives (`GEMINI.md`)
> **Model-Specific Directives for Google Gemini & Antigravity IDE / CLI.**  
> *Author:* Vladimir Bulantsev (@GinCz) | *Repository:* [GinCz/AI](https://github.com/GinCz/AI) | *Version:* v2026-11 (v8.0)

---

## ⚡ MANDATORY BASELINE INHERITANCE
* **Primary Manifest:** Follow all 19 Core Rules and 10 Personal Directives defined in [AGENTS.md](https://github.com/GinCz/AI/blob/main/AGENTS.md).
* **Owner Addressing:** In EVERY response, address Vladimir by name at the very beginning (`Владимир, ...`).
* **Turnkey Execution:** 100% autonomous delivery without permission questions ("Shall I do this? / Делаем? / Начинать?").
* **Single-Line Status Footer:** EVERY final message terminates strictly with the unified v8.0 audit stamp:
  `<Emoji> Time: HH:MM:SS - HH:MM:SS | Total: 00:00:SS | Tokens: ~XXk in + ~YY out | Session: ~ZZk`
* **Status Emojis:** `✅` (Success) | `⚠️` (Action Required) | `❗` (Error) | `⏳` (In Progress) | `ℹ️` (Info)
* **Strict 10-Second SLA & Fast Calculation:** Simple math, calendar differences, logic, and status checks MUST be calculated internally in <= 1s without touching skills or CLI scripts. Response SLA <= 10s.
* **Smart Skills Usage:** Skills are domain-specific tools only. Never open, read, or activate skills for general queries or calculations.
* **Completion Chimes & Telegram Alert:**
  - Windows: `powershell -c "(New-Object Media.SoundPlayer 'C:\Windows\Media\chimes.wav').Play()"`
  - Linux: `bash /root/.AI/GitHub/Secret_Privat/scripts/play_done_sound.sh || printf '\a\e]9;✅ Anti-Gravity: Готово!\e\\'`
  - Telegram Build Alerts: Any server/app build or long preparation pipeline MUST notify Vladimir in Telegram (@GinCz / `261784949`) via `notify_telegram.sh` / `notify_telegram.ps1` upon completion.
* **Mandatory Direct Clickable Links (Zero Manual Search):** Whenever creating, publishing, deploying, or editing ANY post (Facebook, Instagram, Telegram), webpage, release, map item, or asset, the agent MUST immediately output a direct clickable markdown link `[Link Text](https://...)` directly in the chat response. Vladimir must NEVER have to manually search for what was created.
* **Mandatory WORKLOG.md Protocol Before Final Reply:** BEFORE playing the completion sound and sending the final answer, ALWAYS record full technical details into `WORKLOG.md` (and `CHANGELOG.md` for software versions) and execute `git commit -m "docs: ..."` and `git push origin main`. A Git commit message alone is NEVER a substitute for writing into `WORKLOG.md`. An answer without a committed and pushed `WORKLOG.md` is strictly forbidden.
* **Isolated Sandbox:** Temporary scripts and build artifacts must reside strictly in `<model>/temp/` (Windows: `D:\AI\GEMINI\temp\`, Linux: `/root/.AI/AntiGravity/temp/`).
* **Cloud Sandbox Safeguard:** Never clone repositories or create project directories in web/cloud sandboxes (`CLI`, `/workspace`). If running unattached to a server, immediately warn Vladimir to switch to Remote Control.
* **Public GitHub Releases & Dual MEGA Delivery:** For public repos (`GIN-PDF-RW`, `GIN-DNS-Switch`), every version MUST be published to **GitHub Releases** (`gh release create vXXX`) with attached Setup binary. Windows installers deliver simultaneously to Desktop (`/MEGA/DOCS/desktop/`) AND designated Flash folder (`GIN-PDF-RW` -> `/MEGA/WIN-FLASH/Util-WINDOWS/Graphics/PDF/`, `GIN-DNS-Switch` -> `/MEGA/WIN-FLASH/Util-WINDOWS/N E T/`).
* **GIN-Agent Mandatory 3-Folder Delivery:** Every new `GIN-Agent_Windows_vXXX.cmd` version MUST be uploaded to **ALL 3** MEGA folders:
  1. `/MEGA/DOCS/desktop/` (maps to `D:\MEGA\DOCS\desktop\`)
  2. `/MEGA/WIN-FLASH/Util-WINDOWS/N E T/` (maps to `D:\MEGA\WIN-FLASH\Util-WINDOWS\N E T\`)
  3. `/MEGA/WIN-FLASH/Util-WINDOWS/N E T/TeamViewer_RadMin/` (maps to `D:\MEGA\WIN-FLASH\Util-WINDOWS\N E T\TeamViewer_RadMin\`)
  Retain strictly the 2 latest versions in each target (purge older releases via `mega-rm`).
* **MEGA Cloud Sync Standard:** Always prefix MEGA upload paths with `/MEGA/` (e.g. `/MEGA/DOCS/desktop/`, `/MEGA/WIN-FLASH/Util-WINDOWS/`). Unprefixed `/DOCS/` does not sync with PC.
* **Android APK Strict 2-Target Delivery (DE-222 Samba & MEGA Flash Only):** In ALL Android projects, compiled APKs deliver strictly to: 1) Server DE-222 Samba: `de222:/storage/user/APK/<AppName>_vXXX.apk` (`\\s.gincz.com\user\APK`), permissions `664`, owner `vlad:vlad`; 2) MEGA Cloud Flash: `/MEGA/WIN-FLASH/ANDROID/GIN_APK/` (syncs to `D:\MEGA\WIN-FLASH\ANDROID\GIN_APK`). Strictly FORBIDDEN to copy APKs to Desktop (`/MEGA/DOCS/desktop/`). Retain strictly 2 latest versions.
* **GIN-Agent Standalone Standard:** GIN-Agent must strictly be ONE polyglot `.cmd` file with ZERO external `.ps1` files.
* **Strict CRLF Integrity & .gitattributes:** Every `.cmd` and `.bat` file MUST have CRLF line terminators. All repositories with Windows scripts MUST have `.gitattributes` pinning `*.cmd text eol=crlf`.
* **Mandatory versions/ & Companion ZIP for CMD Projects:** All Windows CMD/BAT projects must store scripts in `versions/` (retaining strictly 2 latest versions) and ALWAYS generate a companion `.zip` archive (`<App>_vXXX.zip`) alongside each `.cmd` to protect users against GitHub Web HTML-saving corruption.
* **Mandatory TV Debloat & Chromecast Immunity:** Unconditionally purge Netflix, Prime Video, YouTube Music, Google Play Movies; disable Live Channels and PatchWall; disable Google Play Protect and GMS updates; strictly preserve Chromecast `com.google.android.apps.mediashell` for Chrome/Cent Browser mirroring.
* **Mandatory Low-RAM (≤ 1.5GB) & Stick Emergency Profile:** On any TV stick or box with ≤ 1.5GB RAM (Mi TV Stick, etc.), immediately on first connection: switch UI to 720p (`wm size 1280x720` / `density 213`), disable animations (`window_animation_scale 0`), limit background processes to 2 (`background_process_limit 2`), disable `com.google.android.tvrecommendations`, and enforce dedicated 5V ≥ 1.5A power.

