---
name: gmail
description: Read, search, list, and send emails via Gmail for Vladimir Bulantsev (gin.vladimir@gmail.com). Use whenever the user asks to check email, list recent messages, search inbox, send an email, or clean job rejection emails.
---

# Gmail CLI Skill

The `gmail` command line tool provides access to the user's Google Mail (`gin.vladimir@gmail.com`).

## Available Commands

### 1. Check Status
```bash
gmail status
```
Verifies IMAP and SMTP connections and reports total and unread message counts.

### 2. List Recent Emails
```bash
gmail list [-n LIMIT] [-u] [-f FOLDER]
```
- `-n 10`: Show last 10 emails (default: 10)
- `-u`: Only show unread emails
- `-f INBOX`: Folder name (default: INBOX)

### 3. Read Email by ID
```bash
gmail read <MESSAGE_ID> [--max-chars 3000]
```
Fetches and displays the full subject, sender, date, and body content of the email.

### 4. Search Emails
```bash
gmail search "<QUERY>" [-n LIMIT]
```
Searches for emails where subject or sender matches the query string.

### 5. Send Email
```bash
gmail send --to "<RECIPIENT>" --subject "<SUBJECT>" --body "<BODY_TEXT>"
```
Sends an email from `gin.vladimir@gmail.com`.

### 6. Clean Job Rejections (Почисти почту от отказов о работе)
```bash
gmail clean-rejections [--days 90] [--dry-run] [-f INBOX]
```
Automatically scans, detects, and safely moves job rejection emails (Jobs.cz, LinkedIn, Teamio, StartupJobs, ATS) across Czech, English, German, and Russian into Trash with zero false positives.
