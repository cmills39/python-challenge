import os
import csv

budget_data = os.path.join( "Resources", "budget_data.csv")

total_months = []
total_profits = []
monthly_profit_change = []

with open (budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    #show total months
    total_months = sum(1 for row in csvreader)
    print(total_months)
    
with open (budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    #net amount
    total = 0
    for row in csvreader:
        total += int(row[1])
    print (total)

#average price
print(total/(total_months -1))

    


    
   
          
        
    