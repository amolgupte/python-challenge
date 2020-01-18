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
        a = countKhan
        b = countCorrey
        c = countLi
        d = countOTooley
        e = a+b+c+d

print("Election Results ")
print("-------------------------------")
print("Total Votes: "+ str(count))
print("--------------------------------")
print("Khan: " + str(round(a/e*100,3)) + "% (" + str(countKhan) + ")")
print("Correy: " + str(round(b/e*100,3)) + "% (" + str(b) + ")")
print("Li: " + str(round(c/e*100,3)) + "% (" + str(c) + ")")
print("O'Tooley: "+ str(round(d/e*100,3)) + "% (" + str(d) + ")")
print("-------------------------------")

dict_max = { a:"Khan", b:"Correy", c:"Li", d:"O'Tooley" }

print("Winner: "+dict_max[max(dict_max)])

f = open("C:/Users/amolg/OneDrive/Desktop/DU-DEN-DATA-PT-11-2019-U-C/02-Homework/03-Python/Instructions/PyPoll/Resources/PyPoll.txt",'w')
f.write("Election Results \n") 
f.write("-------------------------------"+"\n")
f.write("Total Votes: "+ str(count)+"\n")
f.write("--------------------------------"+"\n")
f.write("Khan: " + str(round(a/e*100,3)) + "% (" + str(countKhan) + ")"+"\n")
f.write("Correy: " + str(round(b/e*100,3)) + "% (" + str(b) + ")"+"\n")
f.write("Li: " + str(round(c/e*100,3)) + "% (" + str(c) + ")"+"\n")
f.write("O'Tooley: "+ str(round(d/e*100,3)) + "% (" + str(d) + ")"+"\n")
f.write("-------------------------------"+"\n")

dict_max = { a:"Khan", b:"Correy", c:"Li", d:"O'Tooley" }

f.write("Winner: "+dict_max[max(dict_max)])
f.close()     