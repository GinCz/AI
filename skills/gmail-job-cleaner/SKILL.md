---
name: gmail-job-cleaner
description: Universal automated cleaner for job application rejection emails in Vladimir's Gmail (gin.vladimir@gmail.com). Triggers on requests like "почисти мою почту от отказов о работе", "удали отказы по работе", or "clean job rejections".
---

# 🧹 Universal Job Rejection Cleaner Protocol

> **Objective:** 100% accurate, zero-false-positive detection and safe removal of job rejection emails from Gmail (`gin.vladimir@gmail.com`).  
> **Target Sources:** Jobs.cz, Práce.cz, Teamio ATS, LinkedIn InMail / Job Alerts, StartupJobs, Atmoskop, SAP SuccessFactors, Greenhouse, Lever, Workday, SmartRecruiters, and direct corporate HR / career form responses.

---

## ⚡ Canonical Trigger Phrases

When Vladimir says any of the following (or similar variations):
- *«Почисти мою почту от отказов о работе»*
- *«Удали все отказы по резюме из почты»*
- *«Посмотри отказы по вакансиям за последние пару месяцев и удали их»*
- *«Clean job rejections from my email»*

The agent **MUST NOT** ask unnecessary questions. It must immediately execute the universal formula described below.

---

## 🧭 Operational Execution Pipeline

### Method 1: Using the Native CLI (Fastest & Canonical)
```bash
gmail clean-rejections --days 90
```
- Preview without deletion:
  ```bash
  gmail clean-rejections --days 90 --dry-run
  ```

### Method 2: Standalone Python Script
```bash
python3 /root/.AI/github/AI/skills/gmail-job-cleaner/scripts/clean_job_rejections.py --days 90
```

---

## 🔍 The Universal Detection Formula

### 1. Multi-Lingual Rejection Matrix

#### 🇨🇿 Czech Patterns (High-Frequency: Jobs.cz, Teamio, Direct HR)
- `upřednostnili (jsme )?(jiné|jiného|uchazeče|uchazečů)`
- `dali (jsme )?přednost (jiným|jinému|ostatním)`
- `vybrali (jsme )?(jiného|jiné) kandidát`
- `rozhodli (jsme se )?pokračovat s jiným`
- `v tuto chvíli (pro vás )?nemáme vhodnou pozici`
- `s politováním oznámit` / `litujeme`
- `nepostupujete do (dalšího|užšího)` / `do užšího výběru upřednostnili`
- `nebudeme pokračovat` / `nebudeme vás zvát`
- `pozice byla obsazena`
- `bohužel` in proximity to `(kandidát|uchazeč|pozic|vybrali|upřednostnili|nemáme|rozhodli|nepostup)`

#### 🇬🇧 English Patterns (LinkedIn, International ATS: Greenhouse, Lever, SAP)
- `decided to move forward with (other|another) candidate`
- `pursue (other|another) candidate`
- `will not be moving forward` / `not moving forward`
- `decided not to proceed` / `will not be proceeding`
- `regret to inform`
- `not selected for this (role|position)`
- `position has been filled`
- `after careful consideration` + `(other candidates|not selected|decided not)`
- `unfortunately` + `(candidate|move forward|position|role|profile|proceed)`

#### 🇩🇪 German Patterns
- `anderen kandidaten den vorzug`
- `nicht weiterverfolgen`
- `leider` + `(absage|bewerbung|kandidat)`

#### 🇷🇺 Russian Patterns
- `вынуждены отказать`
- `выбрали другого кандидата`
- `не готовы (сейчас )?предложить`
- `к сожалению` + `(отказ|другого кандидата|не готовы)`

---

## 🛡️ Strict Negative Invariants (Zero False Positives — NEVER DELETE)

The cleaner **MUST NEVER** touch or delete the following categories:

1. **Application Confirmations (Подтверждения приёма резюме):**
   - *«Zařadili jsme Vás do výběrového řízení»*
   - *«Děkujeme za projevení zájmu o spolupráci»*
   - *«Your CV is on its way to us»*
   - *«Potvrzení o přijetí odpovědi»*
   - *«Už o vás víme»*
   - *«We received your application»*
2. **Active Recruiter Outreach & Interview Invitations:**
   - *«Pozvánka na pohovor»*, interview scheduling links.
   - LinkedIn InMail recruiter messages (*«Hledáme člověka, který...»*).
3. **Critical Non-Job Emails:**
   - Bank notifications (Fio, Sberbank).
   - Utility and telecom bills (ČEZ, Vodafone, Innogy).
   - Domain and hosting notifications (NIC.cz, Beget, FastVPS).
   - Government and legal portals (DIS+, ČSSZ, Datová schránka).

---

## 🗑️ Safe Deletion Protocol

1. Look up the localized Gmail Trash folder dynamically via IMAP attributes (`\Trash` attribute, e.g. `[Gmail]/&BBoEPgRABDcEOAQ9BDA-` for *Корзина* or `[Gmail]/Trash`).
2. Copy messages by IMAP `UID` to Trash:
   `mail.uid('COPY', uid, trash_folder)`
3. Mark message as `\Deleted` in `INBOX`:
   `mail.uid('STORE', uid, '+FLAGS', '(\\Deleted)')`
4. Execute `mail.expunge()`.
5. Messages remain in Trash for 30 days before permanent Google deletion, ensuring 100% safety and recoverability.

---

## 📊 Standard Report Format

After completing the cleanup, output a structured table/list to Vladimir:

```markdown
### 📋 Список найденных и удалённых писем с отказами:

1. **[Компания] — [Название позиции]**
   - **От:** `sender@domain.com`
   - **Тема:** `Subject line`
   - **Дата:** DD.MM.YYYY HH:MM
   - **Причина:** *«Цитата фразы отказа»*
   - **Статус:** 🗑️ Перемещено в Корзину (UID: `XXXXXX`)
```
