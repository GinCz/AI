# 🤖 Gemini / Antigravity Model Directives (`GEMINI.md`)
> **Model-Specific Sandbox Directives for Google Gemini & Antigravity IDE (Antigravity Home).**  
> *Author:* Vladimir Bulantsev ([@GinCz ↗](https://github.com/GinCz)) | *Repository:* [GinCz/AI ↗](https://github.com/GinCz/AI)

---

## ⚡ MANDATORY BASELINE INHERITANCE
* **Primary Manifest:** Follow all 25 Core Rules defined in [AGENTS.md ↗](file:///D:/AI/GEMINI/AGENTS.md) and [AI_RULES.md ↗](https://github.com/GinCz/AI/blob/main/rules/AI_RULES.md).
* **Owner Addressing:** In EVERY response, address Vladimir by name at the very beginning (`Владимир, ...`).
* **Turnkey Execution:** 100% autonomous delivery without permission questions ("Shall I do this? / Делаем? / Начинать?").
* **Single-Line Status Footer:** EVERY final message terminates with the unified audit stamp:
  `<Status>: Time: HH:MM:SS - HH:MM:SS | Total: HH:MM:SS | Tokens: ~XXX answer [✅|⚠️|🔴] / ~YYYY session [✅|⚠️|🔴]`
* **Completion Chimes:** On 100% task completion (with 0 running tasks), play `C:\Windows\Media\chimes.wav`.
* **Isolated Sandbox:** All temporary files, scripts, and build artifacts must be created strictly in `D:\AI\GEMINI\temp\`. Root `temp/` is forbidden.

## 🏠 ANTIGRAVITY HOME SPECIFICS
* **Central GitHub Directory:** `D:\AI\GitHub\` contains all synchronized Git repositories.
  * Synced automatically at start via `D:\AI\GitHub\sync_repos.ps1`.
  * Every important change must be committed and pushed to the respective repository (`git commit & push`).
* **Append-Only Lifetime Cache:** `D:\AI\GitHub\BASE\` is strictly append-only. Never delete existing knowledge.
* **True Desktop Location:** Real desktop is strictly in MEGA: `D:\MEGA\DOCS\desktop\`.
  * Total ban on standard Windows desktop (`C:\Users\USER\Desktop\`).
  * Total ban on `C:\UTIL\` (only used on CANCOM laptop).
* **User Downloads & Outgoing Files:** Place user attachments/downloads into `D:\DownLOAD\`.
* **Voice / Push-to-Talk:** `F4` (or `Alt+M`) with active PTT daemon (`antigravity_ptt_daemon.js`).

## 📅 ANTIGRAVITY HEALTH AUDIT (АУДИТ ЗДОРОВЬЯ ANTIGRAVITY)
* **Trigger:** Автономное выполнение при первом старте или еженедельно по понедельникам (и принудительно через `-Force`).
* **Execution:** Автономно под ключ выполнить аудит через `D:\AI\GitHub\Windows_scripts\Antigravity_Health_Check.ps1` (или `D:\AI\GEMINI\tools\Antigravity_Health_Check.ps1`):
  1. **Очистка мертвых daemon-хабов (`%USERPROFILE%\.gemini\antigravity\daemon\hub_*.json`):** Проверить PID каждого хаба. Если процесс `language_server.exe` / `Antigravity.exe` не запущен, удалить stale JSON немедленно. Исключает сетевые таймауты (10–30с) при открытии новых чатов.
  2. **Безусловная очистка зависших блокировок (`%USERPROFILE%\.gemini\antigravity\presence\*.lock`):** Удалить все разблокированные `.lock` файлы закрытых сессий при каждом прогоне без пропуска среди недели.
  3. **SQLite WAL & Оптимизация баз данных:** Выполнить WAL checkpoint (`TRUNCATE`), дефрагментацию `VACUUM` и `PRAGMA optimize` для `conversation_summaries.db` и баз диалогов.
  4. **Ротация crash-логов (`%USERPROFILE%\.gemini\antigravity\crashes\`):** Удалить логи сбоев старше 7 дней.
  5. **Watchdog зависших процессов:** Проверить и завершить осиротевшие процессы `powershell`, `git`, `ssh`.
  6. **Фиксация состояния:** Записать дату и статус в `C:\Users\USER\.gemini\antigravity\last_health_check.json`.

## 🛡️ LESSONS LEARNED & STRICT SAFEGUARDS
* **Environment/Service First — Zero Script Rewrites on OS Errors:**
  If a script fails with OS or network errors (e.g. `The network path was not found`, `Сеть отсутствует или не запущена`, `InitializeDefaultDrives`, SMB timeout), **STRICTLY PROHIBITED to rewrite, refactor, or complicate working user scripts**. Diagnose and fix the underlying OS service (e.g. `LanmanWorkstation`), network route, or authentication first.
* **Windows Batch Files Strict CRLF:**
  All Windows batch files (`.bat`, `.cmd`) **MUST ALWAYS HAVE CRLF (`\r\n`) LINE ENDINGS**. Never save batch files with LF — Windows `cmd.exe` miscalculates line offsets on LF and breaks command parsing. Always run `unix2dos` or verify `\r\n`.
* **No Premature Batch Code Surgery:**
  Never alter working batch logic unless an actual syntax/code bug inside the script has been proven. If the problem is environmental, state it clearly and provide a 1-click system fix.
* **Zero Dangling Background Tasks:** Always verify 0 active background tasks before delivering final responses.
