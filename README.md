# Procure-to-Pay (P2P) 3-Way Match and Accounts Payable Exceptions Tracker

## 1. Project Overview

The Procure-to-Pay (P2P) 3-Way Match and Accounts Payable (AP) Exceptions Tracker is a finance and operations analytics project designed to analyze and monitor the invoice validation process within the Procure-to-Pay cycle.

The project applies the 3-way matching principle to compare:

1. Purchase Orders (PO)
2. Goods Receipt Notes (GRN)
3. Vendor Invoices

The primary objective is to identify invoice exceptions, quantify financial discrepancies, analyze vendor and process performance, and provide actionable insights to improve Accounts Payable controls and operational efficiency.

---

## 2. Business Problem

Accounts Payable teams process a large volume of supplier invoices. Manual invoice validation can result in errors, delayed processing, duplicate payments, and financial discrepancies.

Common issues include:

* Quantity mismatches between invoices and goods receipts
* Price discrepancies between purchase orders and invoices
* Missing purchase orders
* Missing goods receipt records
* Duplicate invoices
* Incorrect invoice values
* Invoice processing delays
* Vendor-related discrepancies
* Potential financial leakage

A structured 3-way matching process helps organizations identify these exceptions before invoices are approved and paid.

This project demonstrates how Excel and Python can be used to analyze transaction-level procurement and Accounts Payable data and develop an exception-management framework.

---

## 3. Project Objectives

The key objectives of the project are:

* Automate the comparison of Purchase Orders, Goods Receipts and Vendor Invoices.
* Identify invoices that successfully pass the 3-way matching process.
* Detect quantity mismatches.
* Detect price mismatches.
* Identify duplicate invoices.
* Identify invoices with missing Purchase Orders.
* Identify invoices with missing Goods Receipts.
* Calculate invoice matching and exception rates.
* Analyze vendor-level performance.
* Identify high-value exceptions.
* Analyze Accounts Payable processing performance.
* Develop an exception tracking framework.
* Generate business insights and recommendations.

---

## 4. Procure-to-Pay Process

The project follows the standard Procure-to-Pay process:

```text
Purchase Requisition
        |
        v
Purchase Order
        |
        v
Goods / Services Received
        |
        v
Goods Receipt Note
        |
        v
Vendor Invoice
        |
        v
3-Way Matching
        |
        +------------------+
        |                  |
        v                  v
    Matched             Exception
        |                  |
        v                  v
Invoice Approval     Exception Review
        |                  |
        v                  v
     Payment          Resolution
                           |
                           v
                       Closure
```

---

## 5. What is 3-Way Matching?

3-way matching is an Accounts Payable control used to verify whether a vendor invoice agrees with the corresponding Purchase Order and Goods Receipt.

The three documents are:

### Purchase Order

Defines what the organization agreed to purchase, including:

* Item
* Quantity
* Unit price
* Vendor
* Purchase order value

### Goods Receipt

Confirms what was actually received, including:

* Quantity received
* Receipt date
* Purchase Order reference
* Item information

### Vendor Invoice

Represents what the vendor is requesting payment for, including:

* Invoice number
* Invoice quantity
* Invoice price
* Invoice value
* Purchase Order reference

An invoice is considered matched when the required validation conditions are satisfied within the defined business tolerance.

---

## 6. Example of 3-Way Matching

| Field       | Purchase Order |  Goods Receipt | Vendor Invoice |
| ----------- | -------------: | -------------: | -------------: |
| Quantity    |            100 |            100 |            100 |
| Unit Price  |            500 | Not Applicable |            500 |
| Total Value |         50,000 | Not Applicable |         50,000 |

Matching result:

```text
Purchase Order Match: PASS
Quantity Match: PASS
Price Match: PASS
Value Validation: PASS

Final Status: MATCHED
```

If the vendor invoice contains 110 units while only 100 units were received, the transaction would be classified as an exception.

---

## 7. Exception Categories

The project identifies and classifies Accounts Payable exceptions into several categories.

### 7.1 Quantity Mismatch

Occurs when the invoice quantity differs from the received quantity.

```text
Invoice Quantity != Received Quantity
```

### 7.2 Price Mismatch

Occurs when the invoice unit price differs from the Purchase Order unit price.

```text
Invoice Unit Price != PO Unit Price
```

### 7.3 Missing Purchase Order

Occurs when an invoice cannot be matched to a valid Purchase Order.

### 7.4 Missing Goods Receipt

Occurs when an invoice exists but the corresponding Goods Receipt has not been recorded.

### 7.5 Duplicate Invoice

Occurs when the same invoice is recorded more than once for the same vendor or transaction.

### 7.6 Value Mismatch

Occurs when the calculated invoice value differs from the expected transaction value.

### 7.7 Multiple Exceptions

Occurs when an invoice contains more than one exception type.

---

## 8. Dataset Structure

The project uses structured transaction-level data representing a typical Procure-to-Pay environment.

### Purchase Orders

Typical fields include:

```text
PO_ID
PO_Date
Vendor_ID
Vendor_Name
Item_ID
Item_Description
Ordered_Quantity
Unit_Price
PO_Value
Currency
Department
```

### Goods Receipts

Typical fields include:

```text
GRN_ID
GRN_Date
PO_ID
Vendor_ID
Item_ID
Received_Quantity
Receipt_Status
```

### Vendor Invoices

Typical fields include:

```text
Invoice_ID
Invoice_Date
PO_ID
Vendor_ID
Vendor_Name
Item_ID
Invoice_Quantity
Invoice_Unit_Price
Invoice_Value
Payment_Terms
Invoice_Status
```

---

## 9. 3-Way Matching Methodology

The matching process evaluates each vendor invoice against the corresponding Purchase Order and Goods Receipt.

### Purchase Order Validation

```text
Invoice PO ID = Purchase Order PO ID
```

### Quantity Validation

```text
Invoice Quantity = Received Quantity
```

The project can apply predefined quantity tolerances where appropriate.

### Price Validation

```text
Invoice Unit Price = PO Unit Price
```

The project can apply predefined price tolerances where appropriate.

### Invoice Value Validation

```text
Expected Value = Matched Quantity × PO Unit Price
```

The final transaction status is classified as:

```text
MATCHED
```

or

```text
EXCEPTION
```

depending on the validation results.

---

## 10. Key Performance Indicators

The project calculates several Accounts Payable performance indicators.

### Total Invoices

Total number of invoices processed during the analysis period.

### Matched Invoices

Number of invoices that successfully passed the defined matching criteria.

### Exception Invoices

Number of invoices that failed one or more validation conditions.

### Match Rate

```text
Match Rate =
Matched Invoices / Total Invoices × 100
```

### Exception Rate

```text
Exception Rate =
Exception Invoices / Total Invoices × 100
```

### Exception Value

```text
Exception Value =
Sum of the financial value associated with exception transactions
```

### Average Invoice Processing Time

```text
Processing Time =
Invoice Approval Date - Invoice Receipt Date
```

### Duplicate Invoice Rate

```text
Duplicate Rate =
Duplicate Invoices / Total Invoices × 100
```

---

## 11. Analysis Performed

### 11.1 Overall Exception Analysis

The project evaluates:

* Total invoices
* Matched invoices
* Exception invoices
* Match rate
* Exception rate
* Total exception value

### 11.2 Exception Type Analysis

Exceptions are analyzed based on:

* Quantit
