import pandas as pd
from pathlib import Path
D=Path(__file__).resolve().parents[1]/"data"
po=pd.read_csv(D/"purchase_orders.csv"); gr=pd.read_csv(D/"goods_receipts.csv"); inv=pd.read_csv(D/"supplier_invoices.csv")
idx=po.set_index("PO_ID"); rec=gr.groupby("PO_ID").Received_Qty.sum().to_dict(); seen=set(); out=[]
for _,x in inv.iterrows():
 issues=[]; p=idx.loc[x.PO_ID] if pd.notna(x.PO_ID) and x.PO_ID in idx.index else None; r=rec.get(x.PO_ID,0) if p is not None else 0
 if p is None: issues.append("MISSING_PO")
 else:
  if abs((x.Invoice_Unit_Price-p.PO_Unit_Price)/p.PO_Unit_Price)>.02: issues.append("PRICE_VARIANCE")
  if x.Invoice_Qty>r: issues.append("QTY_OVER_RECEIPT")
  if not x.GRN_ID or r==0: issues.append("MISSING_GRN")
 k=(x.Vendor_ID,round(x.Invoice_Total,2))
 if k in seen: issues.append("DUPLICATE_AMOUNT_VENDOR")
 seen.add(k); out.append({"Invoice_ID":x.Invoice_ID,"PO_ID":x.PO_ID,"GRN_ID":x.GRN_ID,"Vendor_ID":x.Vendor_ID,"Match_Status":"PASS" if not issues else "HOLD","Exception_Type":";".join(sorted(set(issues))) if issues else "CLEAN"})
pd.DataFrame(out).to_csv(D/"match_results_rebuilt.csv",index=False)
print(pd.DataFrame(out).Match_Status.value_counts())
