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
- `upřednostnili (jsme )?(jiné|jiného|ostatní|uchazeče|uchazečů|kandidát)`
- `dali (jsme )?přednost (jiným|jinému|ostatním)`
- `(vybrali|našli) (jsme )?(jiného|jiné) (kandidát|uchazeč)`
- `(do )?(dalšího|druhého|třetího|užšího) kola (výběrového řízení |výběru )?(jsme )?(vybrali|vybrat) (jiného )?(kandidát|uchazeč)` (*«jsme do dalšího kola výběrového řízení vybrali kandidáta...»*)
- `vybrali (jsme )?kandidáta, který .*(odpovídal|odpovídá)`
- `požadavkům odpovídal o něco přesněji` / `(lépe|více|přesněji) odpovídá (našim )?požadavkům`
- `rozhodli (jsme se )?pokračovat s jiným`
- `nemáme (v tuto chvíli )?(pro vás )?(jinou )?(vhodnou )?pozici` (*«V tuto chvíli pro Vás nemáme jinou vhodnou pozici»*)
- `(s politováním|s lítostí) (vám )?(musíme |musím )?(oznámit|sdělit)` / `litujeme`
- `bohužel (vám )?(musím|musíme) (oznámit|sdělit)` (*«Vám bohužel musím oznámit»*)
- `nepostupujete do (dalšího|užšího)`
- `(do )?(užšího|dalšího) (výběru|kola) .*(nezařadili|nepostupujete|upřednostnili)` (*«do užšího výběru nezařadili»*)
- `profil do užšího výběru nezařadili`
- `nebudeme (vás )?(zvát|pokračovat)`
- `pozice byla (obsazena|uzavřena)`
- `bohužel` in proximity (<= 100 chars) to `(kandidát|uchazeč|pozic|vybrali|upřednostnili|nemáme|rozhodli|nepostup|nezařadili|výběr)`

#### 🇬🇧 English Patterns (LinkedIn, International ATS: Greenhouse, Lever, SAP)
- `decided to move forward with (other|another|different)`
- `(pursue|pursuing) (other|another) candidate`
- `(found|selected|chosen) (other|another) candidate`
- `will not be moving forward` / `not moving forward (with your application)?`
- `decided not to proceed` / `will not be proceeding`
- `regret to inform you`
- `not selected for this (role|position|interview)`
- `(role|position) has been filled`
- `after careful consideration` + `(other candidates|not selected|decided not|another candidate)`
- `unfortunately` in proximity (<= 100 chars) to `(candidate|move forward|position|role|profile|proceed|not selected|pursue|another)`
- `do not have any (other )?(open|suitable) (roles|positions)`

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

1. **Protected Senders Whitelist (Outgoing & Family):**
   - Outgoing messages from Vladimir Bulantsev (`gin.vladimir@gmail.com`, `gin@volny.cz`) or family (`elena.bulanceva@gmail.com`).
2. **Active Recruiter Outreach & Interview / Proposal Discussions:**
   - *«Pozvánka na pohovor»*, interview scheduling links, proposal discussions (*«Interview/queries to proposal required»*, *«rádi bychom vás pozvali»*, *«setkat se osobně»*).
   - LinkedIn InMail recruiter messages (*«Hledáme člověka, který...»*).
3. **Application Confirmations in Process (Подтверждения приёма резюме):**
   - *«Zařadili jsme Vás do výběrového řízení»*
   - *«Děkujeme za projevení zájmu o spolupráci ... budeme Vás kontaktovat»*
   - *«Your CV is on its way to us»*
   - *«Potvrzení o přijetí odpovědi»*
   - *«Už o vás víme»*
   - *«We received your application»*
4. **Critical Non-Job Emails:**
   - Bank notifications (Fio, ČS, KB, AirBank, Raiffeisen).
   - Utility and telecom bills (ČEZ, Vodafone, Innogy, O2, T-Mobile).
   - Domain and hosting notifications (NIC.cz, Beget, FastVPS, Hetzner, AWS, Oracle).
   - Government and legal portals (DIS+, ČSSZ, Datová schránka, VZP, OZP).

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
