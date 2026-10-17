---
name: eu-business-law-compliance
description: >-
  Operational reference and compliance frameworks for EU business law, Single Market freedoms, GDPR regulations, EU AI Act, NIS2 cybersecurity directive, DSA/DMA, AML/CFT rules (FAÚ, sanctions, KYC/UBO), and European consumer protection directives.
---
# EU Business Law, Digital Regulations & Compliance (Právo EU a regulatorní rámec)

An operational framework for enterprise compliance, risk management, and commercial operations across the European Union Single Market.

---

## 1. European Union Legal Architecture

### Primary vs. Secondary Legislation:
- **Primary Law**: Treaty on European Union (**TEU**), Treaty on the Functioning of the European Union (**TFEU**), and the Charter of Fundamental Rights.
- **Secondary Law**:
  - **Regulations (*Nařízení*)**: Directly applicable in their entirety across all 27 Member States without requiring national transposition (e.g. GDPR, EU AI Act, DSA, DMA, DORA).
  - **Directives (*Směrnice*)**: Binding as to the result to be achieved, but require transposition into national statutory law by each Member State (e.g. NIS2, Omnibus Directive, VAT Directive).
  - **Decisions (*Rozhodnutí*)**: Binding in their entirety upon those to whom they are addressed.
- **Fundamental Judicial Doctrines**:
  - **Supremacy of EU Law (*Přednost unijního práva*)**: Established in *Costa v. ENEL* (Case 6/64); national laws conflicting with EU law must be set aside by national courts.
  - **Direct Effect (*Přímý účinek*)**: Established in *Van Gend en Loos* (Case 26/62); individuals can enforce clear, precise, and unconditional EU rights directly before national courts.

### The Four Fundamental Freedoms:
1. **Free Movement of Goods**: Prohibition of customs duties, quantitative restrictions, and equivalent measures (Articles 34–36 TFEU).
2. **Freedom to Provide Services (Services Directive 2006/123/EC)**: Cross-border temporary provision of services without requiring a local branch or establishment.
3. **Free Movement of Capital**: Prohibition of restrictions on payments and capital transfers between Member States and with third countries (Article 63 TFEU).
4. **Free Movement of Workers & Posting of Workers (Directive 96/71/EC & 2018/957/EU)**: Requires obtaining an **A1 Certificate** from national social security administrations (e.g. ČSSZ) and observing host country core labor conditions (minimum wage, health and safety).

---

## 2. General Data Protection Regulation (GDPR - Regulation (EU) 2016/679)

### Core Principles of Processing (Article 5):
- **Lawfulness, Fairness & Transparency**: Clear communication of data collection.
- **Purpose Limitation**: Collected only for specified, explicit, and legitimate purposes.
- **Data Minimisation**: Adequate, relevant, and limited to what is strictly necessary.
- **Accuracy**: Keeping data up to date, deleting inaccuracies without delay.
- **Storage Limitation**: Retained only as long as necessary for the processing purpose.
- **Integrity and Confidentiality**: Ensuring appropriate technical and organizational security (encryption, access control).
- **Accountability**: The data controller must be able to demonstrate compliance.

### Legal Bases for Processing (Article 6):
1. **Consent (*Souhlas*)**: Unbundled, freely given, specific, informed, and unambiguous. Must be as easy to withdraw as to give.
2. **Contractual Necessity (*Plnění smlouvy*)**: Necessary for entering into or performing a contract.
3. **Legal Obligation (*Právní povinnost*)**: Complying with statutory law (e.g. tax record retention, accounting acts).
4. **Vital Interests (*Životní zájmy*)**: Protecting life or physical integrity.
5. **Public Interest (*Veřejný zájem*)**: Exercising official authority.
6. **Legitimate Interests (*Oprávněný zájem*)**: Must be supported by a documented **Legitimate Interest Assessment (LIA - Balanční test)** balancing controller interests against individual rights.

### Mandatory Compliance Documentation:
- **Privacy Policy (*Zásady ochrany osobních údajů*)**: Public-facing notice complying with Articles 13 & 14.
- **Data Processing Agreement (DPA - Article 28)**: Mandatory contract with all third-party processors (hosting providers, SaaS, CRMs, payroll agencies).
- **Records of Processing Activities (ROPA - Article 30)**: Internal ledger of data categories, purposes, recipients, and retention periods.
- **Data Protection Impact Assessment (DPIA - Article 35)**: Mandatory before launching high-risk processing (large-scale automated profiling, surveillance, biometric data).

### International Data Transfers (Chapter V):
- **Adequacy Decisions**: Transfers permitted to approved countries (e.g. UK, Switzerland, Japan, Israel).
- **EU-US Data Privacy Framework (DPF)**: Transfers to US certified companies permitted under adequacy decision.
- **Standard Contractual Clauses (SCCs)**: European Commission pre-approved model clauses required when transferring data to non-adequate third countries, accompanied by a **Transfer Impact Assessment (TIA)**.

### Data Breach Management (Articles 33 & 34):
- **72-Hour Clock**: Must formally report any personal data breach to the national supervisory authority (in CZ: *Úřad pro ochranu osobních údajů - ÚOOÚ*) within **72 hours** of becoming aware.
- **Data Subject Notification**: Mandatory without undue delay if the breach poses a high risk to the rights and freedoms of natural persons.
- **Statutory Fines**: Up to **€20,000,000** or **4% of global annual turnover**, whichever is higher.

---

## 3. European Tech, AI & Cybersecurity Legislation

### A. The EU AI Act (Regulation (EU) 2024/1689):
The world's first comprehensive legal framework on Artificial Intelligence:
1. **Prohibited AI Practices (Article 5)**: Unacceptable risk; strictly banned:
   - Subliminal manipulative techniques distorting behavior causing harm.
   - Social scoring systems evaluating trustworthiness.
   - Real-time remote biometric identification in publicly accessible spaces for law enforcement (with narrow exceptions).
   - Biometric categorization deducing race, political opinions, trade union membership, or sexual orientation.
2. **High-Risk AI Systems (Articles 6 & Annex III)**:
   - AI used in critical infrastructure, recruitment/HR management, credit evaluation, educational assessment, biometric identification.
   - **Obligations**: Risk management system, high-quality training datasets, detailed technical documentation, automatic event logging, human oversight mechanisms, accuracy and cybersecurity resilience, CE marking, and registration in the EU database.
3. **General Purpose AI (GPAI) Models**:
   - Technical documentation, summary of training data copyright compliance, cooperation with the European AI Office.
   - Systemic risk GPAI models (cumulative compute > $10^{25}$ FLOPs) subject to model evaluations, adversarial testing (red-teaming), and incident reporting.
4. **Minimal/Limited Risk AI Transparency**:
   - Disclosing that content was generated or manipulated by AI (deepfakes, synthetic audio/video).
   - Informing users when they are interacting with an AI system (chatbots).

### B. NIS2 Directive (Directive (EU) 2022/2555 - Cybersecurity):
- **Entities Covered**: Divided into **Essential Entities** (*Základní subjekty*) and **Important Entities** (*Důležité subjekty*) across critical sectors: IT service providers, cloud computing, data centers, telecoms, energy, healthcare, banking, transport.
- **Core Requirements**:
  - Risk analysis, incident handling, business continuity (backup management, disaster recovery).
  - Supply chain security (auditing suppliers and software dependencies).
  - Cryptography and access control policies.
- **Incident Notification Timeline**:
  - **Early Warning**: Within **24 hours** of becoming aware of a significant incident.
  - **Incident Notification**: Within **72 hours** (initial assessment and severity).
  - **Final Report**: Within **1 month** detailing root cause and mitigation.
- **Direct Management Liability**: Corporate directors and executives can be held personally liable for gross negligence in failing to implement cybersecurity measures, including temporary bans from executive management.

### C. Digital Services Act (DSA) & Digital Markets Act (DMA):
- **DSA (Regulation (EU) 2022/2065)**: Liability exemptions for online intermediaries, illegal content takedown procedures, transparency in recommender algorithms, prohibition of dark patterns in UI.
- **DMA (Regulation (EU) 2022/1925)**: Ex-ante antitrust rules for systemic "gatekeeper" platforms (interoperability, self-preferencing bans, fair data access).

---

## 4. Anti-Money Laundering (AML / CFT) & Sanctions Compliance

Governed by EU AML Directives (5AMLD, 6AMLD), the new EU AML Regulation, and the Czech **AML Act (*Zákon č. 253/2008 Sb.*)**:
- **Obliged Entities (*Povinné osoby*)**: Credit institutions, payment institutions, accountants, tax advisors, auditors, notaries, lawyers in transactional matters, real estate agents, art dealers, and crypto asset service providers (CASPs under MiCA).
- **Customer Due Diligence (CDD / KYC)**:
  - Identification and verification of the client's identity before transaction execution (mandatory for transactions over €1,000 or upon suspicion).
  - **Ultimate Beneficial Owner (UBO / *Skutečný majitel*)**: Verifying physical persons owning or controlling > 25% of capital/voting rights.
  - **Politically Exposed Persons (PEP)**: Enhanced due diligence for individuals holding public political office and their family members.
  - **Source of Funds (*Původ finančních prostředků*)**: Establishing legitimate commercial or personal origins.
- **Sanctions Screening**: Mandatory real-time screening against the **EU Consolidated Financial Sanctions List** and international sanctions regimes (freeze of assets, prohibition of making funds available).
- **Mandatory Reporting of Suspicious Transactions (*Oznámení podezřelého obchodu*)**: Obliged entities must report suspicious transactions to the **Financial Analytical Office (*Finanční analytický úřad - FAÚ*)** without delay.

---

## 5. European Consumer Protection & E-Commerce

Governed by the Consumer Rights Directive (2011/83/EU) and the **Omnibus Directive ((EU) 2019/2161)**:
- **14-Day Right of Withdrawal (*Právo na odstoupení od smlouvy bez udání důvodu*)**:
  - Consumers shopping online have 14 days from receipt of goods to withdraw without penalty.
  - Exceptions: Custom-made products, sealed hygiene products once opened, digital content if consumer explicitly waived withdrawal rights upon immediate download commencement.
- **Price Transparency & Discounts (Article 6a)**:
  - Any announced price reduction (e.g. "Sale -30%") must clearly state the **lowest price applied by the seller during the preceding 30 days** (*historická nejnižší cena za posledních 30 dní*).
- **Verified Customer Reviews**:
  - Commercial sellers must disclose whether and how they ensure that published product reviews originate from consumers who actually purchased or used the product. Publishing unverified or fake reviews is treated as an aggressive unfair commercial practice.
- **Statutory Conformity Guarantee (Directive (EU) 2019/771)**:
  - Mandatory statutory 2-year guarantee for consumer goods.
  - Any defect that becomes apparent within **1 year** (in many states extended to 2 years) of delivery is legally presumed to have existed at the time of delivery unless proven otherwise by the seller.
