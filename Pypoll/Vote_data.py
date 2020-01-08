import os
import csv

election_data = os.path.join( "Resources", "election_data.csv")


with open (election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    #show total votes
    total = 0
    for row in csvreader:
        total += int(row[1])
    print (total)

    