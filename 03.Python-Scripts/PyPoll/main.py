'''
    Name: PyPoll Script
    Author: Diana Dumitrascu
    Date: Jan 31, 2019
    
    Description: This script analyzes the 'election_data.csv' file and exports the following calculations to a text file:
    - Total Number of Votes
    - A complete list of candidates who received votes
    - The percentage of votes each candidate won
    - The total number of votes each candidate won
    - The number of the election based on popular vote
    
    About the 'election_data.csv file:
    - the file contains three columns: 'Voter ID', 'Country' and 'Candidate'
    - each row contains a unique month
'''

# Read csv file and store it in an array
import csv
election_data = []
path = 'election_data.csv'
with open(path,newline ='') as csv_file:
    csvreader = csv.reader(csv_file,delimiter =',')
    for row in csvreader:
        election_data.append(row)

election_data = election_data[1:]

# Loop through data and store everything in a dictionaty.
# key = candidate name          val = number of votes
candidates = {}
total_votes = 0
for row in election_data:
    total_votes += 1
    if row[2] in candidates:
        candidates[row[2]] += 1
    else:
        candidates[row[2]] = 1

# Add results to text and determine winner
winner_val = 0
winner = ''
text = "Election Result \n"
text += "-------------------------\n"
text += "Total Votes: " + str(total_votes) + "\n"
text += "-------------------------\n"
for key in candidates:
    text += key + ": " + str(round(candidates[key]/total_votes*100,3)) + "% (" + str(candidates[key])+")\n"
    if candidates[key] > winner_val:
        winner = key
        winner_val = candidates[key]
text += "-------------------------\n"
text += "Winner: " + winner + "\n"
text += "-------------------------\n"

#Print text to console
print(text)

#Write text to txt file
path = "results.txt"
f = open(path,'w')
f.write(text)
f.close()
