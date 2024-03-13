import csv
import os

# set path for resources csv file
csvpath = r'D:\James\Data Analytics Bootcamp\Module 2 Python\Homework\Starter_Code\Starter_Code\Python-Challenge\PyPoll\Resources\election_data.csv'

#initialise my variables
votes_total = 0
charles_count = 0
diana_count = 0
raymon_count = 0

#create lists to store multiple things
candidates = []
#open the csv reader in read mode
with open(csvpath) as csvfile:
    #create a csv reader object
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip the first row as it contains headers
    next(csvreader)

    #loop through the rows in the csv file
    for rows in csvreader:
        #add one vote to the vote counter
        votes_total +=1 
        #store each candidate name in the list from the 3rd column
        candidate_name = rows[2]
        candidates.append(candidate_name)
        #check each candidate and add 1 to their counter for votes
        if candidate_name == "Charles Casper Stockham":
            charles_count +=1
        elif candidate_name == "Diana DeGette":
            diana_count +=1
        else:
            raymon_count +=1 


#make a set of unique candidates as a set has no duplicates
unique_candidates_set = set(candidates)
#convert back to a list so that we can index, however as the set has no order, this makes it a different index each time so it is useless
unique_candidates_list = list(unique_candidates_set)
#calculate percentages based off each vote count
charles_percent = round((charles_count/votes_total)*100, 3)
diana_percent = round((diana_count/votes_total)*100, 3)
raymond_percent = round((raymon_count/votes_total)*100, 3)

# Calculate the total number of votes each candidate received
candidate_votes = {
    "Charles Casper Stockham": charles_count,
    "Diana DeGette": diana_count,
    "Raymon Anthony Doane": raymon_count
}

# Find the winner based on the maximum number of votes
winner = max(candidate_votes, key=candidate_votes.get)

print(f'Total Votes: {votes_total}')
print(f'Charles Casper Stockham: {charles_percent}% ({charles_count})')
print(f'Diana DeGette: {diana_percent}% ({diana_count})')
print(f'Raymon Anthony Doane: {raymond_percent}% ({raymon_count})')
print(f'Winner: {winner}')
with open('Analysis/outputPyPoll.txt', 'w') as file:
    file.write(f"Election Results\n\n")
    file.write(f"--------------------------\n\n")
    file.write(f"Total Votes: {votes_total}\n")
    file.write(f"--------------------------\n\n")
    file.write(f"Charles Casper Stockham: {charles_percent}% ({charles_count})\n\n")
    file.write(f"Diana DeGette: {diana_percent}% ({diana_count})\n\n")
    file.write(f"Raymon Anthony Doane: {raymond_percent}% ({raymon_count})\n\n")
    file.write(f"--------------------------\n\n")
    file.write(f"Winner: {winner} \n\n")
print("output has been successfully written to outputPyPoll.txt")   