import os
import csv


csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)

    print(csvreader)
