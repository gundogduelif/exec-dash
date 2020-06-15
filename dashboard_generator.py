## dashboard_generator.py
import pandas as pd
import os
import matplotlib.pyplot as plt
## utility function to convert float or integer to usd-formatted string (for printing)
def to_usd(my_price):
    return "${0:,.2f}".format(my_price)  # > $12,000.71
#
valid_ids = range(201801, 201804, 1)           #Range Approach REFERENCE: https://www.pythoncentral.io/pythons-range-function-explained/#:~:text=range()%20(and%20Python%20in,%2C%20but%20not%20including%2C%20stop%20.            
report_ids = []                       #The Infinite Loop REFERENCE : https://www.tutorialspoint.com/python/python_while_loop.htm
var = 1                
while var == 1 :
    try:
        report_id = int(input("Please report number from 201801 to 201803:"))
        if report_id in valid_ids:
           report_ids.append(report_id)
           break
        else:
            print("Please make sure to enter a valid report number!")
            break
           # while var == 1: 
            # report_id = int(input("Please report number from 201801 to 201803:")) 
             #if report_id in valid_ids:
               #report_ids.append(report_id)
             #else:
                 #print("Restart") 
                 #break        
    except ValueError:
        print("Invalid report number!Please try again!")
        break
print("REPORT NUMBERS INCLUDE:",(report_ids))


#valid_ids = range (1, 21, 1)           #Range Approach REFERENCE: https://www.pythoncentral.io/pythons-range-function-explained/#:~:text=range()%20(and%20Python%20in,%2C%20but%20not%20including%2C%20stop%20.            
#product_ids = []                       #The Infinite Loop REFERENCE : https://www.tutorialspoint.com/python/python_while_loop.htm
#var = 1                
#while var == 1 :     
# report_id = input('Please input report number from 201801 to 201803:')
#  if report_id == "DONE":
#    break
#  elif report_id == "done": 
#    break
#  elif report_id.isalpha():               #isalpha Approach REFERENCE: Prof. Rossetti & https://www.w3schools.com/python/ref_string_isalpha.asp
#      print ("Error Message Bar: Entered letters! Please input numbers only!")
#  elif report_id in string.punctuation:   #string.punctuation REFERENCE: https://www.geeksforgeeks.org/string-punctuation-in-python/
#      print("Error Message Bar: Entered punctuation mark! Please input numbers only!") #Error Message bar: Please input numbers only!   
#  elif int(report_id) in valid_ids:
#        report_ids.append(report_id)     #list append() REFERENCE : https://www.youtube.com/watch?v=3BaGb-1cIr0&feature=youtu.be
#  else:
#    print("Error Message Bar: Report number isn't correct! Please try again!") 
#print("REPORT NUMBERS INCLUDE:",(report_ids)) 
    









  #REFERENCE 1) https://www.youtube.com/watch?v=eMOA1pPVUc4

#files = [file for file in os.listdir('./data')] 
#all_month_data = pd.DataFrame()
#
#for file in files:
#    df = pd.read_csv("./data/"+file)
#    all_month_data = pd.concat([all_month_data, df])
#all_month_data.to_csv("all_data.csv",index=False)  
#all_data = pd.read_csv("all_data.csv")
#print(all_data.head())
#
#monthly_total = all_data["sales price"].sum()
#
#product_totals = all_data.groupby(["product"]).sum()
#
#product_totals = product_totals.sort_values("sales price", ascending=False)
#
#
#top_sellers = []
#rank = 1
#for i, row in product_totals.iterrows():
#    d = {"rank": rank, "name": row.name, "monthly_sales": row["sales price"]}
#    top_sellers.append(d)
#    rank = rank + 1
#
#print("-----------------------")
#print("MONTH: March 2018")
#
#print("-----------------------")
#print("CRUNCHING THE DATA...")
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












###combine dataframes
#CSV_FILENAME = "sales-201803.csv"

#csv_filepath = os.path.join("data", CSV_FILENAME)

#sales = pd.read_csv(csv_filepath)

# print(sales.head())

#dataframe1 = pd.read_csv("sales-201801.csv")
#dataframe2 = pd.read_csv("sales-201802.csv")
#dataframe3 = pd.read_csv("sales-201803.csv")
#filesnames = ["sales-201801.csv","sales-201802.csv","sales-201803.csv"]
#csv_filepath = os.path.join("data", filesnames)
#dataframes = [pd.read_csv(f) for f in filesnames]

#filenames = glob("sales*.csv")
#dataframes = [pd.read_csv(f) for f in filenames]
#print(dataframes.head())