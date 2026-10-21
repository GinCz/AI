# 🤖 Production System Prompts Catalog for External LLMs

> **Ready-to-Use System Prompts Library:** 26 Specialized Expert Domains  
> **Purpose:** Instant transfer of deep domain skills into standalone LLMs (ChatGPT Custom GPTs, Claude Projects, DeepSeek, LLaMA, Mistral).  
> **Format:** Pure, self-contained instruction text decoupled from local filesystem paths or proprietary tools.  
> *Repository:* [GitHub: GinCz/AI ↗](https://github.com/GinCz/AI) | *Author:* [Vladimir Bulantsev (@GinCz) ↗](https://github.com/GinCz) | *Version:* v2026-10-21

---

## 🧭 Navigation & Directory Table

| # | Domain / Category | Master Prompt Name | Prompt File (Ready-to-Use) | Baseline Skill (Antigravity/Agent) |
| :-: | :--- | :--- | :--- | :--- |
| 01 | **Czech Accounting & Taxes** | Czech Accounting, Taxation & Reporting Expert | [`01_CZECH_ACCOUNTING_TAX_PROMPT.md` ↗](01_CZECH_ACCOUNTING_TAX_PROMPT.md) | [`czech-accounting-tax` ↗](../czech-accounting-tax/SKILL.md) |
| 02 | **Czech Legal & Compliance** | Czech Corporate, Business & Contract Law Expert | [`02_CZECH_BUSINESS_LAW_PROMPT.md` ↗](02_CZECH_BUSINESS_LAW_PROMPT.md) | [`czech-business-law` ↗](../czech-business-law/SKILL.md) |
| 03 | **EU VAT & Pan-European Tax** | EU VAT, Cross-Border Taxation & Pan-European Accounting Expert | [`03_EU_VAT_ACCOUNTING_PROMPT.md` ↗](03_EU_VAT_ACCOUNTING_PROMPT.md) | [`eu-vat-accounting` ↗](../eu-vat-accounting/SKILL.md) |
| 04 | **EU Legal & Compliance** | EU Business Law, Regulatory Compliance & AI Governance Expert | [`04_EU_BUSINESS_LAW_COMPLIANCE_PROMPT.md` ↗](04_EU_BUSINESS_LAW_COMPLIANCE_PROMPT.md) | [`eu-business-law-compliance` ↗](../eu-business-law-compliance/SKILL.md) |
| 05 | **DevOps & Cloud Engineering** | Principal DevOps & Cloud Infrastructure Engineer | [`05_DEVOPS_CLOUD_ENGINEERING_PROMPT.md` ↗](05_DEVOPS_CLOUD_ENGINEERING_PROMPT.md) | [`devops-cloud-engineering` ↗](../devops-cloud-engineering/SKILL.md) |
| 06 | **SysAdmin & Networking** | Senior Systems Administrator & Network Engineering Expert | [`06_SYSADMIN_NETWORK_ENGINEERING_PROMPT.md` ↗](06_SYSADMIN_NETWORK_ENGINEERING_PROMPT.md) | [`sysadmin-network-engineering` ↗](../sysadmin-network-engineering/SKILL.md) |
| 07 | **Server Hardening & Compliance** | Enterprise Server Hardening, Zero Trust & PCI DSS Compliance Architect | [`07_SERVER_HARDENING_ZEROTRUST_PROMPT.md` ↗](07_SERVER_HARDENING_ZEROTRUST_PROMPT.md) | [`server-hardening-zerotrust` ↗](../server-hardening-zerotrust/SKILL.md) |
| 08 | **Cybersecurity & Pentesting** | Offensive Security, Penetration Testing & Threat Hunting Specialist | [`08_CYBER_DEFENSE_PENTEST_PROMPT.md` ↗](08_CYBER_DEFENSE_PENTEST_PROMPT.md) | [`cyber-defense-pentest` ↗](../cyber-defense-pentest/SKILL.md) |
| 09 | **Endpoint & Mobile Security** | Endpoint, Workstation, Laptop & Mobile Security Hardening Specialist | [`09_ENDPOINT_MOBILE_SECURITY_PROMPT.md` ↗](09_ENDPOINT_MOBILE_SECURITY_PROMPT.md) | [`endpoint-mobile-security` ↗](../endpoint-mobile-security/SKILL.md) |
| 10 | **Automotive Engineering** | Master Automotive Mechanical Engineer & Powertrain Specialist | [`10_AUTO_MECHANICS_POWERTRAIN_PROMPT.md` ↗](10_AUTO_MECHANICS_POWERTRAIN_PROMPT.md) | [`auto-mechanics-powertrain` ↗](../auto-mechanics-powertrain/SKILL.md) |
| 11 | **Automotive Electronics & EV** | Master Automotive Electrical, Network Diagnostics & EV Systems Specialist | [`11_AUTO_ELECTRONICS_DIAGNOSTICS_PROMPT.md` ↗](11_AUTO_ELECTRONICS_DIAGNOSTICS_PROMPT.md) | [`auto-electronics-diagnostics` ↗](../auto-electronics-diagnostics/SKILL.md) |
| 12 | **Clinical Medicine & Cardiology** | Consultant Cardiologist & Cardiac Surgery Specialist | [`12_CLINICAL_CARDIOLOGY_SURGERY_PROMPT.md` ↗](12_CLINICAL_CARDIOLOGY_SURGERY_PROMPT.md) | [`clinical-cardiology-surgery` ↗](../clinical-cardiology-surgery/SKILL.md) |
| 13 | **Orthopedics & Sports Medicine** | Consultant Orthopedic Surgeon & Knee Rehabilitation Specialist | [`13_ORTHOPEDICS_KNEE_REHAB_PROMPT.md` ↗](13_ORTHOPEDICS_KNEE_REHAB_PROMPT.md) | [`orthopedics-knee-rehab` ↗](../orthopedics-knee-rehab/SKILL.md) |
| 14 | **Ophthalmology & Vision Care** | Consultant Ophthalmologist & Ophthalmic Surgeon | [`14_OPHTHALMOLOGY_VISION_CARE_PROMPT.md` ↗](14_OPHTHALMOLOGY_VISION_CARE_PROMPT.md) | [`ophthalmology-vision-care` ↗](../ophthalmology-vision-care/SKILL.md) |
| 15 | **Internal Medicine & Diagnostics** | Consultant Physician in Internal Medicine, Hematology & Clinical Diagnostics | [`15_INTERNAL_MEDICINE_HEMATOLOGY_PROMPT.md` ↗](15_INTERNAL_MEDICINE_HEMATOLOGY_PROMPT.md) | [`internal-medicine-hematology` ↗](../internal-medicine-hematology/SKILL.md) |
| 16 | **Neurology & Emergency Triage** | Consultant Neurologist, Neurosurgeon & Emergency Neuro-Triage Specialist | [`16_NEUROLOGY_NEUROSURGERY_TRIAGE_PROMPT.md` ↗](16_NEUROLOGY_NEUROSURGERY_TRIAGE_PROMPT.md) | [`neurology-neurosurgery-triage` ↗](../neurology-neurosurgery-triage/SKILL.md) |
| 17 | **Russian Accounting & Taxes** | Russian Accounting, Taxation & Tax Audit Defense Expert | [`17_RU_ACCOUNTING_TAX_PROMPT.md` ↗](17_RU_ACCOUNTING_TAX_PROMPT.md) | [`ru-accounting-tax` ↗](../ru-accounting-tax/SKILL.md) |
| 18 | **Russian Legal & Corporate** | Russian Civil, Commercial & Corporate Law Expert | [`18_RU_CIVIL_CORPORATE_LAW_PROMPT.md` ↗](18_RU_CIVIL_CORPORATE_LAW_PROMPT.md) | [`ru-civil-corporate-law` ↗](../ru-civil-corporate-law/SKILL.md) |
| 19 | **Russian Litigation & Defense** | Russian Litigation, Trial Advocacy & Debt Enforcement Expert | [`19_RU_LITIGATION_ADVOCACY_PROMPT.md` ↗](19_RU_LITIGATION_ADVOCACY_PROMPT.md) | [`ru-litigation-advocacy` ↗](../ru-litigation-advocacy/SKILL.md) |
| 20 | **Czech Litigation & Enforcement** | Czech Litigation, Judicial Procedure & Advocacy Expert | [`20_CZECH_LITIGATION_ADVOCACY_PROMPT.md` ↗](20_CZECH_LITIGATION_ADVOCACY_PROMPT.md) | [`czech-litigation-advocacy` ↗](../czech-litigation-advocacy/SKILL.md) |
| 21 | **EU & Cross-Border Litigation** | European Cross-Border Litigation, CJEU, ECtHR & Arbitration Expert | [`21_EU_LITIGATION_CROSSBORDER_LAW_PROMPT.md` ↗](21_EU_LITIGATION_CROSSBORDER_LAW_PROMPT.md) | [`eu-litigation-crossborder-law` ↗](../eu-litigation-crossborder-law/SKILL.md) |
| 22 | **International Contracts & IP** | International Contract Engineering & Cross-Border IP Expert | [`22_INTL_CONTRACT_DRAFTING_IP_PROMPT.md` ↗](22_INTL_CONTRACT_DRAFTING_IP_PROMPT.md) | [`intl-contract-drafting-ip` ↗](../intl-contract-drafting-ip/SKILL.md) |
| 23 | **Sanctions Compliance & AML** | Sanctions, AML/CFT & Crypto Regulatory Compliance Expert | [`23_COMPLIANCE_ANTI_SANCTIONS_AML_PROMPT.md` ↗](23_COMPLIANCE_ANTI_SANCTIONS_AML_PROMPT.md) | [`compliance-anti-sanctions-aml` ↗](../compliance-anti-sanctions-aml/SKILL.md) |
| 24 | **Bankruptcy & Restructuring** | Corporate Bankruptcy, Insolvency & Subsidiary Liability Defense Expert | [`24_BANKRUPTCY_INSOLVENCY_RESTRUCTURING_PROMPT.md` ↗](24_BANKRUPTCY_INSOLVENCY_RESTRUCTURING_PROMPT.md) | [`bankruptcy-insolvency-restructuring` ↗](../bankruptcy-insolvency-restructuring/SKILL.md) |
| 25 | **Allergology & Immunology** | Consultant Allergist & Clinical Immunologist | [`25_ALLERGOLOGY_CLINICAL_IMMUNOLOGY_PROMPT.md` ↗](25_ALLERGOLOGY_CLINICAL_IMMUNOLOGY_PROMPT.md) | [`allergology-clinical-immunology` ↗](../allergology-clinical-immunology/SKILL.md) |
| 26 | **Proctology & Colorectal Surgery** | Consultant Proctologist & Colorectal Surgeon | [`26_PROCTOLOGY_COLORECTAL_SURGERY_PROMPT.md` ↗](26_PROCTOLOGY_COLORECTAL_SURGERY_PROMPT.md) | [`proctology-colorectal-surgery` ↗](../proctology-colorectal-surgery/SKILL.md) |

---

## 🚀 How to Deploy in 30 Seconds

1. Open any prompt file from the table above.
2. Click **Copy** on the code block containing the System Prompt.
3. Paste into your target platform:
   - **ChatGPT Custom GPT:** Paste into the **Instructions** box in the GPT Builder.
   - **Claude Projects:** Paste into the **Project Custom Instructions** box.
   - **ChatGPT / Claude Global Settings:** Paste into **Custom Instructions** ("How would you like the model to respond?").
   - **Terminal / Web Chat:** Paste as the very first message in a fresh session.
