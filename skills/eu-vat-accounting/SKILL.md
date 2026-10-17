---
name: eu-vat-accounting
description: >-
  Operational guidelines and checklists for EU VAT Directives, cross-border B2B/B2C transactions, Reverse Charge mechanism, One Stop Shop (OSS/IOSS), Identifikovaná osoba status, VIES validation, DAC7, and pan-European financial standards (IFRS, local GAAP, Transfer Pricing).
---
# EU VAT, Cross-Border Transactions & Pan-European Accounting

A comprehensive operational manual for navigating the European Union Value Added Tax system, cross-border digital and physical trade, and European financial reporting standards.

---

## 1. European Union VAT Architecture

The European VAT system is harmonized under:
- **Council Directive 2006/112/EC** (The EU VAT Directive): Sets the baseline for taxable persons, taxable transactions, place of supply, tax exemptions, and rates.
- **Council Implementing Regulation (EU) No 282/2011**: Uniform application of place of supply rules for telecommunications, broadcasting, and electronic services.
- **Council Directive 2020/285/EU**: Modernized SME scheme allowing cross-border VAT exemptions for small businesses.
- **ViDA Initiative (VAT in the Digital Age)**: Introduction of digital reporting requirements, mandatory e-invoicing for cross-border B2B transactions, and single VAT registration.

---

## 2. Czech Implementation & Status Categories

In the Czech Republic, the EU VAT Directive is enacted through the **Act on Value Added Tax** (*Zákon č. 235/2004 Sb., o dani z přidané hodnoty - ZDPH*).

### Business Categories:
1. **Neplátce DPH (Non-VAT Registered)**:
   - Turnover under **2,000,000 CZK** in 12 consecutive calendar months (§ 6 ZDPH).
   - Invoices without VAT, cannot deduct input VAT on domestic business purchases.
2. **Plátce DPH (Full VAT Payer)**:
   - Compulsory registration upon crossing the 2,000,000 CZK threshold (application due within 10 days after the end of the month in which the limit was exceeded).
   - Voluntary registration allowed (subject to proving economic activity).
   - Charges VAT on domestic sales, deducts input VAT (*odpočet na vstupu*), files monthly/quarterly VAT return and *Kontrolní hlášení*.
3. **Identifikovaná osoba (Identified Person - § 6g to § 6i ZDPH)**:
   - Essential category for Czech digital businesses, freelancers, and small entities not registered for domestic VAT.
   - **Trigger 1 (§ 6g)**: Acquisition of goods from another EU member state exceeding 326,000 CZK/year.
   - **Trigger 2 (§ 6h)**: Purchase of services with place of supply in CZ from an EU or non-EU foreign provider (e.g. Google Workspace, Meta Ads, OpenAI, AWS, Stripe, GitHub, Hetzner, Adobe).
   - **Trigger 3 (§ 6i)**: Provision of cross-border B2B services to a customer in another EU member state under § 9 odst. 1 (where the customer pays tax under reverse charge).
   - **Operating Rules for Identifikovaná osoba**:
     - Remains a **non-VAT payer domestically** (invoices domestic Czech clients without VAT).
     - Receives a Czech VAT ID (`CZ...`).
     - Files a VAT return **only in the months** when an EU/foreign cross-border service was acquired, and pays 21% VAT to the Czech Financial Office (with no right to input tax deduction).
     - Files a *Souhrnné hlášení* (Recapitulative statement) only in the months when services were provided to an EU business.

---

## 3. Cross-Border B2B Supply & Reverse Charge

### The General Rule for Services (B2B):
- **Article 44 of the EU VAT Directive / § 9 odst. 1 ZDPH**:
  > The place of supply of services to a taxable person (business) is the place where that person has established their business.
- **Result**: The transaction is not taxed in the supplier's country. Tax liability shifts entirely to the customer.

### Operational Reverse Charge Checklist:
1. **Mandatory VIES Verification**:
   - Check the customer's VAT ID in the official European Commission VIES database: `https://ec.europa.eu/taxation_customs/vies/`
   - Store or print the VIES validation certificate (with timestamp and consultation number) in your accounting records.
2. **Invoice Requirements (Directive 2010/45/EU)**:
   - Must show the supplier's full name, address, and VAT ID.
   - Must show the customer's full name, address, and valid EU VAT ID.
   - **Mandatory Reverse Charge Clause**:
     - English: *"Invoice subject to the VAT Reverse Charge mechanism pursuant to Article 196 of Council Directive 2006/112/EC. VAT to be accounted for by the recipient."*
     - Czech: *"Daň odvede zákazník dle § 9 odst. 1 a § 92a zákona č. 235/2004 Sb. (Reverse charge - přenesená daňová povinnost)."*
   - Net amount only (0% VAT shown on the invoice).
3. **Reporting via Souhrnné hlášení (EC Sales List)**:
   - Filed electronically by the **25th of the following month**.
   - Code **3**: Provision of services with place of supply in another Member State pursuant to Art. 44 / § 9 odst. 1.
   - Code **0**: Intra-Community supply of goods (*Dodání zboží do jiného členského státu*).

### Intra-Community Supply of Goods (B2B):
- **Article 138 EU VAT Directive / § 64 ZDPH**:
  - Supply of goods to a VAT-registered business in another Member State is **exempt with credit** (0% VAT).
  - **Condition**: The goods must physically leave the territory of the supplier's Member State and enter the customer's Member State.
  - **Burden of Proof (Implementing Regulation 2018/1912)**: At least two non-contradictory pieces of evidence prepared by independent parties (e.g. signed CMR consignment note, bill of lading, carrier tracking document, bank receipt).

---

## 4. Cross-Border B2C E-Commerce & The One Stop Shop (OSS)

For sales of goods and digital services to non-business consumers (B2C) across the European Union:

### Pan-European Distance Selling Threshold:
- **€10,000 / 256,000 CZK threshold**: Total cross-border B2C sales across all other 26 EU member states combined in a calendar year.
- **Below €10,000**: Seller may apply domestic VAT rates (e.g. Czech 21%) and pay to the home tax authority.
- **Above €10,000**: VAT must be charged at the **destination country's statutory rate** (e.g., 19% for Germany, 20% for France, 25% for Sweden).

### The One Stop Shop (OSS - Režim jednoho správního místa):
Eliminates the requirement to register for VAT in every individual EU destination country:
1. **Union Scheme (*Režim EU*)**:
   - Covers intra-EU distance sales of goods and B2C services.
   - Registration with the home tax authority (in CZ: Finanční úřad pro Jihomoravský kraj - Územní pracoviště Brno I).
   - Single quarterly electronic tax return filed by the end of the month following the calendar quarter.
   - Single quarterly payment in EUR to the home authority, which automatically redistributes funds to the destination Member States.
2. **Import Scheme (IOSS - *Dovozní režim*)**:
   - Covers distance sales of goods imported from third countries (outside the EU) in consignments with an intrinsic value not exceeding **€150**.
   - Simplifies customs clearance; VAT is collected directly at checkout and remitted monthly via IOSS.

---

## 5. European Platform Economy & DAC7

Under **Council Directive (EU) 2021/514 (DAC7)**:
- Digital platform operators (marketplaces, ride-hailing apps like Uber/Bolt, accommodation platforms like Airbnb/Booking, freelancing platforms) are legally obligated to collect and report annual seller earnings to EU tax administrations.
- **Data reported**: Seller identification, tax identification numbers (TIN/DIČ), bank account numbers, total gross remuneration paid, and transaction counts.
- **Automatic Exchange of Information**: The Czech Financial Administration automatically matches DAC7 data against reported DPFO/DPPO returns to detect undeclared income.

---

## 6. European Financial Reporting & Accounting Standards

### IFRS / IAS vs. European National GAAPs:
- **IFRS (International Financial Reporting Standards)**: Mandatory for consolidated financial statements of publicly listed companies across the EU (Regulation (EC) No 1606/2002); widely used by large cross-border corporate groups.
- **Core Pan-European Accounting Principles**:
  1. **True and Fair View (*Věrný a poctivý obraz*)**: Overriding qualitative standard.
  2. **Accrual Principle (*Akruální báze / Časové rozlišení*)**: Revenues and costs are recognized in the period they occur, not when cash is transferred:
     - Deferred expenses / accrued income (*Náklady / Příjmy příštích období*).
     - Accrued expenses / deferred income (*Výdaje / Výnosy příštích období*).
  3. **Prudence Principle (*Zásada opatrnosti*)**: Recognizing anticipated liabilities, foreseeable losses, and bad debt impairments (*opravné položky a rezervy*), while not recognizing anticipated profits.
  4. **Going Concern (*Předpoklad trvání podniku*)**: Valuation assumes the entity will continue operational activities for at least 12 months.

### Transfer Pricing within EU Corporate Groups:
- **Arm's Length Principle (§ 23 odst. 7 ZDP / OECD Guidelines)**:
  > Prices charged in commercial or financial transactions between associated enterprises (cross-border sister/parent entities) must reflect market prices that would have been agreed between independent entities under identical circumstances.
- **Documentation Standards**:
  - **Master File**: Overview of the global group, IP ownership, financial arrangements.
  - **Local File**: Detailed transactional analysis of local entity, functional and risk analysis (*funkční a riziková analýza*), selection of transfer pricing method (CUP, Cost Plus, Resale Price, TNMM).
  - Penalty for non-compliance: Unilateral retroactive tax base adjustments by tax authorities with 20% penalty and statutory interest on arrears.
