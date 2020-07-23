#PyPoll Homework


#import modules
import os
import csv


#set path to file
cvspath = os.path.join(r"C:\Users\matt\Downloads\election_data.csv")

#set variables
total_votes = 0
candidates_unique = []
candidate_vote_count = []

#open and read the csv file
with open(cvspath, newline="") as csvfile:

    #specify delimiter
    csvreader = csv.reader(csvfile, delimiter=",")

    #header row
    csv_header = next(csvreader)

    for row in csvreader:
        #total votes cast
        total_votes = total_votes + 1

        #candidate column
        candidate_name = (row[2])

        #find unique candidates
        if candidate_name in candidates_unique:
            candidate_namedex = candidates_unique.index(candidate_name)
            candidate_vote_count[candidate_namedex] = candidate_vote_count[candidate_namedex] + 1

        else:
            #add new candidate and votes to list
            candidates_unique.append(candidate_name)
            candidate_vote_count.append(1)



pct = []
max_votes = candidate_vote_count[0]
max_index = 0

for x in range(len(candidates_unique)):
   
    vote_pct = round(candidate_vote_count[x]/total_votes*100, 2)
    pct.append(vote_pct)
    
    if candidate_vote_count[x] > max_votes:
        max_votes = candidate_vote_count[x]
        max_index = x

election_winner = candidates_unique[max_index] 

#print the analysis

print(f"-----------------------")
print(f"Election Results")
print(f"-----------------------")
print(f'Total Votes: {total_votes}')
print(f"-----------------------")
for x in range(len(candidates_unique)):
    print(f'{candidates_unique[x]} : {pct[x]}% ({candidate_vote_count[x]})')
print(f"-----------------------")
print(f'Winner: {election_winner}')
print(f"-----------------------")



#export text file
output_file = os.path.join('.','PyPoll','Analysis',"PyPoll_analysis.txt")

with open(output_file, "w", newline="") as PyPoll_export:

    PyPoll_export.write(f"-----------------------\n")
    PyPoll_export.write(f"Election Results\n")
    PyPoll_export.write(f"-----------------------\n")
    PyPoll_export.write(f"Total Votes: {total_votes}\n")
    PyPoll_export.write(f"-----------------------\n")

    for x in range(len(candidates_unique)):
        PyPoll_export.write(f'{candidates_unique[x]} : {pct[x]}% ({candidate_vote_count[x]})\n')
    PyPoll_export.write(f"-----------------------\n")

    PyPoll_export.write(f'Winner: {election_winner}\n')
    PyPoll_export.write(f"-----------------------\n")
   
