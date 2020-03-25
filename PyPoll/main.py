import os
import csv
from datetime import datetime
import calendar
import pandas as pd
#import panda

#path of the csv file
csvpath = os.path.join(".", "Resources", "election_data.csv")
# Save path for the panda
data_file = "Resources/election_data.csv"
#Read the panda files
data_file_pd = pd.read_csv(data_file)
#Testing to see the data
#print(data_file_pd.head(6))

#print(csvpath)
with open(csvpath, newline='') as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
#Skip first row
    csv_header = next(csvreader)

#Variables
    Voter_ID = []
    Country = []
    Candidate = []


    #Function
    def candiateList(name):
        Length = len(name)
        #print(Length)
        x = 0
        finalList = []
        i = 0   
        while x < Length:
            #print(x)
            #print(name[x])
            listLength = len(finalList)
            #print(listLength)
            if listLength == 0:
                finalList.append(name[x])
            #    print(name)
            while i < listLength:
               if name[x] != finalList[i]:
                   #print(name[x])
                   finalList.append(name[x])
               i += 1
            x += 1
        print("Final")  
        print(listLength)
        print(finalList)
        return(finalList)

    # Reading the file
    for row in csvreader:
        Voter_ID.append(row[0])
        Country.append(row[1])
        Candidate.append(row[2])

pollList = zip(Voter_ID,Country,Candidate)
candiateList(Candidate)
print("Election Results")
print("----------------------------")
#Total number of Votes length of the voter ID table
print("Total Votes: " + (str(len(Voter_ID))))
#print(Voter_ID)
print("----------------------------")
votes = data_file_pd["Candidate"].value_counts()
print(votes)