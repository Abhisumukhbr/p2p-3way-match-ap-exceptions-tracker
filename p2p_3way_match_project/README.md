# Procure-to-Pay 3-Way Match & AP Exceptions Tracker

## Excel + Python portfolio project

### Business problem
Accounts Payable should not approve a PO-backed invoice until the ordered, received and billed quantities/prices reconcile within approved tolerances. Enterprise systems document this as three-way matching. Microsoft describes it as comparing invoice pricing with the purchase order and invoice quantity with product receipts; SAP and Oracle document similar matching and exception concepts.

### Important data disclosure
A complete public PO + GRN + invoice ERP dataset is uncommon. Public resources such as DocILE contain real business-document invoice/order benchmarks, while government procurement portals expose purchase orders/contracts, but they do not provide a universal linked PO→GRN→invoice dataset. Therefore the transaction tables in this repository are **synthetic ERP-style data**, generated with seed 42, and are not claimed to be real company financial records. The project uses public sources for domain validation and can be extended with public invoice documents.

### Included dataset
- 40 vendors
- 80 SKUs
- 2,500 purchase orders
- ~2,400+ supplier invoices
- 2,500 goods receipts
- three-way match output
- exception tracker

### Matching controls
1. PO existence
2. Invoice unit price within ±2% of PO price
3. Invoice quantity <= received quantity
4. GRN required
5. Duplicate vendor + amount pattern
6. Exception owner and priority
7. Potential overbilling exposure

The 2% tolerance is a project assumption, not a universal accounting rule. Production thresholds should be approved by Finance/Procurement.

### Workbook
`reports/P2P_3Way_Match_AP_Exceptions.xlsx` contains Dashboard, masters, PO, GRN, Invoice, Match Results, Exceptions and Sources/Notes.

### Run Python
```bash
pip install -r requirements.txt
python src/match_engine.py
python src/kpi_report.py
```

### GitHub resume bullets
- Built an end-to-end Procure-to-Pay three-way match control comparing PO, GRN and supplier-invoice data to identify price, quantity, missing-receipt and duplicate-payment exceptions.
- Developed a Python matching engine with configurable tolerance rules, exception classification, ownership routing and potential overbilling exposure.
- Created an Excel AP dashboard covering match rate, exception rate, root cause, invoice exposure and exception aging.
- Designed a reproducible ERP-style dataset with 2,500 POs, 40 vendors and 80 SKUs using documented enterprise AP matching concepts.

### Interview answer
**Problem:** AP payment can be delayed or exposed to overbilling when ordered, received and invoiced quantities/prices do not agree.

**Solution:** Join PO, GRN and invoice records; calculate price/quantity variances; apply tolerance rules; classify and route exceptions; quantify exposure.

**Business value:** stronger payment controls, faster exception ownership, better auditability and visibility into vendor/receiving issues.

### Public references
- Microsoft Dynamics 365 AP invoice matching: https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/accounts-payable-invoice-matching
- SAP Concur three-way matching rules: https://help.sap.com/docs/concur-invoice/concur-invoice-professional-edition-tools-guides/exceptions-and-three-way-matching-rules
- Oracle matching approval levels: https://docs.oracle.com/en/cloud/saas/procurement/26b/oapro/match-approval-level-options.html
- DocILE invoice/order benchmark: https://docile.rossum.ai/
- Data.gov purchase-order datasets: https://catalog.data.gov/dataset/purchase-orders-and-contracts

### Future enhancements
Power BI, SQL, fuzzy invoice matching, OCR extraction, vendor risk scoring, process mining, SAP/Oracle field mapping and automated exception emails.
