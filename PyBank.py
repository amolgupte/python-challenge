# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
os.chdir('C:/Users/amolg/OneDrive/Desktop/DU-DEN-DATA-PT-11-2019-U-C/02-Homework/03-Python/Instructions/PyBank/Resources')
# Module for reading CSV files
import csv
os.getcwd
csvpath = os.path.join("..", 'Resources', 'budget_data.csv')

# # Method 1: Plain Reading of CSV files
#with open(csvpath, 'r') as file_handler:
     #lines = file_handler.read()
     #print(lines)
     #print(type(lines))
# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)

    print(csvreader)

    #Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    
    count = 0
    add = 0
    
    # Read each row of data after the header
    for row in csvreader:
        print(row)
        count = count +1
        add= add+ int(row[1])
    
    print("Total Months "  + str(count) )
    print("Total " + str(add))
    

  
    