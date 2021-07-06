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
print(f"-------------------------")
print(f"Total Votes: {total}")
print(f"-------------------------")
print(f"Khan: {khan_percent:.3%} ({khan})")
print(f"Correy: {correy_percent:.3%} ({correy})")
print(f"Li: {li_percent:.3%} ({li})")
print(f"O'Tooley: {otooley_percent:.3%} ({otooley})")
print(f"-------------------------")
print(f"Winner: {winner_name}")
print(f"-------------------------")

results = os.path.join("..", "PyPoll", "Analysis", "results.txt")

with open(results, 'w',) as txtfile:

    txtfile.write(f"Election Results\n")
    txtfile.write(f"-------------------------\n")
    txtfile.write(f"Total Votes: {total}\n")
    txtfile.write(f"-------------------------\n")
    txtfile.write(f"Khan: {khan_percent:.3%} ({khan})\n")
    txtfile.write(f"Correy: {correy_percent:.3%} ({correy})\n")
    txtfile.write(f"Li: {li_percent:.3%} ({li})\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.3%} ({otooley})\n")
    txtfile.write(f"-------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f"-------------------------\n")
