---
name: czech-pohoda-accounting-operations
description: >-
  Operational workflows, XML automation, chart of accounts, VAT control statement reconciliation, and financial closing procedures for the Czech Stormware POHODA accounting software.
---
# Stormware POHODA ERP: Operational Bookkeeping & Automation

A specialized operational manual for executing bookkeeping, invoicing, XML data transformations, bank reconciliation, VAT reporting, and year-end closing within the Czech Stormware POHODA accounting ecosystem.

---

## 1. POHODA Architecture & Data Exchange (XML Interface)

### A. Core Directory Structure & Windows Environment:
- Standard paths on dedicated accounting servers:
  - Database root: `C:\Program Files (x86)\Stormware\Pohoda\Data\` (MDB file for POHODA Standard/Profi, Microsoft SQL Server for POHODA SQL/E1).
  - XML Exchange folders: `...\Data\XML\Input\` and `...\Data\XML\Output\`.
- **Command-Line Silent Automation (`pohoda.exe`)**:
  ```powershell
  # Run automated XML import of invoices into POHODA in batch mode
  & "C:\Program Files (x86)\Stormware\Pohoda\Pohoda.exe" /XML "C:\Accounting\Batch\invoice_import.xml" /CONFIG "C:\Accounting\Batch\pohoda_config.ini"
  ```

### B. Standard POHODA XML Invoicing Structure:
```xml
<?xml version="1.0" encoding="utf-8"?>
<dat:dataPack id="PACK_2026_001" ico="12345678" application="CustomERP" version="2.0" 
              note="Import Issued Invoices" xmlns:dat="http://www.stormware.cz/schema/version_2/data.xsd" 
              xmlns:inv="http://www.stormware.cz/schema/version_2/invoice.xsd" 
              xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">
  <dat:dataPackItem id="INV_1079" version="2.0">
    <inv:invoice version="2.0">
      <inv:invoiceHeader>
        <inv:invoiceType>issuedInvoice</inv:invoiceType>
        <inv:number>
          <typ:numberRequested>2026001079</typ:numberRequested>
        </inv:number>
        <inv:symVar>2026001079</inv:symVar>
        <inv:date>2026-10-07</inv:date>
        <inv:dateTax>2026-10-07</inv:dateTax>
        <inv:dateDue>2026-10-21</inv:dateDue>
        <inv:text>IT Consultancy & Infrastructure Engineering</inv:text>
        <inv:partnerIdentity>
          <typ:address>
            <typ:company>EU Partner S.r.l.</typ:company>
            <typ:country>
              <typ:ids>ITA</typ:ids>
            </typ:country>
            <typ:vatId>IT12345678901</typ:vatId>
          </typ:address>
        </inv:partnerIdentity>
        <inv:classificationVAT>
          <!-- Reverse Charge EU services § 24a / Souhrnné hlášení code 3 -->
          <typ:ids>UDslEU</typ:ids>
        </inv:classificationVAT>
      </inv:invoiceHeader>
      <inv:invoiceDetail>
        <inv:invoiceItem>
          <inv:text>DevOps & Cloud Engineering Services</inv:text>
          <inv:quantity>1</inv:quantity>
          <inv:unit>hours</inv:unit>
          <inv:homeCurrency>
            <typ:unitPrice>25000</typ:unitPrice>
          </inv:homeCurrency>
        </inv:invoiceItem>
      </inv:invoiceDetail>
    </inv:invoice>
  </dat:dataPackItem>
</dat:dataPack>
```

---

## 2. Chart of Accounts (*Účtový rozvrh*) & Posting Rules for s.r.o.

### Standard Account Classes & Typical Journal Entries:
| Class | Account | Description | Debit (MD) | Credit (D) | Business Context |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0** | `022 / 082` | Tangible Assets & Depreciation | `551` | `082` | Monthly asset depreciation ($> 80\text{k CZK}$) |
| **2** | `221` | Bank Account (Fio, ČSOB) | `221` | `311` | Client invoice payment received |
| **2** | `221` | Bank Account | `321` | `221` | Supplier invoice payment sent |
| **3** | `311` | Trade Receivables (*Odběratelé*) | `311` | `602` | Issued invoice for services |
| **3** | `321` | Trade Payables (*Dodavatelé*) | `518 / 501`| `321` | Received invoice for hosting / software |
| **3** | `343` | Value Added Tax (DPH) | `343` | `321` | Input VAT on domestic purchases |
| **3** | `343` | Value Added Tax (DPH) | `311` | `343` | Output VAT on domestic sales (21%) |
| **3** | `331 / 336`| Wages & Social/Health Insurance | `521 / 524`| `331 / 336`| Monthly payroll obligations |
| **5** | `563` | Foreign Exchange Loss | `563` | `311 / 321`| Negative exchange difference at settlement |
| **6** | `663` | Foreign Exchange Gain | `311 / 321`| `663` | Positive exchange difference at settlement |

---

## 3. Bank Statement Automation & Pairing (*Homebanking*)

1. **Format Standards**:
   - ABO format (`.gpc`) or Fio XML bank statement format.
2. **Automated Pairing Algorithm in POHODA**:
   - POHODA pairs incoming and outgoing transactions against open invoices based on:
     1. **Variabilní symbol (VS)**: Primary unique key. Must strictly match invoice number.
     2. **Amount**: Currency and exact sum matching.
     3. **Counterparty Bank Account**: Pairing against saved Address Book accounts.
3. **Internal Transfers & Transit Account (`261 - Peníze na cestě`)**:
   - Never post cash withdrawals or bank-to-bank transfers directly between two bank accounts (`221_1` to `221_2`). Always route through transit account `261`:
     - Bank 1 outflow: `MD 261 / D 221_1`
     - Bank 2 inflow: `MD 221_2 / D 261`
   - Balance on account `261` must equal zero at closing.

---

## 4. VAT & Control Statement Audit (*Členění DPH a Kontrolní hlášení*)

### POHODA VAT Classification Codes Matrix:
- `UD`: Domestic supply with standard VAT 21% $\rightarrow$ DPH return line 1, Kontrolní hlášení section **A.4** (if $> 10,000\text{ CZK}$) or **A.5** (if $\le 10,000\text{ CZK}$).
- `PD`: Domestic purchase with VAT credit $\rightarrow$ DPH return line 40, Kontrolní hlášení section **B.2** ($> 10,000\text{ CZK}$) or **B.3** ($\le 10,000\text{ CZK}$).
- `UDslEU`: Supply of service to an EU VAT-registered business under Reverse Charge (§ 24a ZDPH) $\rightarrow$ DPH return line 21, **Souhrnné hlášení code 3**. Zero domestic VAT.
- `PDP`: Local Reverse Charge in the Czech Republic (§ 92a ZDPH: construction work, IT hardware wholesale $> 100\text{k CZK}$) $\rightarrow$ DPH return line 25, Kontrolní hlášení section **A.1 / B.1**.

---

## 5. Month-End & Year-End Closing Protocol (*Účetní uzávěrka*)

1. **Foreign Exchange Revaluation as of December 31**:
   - All foreign currency accounts (EUR, USD in Fio banka) and unpaid foreign receivables/payables must be revalued using the Czech National Bank (ČNB) fixing rate published on December 31 (§ 24 odst. 6 Act on Accounting).
2. **Accruals & Deferrals (*Časové rozlišení*)**:
   - Costs of future periods (`381 - Náklady příštích období`): Annual software licenses, domain hosting, or insurance paid in advance for the next year.
   - Accrued revenue (`385 - Příjmy příštích období`): Work delivered in current year but invoiced in January.
3. **Inventory & Fixed Asset Depreciation**:
   - Execute annual tax depreciation run (*Daňové odpisy*) and compare against accounting depreciation (*Účetní odpisy*). Difference booked as tax adjustment in the Corporate Tax Return (DPPO).
