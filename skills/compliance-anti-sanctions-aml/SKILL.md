---
name: compliance-anti-sanctions-aml
description: >-
  International sanctions compliance (EU Council Regulations 833/2014 & 269/2014, US OFAC SDN/SSI lists, UK OFSI, 50-Percent Rule), Dual-Use export controls (Regulation 2021/821, EAR), Anti-Money Laundering and Counter-Terrorist Financing (AMLD5, AMLD6, AMLA, KYC/CDD, UBO registers), and cryptocurrency regulatory compliance (MiCA, CASP licensing, Travel Rule Regulation 2023/1113).
---
# Sanctions Compliance, Anti-Money Laundering (AML/CFT) & Crypto Regulation

An authoritative operational and regulatory reference for Chief Compliance Officers (CCO), Money Laundering Reporting Officers (MLRO), international trade lawyers, and financial institution risk managers.

---

## 1. Global Sanctions Regimes & Enforcement Architecture

Entities engaging in international trade, banking, and technology transfers operate under the jurisdiction of three overlapping sanctions authorities:

```
               [ Global Sanctions & Trade Enforcement ]
                                  |
     +----------------------------+----------------------------+
     |                            |                            |
[ European Union (EU) ]     [ United States (OFAC/BIS) ]   [ United Kingdom (OFSI) ]
 - Reg 833/2014 (Sectoral)    - SDN List (Blocked Persons)   - Sanctions and Anti-Money
 - Reg 269/2014 (Individual)  - Sectoral Sanctions (SSI)       Laundering Act 2018
 - AMLA Enforcement Hub       - Secondary Sanctions          - Consolidated List
```

### A. European Union Sanctions Architecture:
- **Council Regulation (EU) No 269/2014**: Asset freezes and prohibition on making funds or economic resources available directly or indirectly to listed individuals and entities.
- **Council Regulation (EU) No 833/2014**: Comprehensive sectoral restrictions:
  - Banking & financial transactions: Disconnection from SWIFT, prohibition on accepting deposits over 100,000 EUR from Russian nationals, prohibitions on transactions with the Central Bank of Russia.
  - Technology, industrial goods, and software bans: Dual-use goods, semiconductors, advanced electronics, enterprise management software (ERP, CRM, CAD).
  - Anti-Circumvention Rule (Article 12): Strict prohibition against knowingly and intentionally participating in activities the object or effect of which is to circumvent the prohibitions.
  - Mandatory "No-Russia" Clause (Article 12g): Exporters must contractually prohibit re-exportation of sensitive goods to Russia and include strict liquidated damages remedies.

### B. United States Sanctions (OFAC - Department of the Treasury):
- **Specially Designated Nationals (*SDN List*)**: All property and interests in property within US jurisdiction are blocked; US persons are prohibited from engaging in any transactions.
- **Secondary Sanctions**: Foreign financial institutions (FFI) and foreign companies risk being designated on the SDN list or cut off from the US correspondent banking system if they facilitate significant transactions with blocked persons or designated military-industrial sectors (Executive Order 14114).
- **Executive Orders & Sectoral Determinations**: Broad restrictions covering maritime transport, oil price caps ($60/barrel), mining, and technology.

---

## 2. The 50-Percent Rule & Corporate Control Test

A company that is not explicitly named on a sanctions list may nonetheless be legally blocked by operation of law:

### A. The OFAC 50-Percent Rule:
- Any entity owned in the aggregate, **directly or indirectly, 50 percent or more by one or more blocked persons** is considered blocked, regardless of whether the entity itself is designated by name.
- Ownership is **cumulative**: If Blocked Person A owns 25% and Blocked Person B owns 25%, the entity is 50% owned and automatically blocked.

### B. The European Union Ownership & Control Test:
Under EU Council guidelines and CJEU jurisprudence:
1. **Ownership Criterion**: 50% or more of the proprietary rights or majority interest held by a listed person.
2. **Control Criterion (Factual Control)**: Even if ownership is under 50%, an entity is deemed controlled and blocked if a listed person has:
   - The right or power to appoint or remove a majority of the board of directors or executive management.
   - The right to exercise a dominant influence pursuant to a contract or constitutional provision.
   - The power to manage or direct the company's financial or operational affairs (e.g. through nominee shareholders, close family relatives acting as proxies, or shadow directing).

---

## 3. Dual-Use Export Controls & Technology Transfer

Governed in the EU by **Regulation (EU) 2021/821** and in the US by the **Export Administration Regulations (EAR)**:

- **Dual-Use Goods Definition**: Items, software, and technology that can be used for both civil and military purposes, including items that can assist in the design, development, production, or use of nuclear, chemical, or biological weapons.
- **Classification & Control Lists**:
  - Export Control Classification Number (**ECCN**) under the Commerce Control List (CCL) or Annex I of EU Regulation 2021/821 (Category 0 to 9: Nuclear, Materials, Electronics, Computers, Telecommunications, Information Security, Sensors, Navigation, Aerospace).
- **Catch-All Clause**: Mandatory export authorization even for non-listed items if the exporter has been informed by authorities or has reason to know that the items may be intended for military end-use or weapons of mass destruction.
- **Know Your Customer (KYC) in Supply Chains**: Verification of ultimate consignee, end-use statements (EUS), and anti-diversion screening against denied persons lists.

---

## 4. Anti-Money Laundering & Counter-Terrorist Financing (AML/CFT)

Operating under the **Financial Action Task Force (FATF)** recommendations and the **EU AML Package (AMLD5, AMLD6 & AMLA)**:

### A. Customer Due Diligence (CDD) Protocols:
- **Simplified Due Diligence (SDD)**: Low-risk domestic public entities, listed companies.
- **Standard Due Diligence (CDD)**:
  - Identity verification of physical persons (government ID, proof of address).
  - Commercial entities: Verification of legal form, registration extract, articles of association, active management.
  - Identification of the **Ultimate Beneficial Owner (UBO)**: Every physical person who ultimately owns or controls more than **25%** of the shares, voting rights, or ownership interest in the legal entity.
- **Enhanced Due Diligence (EDD)**:
  - Mandatory for: (1) High-risk third countries on FATF black/grey lists, (2) Politically Exposed Persons (**PEP**) and their family members / close associates, (3) Cross-border correspondent banking relationships, (4) Complex or unusually large transactions with no clear economic purpose.
  - Requires: Source of Wealth (SoW) and Source of Funds (SoF) documentary evidence, senior management approval for onboarding, intensified ongoing monitoring.

### B. Obliged Entities & Reporting Obligations:
- Banks, payment institutions, crypto-asset providers, auditors, tax advisors, real estate brokers, and lawyers.
- Mandatory filing of **Suspicious Transaction Reports (STR / SAR)** to the national Financial Intelligence Unit (**FIU** / *FAU in Czechia*, *Rosfinmonitoring in RF*).
- **Prohibition of Tipping-Off**: Obliged entities and their employees are strictly prohibited from disclosing to the customer or third parties that a report has been filed or that a money laundering investigation is underway.

---

## 5. Cryptocurrency Regulation: MiCA & The EU Travel Rule

The European Union has established the world's first comprehensive regulatory framework for crypto-assets:

### A. Markets in Crypto-Assets Regulation (MiCA - Regulation (EU) 2023/1114):
- **Classification of Crypto-Assets**:
  1. *Asset-Referenced Tokens (ART)*: Tokens that purport to maintain a stable value by referencing multiple currencies, commodities, or other crypto-assets. Strict reserve and capital requirements.
  2. *Electronic Money Tokens (EMT)*: Stablecoins pegged to a single official currency (e.g. EUR, USD). Must be issued by authorized credit or electronic money institutions.
  3. *Utility Tokens & Other Crypto-Assets*: Require publication of an approved **Crypto-Asset White Paper**.
- **Crypto-Asset Service Providers (CASP)**:
  - Entities providing custody, exchange of crypto for fiat or other crypto, operation of trading platforms, and execution of orders.
  - Mandatory licensing and authorization by national competent authorities (e.g. ČNB in Czechia, BaFin in Germany, AMF in France) with EU-wide passporting rights.
  - Strict prudential requirements: Capital reserves (50k to 150k EUR), governance standards, segregation of client assets, IT security (DORA compliance).

### B. The EU Crypto Travel Rule (Regulation (EU) 2023/1113):
- Extends the traditional FATF wire transfer rules to transfers of crypto-assets.
- **Mandatory Information Transmission**: When executing a crypto transfer, the sending CASP must collect, verify, and immediately transmit to the receiving CASP:
  - Name of the originator (sender), originator's crypto wallet address, account number, physical address, national identity number or date/place of birth.
  - Name of the beneficiary (recipient) and beneficiary's wallet address.
- **Self-Hosted Wallets (Unhosted Wallets)**: For transfers exceeding **1,000 EUR** to/from unhosted wallets, CASPs are mandated to verify whether the wallet is effectively owned or controlled by the customer.
