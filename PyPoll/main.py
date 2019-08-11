import os
import csv

csvpath = os.path.join("election_data.csv")
amt_votes = []
candidates = []
percent_votes = []
total_votes = 0

#The total number of votes cast
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        
#A complete list of candidates who received votes   
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            amt_votes.append(1)
        else:
            index = candidates.index(row[2])
            amt_votes[index] += 1
    
#The percentage of votes each candidate won
    for votes in amt_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
    
#The winner of the election based on popular vote.
    winner = max(amt_votes)
    index = amt_votes.index(winner)
    winning_candidate = candidates[index]

# Print Analysis
print("Election Results")
print("-------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(amt_votes[i])})")
print("-------------------------")
print(f"Winner: {winning_candidate}")
print("-------------------------")

#Text Output
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percent_votes[i])} ({str(amt_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"

