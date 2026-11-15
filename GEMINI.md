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
* **Completion Chimes:**
  - Windows: `powershell -c "(New-Object Media.SoundPlayer 'C:\Windows\Media\chimes.wav').Play()"`
  - Linux: `bash /root/.AI/GitHub/Secret_Privat/scripts/play_done_sound.sh || printf '\a\e]9;✅ Anti-Gravity: Готово!\e\\'`
* **Isolated Sandbox:** Temporary scripts and build artifacts must reside strictly in `<model>/temp/` (Windows: `D:\AI\GEMINI\temp\`, Linux: `/root/.AI/AntiGravity/temp/`).
* **Cloud Sandbox Safeguard:** Never clone repositories or create project directories in web/cloud sandboxes (`CLI`, `/workspace`). If running unattached to a server, immediately warn Vladimir to switch to Remote Control.
