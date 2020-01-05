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
     countKhan = 0
     countCorrey = 0
     countLi = 0
     countOTooley = 0
     for row in csvreader:
        count=count+1
        if (row[2] == "Khan"):
            countKhan = countKhan+1
        elif(row[2] == "Correy"):
            countCorrey=countCorrey+1
        elif(row[2] =="Li"):
            countLi=countLi+1
        elif(row[2]=="O'Tooley"):
            countOTooley=countOTooley+1

     print("Election Results ")
     print("-------------------------------")
     print("Total Votes: "+ str(count))
     print("--------------------------------")
     print("Khan: " +str(countKhan))
     print("Correy: " + str(countCorrey))
     print("Li: " + str(countLi))
     print("O'Tooley: "+ str(countOTooley))
     print("-------------------------------")