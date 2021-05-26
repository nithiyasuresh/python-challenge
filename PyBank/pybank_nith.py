# Nithiya's pyBank analysis 
print("Nithiya")

# Load python modules
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv


# # Load csv files from resource folder
# csvpath = os.path.join('.', 'Resources', 'PyBankData.csv')
# # "..\\Resource\\PyBankData.csv"

# output_path = os.path.join('.', 'Analysis', 'Analysis.txt')



# # # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     # print(lines)
#     # print(type(lines))

# # Initialise variables - global variables
# # The total number of months included in the dataset - TotalMonths
# TotalMonths = 0



# # Iterate through csv file and extract information


# """task is to create a Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period
# """


# # Generate output to terminal
# output = (
#     f'Total number of months is {TotalMonths}'




# )
# print(output)
# # save/output to a text file
# # Open the file using "write" mode. Specify the variable to hold the contents
# with open(output_path, 'w') as txt_file:
#     txt_file.write(output)
