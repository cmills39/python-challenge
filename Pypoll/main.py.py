import os
import csv

election_data = os.path.join("Resources", "election_data.csv")

total_votes = 0

candidate_options =[]

candidate_votes ={}

winning_cadnidate = ""

winning_count = 0

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile)
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    for row in csvreader:
        total_votes = total_votes + 1
        
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
            
            candidate_options.append(candidate_name)
            
            candidate_votes[candidate_name] =  0
            
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
    
    election_results = (
            f"\n\nElection Results\n"
            f"----------------------"
            f"Total Votes: {total_votes}\n"
            f"--------------------\n")
     #print(election_results, ends="")
    
    for candidate in candidate_votes:
        
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes)*100

        if (votes > winning_count):
             winning_count = votes
             winning_candidate = candidate
             
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")
             
        winning_candidate_summary = (
            f"----------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"----------------------------\n"
        )
        print(winning_candidate_summary)
 
         
             
             
    
            
            
        
    
