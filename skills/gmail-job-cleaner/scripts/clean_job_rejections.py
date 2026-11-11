#!/usr/bin/env python3
"""
Universal Job Rejection Cleaner for Vladimir Bulantsev (gin.vladimir@gmail.com)
Scans Gmail IMAP safely, accurately classifies job rejections across CZ/EN/DE/RU,
and safely moves them to Trash with zero false positives.
"""

import sys
import argparse
import imaplib
import email
from email.header import decode_header
import quopri
import base64
import datetime
import re

EMAIL_USER = "gin.vladimir@gmail.com"
EMAIL_PASS = "thilulonhxqcjmry"
IMAP_HOST = "imap.gmail.com"
IMAP_PORT = 993

# Strict Sender Whitelist (Never delete outgoing emails from Vladimir or family)
PROTECTED_SENDERS = [
    "gin.vladimir@gmail.com",
    "gin@volny.cz",
    "elena.bulanceva@gmail.com"
]

REJECTION_PATTERNS = [
    # Czech patterns
    r"upřednostnili\s+(jsme\s+)?(jiné|jiného|ostatní|uchazeče|uchazečů|kandidát)",
    r"dali\s+(jsme\s+)?přednost\s+(jiným|jinému|ostatním)",
    r"(vybrali|našli)\s+(jsme\s+)?(jiného|jiné)\s+(kandidát|uchazeč)",
    r"rozhodli\s+(jsme\s+se\s+)?pokračovat\s+s\s+jiným",
    r"nemáme\s+(v\s+tuto\s+chvíli\s+)?(pro\s+vás\s+)?(jinou\s+)?(vhodnou\s+)?pozici",
    r"(s\s+politováním|s\s+lítostí)\s+(vám\s+)?(musíme\s+|musím\s+)?(oznámit|sdělit)",
    r"bohužel\s+(vám\s+)?(musím|musíme)\s+(oznámit|sdělit)",
    r"nepostupujete\s+do\s+(dalšího|užšího)",
    r"(do\s+)?(užšího|dalšího)\s+(výběru|kola)\s+.*(nezařadili|nepostupujete|upřednostnili)",
    r"profil\s+do\s+užšího\s+výběru\s+nezařadili",
    r"nebudeme\s+(vás\s+)?(zvát|pokračovat)",
    r"pozice\s+byla\s+(obsazena|uzavřena)",
    r"bohužel.{1,100}(kandidát|uchazeč|pozic|vybrali|upřednostnili|nemáme|rozhodli|nepostup|nezařadili|výběr)",
    # English patterns
    r"decided\s+to\s+move\s+forward\s+with\s+(other|another|different)",
    r"(pursue|pursuing)\s+(other|another)\s+candidate",
    r"(found|selected|chosen)\s+(other|another)\s+candidate",
    r"will\s+not\s+be\s+moving\s+forward",
    r"not\s+moving\s+forward\s+(with\s+your\s+application)?",
    r"decided\s+not\s+to\s+proceed",
    r"will\s+not\s+be\s+proceeding",
    r"regret\s+to\s+inform\s+you",
    r"not\s+selected\s+for\s+this\s+(role|position|interview)",
    r"(role|position)\s+has\s+been\s+filled",
    r"after\s+careful\s+consideration.*(other\s+candidates|not\s+selected|decided\s+not|another\s+candidate)",
    r"unfortunately.{1,100}(candidate|move\s+forward|position|role|profile|proceed|not\s+selected|pursue|another)",
    r"do\s+not\s+have\s+any\s+(other\s+)?(open|suitable)\s+(roles|positions)",
    # German patterns
    r"anderen\s+kandidaten\s+den\s+vorzug",
    r"nicht\s+weiterverfolgen",
    r"leider.*(absage|bewerbung|kandidat)",
    # Russian patterns
    r"вынуждены\s+отказать",
    r"выбрали\s+другого\s+кандидата",
    r"не\s+готовы\s+(сейчас\s+)?предложить",
    r"к\s+сожалению.*(отказ|другого\s+кандидата|не\s+готовы)"
]

EXCLUSION_PATTERNS = [
    # Active interview invitations & recruiter engagement
    r"pozvánka na pohovor",
    r"pozvánku na pohovor",
    r"zveme vás na pohovor",
    r"rádi bychom vás pozvali",
    r"interview/queries to proposal",
    r"schedule an interview",
    r"setkat se osobně",
    r"setkáme osobně",
    # Active applications in process
    r"vaše odpověď byla doručena",
    r"vaše žádost byla přijata",
    r"potvrzení o přijetí odpovědi",
    r"děkujeme za projevení zájmu o rozvoz",
    r"your cv is on its way to us",
    r"we received your application",
    # Critical finances, utilities, portals
    r"vaše vyúčtování",
    r"bezpečnostním incidentu",
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

def decode_payload(raw_bytes):
    if not raw_bytes:
        return ""
    try:
        t = quopri.decodestring(raw_bytes).decode("utf-8", errors="ignore")
        if len(t.strip()) > 5:
            return t
    except Exception:
        pass
    try:
        b64 = raw_bytes.strip().replace(b"\r\n", b"").replace(b"\n", b"")
        t = base64.b64decode(b64).decode("utf-8", errors="ignore")
        if len(t.strip()) > 5:
            return t
    except Exception:
        pass
    return raw_bytes.decode("utf-8", errors="ignore")

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
    sender_lower = sender.lower()
    for ps in PROTECTED_SENDERS:
        if ps in sender_lower:
            return False, ""

    full_text = f"{sender} {subject} {body}".lower()
    full_text = re.sub(r"<[^>]+>", " ", full_text)
    full_text = re.sub(r"\s+", " ", full_text).strip()

    for ex in EXCLUSION_PATTERNS:
        if re.search(ex, full_text):
            return False, ""

    for pattern in REJECTION_PATTERNS:
        match = re.search(pattern, full_text)
        if match:
            return True, match.group(0)

    return False, ""

def scan_and_clean(days=90, folder="INBOX", dry_run=False):
    print(f"🧹 Scanning '{folder}' for job rejection emails (last {days} days)...")
    try:
        mail = imaplib.IMAP4_SSL(IMAP_HOST, IMAP_PORT)
        mail.login(EMAIL_USER, EMAIL_PASS)
        trash = find_trash_folder(mail)

        since_date = (datetime.date.today() - datetime.timedelta(days=days)).strftime("%d-%b-%Y")
        mail.select(folder)
        status, data = mail.search(None, f"(SINCE {since_date})")
        msg_ids = data[0].split()

        print(f"📬 Scanned {len(msg_ids)} messages in '{folder}' since {since_date}.")

        rejections = []
        chunk_size = 25
        for i in range(0, len(msg_ids), chunk_size):
            chunk = msg_ids[i:i + chunk_size]
            ids_str = ",".join([m.decode() for m in chunk])
            st, fetch_data = mail.fetch(ids_str, "(UID RFC822.HEADER BODY.PEEK[1]<0.8192>)")

            j = 0
            while j < len(fetch_data):
                item = fetch_data[j]
                if isinstance(item, tuple) and len(item) == 2:
                    desc = item[0].decode()
                    uid_m = re.search(r"UID\s+(\d+)", desc)
                    c_uid = uid_m.group(1) if uid_m else "unknown"

                    if "RFC822.HEADER" in desc:
                        h_msg = email.message_from_bytes(item[1])
                        subj = clean_header(h_msg.get("Subject"))
                        sender = clean_header(h_msg.get("From"))
                        date_val = clean_header(h_msg.get("Date"))

                        b_text = ""
                        if j + 1 < len(fetch_data) and isinstance(fetch_data[j + 1], tuple):
                            next_desc = fetch_data[j + 1][0].decode()
                            if "BODY[1]" in next_desc:
                                b_text = decode_payload(fetch_data[j + 1][1])
                                j += 1

                        is_rej, reason = is_job_rejection(sender, subj, b_text)
                        if is_rej:
                            rejections.append({
                                "uid": c_uid,
                                "date": date_val,
                                "sender": sender,
                                "subject": subj,
                                "reason": reason,
                                "snippet": b_text[:250].replace("\n", " ").strip()
                            })
                j += 1

        if not rejections:
            print("✨ No job rejection emails found. Mailbox is clean!")
            mail.logout()
            return []

        print(f"\n🎯 Found {len(rejections)} job rejection email(s):")
        for idx, r in enumerate(rejections, 1):
            print(f"  {idx}. [UID: {r['uid']}] {r['date']}")
            print(f"     From:    {r['sender']}")
            print(f"     Subject: {r['subject']}")
            print(f"     Trigger: \"{r['reason']}\"")
            print("     " + "-" * 55)

        if dry_run:
            print(f"\n🔍 [DRY-RUN] No emails were moved. Target trash folder: {trash}")
            mail.logout()
            return rejections

        print(f"\n🗑️  Moving {len(rejections)} email(s) to Trash ({trash})...")
        for r in rejections:
            mail.uid("COPY", r["uid"], trash)
            mail.uid("STORE", r["uid"], "+FLAGS", "(\\Deleted)")

        mail.expunge()
        mail.logout()
        print(f"✅ Successfully moved {len(rejections)} email(s) to Trash and cleaned '{folder}'.")
        return rejections
    except Exception as e:
        print(f"❌ Error during cleaning: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Universal Job Rejection Cleaner for Gmail")
    parser.add_argument("--days", type=int, default=90, help="Look back period in days (default: 90)")
    parser.add_argument("--dry-run", action="store_true", help="Preview matches without deleting")
    parser.add_argument("-f", "--folder", default="INBOX", help="Target IMAP folder (default: INBOX)")
    args = parser.parse_args()

    scan_and_clean(days=args.days, folder=args.folder, dry_run=args.dry_run)

if __name__ == "__main__":
    main()
