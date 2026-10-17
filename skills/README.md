# 🧠 Universal AI Skills Framework & Autonomous Execution Engine
> **Open-Source Enterprise Knowledge, Operational Workflows, and Diagnostic Protocols for Autonomous AI Agents and Multi-Model Systems**  
> 
> *Repository:* [GinCz/AI ↗](https://github.com/GinCz/AI) | *Owner:* Vladimir Bulantsev ([GinCz ↗](https://github.com/GinCz)) | *Version:* `v2026.1`  
> *Target Environments:* Google Antigravity, Claude, ChatGPT, Cursor, Windsurf, VS Code, Local LLMs (Ollama / vLLM)

---

## 🧭 Overview & Autonomous AI Ingestion

This directory contains **20 battle-tested, production-ready operational skills** designed to turn any raw Large Language Model (Gemini, Claude, GPT-4/o1, DeepSeek, Llama 3) into a specialized, domain-expert autonomous agent.

Each skill is architected with a strict **three-tier maturity model (Level 1: Beginner ➔ Level 2: Intermediate ➔ Level 3: Production Master)**, complete with operational trigger matrices, diagnostic decision trees, and companion reference guides.

> [!TIP]
> **Zero-Dependency Guarantee:** These skills are 100% public, modular, and self-contained. Any AI system can ingest, learn, and execute them directly via the public GitHub URLs **without requiring access to any private repositories, proprietary tooling, or authentication tokens**.

---

## ⚡ 1-Click Prompt: Feed this to ANY AI Model to Self-Learn

Copy and paste this prompt into **ChatGPT, Claude, Gemini, Copilot, Cursor, or any local LLM** to instruct it to adopt these skills immediately:

```markdown
You are an Advanced Autonomous AI Agent. 
Adopt and activate the master open-source skills framework from:
https://github.com/GinCz/AI/tree/main/skills

Explore the skills directory and apply the corresponding operational workflows:
1. Systems & DevOps: devops-cloud-engineering, sysadmin-network-engineering, server-hardening-zerotrust.
2. Cybersecurity: cyber-defense-pentest, endpoint-mobile-security, code-review.
3. Troubleshooting & Planning: systematic-debugging, writing-plans, agent-browser.
4. Automotive Engineering: auto-electronics-diagnostics, auto-mechanics-powertrain.
5. EU & Czech Business / Tax: czech-accounting-tax, czech-business-law, eu-business-law-compliance, eu-vat-accounting.
6. Clinical Medicine & Surgery: clinical-cardiology-surgery, internal-medicine-hematology, neurology-neurosurgery-triage, ophthalmology-vision-care, orthopedics-knee-rehab.

Follow the three-tier execution hierarchy (L1 Fundamentals -> L2 Standard SOPs -> L3 Hardened Production). Always provide complete, production-grade solutions without omitting edge cases.
```

---

## 🏗️ The 3-Tier Skill Mastery Curve (Beginner to Expert)

Every skill in this repository is structured to scale across all skill levels:

```
┌────────────────────────────────────────────────────────────────────────┐
│ LEVEL 1: FOUNDATIONS & TAXONOMY (Beginner / Junior)                    │
│ • Core terminology, standard standards, foundational architectural models│
│ • Syntax verification, baseline tool usage, safety guardrails          │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ LEVEL 2: OPERATIONAL WORKFLOWS & SOPS (Intermediate / Mid-Level)       │
│ • Step-by-step diagnostic trees, root-cause isolation algorithms        │
│ • Real-time telemetry analysis, configuration templates, script audits │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ LEVEL 3: ENTERPRISE OVERHAUL & ZERO-TRUST (Senior / Principal Master)  │
│ • Zero-Trust defense, kernel parameter tuning, distributed architectures│
│ • Emergency triage, deep forensic analysis, strict legal/tax compliance│
└────────────────────────────────────────────────────────────────────────┘
```

---

## 📚 Master Catalog of the 20 Production Skills

### 🖥️ I. Infrastructure, DevOps & Cloud Engineering

#### 1. [`devops-cloud-engineering`](devops-cloud-engineering/SKILL.md)
* **Domain:** Cloud Infrastructure, Containerization & CI/CD Pipelines
* **Core Stack:** Docker (rootless), Docker Compose, GitHub Actions, Terraform, Ansible, Oracle OCI, AWS, Netcup, Prometheus, Grafana, Loki.
* **Tiered Mastery:**
  * **L1 (Beginner):** Writing clean `Dockerfile` with multi-stage builds, basic Compose services, CI/CD syntax validation.
  * **L2 (Intermediate):** Self-hosted runner setup, Terraform state management, Prometheus metric scraping, Loki log pipeline ingestion.
  * **L3 (Production Master):** Kernel `sysctl` TCP optimization for high-throughput nodes, zero-downtime blue/green deployments, rootless container security hardening.

#### 2. [`sysadmin-network-engineering`](sysadmin-network-engineering/SKILL.md)
* **Domain:** Enterprise Systems Administration, Routing & Network Obfuscation
* **Core Stack:** Linux (Debian/Ubuntu/RHEL), Windows Server, Nginx, Caddy, HAProxy, BIND9, Unbound, WireGuard, Xray (VLESS-XTLS-Reality), 3X-UI, BorgBackup, Rclone.
* **References:** [`references/xray_vless_reality_quickref.md`](sysadmin-network-engineering/references/xray_vless_reality_quickref.md)
* **Tiered Mastery:**
  * **L1 (Beginner):** Systemd service management, DNS A/AAAA/CNAME setup, UFW firewall rules, SSH key generation.
  * **L2 (Intermediate):** Reverse proxy configuration with automatic TLS (acme.sh/Let's Encrypt), automated 3-2-1 backup rotation with Borg encryption, WireGuard site-to-site tunnels.
  * **L3 (Production Master):** DPI-resistant censorship circumvention using Xray VLESS-Reality with uTLS camouflage, policy routing (FWMARK), BGP peering, MTU black hole discovery.

#### 3. [`server-hardening-zerotrust`](server-hardening-zerotrust/SKILL.md)
* **Domain:** Enterprise Server Hardening & Zero-Trust Architecture
* **Core Stack:** SSH ed25519 with 2FA (libpam-google-authenticator), Nftables, Fail2ban, CrowdSec, ModSecurity/Coraza WAF, AppArmor/SELinux, PCI DSS v4.0.
* **References:** [`references/linux_hardening_script_template.md`](server-hardening-zerotrust/references/linux_hardening_script_template.md)
* **Tiered Mastery:**
  * **L1 (Beginner):** Disabling password authentication in SSH, configuring non-standard ports, basic Fail2ban jails.
  * **L2 (Intermediate):** Nftables stateful filtering, CrowdSec multi-server log bouncer setup, automated security patch pipelines (unattended-upgrades).
  * **L3 (Production Master):** Full PCI DSS v4.0 system hardening, kernel memory protection (`kernel.kptr_restrict`, `fs.protected_fifos`), mTLS bastion mesh, zero-trust microsegmentation.

---

### 🛡️ II. Cybersecurity, Pentesting & Endpoint Defense

#### 4. [`cyber-defense-pentest`](cyber-defense-pentest/SKILL.md)
* **Domain:** Offensive Security, Vulnerability Assessment & Threat Hunting
* **Core Stack:** MITRE ATT&CK framework, OWASP Top 10, Nmap, Nuclei, Nikto, Burp Suite, Metasploit, Linux SUID audit, Windows Potato privilege escalation, PCAP packet analysis.
* **References:** [`references/mitre_attack_privesc_cheatsheet.md`](cyber-defense-pentest/references/mitre_attack_privesc_cheatsheet.md)
* **Tiered Mastery:**
  * **L1 (Beginner):** Safe network reconnaissance, port scanning fundamentals, banner grabbing, common vulnerability scanning.
  * **L2 (Intermediate):** OWASP Top 10 exploitation (SQLi, IDOR, SSRF), Linux SUID/SGID auditing, sudoers misconfiguration exploitation, cron job hijacking.
  * **L3 (Production Master):** Advanced privilege escalation (PrintSpoofer, GodPotato on Windows Server), Active Directory Kerberoasting, evasive lateral movement analysis, incident threat hunting.

#### 5. [`endpoint-mobile-security`](endpoint-mobile-security/SKILL.md)
* **Domain:** Workstation, Mobile & Hardware Endpoint Defense
* **Core Stack:** BitLocker TPM 2.0, LUKS2, UEFI Secure Boot, Browser sandbox isolation, Android APK decompilation (`jadx`, `apktool`), Frida, VPN Kill-Switch.
* **References:** [`references/android_apk_security_audit_checklist.md`](endpoint-mobile-security/references/android_apk_security_audit_checklist.md)
* **Tiered Mastery:**
  * **L1 (Beginner):** Full-disk encryption setup, browser tracking protection, password manager enforcement, 2FA hygiene.
  * **L2 (Intermediate):** Strict VPN kill-switch implementation with routing rules, DNS leak prevention, mobile permission auditing, SIM-swap defense.
  * **L3 (Production Master):** Deep Android APK static/dynamic reverse engineering, obfuscated malware unpacking, hardcoded secret extraction, Pegasus/FinFisher-style spyware forensic triage.

---

### 💻 III. Software Engineering, Auditing & Debugging

#### 6. [`code-review`](code-review/SKILL.md)
* **Domain:** Script & Code Security Auditing
* **Capabilities:** Static analysis for Bash, PowerShell, and Python. Detecting command injection, unquoted variables, insecure temporary files, and unhandled edge cases.

#### 7. [`systematic-debugging`](systematic-debugging/SKILL.md)
* **Domain:** Methodical Root-Cause Analysis
* **Capabilities:** Eliminates guess-work and blind patches. Enforces a strict 4-step scientific protocol: Reproduce ➔ Isolate Variable ➔ Formulate Hypothesis ➔ Validate Resolution.

#### 8. [`writing-plans`](writing-plans/SKILL.md)
* **Domain:** Pre-Implementation Architecture & Execution Planning
* **Capabilities:** Mandatory phased planning before executing complex multi-system changes. Guarantees rollback paths, dependency graphs, and testable milestones.

#### 9. [`agent-browser`](agent-browser/SKILL.md)
* **Domain:** Technical Documentation Lookup & Command Verification
* **Capabilities:** Live consultation of official system documentation, cmdlet parameters, API schemas, and RFC standards to eliminate hallucinated flags.

---

### 🚗 IV. Automotive Engineering & Powertrain Diagnostics

#### 10. [`auto-electronics-diagnostics`](auto-electronics-diagnostics/SKILL.md)
* **Domain:** Automotive Electrical Systems, Multiplex Networks & ECU Tuning
* **Core Stack:** CAN Bus (High/Low Speed), LIN, FlexRay, DoIP, SAE J1939, Digital Oscilloscope (PicoScope), Parasitic Drain (mA) testing, Immobilizer / EEPROM, EV/Hybrid High Voltage (DIN EN 50110).
* **References:** [`references/can_bus_oscilloscope_waveforms.md`](auto-electronics-diagnostics/references/can_bus_oscilloscope_waveforms.md)
* **Tiered Mastery:**
  * **L1 (Beginner):** OBD-II standard PID reading, DTC interpretation (P, C, B, U codes), 12V battery and alternator charging ripple test.
  * **L2 (Intermediate):** Parasitic drain measurement using fuse voltage drop tables, CAN bus termination resistance testing (60Ω), sensor waveform capture (Crankshaft CKP / Camshaft CMP sync).
  * **L3 (Production Master):** Deep CAN/LIN frame decoding, gateway communication loss troubleshooting, ECU flash/EEPROM checksum calculation, High-Voltage interlock loop (HVIL) isolation testing.

#### 11. [`auto-mechanics-powertrain`](auto-mechanics-powertrain/SKILL.md)
* **Domain:** Powertrain Mechanics, Commercial Trucks & Transmission Overhaul
* **Core Stack:** ICE Petrol (GDI, MPI), Common Rail Diesel (CRDI 2500+ bar), Commercial Trucks (Euro 3-6, Tatra, Foton, MAN, Scania), Pneumatics (Wabco/Knorr-Bremse), SCR/AdBlue, DSG/DCT.
* **References:** [`references/commercial_truck_air_brake_systems.md`](auto-mechanics-powertrain/references/commercial_truck_air_brake_systems.md)
* **Tiered Mastery:**
  * **L1 (Beginner):** Compression testing, fluid specifications, brake pad/rotor wear measurement, basic suspension inspection.
  * **L2 (Intermediate):** Common Rail injector leak-off testing, turbocharger wastegate/VNT actuator calibration, dual-clutch transmission (DSG DQ250/DQ500) adaptation.
  * **L3 (Production Master):** Heavy commercial truck pneumatic dual-circuit brake troubleshooting (four-circuit protection valve, EBS relay), SCR AdBlue dosing unit diagnostic, engine cylinder sleeve overhaul.

---

### ⚖️ V. European & Czech Law, Taxation & Accounting

#### 12. [`czech-accounting-tax`](czech-accounting-tax/SKILL.md)
* **Domain:** Czech Accounting, Taxation & Mandatory Electronic Filings
* **Core Framework:** Income Tax Act (ZDP No. 586/1992 Sb.), VAT Act (ZDPH No. 235/2004 Sb.), ČSSZ, VZP/OZP health insurance, Paušální daň (Bands 1-3), Paušální výdaje (40/60/80%), DIS+, ISDS Datová schránka.
* **References:** [`references/czech_tax_calendar_and_rates.md`](czech-accounting-tax/references/czech_tax_calendar_and_rates.md)
* **Tiered Mastery:**
  * **L1 (Beginner):** Tax calendar deadlines, flat-rate expense limits (60% up to 1.2M CZK), mandatory invoicing elements according to ZDPH § 29.
  * **L2 (Intermediate):** DPFO / DPPO calculation, Přehled ČSSZ and health insurance reconciliations, DPP and DPČ social threshold compliance, Datová schránka XML submission.
  * **L3 (Production Master):** VAT inspection report (*Kontrolní hlášení*) section matching, Identifikovaná osoba cross-border filings, dividend tax withholding (15% srážková daň) optimization.

#### 13. [`czech-business-law`](czech-business-law/SKILL.md)
* **Domain:** Czech Corporate Law & Commercial Governance
* **Core Framework:** Business Corporations Act (ZOK No. 90/2012 Sb. - s.r.o. governance), Civil Code (NOZ No. 89/2012 Sb.), Trade Licensing Act (Živnostenský zákon), Labour Code (*Schwarzsystém* audit).
* **References:** [`references/czech_sro_incorporation_and_governance.md`](czech-business-law/references/czech_sro_incorporation_and_governance.md)
* **Tiered Mastery:**
  * **L1 (Beginner):** Trade license (*Živnost*) registration, mandatory commercial register disclosures, standard contract clause structures.
  * **L2 (Intermediate):** Drafting *Jednatelská smlouva* (Executive service contract), General Meeting (*Valná hromada*) resolution templates, statute of limitations tracking.
  * **L3 (Production Master):** Piercing the corporate veil (*Péče řádného hospodáře* fiduciary breach defense), insolvency liability mitigation (§ 68 ZOK), anti-Schwarzsystém audit compliance.

#### 14. [`eu-business-law-compliance`](eu-business-law-compliance/SKILL.md)
* **Domain:** EU Regulatory Compliance, Digital Law & Cyber Directives
* **Core Framework:** EU Single Market freedoms, GDPR (Art. 6/9, DPIA, RoPA), EU AI Act (Risk tiers: Prohibited, High, GPAI), NIS2 Directive, DSA / DMA, AML/CFT (FAÚ, UBO/ESM register).
* **References:** [`references/eu_ai_act_risk_matrix.md`](eu-business-law-compliance/references/eu_ai_act_risk_matrix.md)
* **Tiered Mastery:**
  * **L1 (Beginner):** Cookie consent and privacy policy essentials under GDPR, basic AML customer verification.
  * **L2 (Intermediate):** Drafting Data Processing Agreements (DPA), Register of Processing Activities (RoPA), NIS2 supply chain risk assessment.
  * **L3 (Production Master):** EU AI Act high-risk classification audit, conformity assessment documentation, Ultimate Beneficial Owner (UBO) compliance, cross-border corporate structuring.

#### 15. [`eu-vat-accounting`](eu-vat-accounting/SKILL.md)
* **Domain:** Pan-European VAT Directives & Cross-Border Transactions
* **Core Framework:** EU VAT Directive (2006/112/EC), Reverse Charge mechanism (Art. 196), One Stop Shop (OSS / IOSS), VIES automated validation, DAC7 digital platform reporting.
* **References:** [`references/reverse_charge_invoice_clauses.md`](eu-vat-accounting/references/reverse_charge_invoice_clauses.md)
* **Tiered Mastery:**
  * **L1 (Beginner):** B2B vs B2C cross-border tax treatment rules, mandatory invoice reverse-charge citations in 3 languages.
  * **L2 (Intermediate):** VIES API batch validation, triangulation trade mechanics (*třístranný obchod*), OSS quarterly returns calculation.
  * **L3 (Production Master):** Complex cross-border software/SaaS licensing taxation, transfer pricing documentation, input VAT deduction apportionment for mixed exempt/taxable activities.

---

### 🏥 VI. Clinical Medicine, Surgery & Emergency Triage

> [!CAUTION]
> **Clinical AI Notice:** These skills are engineered for clinical decision support, medical education, differential diagnosis structuring, and triage evaluation. They do not replace hands-on medical examination.

#### 16. [`clinical-cardiology-surgery`](clinical-cardiology-surgery/SKILL.md)
* **Domain:** Clinical Cardiology, Cardiac Surgery & Hemodynamics
* **Core Framework:** 12-lead ECG systematic interpretation, ESC Arterial Hypertension guidelines, Coronary Artery Disease (CAD / STEMI / NSTEMI), Heart Failure GDMT (4 pillars: ARNI/ACEi, Beta-blocker, MRA, SGLT2i), Post-CABG / Valve replacement monitoring.
* **References:** [`references/ecg_interpretation_and_acs_pathway.md`](clinical-cardiology-surgery/references/ecg_interpretation_and_acs_pathway.md)
* **Tiered Mastery:**
  * **L1 (Beginner):** ECG axis calculation, normal intervals (PR, QRS, QTc), AHA/ESC blood pressure stage classification.
  * **L2 (Intermediate):** Localizing acute myocardial infarction on 12-lead ECG (Anterior, Inferior, Lateral, Posterior), Heart Failure ejection fraction categorization (HFrEF, HFmrEF, HFpEF).
  * **L3 (Production Master):** Post-cardiotomy hemodynamic instability triage, cardiac tamponade diagnosis (Beck's triad, pulsus paradoxus), malignant ventricular arrhythmia management protocols.

#### 17. [`internal-medicine-hematology`](internal-medicine-hematology/SKILL.md)
* **Domain:** Internal Medicine, Hematology & Biochemical Panels
* **Core Framework:** Complete Blood Count (CBC) with differential, Anemia diagnostic algorithm (Microcytic MCV <80, Normocytic, Macrocytic MCV >100), Coagulation panels (INR, aPTT, D-dimer, Fibrinogen), Liver enzymes (ALT, AST, ALP, GGT), Renal markers (eGFR CKD-EPI, Creatinine), Biomarkers (CRP, Procalcitonin).
* **References:** [`references/lab_reference_ranges_quickref.md`](internal-medicine-hematology/references/lab_reference_ranges_quickref.md)
* **Tiered Mastery:**
  * **L1 (Beginner):** Normal laboratory reference ranges, basic metabolic panel interpretation.
  * **L2 (Intermediate):** Microcytic anemia differential (Iron deficiency vs Thalassemia vs Anemia of Chronic Disease via Ferritin/TIBC), acute kidney injury staging (KDIGO).
  * **L3 (Production Master):** Disseminated Intravascular Coagulation (DIC) scoring, heparin-induced thrombocytopenia (4Ts score), acute pancreatitis severity stratification.

#### 18. [`neurology-neurosurgery-triage`](neurology-neurosurgery-triage/SKILL.md)
* **Domain:** Neurology, Acute Neurosurgical Emergencies & Stroke Care
* **Core Framework:** Acute Ischemic Stroke protocol (FAST, NIHSS scale, IV tPA 4.5h window, Mechanical Thrombectomy 6-24h window), Intracranial Pressure (ICP) management, Traumatic Brain Injury (Epidural vs Subdural vs Subarachnoid hematoma), Cranial nerve palsy localization, SNOOP4 red-flag headache triage.
* **References:** [`references/stroke_fast_and_nihss_scale.md`](neurology-neurosurgery-triage/references/stroke_fast_and_nihss_scale.md)
* **Tiered Mastery:**
  * **L1 (Beginner):** FAST stroke screening, cranial nerves I–XII functional testing, Glasgow Coma Scale (GCS) calculation.
  * **L2 (Intermediate):** NIHSS stroke scoring, distinguishing ischemic stroke vs hemorrhagic stroke on non-contrast head CT, SNOOP4 secondary headache screening.
  * **L3 (Production Master):** Cushing's triad recognition for impending herniation, hyperosmolar therapy dosing (Mannitol / 3% Hypertonic Saline), emergency status epilepticus refractory protocols.

#### 19. [`ophthalmology-vision-care`](ophthalmology-vision-care/SKILL.md)
* **Domain:** Ophthalmology, Vision Diagnostics & Ocular Emergencies
* **Core Framework:** Slit lamp examination, Intraocular Pressure (IOP) management, Open-angle vs Acute Angle-Closure Glaucoma, Retinal pathology (Diabetic / Hypertensive Retinopathy, Retinal Detachment warning signs), Age-related Macular Degeneration (AMD: Dry vs Wet), Cataracts, Dry Eye Syndrome (OSDI, Tear Break-Up Time).
* **References:** [`references/ophthalmic_emergencies_checklist.md`](ophthalmology-vision-care/references/ophthalmic_emergencies_checklist.md)
* **Tiered Mastery:**
  * **L1 (Beginner):** Visual acuity notation (Snellen), basic eye anatomy, conjunctivitis differential (viral vs bacterial vs allergic).
  * **L2 (Intermediate):** Acute red eye diagnostic tree, fundoscopic evaluation of hypertensive retinopathy grades I-IV, diabetic macular edema evaluation.
  * **L3 (Production Master):** Acute Angle-Closure Glaucoma emergency cocktail protocol (Timolol, Acetazolamide, Pilocarpine, Mannitol), Central Retinal Artery Occlusion (CRAO) immediate triage, chemical eye burn immediate decontamination.

#### 20. [`orthopedics-knee-rehab`](orthopedics-knee-rehab/SKILL.md)
* **Domain:** Orthopedic Surgery, Knee Joint Pathology & Rehabilitation Protocols
* **Core Framework:** Knee biomechanics and ligamentous anatomy, Clinical diagnostic tests (Lachman, Pivot Shift, Anterior/Posterior Drawer, McMurray, Thessaly, Patellar Apprehension), Meniscal tears, ACL/PCL reconstruction, Gonarthrosis (Kellgren-Lawrence Grades 1-4), Injections (PRP, Hyaluronic acid, Corticosteroids), Phase-based post-op rehab protocols.
* **References:** [`references/knee_rehabilitation_exercises_guide.md`](orthopedics-knee-rehab/references/knee_rehabilitation_exercises_guide.md)
* **Tiered Mastery:**
  * **L1 (Beginner):** Knee joint anatomical landmarks, ROM measurement, basic RICE protocol for acute sprains.
  * **L2 (Intermediate):** Step-by-step performance of Lachman and McMurray tests, Kellgren-Lawrence radiographic grading, conservative injection therapy indications.
  * **L3 (Production Master):** ACL postoperative return-to-sport testing (LSI >90%, Y-balance), surgical repair vs meniscectomy decision tree, total knee arthroplasty (TKA) rehabilitation complications (arthrofibrosis, DVT).

---

## 🚀 How to Install and Activate These Skills

### Option A. Google Antigravity (Local / Global)

#### 1. Global Installation (Recommended — Available to all workspaces):
Clone or copy the `skills` folder into your global Gemini/Antigravity configuration:
```bash
# Linux / macOS
git clone https://github.com/GinCz/AI.git /tmp/GinCz_AI
cp -r /tmp/GinCz_AI/skills/* ~/.gemini/config/skills/
rm -rf /tmp/GinCz_AI
```

```powershell
# Windows PowerShell
$tmp = Join-Path $env:TEMP "GinCz_AI"
git clone https://github.com/GinCz/AI.git $tmp
Copy-Item -Path "$tmp\skills\*" -Destination "$env:USERPROFILE\.gemini\config\skills\" -Recurse -Force
Remove-Item -Path $tmp -Recurse -Force
```

#### 2. Project-Level Workspace:
Inside any active workspace, place the skills into:
```
<your-project>/.gemini/skills/<skill-name>/SKILL.md
```

---

### Option B. Cursor, Windsurf & VS Code (AI IDEs)

1. Clone or download the repository into your development directory:
   ```bash
   git clone https://github.com/GinCz/AI.git
   ```
2. Reference the skill directly in `.cursorrules` or `.vscode/settings.json`:
   ```json
   {
     "ai.instructions": "Refer to skills located in ./skills/ for domain-specific tasks. Read the corresponding SKILL.md before execution."
   }
   ```
3. To invoke a skill in chat, mention the file: `@skills/cyber-defense-pentest/SKILL.md`.

---

### Option C. Claude (Anthropic Projects & Workbench)

1. Open your **Project** in [Claude.ai](https://claude.ai).
2. Go to **Project Knowledge**.
3. Upload the target `SKILL.md` (and files from `references/`) as project files.
4. Add this to Project Custom Instructions:
   > *"When performing tasks related to [Domain], strictly follow the guidelines and checklists defined in the uploaded SKILL.md file."*

---

### Option D. ChatGPT / Custom GPTs (OpenAI)

1. Go to **My GPTs ➔ Create a GPT ➔ Configure**.
2. Under **Knowledge**, upload the desired `SKILL.md` files.
3. In **Instructions**, add:
   > *"You have expert skills attached in your knowledge base. When a user asks about cybersecurity, DevOps, automotive diagnostics, Czech law, or clinical medicine, search and follow the exact instructions in the respective SKILL.md file."*

---

## 🌐 Direct Raw Links for Headless AI Fetching

Autonomous AI agents can fetch any skill directly at runtime using `curl` or `fetch`:

* **Master Index:** `https://raw.githubusercontent.com/GinCz/AI/main/skills/README.md`
* **DevOps Engineering:** `https://raw.githubusercontent.com/GinCz/AI/main/skills/devops-cloud-engineering/SKILL.md`
* **Network & SysAdmin:** `https://raw.githubusercontent.com/GinCz/AI/main/skills/sysadmin-network-engineering/SKILL.md`
* **Server Hardening:** `https://raw.githubusercontent.com/GinCz/AI/main/skills/server-hardening-zerotrust/SKILL.md`
* **Cyber Defense & Pentest:** `https://raw.githubusercontent.com/GinCz/AI/main/skills/cyber-defense-pentest/SKILL.md`
* **Endpoint & Mobile:** `https://raw.githubusercontent.com/GinCz/AI/main/skills/endpoint-mobile-security/SKILL.md`
* **Auto Electronics:** `https://raw.githubusercontent.com/GinCz/AI/main/skills/auto-electronics-diagnostics/SKILL.md`
* **Auto Mechanics:** `https://raw.githubusercontent.com/GinCz/AI/main/skills/auto-mechanics-powertrain/SKILL.md`
* **Czech Tax & Accounting:** `https://raw.githubusercontent.com/GinCz/AI/main/skills/czech-accounting-tax/SKILL.md`
* **Czech Business Law:** `https://raw.githubusercontent.com/GinCz/AI/main/skills/czech-business-law/SKILL.md`
* **EU Business & AI Act:** `https://raw.githubusercontent.com/GinCz/AI/main/skills/eu-business-law-compliance/SKILL.md`
* **EU VAT Accounting:** `https://raw.githubusercontent.com/GinCz/AI/main/skills/eu-vat-accounting/SKILL.md`
* **Cardiology & Surgery:** `https://raw.githubusercontent.com/GinCz/AI/main/skills/clinical-cardiology-surgery/SKILL.md`
* **Internal Medicine:** `https://raw.githubusercontent.com/GinCz/AI/main/skills/internal-medicine-hematology/SKILL.md`
* **Neurology & Triage:** `https://raw.githubusercontent.com/GinCz/AI/main/skills/neurology-neurosurgery-triage/SKILL.md`
* **Ophthalmology:** `https://raw.githubusercontent.com/GinCz/AI/main/skills/ophthalmology-vision-care/SKILL.md`
* **Orthopedics Rehab:** `https://raw.githubusercontent.com/GinCz/AI/main/skills/orthopedics-knee-rehab/SKILL.md`

---

## 📄 License & Attribution
All skills in this directory are open-source and released under the **MIT License**.  
Maintained by **Vladimir Bulantsev ([GinCz ↗](https://github.com/GinCz))** as part of the [GinCz/AI ↗](https://github.com/GinCz/AI) master enterprise ecosystem.
