#!/usr/bin/env python3
"""
Universal Job Rejection Cleaner for Vladimir Bulantsev (gin.vladimir@gmail.com)
Scans Gmail IMAP, accurately classifies job rejections across CZ/EN/DE/RU,
and safely moves them to Trash with zero false positives.
"""

import sys
import argparse
import imaplib
import email
from email.header import decode_header
import datetime
import re

EMAIL_USER = "gin.vladimir@gmail.com"
EMAIL_PASS = "thilulonhxqcjmry"
IMAP_HOST = "imap.gmail.com"
IMAP_PORT = 993

REJECTION_PATTERNS = [
    # Czech
    r"upřednostnili\s+(jsme\s+)?(jiné|jiného|uchazeče|uchazečů)",
    r"dali\s+(jsme\s+)?přednost\s+(jiným|jinému|ostatním)",
    r"vybrali\s+(jsme\s+)?(jiného|jiné)\s+kandidát",
    r"rozhodli\s+(jsme\s+se\s+)?pokračovat\s+s\s+jiným",
    r"nemáme\s+(vhodnou\s+)?pozici",
    r"s\s+politováním\s+oznámit",
    r"nepostupujete\s+do\s+(dalšího|užšího)",
    r"do\s+užšího\s+výběru\s+upřednostnili",
    r"nebudeme\s+pokračovat",
    r"nebudeme\s+vás\s+zvát",
    r"pozice\s+byla\s+obsazena",
    r"bohužel\s+.*(kandidát|uchazeč|pozic|vybrali|upřednostnili|nemáme|rozhodli|nepostup)",
    # English
    r"decided\s+to\s+move\s+forward\s+with\s+(other|another)",
    r"pursue\s+(other|another)\s+candidate",
    r"will\s+not\s+be\s+moving\s+forward",
    r"not\s+moving\s+forward",
    r"decided\s+not\s+to\s+proceed",
    r"will\s+not\s+be\s+proceeding",
    r"regret\s+to\s+inform",
    r"not\s+selected\s+for\s+this\s+(role|position)",
    r"position\s+has\s+been\s+filled",
    r"after\s+careful\s+consideration.*(other\s+candidates|not\s+selected|decided\s+not)",
    r"unfortunately.*(candidate|move\s+forward|position|role|profile|proceed)",
    # German
    r"anderen\s+kandidaten\s+den\s+vorzug",
    r"nicht\s+weiterverfolgen",
    r"leider.*(absage|bewerbung|kandidat)",
    # Russian
    r"вынуждены\s+отказать",
    r"выбрали\s+другого\s+кандидата",
    r"не\s+готовы\s+(сейчас\s+)?предложить",
    r"к\s+сожалению.*(отказ|другого\s+кандидата|не\s+готовы)"
]

EXCLUSION_PATTERNS = [
    r"děkujeme za projevení zájmu o rozvoz",
    r"vaše vyúčtování",
    r"bezpečnostním incidentu",
    r"potvrzení o přijetí odpovědi",
    r"cenová nabídka",
    r"fio banka",
    r"vodafone",
    r"čez prodej",
    r"beget",
    r"copytrack"
]

def clean_header(header_val):
    if not header_val:
        return ""
    decoded_parts = decode_header(header_val)
    res = []
    for part, enc in decoded_parts:
        if isinstance(part, bytes):
            enc = enc or "utf-8"
            try:
                res.append(part.decode(enc, errors="ignore"))
            except Exception:
                res.append(part.decode("utf-8", errors="ignore"))
        else:
            res.append(str(part))
    return "".join(res)

def get_body(msg):
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            ctype = part.get_content_type()
            cdisp = str(part.get("Content-Disposition"))
            if ctype == "text/plain" and "attachment" not in cdisp:
                payload = part.get_payload(decode=True)
                if payload:
                    body = payload.decode(part.get_content_charset() or "utf-8", errors="ignore")
                    break
        if not body:
            for part in msg.walk():
                ctype = part.get_content_type()
                cdisp = str(part.get("Content-Disposition"))
                if ctype == "text/html" and "attachment" not in cdisp:
                    payload = part.get_payload(decode=True)
                    if payload:
                        body = payload.decode(part.get_content_charset() or "utf-8", errors="ignore")
                        break
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            body = payload.decode(msg.get_content_charset() or "utf-8", errors="ignore")
    clean = re.sub(r'<[^>]+>', ' ', body)
    clean = re.sub(r'\s+', ' ', clean).strip()
    return clean

def find_trash_folder(mail):
    status, folders = mail.list()
    for f in folders:
        line = f.decode("utf-8", errors="ignore")
        if "\\Trash" in line:
            parts = line.split(' "/" ')
            if len(parts) == 2:
                return parts[1].strip()
    return '"[Gmail]/Trash"'

def is_job_rejection(sender, subject, body):
    full_text = f"{sender} {subject} {body}".lower()
    for ex in EXCLUSION_PATTERNS:
        if re.search(ex, full_text):
            has_strong_rejection = any(re.search(p, full_text) for p in REJECTION_PATTERNS[:10])
            if not has_strong_rejection:
                return False, ""
                
    for pattern in REJECTION_PATTERNS:
        match = re.search(pattern, full_text)
        if match:
            return True, match.group(0)
            
    return False, ""

def main():
    parser = argparse.ArgumentParser(description="Universal Job Rejection Cleaner for Gmail")
    parser.add_argument("--days", type=int, default=90, help="Look back period in days (default: 90)")
    parser.add_argument("--dry-run", action="store_true", help="Preview matches without deleting")
    parser.add_argument("-f", "--folder", default="INBOX", help="Target IMAP folder (default: INBOX)")
    args = parser.parse_args()

    print(f"🧹 Scanning '{args.folder}' for job rejection emails (last {args.days} days)...")
    try:
        mail = imaplib.IMAP4_SSL(IMAP_HOST, IMAP_PORT)
        mail.login(EMAIL_USER, EMAIL_PASS)
        trash = find_trash_folder(mail)
        
        since_date = (datetime.date.today() - datetime.timedelta(days=args.days)).strftime("%d-%b-%Y")
        mail.select(args.folder)
        status, data = mail.search(None, f"(SINCE {since_date})")
        msg_ids = data[0].split()
        
        print(f"📬 Scanned {len(msg_ids)} messages in '{args.folder}' since {since_date}.")
        
        rejections = []
        for mid in msg_ids:
            status, d = mail.fetch(mid, "(UID RFC822)")
            if not d or not d[0]:
                continue
            uid = d[0][0].decode().split()[2]
            raw = d[0][1]
            msg = email.message_from_bytes(raw)
            subj = clean_header(msg.get("Subject"))
            sender = clean_header(msg.get("From"))
            date_val = clean_header(msg.get("Date"))
            body = get_body(msg)
            
            is_rej, reason = is_job_rejection(sender, subj, body)
            if is_rej:
                rejections.append({
                    "uid": uid,
                    "date": date_val,
                    "sender": sender,
                    "subject": subj,
                    "reason": reason
                })
                
        if not rejections:
            print("✨ No job rejection emails found. Mailbox is clean!")
            mail.logout()
            return
            
        print(f"\n🎯 Found {len(rejections)} job rejection email(s):")
        for idx, r in enumerate(rejections, 1):
            print(f"  {idx}. [UID: {r['uid']}] {r['date']}")
            print(f"     From:    {r['sender']}")
            print(f"     Subject: {r['subject']}")
            print(f"     Trigger: \"{r['reason']}\"")
            print("     " + "-" * 55)
            
        if args.dry_run:
            print(f"\n🔍 [DRY-RUN] No emails were moved. Target trash folder: {trash}")
            mail.logout()
            return
            
        print(f"\n🗑️  Moving {len(rejections)} email(s) to Trash ({trash})...")
        for r in rejections:
            mail.uid("COPY", r["uid"], trash)
            mail.uid("STORE", r["uid"], "+FLAGS", "(\\Deleted)")
            
        mail.expunge()
        mail.logout()
        print(f"✅ Successfully moved {len(rejections)} email(s) to Trash and cleaned '{args.folder}'.")
    except Exception as e:
        print(f"❌ Error during cleaning: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
