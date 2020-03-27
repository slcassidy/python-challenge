import os
import csv
from datetime import datetime
import calendar
import pandas as pd
#import panda

# path of the csv file
csvpath = os.path.join(".", "Resources", "election_data.csv")
# Save path for the panda
data_file = "Resources/election_data.csv"
# Read the panda files
data_file_pd = pd.read_csv(data_file)
# Testing to see the data
# print(data_file_pd.head(6))

# print(csvpath)
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
# Skip first row
    csv_header = next(csvreader)

# Variables
    Voter_ID = []
    Country = []
    Candidate = []

    # Function

    def candiateList(name):
        Length = len(name)
        # print(Length)
        x = 0
        finalList = []
        i = 0
        while x < Length:
            # print(x)
            # print(name[x])
            listLength = len(finalList)
            # print(listLength)
            if listLength == 0:
                finalList.append(name[x])
            #    print(name)
            while i < listLength:
                if name[x] != finalList[i]:
                    # print(name[x])
                    finalList.append(name[x])
                i += 1
            x += 1
        # print("Final")
        # print(listLength)
        # print(finalList)
        return(finalList)

    # Reading the file
    for row in csvreader:
        Voter_ID.append(row[0])
        Country.append(row[1])
        Candidate.append(row[2])

pollList = zip(Voter_ID, Country, Candidate)
candiateList(Candidate)
print("Election Results")
print("----------------------------")
# Total number of Votes length of the voter ID table
print("Total Votes: " + (str(len(Voter_ID))))
# print(Voter_ID)
print("----------------------------")
votes_pd = data_file_pd["Candidate"].value_counts()
# print(votes_pd)

votes_pd1 = votes_pd.reset_index()

votes_pd_rename = votes_pd1.rename(columns={
    "index": "Candidate", "Candidate": "Votes"
})

percentage_pd = (votes_pd_rename["Votes"]/len(Voter_ID)) * 100
#percentage_pd.astype(str) + '%'
votes_pd_rename["Percentage Won"] = percentage_pd.round(
    decimals=4).astype(str) + '%'
# .round(decimals=4)
# .astype(str) + '%'
final_pd = votes_pd_rename.head()

final_reorder = votes_pd_rename[["Candidate", "Percentage Won", "Votes"]]
# final_reorder.["Percentage Won"].round(decimals=4)
# final_reorder.index(drop=True)
#votes_pd1 = data_file_pd["Candidate"].value_counts().unstack().fillna(0)
# print(votes_pd1)
# print(votes_pd_rename)
# print(final_pd)
print(final_reorder)
print("----------------------------")
max_Votes = final_reorder["Votes"].max()

max_Cand_row = final_reorder.loc[final_reorder["Votes"] == max_Votes, :]
max_Cand = max_Cand_row["Candidate"].head()
winner = pd.DataFrame({"Winner": max_Cand})
winner.T
# print(winner)
#max_reset = max_Cand.resetIndex()
# print(max_Votes.index())
#max_Cand = final_reorder["Votes" == max_Votes]
#max_Cand = final_reorder.groupby(["Candidate"])["Votes"].max()
#max_Cand = final_reorder.index(max_Votes.index())
# print(max_Votes)
print("Winner " + str(max_Cand))
#winner = max_Cand["Winner "]
# print(max_reset)
print("----------------------------")

# Set variable for output file
#output_file = os.path.join("Vote_results.csv")
# final_reorder.drop(columns=['index'])
# Output with Panda
df_header = pd.DataFrame(["Election Results"])
df_lines = pd.DataFrame(["------------------------------------"])
df_total = pd.DataFrame(["Total Votes: " + (str(len(Voter_ID)))])

#print(df_header.shape, df_lines.shape, df_total.shape)
df_winner = pd.DataFrame(["Winner"])
# print(df_header)
df_header.to_csv("Vote_results.csv", mode="a", index=False, header=False)
df_lines.to_csv("Vote_results.csv", mode="a", index=False, header=False)
df_total.to_csv("Vote_results.csv", mode="a", index=False, header=False)
df_lines.to_csv("Vote_results.csv", mode="a", index=False, header=False)
final_reorder.to_csv("Vote_results.csv", mode="a", index=False, header=False)
df_lines.to_csv("Vote_results.csv", mode="a", index=False, header=False)
df_winner.to_csv("Vote_results.csv", mode="a", index=False, header=False)
winner.to_csv("Vote_results.csv", mode="a", index=False, header=False)
df_lines.to_csv("Vote_results.csv", mode="a", index=False, header=False)
#  Open the output file
# with open(output_file, "w", newline="", encoding='utf-8') as datafile:
#writer = csv.writer(datafile)
#writer1 = csv.writer(final_reorder)

# Write the header row
#writer.writerow(["Election Results"])
#title = (["Election Results"])
#df_concat =pd.concat(title,separate)
# writer.writerow(["------------------------------------"])
#separate = (["------------------------------------"])
#writer.writerow(["Total Votes: " + (str(len(Voter_ID)))])
# writer.writerow(["------------------------------------"])
#final_reorder.to_csv("Vote_results.csv", mode="a", index=False, header=True)
# writer.writerow([final_reorder])
# writer.writerow(["------------------------------------"])
#writer.writerow(["Winner " + str(max_Cand)])
# writer.writerow(["------------------------------------"])

