import pandas as pd
from pathlib import Path
D=Path(__file__).resolve().parents[1]/"data"; m=pd.read_csv(D/"three_way_match_results.csv"); inv=pd.read_csv(D/"supplier_invoices.csv"); p=(m.Match_Status=="PASS").mean()
print(f"Invoices: {len(m):,}"); print(f"Pass rate: {p:.2%}"); print(f"Exception rate: {1-p:.2%}"); print(f"Invoice value: INR {inv.Invoice_Total.sum():,.2f}"); print(f"Potential overbilling: INR {m.Potential_Overbilling.sum():,.2f}")
