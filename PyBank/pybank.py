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
#The total number of months included in the dataset
TotalMonths = 0

#The net total amount of "Profit/Losses" over the entire period
net_total_amount = 0

#Finding the value of the first row
value = 0

#Defining variable for the P&L change
change = 0
dates = []
profits = []


# # Method 1: Plain Reading of CSV files
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)
    # print(lines)
    #print(type(lines))

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    first_row = next(csvreader)
    TotalMonths += 1
    net_total_amount += int(first_row[1])
    value = int(first_row[1])

    # Read each row of data after the header
    for row in csvreader:
        # Keeping track of the dates
        dates.append(row[0])

        # Calculate the change, then add it to list of changes
        pl_change = int(row[1]) - value
        profits.append(pl_change)
        value = int(row[1])

        #Total number of months
        TotalMonths += 1

        #Total net amount of "Profit/Losses over entire period"
        net_total_amount = net_total_amount + int(row[1])

        #Greatest increase in profits
        greatest_increase = max(profits)
        greatest_index = profits.index(greatest_increase)
        greatest_date = dates[greatest_index]

        #Greatest decrease (lowest increase) in profits
        greatest_decrease = min(profits)
        worst_index = profits.index(greatest_decrease)
        worst_date = dates[worst_index]

        #Average change in "Profit/Losses between months over entire period"
        avg_change = sum(profits) / len(profits)

# Generate output to terminal
Analysis = (
    f'Financial Analysis\n'
    f'---------------------------------\n'
    f'Total months: {str(TotalMonths)}\n'
    f'Total: ${str(net_total_amount)}\n'
    f'Average Change: ${str(avg_change)}\n'
    f'Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})\n'
    f'Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})\n'
)

print(Analysis)
# save/output to a text file
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txt_file:
    txt_file.write(Analysis)
