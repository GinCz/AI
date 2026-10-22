---
name: czech-real-estate-utilities-property
description: >-
  Operational workflows and legal reference for Czech real estate, property management, energy utilities (ČEZ, Innogy), SVJ governance, land registry (Katastr nemovitostí), property taxation (Daň z nemovitých věcí), and mortgage administration.
---
# Czech Real Estate, Energy Utilities, SVJ & Property Governance

A master operational and legal manual for managing residential and commercial real estate in the Czech Republic, navigating utility contracts (ČEZ, gas, water), governing homeowners' associations (SVJ), securing rights in the Land Registry (Katastr nemovitostí), and complying with property taxation.

---

## 1. Energy Utilities Management (ČEZ, Plyn, Elektřina)

### A. Core Technical & Contractual Identifiers:
- **EAN (European Article Number for Electricity)**: 18-digit unique code identifying the electricity consumption point (*odběrné místo - OM*).
- **EIC (Energy Identification Code for Gas)**: 16-character alphanumeric code identifying the gas consumption point.
- **Zákaznické číslo & Variabilní symbol (VS)**: Account pairing identifiers for billing and monthly prepayments (*zálohy*).
- **Distribution Rate (*Distribuční sazba*)**:
  - `D02d`: Standard residential rate for lighting, appliances, without electric heating/boiler.
  - `D25d / D57d`: Dual-tariff rates (high tariff VT / low tariff NT - *noční proud*) for electric water heating (boiler) or heat pumps (*tepelné čerpadlo*). Requires ripple control receiver (*HDO - hromadné dálkové ovládání*).

### B. Bill Auditing & Prepayment Optimization (*Vyúčtování a zálohy*):
1. **Annual Reconciliation (*Roční vyúčtování*)**:
   - Check invoiced meter readings (*počáteční a koncový stav měřidla*) against physical meter photos.
   - Differentiate between **regulated prices** set by the Energy Regulatory Office (*Energetický regulační úřad - ERÚ*: distribution fee, system services, OZE renewables surcharge) and **unregulated commodity prices** set by the supplier (MWh price + fixed monthly fee).
2. **Prepayment Adjustments (*Optimalizace záloh*)**:
   - In periods of reduced income or vacancy, immediately lower monthly prepayments via the ČEZ ON-LINE portal to the statutory minimum required by historical consumption.
3. **Supplier Switching & Fixed vs Spot Contracts**:
   - Notice period for indefinite contracts: 3 months starting from the 1st day of the next calendar month (§ 11a Energetický zákon č. 458/2000 Sb.).
   - Fixed-term contracts (*smlouva na dobu určitou*): Termination before term incurs contractual penalties unless exiting upon price increase (§ 11a odst. 4).

---

## 2. SVJ Governance & Community Living (NOZ §§ 1158–1222)

### A. Legal Structure of Společenství vlastníků jednotek (SVJ):
- **Statutory Bodies**: Committee (*Výbor SVJ*) or Professional Chairman (*Předseda SVJ*). Highest body is the General Assembly (*Shromáždění vlastníků*).
- **Bylaws (*Stanovy SVJ*)**: Primary governing document defining common parts of the building, quorum rules, and voting shares based on unit floor area ratio (*podlahová plocha jednotky*).
- **Voting Mechanism**:
  - Standard decisions: Absolute majority of votes of present owners at a quorate assembly ($\ge 50\%$ of all shares present).
  - Voting outside meeting (*Per rollam* - § 1210 NOZ): Written ballot within a statutory deadline (typically 15–30 days). Non-response is considered a negative vote.

### B. Financial Obligations & Service Billing (*Vyúčtování služeb*):
1. **Long-Term Advance / Repair Fund (*Fond oprav / Dlouhodobá záloha*)**:
   - Contributions per square meter. Non-refundable upon unit sale; transfers to the new owner.
   - Right to audit: Every owner has the enforceable right under § 1179 NOZ to inspect SVJ bank statements, accounting books, and contractor invoices.
2. **Annual Service Cost Allocation (Act No. 67/2013 Sb. & Decree No. 269/2015 Sb.)**:
   - Delivery deadline: Landlord/SVJ must deliver annual service reconciliation by **April 30** of the following year.
   - Financial settlement deadline: Payment of surpluses or arrears (*přeplatky/nedoplatky*) is due by **August 31**.
   - Heating allocation: Split into basic component (*základní složka* 30–50% by area) and consumption component (*spotřební složka* 50–70% by heat cost allocators / RTN). Penalty for late delivery: **50 CZK per day of delay** (§ 13 Act 67/2013 Sb.).

---

## 3. Land Registry Administration (Katastr nemovitostí - Act No. 256/2013 Sb.)

### A. Ownership Verification & Encumbrances (List vlastnictví - LV):
- **Part A**: Property owners and ownership share ratios.
- **Part B**: Real estate descriptions (land parcel number, building number, apartment unit number).
- **Part C (Encumbrances / Omezení vlastnického práva)**:
  - *Zástavní právo smluvní*: Bank mortgage lien.
  - *Věcné břemeno / Služebnost*: Easements (utility passage, right of way *právo cesty*, lifelong dwelling rights *výměnek*).
  - *Zákaz zcizení a zatížení*: Negative pledge prohibiting sale or encumbrance without bank consent.
- **Part D**: Notes and ongoing proceedings (*Plomba* - indicates active pending registry change).

### B. Registry Filings (Návrh na vklad do katastru):
- Administrative filing fee: **2 000 CZK** per proposal via official electronic form or paper.
- Mandatory 20-day statutory protection period (*ochranná lhůta*): Katastrální úřad cannot register rights earlier than 20 days after notifying the registered owner, preventing fraudulent conveyances.

---

## 4. Property Taxation (Daň z nemovitých věcí - Act No. 338/1992 Sb.)

### A. Annual Tax Filing & Deadlines:
- **Tax Return Deadline**: **January 31** of the tax year following the year of acquisition or alteration of parameters (e.g. extension, change of land type).
- **Payment Deadline**: **May 31** (or split in two equal installments due May 31 and November 30 if tax exceeds 5 000 CZK).
- **Calculation Mechanism**:
  $$\text{Tax} = \text{Base Area } (m^2) \times \text{Statutory Rate} \times \text{Municipality Coefficient } (1.0–4.5) \times \text{Local Municipal Coefficient } (1–5)$$
  (Municipalities like Nupaky set specific local coefficients determining the final bill).

---

## 5. Mortgage Restructuring & Financial Distress Defense

### A. Consumer Credit Act Protections (Act No. 257/2016 Sb. o spotřebitelském úvěru):
1. **End of Fixation Period (*Konec fixace*)**:
   - The bank must communicate new interest rates and conditions at least 3 months prior to the end of the fixation period.
   - Right to repay in full or refinance to another bank **completely free of charge** within the refixation window.
2. **Extraordinary Prepayments (*Mimořádné splátky*)**:
   - Every borrower has the statutory right to repay up to **25% of the total loan principal free of penalties** within one month prior to each anniversary of the credit agreement.
   - In difficult life situations (death, permanent disability, or severe illness of borrower or spouse), full early repayment without penalty is guaranteed by law.
3. **Hardship Restructuring with the Bank**:
   - If faced with job loss, proactively submit a formal request for loan restructuring *before* missing payments:
     - Request temporary deferral of principal (*odklad splátek jistiny*) paying only interest for 3–6 months.
     - Request loan term extension (e.g. extending from 20 to 30 years to minimize monthly cash outflow).
