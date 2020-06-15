import pandas as pd
import os
import matplotlib.pyplot as plt
## utility function to convert float or integer to usd-formatted string (for printing)
def to_usd(my_price):
    return "${0:,.2f}".format(my_price)  # > $12,000.71
#REFERENCE 1) https://www.youtube.com/watch?v=eMOA1pPVUc4

files = [file for file in os.listdir('./data')] 
all_month_data = pd.DataFrame()

for file in files:
    df = pd.read_csv("./data/"+file)
    all_month_data = pd.concat([all_month_data, df])
all_month_data.to_csv("all_data.csv",index=False)  
all_data = pd.read_csv("all_data.csv")
print(all_data.head())

monthly_total = all_data["sales price"].sum()

product_totals = all_data.groupby(["product"]).sum()

product_totals = product_totals.sort_values("sales price", ascending=False)


top_sellers = []
rank = 1
for i, row in product_totals.iterrows():
    d = {"rank": rank, "name": row.name, "monthly_sales": row["sales price"]}
    top_sellers.append(d)
    rank = rank + 1

print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print(f"TOTAL MONTHLY SALES: {to_usd(monthly_total)}")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
for d in top_sellers:
    print("  " + str(d["rank"]) + ") " + d["name"] +
          ": " + to_usd(d["monthly_sales"]))



