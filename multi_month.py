import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

def to_usd(my_price):   # REFERENCE: https://github.com/prof-rossetti/intro-to-python/blob/master/exercises/monthly-sales-reporting/pandas_solution_further.py
    return "${0:,.2f}".format(my_price)  # > $12,000.71


#Read more than one csv files into a pandas dataframe object REFERENCE: https://www.youtube.com/watch?v=eMOA1pPVUc4
files = [file for file in os.listdir('./data')] 
all_month_data = pd.DataFrame()

for file in files:
    df = pd.read_csv("./data/"+file)
    all_month_data = pd.concat([all_month_data, df])
all_month_data.to_csv("all_data.csv",index=False)  
all_data = pd.read_csv("all_data.csv")

#BAR CHART REFERENCE : https://www.youtube.com/watch?v=eMOA1pPVUc4
# Which months have the highest & lowest sales & sales trend?

# Expected to get: 
#month	qty	total
#jan	 250 	 $12,928.86 
#feb	 241 	 $12,005.81 
#march	 266 	 $12,000.71 
#total	 757 	 $36,935.38 


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