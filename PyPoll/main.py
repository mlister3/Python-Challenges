import os

import csv

Votes_Index = 0
t_votes = 0
Candidates_all = {}
candidate = []
Winner = ""
WinVote = 0


Filepath = os.path.join('Resources', 'election_data.csv')
#print(os.path.abspath(Filepath))

with open(Filepath, encoding='utf') as EData:
    csvreader = csv.reader(EData, delimiter=",")

    next(EData)

    for row in csvreader:
        t_votes = t_votes + 1

        candidate = row[2]

        if candidate not in Candidates_all:
            Candidates_all[candidate] = 0

        Candidates_all[candidate] += 1

for candidate in Candidates_all:
    Votes_Index = Candidates_all[candidate]
    if Votes_Index > WinVote:
        Winner = candidate
        WinVote = Votes_Index
    elif Votes_Index == WinVote:
        Winner = "Tie"

print("Election Results")
print("----------------------------")
print(f"Total Votes: {t_votes}")
print("----------------------------")
for candidate in Candidates_all:
    Votes_Index = Candidates_all[candidate]
    percentage_ratio = Votes_Index / t_votes * 100
    print(f"{candidate}: {percentage_ratio:.3f}% ({Votes_Index})")
print("----------------------------")
print(f"Winner: {Winner}")
print("----------------------------")


#// Write a text file with analysis
txt_output = os.path.join("analysis", "Analysis_Output.txt")

#print(os.path.abspath(txt_output)) // Test for output file path

#// in the txt output lines
with open(txt_output, "w") as txt_writer:
        txt_writer.write("Election Results\n")
        txt_writer.write("----------------------------\n")
        txt_writer.write(f"Total Votes: {t_votes}\n")
        txt_writer.write("----------------------------\n")
        for candidate in Candidates_all:
            Votes_Index = Candidates_all[candidate]
            percentage_ratio = Votes_Index / t_votes * 100
            txt_writer.write(f"{candidate}: {percentage_ratio:.3f}% ({Votes_Index})\n")
        txt_writer.write("----------------------------\n")
        txt_writer.write(f"Winner: {Winner}\n")
        txt_writer.write("----------------------------\n")