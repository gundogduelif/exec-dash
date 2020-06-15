## dashboard_generator.py
import pandas as pd
import os
import matplotlib.pyplot as plt
## utility function to convert float or integer to usd-formatted string (for printing)
def to_usd(my_price):
    return "${0:,.2f}".format(my_price)  # > $12,000.71


valid_ids = 201801                      #The Infinite Loop REFERENCE : https://www.tutorialspoint.com/python/python_while_loop.htm
var = 1     
while var == 1 :
    try:
        report_id = int(input("Please enter a valid report number:"))
        if report_id == valid_ids:
            #report_ids.append(report_id)
            print("REPORT NUMBER IS APPROVED!")  
            break
    except ValueError:
        print("Please make sure to enter a number! Try again!")
        

filename = "sales-201801.csv"
csv_filepath = os.path.join("data", filename)
reportsales = pd.read_csv(csv_filepath)
print(reportsales.head())

monthly_total = reportsales["sales price"].sum()
product_totals = reportsales.groupby(["product"]).sum()
product_totals = product_totals.sort_values("sales price", ascending=False)

top_sellers = []
rank = 1
for i, row in product_totals.iterrows():
    d = {"rank": rank, "name": row.name, "monthly_sales": row["sales price"]}
    top_sellers.append(d)
    rank += + 1

print("-----------------------")
print("MONTH: JANUARY 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print(f"TOTAL MONTHLY SALES: {to_usd(monthly_total)}")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
for d in top_sellers:
    print("  " + str(d["rank"]) + ") " + d["name"] +
          ": " + to_usd(d["monthly_sales"]))