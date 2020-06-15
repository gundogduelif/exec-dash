## dashboard_generator.py
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)  


valid_ids = 201801 #The infinite loop REFERENCE : https://www.tutorialspoint.com/python/python_while_loop.htm
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
        

filename = "sales-201801.csv"   # Read csv file into a pandas dataframe object REFERENCE: https://github.com/prof-rossetti/intro-to-python/blob/master/exercises/monthly-sales-reporting/pandas_solution_further.py
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
print(f"TOTAL MONTHLY SALES: {to_usd(monthly_total)}")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
for d in top_sellers:
    print("  " + str(d["rank"]) + ") " + d["name"] +
          ": " + to_usd(d["monthly_sales"]))



#Bar Chart REFERENCE: # 1) #https://www.youtube.com/watch?v=eMOA1pPVUc4

product_group = reportsales.groupby(["product"])
quantity_ordered = product_group.sum()["sales price"]
keys = [pair for pair, reportsales in product_group]
plt.title("JANUARY 2018 TOP SELLING  PRODUCTS")
plt.bar(keys, quantity_ordered)

plt.ylabel("Sales in USD ($)")
plt.xlabel("Products")
for i in range(len(quantity_ordered)):
    plt.annotate(to_usd(quantity_ordered[i]), xy=(keys[i],quantity_ordered[i])) #Annotate REFERENCE: https://stackoverflow.com/questions/28931224/adding-value-labels-on-a-matplotlib-bar-chart

plt.xticks(keys, rotation='vertical', size=8)
plt.show()
