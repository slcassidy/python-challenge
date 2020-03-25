import os
import csv
from datetime import datetime
import calendar
#import panda

#path of the csv file
csvpath = os.path.join(".", "Resources", "budget_data.csv")

#print(csvpath)
with open(csvpath, newline='') as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
#Skip first row
    csv_header = next(csvreader)
#Variables
    count = 0
    total = 0
    profit_loss_List = []
    maxProfit = 0
    minLoss = 0
    dateList = []
    changeRate = []
    len_month = 0
    minDate = 0
    maxDate = 0

#Function to get the Average Change
    def rateChange(money):
        length = len(money)
        #print(length)
        total = 0.0
        totalChange = 0.0
        x = 1
        average = 0
        while x < length:
            moneyChange = money[x] - money[x-1]
            #print(moneyChange)
            changeRate.append(moneyChange)
            total += money[x]
            totalChange += moneyChange
            x += 1
        #print(changeRate)
        #print(totalChange)
        average = round(abs(totalChange/(length-1)),2)
        #print(average)
        return (average)
    

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
        #Get Min and Max of the profits and losses
            #Create an array with the list of profits
            profit_loss_List.append(profit_loss)
            #create array with list of Dates
            dateList.append(row[0]) 
            #Max in the list
            maxProfit = max(profit_loss_List)
            #Min in the list
            minLoss = min(profit_loss_List)
            #Find the dates of the min and max
            minDate = profit_loss_List.index(minLoss)
            maxDate = profit_loss_List.index(maxProfit)
            #print(profit_loss_List)
            #print(maxDate)
            #print(dateList[maxDate])
            len_month = len(dateList)
            #print(len_month)

            

    #Average Change testing
    #rateChange(profit_loss_List)
    #print(rateChange(profit_loss_List))

    #Print the number of months aka rows in the file
    print("Financial Analysis")
    print("------------------------------------")
    #print("Total Months: " + str(count)) 
    print("Total Months: " + str(len_month)) 
    print("Total: $" + str(total))  
    print("Average Change: $" +str(rateChange(profit_loss_List)))
    print("Greatest Increase in Profits: " + str(dateList[maxDate]) + " $" +str(max(changeRate)))
    print("Greatest Decrease in Profits: " + str(dateList[minDate]) + " $" +str(min(changeRate)))

# Set variable for output file
output_file = os.path.join("budget_results.csv")

#  Open the output file
with open(output_file, "w", newline="", encoding='utf-8') as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Financial Analysis"])
    writer.writerow(["------------------------------------"])
    writer.writerow(["Total Months: " + str(len_month)])
    writer.writerow(["Total: $" + str(total)])
    writer.writerow(["Average Change: $" +str(rateChange(profit_loss_List))])
    writer.writerow(["Greatest Increase in Profits: " + str(dateList[maxDate]) + " $" +str(max(changeRate))])
    writer.writerow(["Greatest Decrease in Profits: " + str(dateList[minDate]) + " $" +str(min(changeRate))])



