import os
import csv

csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    months = len(list(csvreader))
    print(months)
