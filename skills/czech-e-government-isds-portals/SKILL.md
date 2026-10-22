---
name: czech-e-government-isds-portals
description: >-
  Operational workflows, legal rules, and filing standards for Czech electronic public administration: Data Boxes (ISDS), Tax Portal MOJE daně (DIS+), e-Portál ČSSZ, health insurance portals (VZP, OZP), and BankID.
---
# Czech E-Government: ISDS Data Boxes, DIS+ & State Portals

A comprehensive operational manual for navigating electronic public administration in the Czech Republic, managing official Data Box (ISDS) communications, submitting mandatory tax filings via DIS+, and auditing social and health insurance portals.

---

## 1. Data Boxes (Datové schránky / ISDS - Act No. 300/2008 Sb.)

### A. Legal Nature & Mandatory Allocation:
- **Mandatory Creation by Law**:
  - All legal entities (*právnické osoby* - s.r.o., a.s.) and registered sole proprietors (*podnikající fyzické osoby - OSVČ*).
  - Private individuals (*fyzické osoby nepodnikající*) can activate optionally or automatically upon logging into public administration via BankID.
- **Statutory Delivery Rule (*Fikce doručení* - § 17 odst. 4 Act 300/2008 Sb.)**:
  - A message sent by a public authority is legally delivered the moment the authorized user logs into the Data Box.
  - **Fictional Delivery after 10 Days**: If the user does not log into the Data Box within **10 days** from the day the message was deposited, the message is considered **legally delivered on the 10th day**, even if never opened or read. Procedural appeal deadlines (typically 15 or 30 days) start running immediately from day 10.
  - *Exclusion of Delivery Fiction*: Only if the document is explicitly designated for personal delivery (*do vlastních rukou*) and law excludes fictional delivery.

### B. Technical Formats, Signatures & Message Retention:
- **Statutory Formats**: Official filings to authorities must be in `PDF/A`, `XML` (prescribed schemas for tax and social security), or `ZFO` (digitally signed data message container).
- **Automated Electronic Signature**: Messages sent from the user's Data Box to a public authority do not require a separate qualified electronic signature (QES / *uznávaný elektronický podpis*); delivery via the authenticated Data Box serves as statutory personal signature (§ 18 odst. 2).
- **Standard 90-Day Deletion Window**:
  - By default, messages are permanently erased from the ISDS portal after **90 days**.
  - *Operational Defense*: Download and archive all incoming/outgoing messages in `.zfo` format (includes the complete cryptographic timestamp and digital certificate chain for court evidence) or activate the paid *Datový trezor* service.

---

## 2. Tax Portal MOJE daně & Daňová informační schránka plus (DIS+)

### A. Mandatory Electronic Filing (§ 72 & § 247a Daňový řád - DŘ):
- **Statutory Form Requirement**: Any taxpayer who has a statutory Data Box (*ze zákona zřízená datová schránka*) is **strictly obligated** to submit tax returns, supplementary returns, and notifications electronically in XML format via:
  1. Datová schránka (uploading XML generated from accounting software or EPO).
  2. The DIS+ portal (authenticated via BankID, MojeID, or eObčanka).
- **Penalty for Paper or Invalid Format (§ 247a odst. 2 DŘ)**:
  - If a tax return is filed in paper format or sent via email without a qualified electronic signature, the Tax Authority automatically issues a statutory penalty of **1 000 CZK**.
  - If the taxpayer fails to remedy the defect after official notice, the penalty can reach up to **50 000 CZK**.

### B. DIS+ Operational Capabilities:
- View real-time **Personal Tax Accounts (*Osobní daňové účty*)**: check overpayments, underpayments, and accrued interest (*úroky z prodlení*) across individual taxes (DPH, DPFO, DPPO, srážková daň).
- Automatic generation of payment QR codes (**SPAYD standard**) with correct bank accounts, prefix codes, and Variabilní symbol (Birth number for individuals, IČO for legal entities).

---

## 3. Social Security Administration (e-Portál ČSSZ)

### A. Mandatory Electronic Submissions:
- All filings for employers and OSVČ must be executed electronically via the VREP framework or authenticated via e-Portál ČSSZ:
  - **Přehled o příjmech a výdajích OSVČ**: Annual overview of income and expenses.
  - **Evidenční list důchodového pojištění (ELDP)**: Annual pension insurance record per employee.
  - **Oznámení o nástupu do zaměstnání (ONZ)**: Reporting commencement/termination of employment within 8 calendar days.

### B. Verification of Insurance Periods (*Konto pojištěnce*):
- Audit personal pension insurance history (*Informativní osobní list důchodového pojištění - IOLDP*): verify all registered years of employment, substitute insurance periods (*náhradní doby pojištění* - studies, care of children), and wage assessment bases (*vyměřovací základy*).

---

## 4. Health Insurance Portals (VZP Point & Vitakarta OZP)

### A. Employer & OSVČ Obligations:
- Annual filing of **Přehled OSVČ pro zdravotní pojišťovnu** within 1 month following the tax return deadline.
- Mass reporting of insured persons: 8-day deadline to report changes (hiring, termination, commencement of unpaid leave).
- Account balance verification: Real-time monitoring of monthly prepayment allocations (*přehled plateb a záloh*).

### B. Digital Identity Ecosystem (Identita občana & BankID):
- National identity gateway (*Národní bod pro identifikaci a autentizaci - NIA*).
- **BankID (Bankovní identita)**: Primary zero-cost authentication tool for all Czech e-government portals, signing PDF documents, and verifying identity across banks, utilities (ČEZ ON-LINE), and state registries.
