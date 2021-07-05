import os
import csv


csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)

    total = 0
    khan = 0
    correy = 0
    li = 0
    otooley = 0

    for row in csvreader:

        total += 1

        if (row[2] == "Khan"):
            khan += 1

        elif (row[2] == "Correy"):
            correy += 1

        elif (row[2] == "Li"):
            li += 1

        elif (row[2] == "O'Tooley"):
            otooley += 1
        khan_percent = khan / total

    correy_percent = correy / total
    li_percent = li / total
    otooley_percent = otooley / total

    election_winner = max(khan, correy, li, otooley)

    if election_winner == khan:
        winner_name = "Khan"
    elif election_winner == correy:
        winner_name = "Correy"
    elif election_winner == li:
        winner_name = "Li"
    elif election_winner == otooley:
        winner_name = "O'Tooley"

print(f"Election Results")
print(f"------------------------------")
print(f"Total Votes: {total}")
print(f"------------------------------")
print(f"Khan: {khan_percent} ({khan})")
print(f"Correy: {correy_percent} ({correy})")
print(f"Khan: {li_percent} ({li})")
print(f"Khan: {otooley_percent} ({otooley})")
print(f"------------------------------")
print(f"Winner: {winner_name}")
print(f"------------------------------")
