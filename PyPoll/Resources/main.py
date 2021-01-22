#Create a Python Script to analyz the votes and calculation
#1.The total number of votes cast--- the sum of all the votes casted
#2.A complete list of candidates who received votes
#3.The percentage of votes each candidate won
#4.the total number of votes each candiate won
#5.The winner of the election based on popular vote.

#OS will allow to create file path across operating systems
#Module for reading CSV files
import os
import csv
import collections

#set the path to the file
election_data = os.path.join("PyPoll", "Resources","election_data.csv")

#create the lists of stored data
votes = 0
candidates = []
unique_candidates = []
count_vote = []
vote_percent = []

#Open path for the CSV file, path election_data
with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    csv_header = next(csvreader)

    #Begin to loop though the file
    for row in csvreader:

        #sum the total number of votes
        votes = votes + 1

        #look for the candidates in the file
        candidates.append(row[2])

        #filter the data to get the candidates, using unique
    for r in set(candidates):
        unique_candidates.append(r)

        #x the will be the total number of candidates
        x = candidates.count(r)
        count_vote.append(x)

        # value y will be set the percentage, to get the percent you divide candidates/votes *100
        y = (x/votes)*100 
        vote_percent.append(y)

    vote_winner = max(count_vote)
    winner = unique_candidates[count_vote.index(vote_winner)]

print ("----------------")
print ("Election Results")
print ("Total Votes:" + str(votes))
print ("----------------")
print ("The winner is:" + winner)
print ("----------------")

# Print to a text file: election_results.txt
election_results = os.path.join("PyPoll","Output", "election_results.txt")
with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(votes) + "\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")

    



