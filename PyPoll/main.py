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
