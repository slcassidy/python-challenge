import os
import csv
from datetime import datetime
import calendar
#import panda

#path of the csv file
csvpath = os.path.join(".", "Resources", "budget_data.csv")

print(csvpath)
with open(csvpath, newline='') as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
#Skip first row
    csv_header = next(csvreader)
    count = 0
    total = 0
    change = 0
    changeList = [0]
    total_change = 0
    profit_loss_List = []
 #   profit_list = []
#   loss_list = []
    maxProfit = 0
    minLoss = 0
    dateList = []

#def month_count(months):
    for row in csvreader:
        #Testing the Month & Count of months
            #print(row[0])
            #dateMY = row[0]
            #month = dateMY.split('-')[0]
            #print(month)
                     
            #Count the number of lines within the table
            count += 1
        #Testing column & Get to total
            #print(row[1])
            profit_loss = int(row[1])
            #print(profit_loss)
            total += profit_loss
        #Get the average change
            #change = (profit_loss - changeList[count]) 
            #change = profit_loss - change
            #changeList.append(change)
            #print(change)
            #print(changeList[count])
            #total_change += changeList[0]
        #Max in the list
            profit_loss_List.append(profit_loss)
            dateList.append(row[0]) 
            #if (profit_loss >= 1):
                #print(profit_loss)
                #profit_list.append(profit_loss)
            #if (profit_loss < 0):
                #loss_list.append(profit_loss)
            #maxProfit = max(profit_list)
            #minLoss = min(loss_list)
            maxProfit = max(profit_loss_List)
            minLoss = min(profit_loss_List)
            minDate = profit_loss_List.index(minLoss)
            maxDate = profit_loss_List.index(maxProfit)
            #print(profit_loss_List)
            #print(maxDate)
            #print(dateList[maxDate])

    #Print the number of months aka rows in the file
    print("Financial Analysis")
    print("------------------------------------")
    print("Total Months: " + str(count)) 
    print("Total: $" + str(total))  
    print("Average Change: $" +str(total_change))
    print("Max: " + str(dateList[maxDate]) + " $" +str(maxProfit))
    print("Min: " + str(dateList[minDate]) + " $" +str(minLoss))

        #if (month) == Jan:



            
        
            #date = datetime(row[0])
            #month = date.month
            #print(month[0])



