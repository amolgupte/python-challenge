import os
import csv
os.chdir("C:/Users/amolg/OneDrive/Desktop/DU-DEN-DATA-PT-11-2019-U-C/02-Homework/03-Python/Instructions/PyPoll/Resources")
csvpath = os.path.join("..", 'Resources', 'election_data.csv')
with open(csvpath, newline='') as csvfile:
     csvreader = csv.reader(csvfile)
     print(csvreader)
     csv_header = next(csvreader)
     print(f"CSV Header: {csv_header}")
     count=0
     for row in csvreader:
         count=count+1
     print("Election Results ")
     print("-------------------------------")
     print("Total Votes: "+ str(count))
     print("--------------------------------")
     