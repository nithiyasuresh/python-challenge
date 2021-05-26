# Nithiya's pyBank analysis 
"""task is to create a Python script that analyzes the records to calculate each of the following:

The total number of months included in the dataset

The net total amount of "Profit/Losses" over the entire period

Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in losses (date and amount) over the entire period
"""


# Load python modules
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Load csv files from resource folder
csvpath = os.path.join('.', 'Resources', 'PyBankData.csv')
# "..\\Resource\\PyBankData.csv"

output_path = os.path.join('.', 'Analysis', 'Analysis.txt')


# Initialise variables - global variables
# The total number of months included in the dataset - TotalMonths
TotalMonths = 0

# The net total amount of "Profit/Losses" over the entire period - net_total_amount
net_total_amount = 0

# Calculate the changes in "Profit/Losses" over the entire period - pl_changes
changes = 0

# avg_change = sum of all changes/no of changes


# # Method 1: Plain Reading of CSV files
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)
    # print(lines)
    #print(type(lines))

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    first_month = next(csvreader)
    # print(first_month)

    TotalMonths += 1

    net_total_amount += int(first_month[1])
    previous_month = int(first_month[1])

    # Read each row of data after the header
    for row in csvreader:
        # print(row)


        # Increase months by 1 to calculate the total no of months
        TotalMonths += 1

        # Calculate net_total_amount of P&L
        net_total_amount += int(row[1])

        # Difference between each month
        # difference = current montsh - last month
        difference = int(row[1]) - previous_month
        print(difference)

        # Add the values in the profit and loss list
        changes += difference
        # changes.append(difference)

# print(changes)
# print(len(changes))
# print(sum(changes))
average_change = changes/ 85


# Generate output to terminal
output = (
    f'Total months: {TotalMonths}\n'
    f'Total: ${net_total_amount}\n'
    f'Average Change: {average_change}\n'




)
print(output)
# save/output to a text file
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txt_file:
    txt_file.write(output)
