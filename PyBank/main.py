import os
import csv

csvpath = os.path.join('..','PyBank', 'budget_data.csv')

total_months = 0
total_profit_losses = 0
value = 0
change = 0
months = []
profits_losses = []

with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvreader)
    first_row = next(csvreader)
    total_months += 1
    total_profit_losses += int(first_row[1])
    value = int(first_row[1])
    
#The total number of months included in the dataset
    for row in csvreader:
        months.append(row[0])
        change = int(row[1]) - value
        profits_losses.append(change)
        value = int(row[1])
        total_months += 1
        
#The net total amount of "Profit/Losses" over the entire period
        total_profit_losses = total_profit_losses + int(row[1])

#The average of the changes in "Profit/Losses" over the entire period
average = sum(profits_losses)/len(profits_losses)

#The greatest increase in profits (date and amount) over the entire period
max_increase = max(profits_losses)
max_index = profits_losses.index(max_increase)
max_month = months[max_index]

#Print Financial Analysis
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_profit_losses)}")
print(f"Average Change: ${str(round(average,2))}")
print(f"Greatest Increase in Profits: {max_month} (${str(max_increase)})")
print(f"Greatest Decrease in Profits: {min_month} (${str(min_increase)})")

#txt file
output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "----------------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_profit_losses)}")
line5 = str(f"Average Change: ${str(round(average,2))}")
line6 = str(f"Greatest Increase in Profits: {max_month} (${str(max_increase)})")
line7 = str(f"Greatest Decrease in Profits:  {min_month} (${str(min_increase)})")