import os
import csv


csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    row = next(csvreader)

    dates = []
    change = []
    months = 0
    total = 0
    increase = 0
    increase_month = 0
    decrease = 0
    decrease_month = 0

    months += 1
    previous_row = int(row[1])

    for row in csvreader:
        months += 1
        total += int(row[1])
        revenue_change = int(row[1]) - previous_row
        change.append(revenue_change)
        previous_row = int(row[1])
        dates.append(row[0])

        if int(row[1]) > increase:
            increase = int(row[1])
            increase_month = row[0]

        if int(row[1]) < decrease:
            decrease = int(row[1])
            decrease_month = row[0]

    average = sum(change) / len(change)

    highest_amount = max(change)
    lowest_amount = min(change)

print("Financial Analysis")
print("---------------------------")
print("Total Months: ", + months)
print("Total: ", + total)
print("Average Change: $", + average)
print("Greatest Increase in Profits: " +
      increase_month, "$", highest_amount)
print("Greatest Decrease in Profits: " +
      decrease_month,  "$", lowest_amount)


results = os.path.join("..", "PyBank", "Analysis", "results.txt")

with open(results, 'w',) as txtfile:
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"------------------------------\n")
    txtfile.write(f"Total Months: {months}\n")
    txtfile.write(f"Total: ${total}\n")
    txtfile.write(f"Average Change: ${average}\n")
    txtfile.write(
        f"Greatest Increase in Profits:, {increase_month}, (${highest_amount})\n")
    txtfile.write(
        f"Greatest Decrease in Profits:, {decrease_month}, (${lowest_amount})\n")
