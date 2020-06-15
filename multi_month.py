import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np


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


# 1) & 2) Which months have the highest & lowest sales?

all_data["month"] = all_data["date"].str[6]
results = all_data.groupby("month").sum()

sales_total = all_data["sales price"].sum()
month_total = all_data["month"].sum()

months = range(1,4)
plt.title("THE HIGHEST SALES")
plt.bar(months, results["sales price"], color='y')
plt.ylabel("Sales in USD ($)")
plt.xlabel("Months")
for i in range(len(results["sales price"])):
    plt.annotate(to_usd(results["sales price"][i]), xy=(months[i],results["sales price"][i]))
plt.xticks(months, rotation='horizontal', size=8)
plt.show()

# 3)What is the trend of sales over time?










#top_sellers = []
#rank = 1
#for i, row in product_totals.iterrows():
#    d = {"rank": rank, "name": row.name, "monthly_sales": row["sales price"]}
#    top_sellers.append(d)
#    rank = rank + 1
#
#
#print("-----------------------")
#print(f"TOTAL MONTHLY SALES: {to_usd(monthly_total)}")
#
#print("-----------------------")
#print("TOP SELLING PRODUCTS:")
#for d in top_sellers:
#    print("  " + str(d["rank"]) + ") " + d["name"] +
#          ": " + to_usd(d["monthly_sales"]))
#
#month	qty	       total
#jan    250 	 $12,928.86 
#feb    241 	 $12,005.81 
#march	266 	 $12,000.71 

#total   757 	 $36,935.38 

# 1) Which months have the highest sales?
# 2) Which months have the lowest sales? 

#monthly_total = all_data["sales price"].sum()
#
#product_totals = all_data.groupby(["product"]).sum()
#product_totals = product_totals.sort_values("sales price", ascending=False)

#product_group = reportsales.groupby(["product"])
#quantity_ordered = product_group.sum()["sales price"]
#keys = [pair for pair, reportsales in product_group]
#plt.title("TOP SELLING  PRODUCTS")
#plt.bar(keys, quantity_ordered)
#
#plt.ylabel("Sales in USD ($)")
#plt.xlabel("Products")
#for i in range(len(quantity_ordered)):
#    plt.annotate(to_usd(quantity_ordered[i]), xy=(keys[i],quantity_ordered[i]))
#
#plt.xticks(keys, rotation='vertical', size=8)
#plt.show()