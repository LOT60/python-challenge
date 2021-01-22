#Python Challeneg, create a python script for the financial records
# 1.The total number of months included in the dataset
# 2.The net total amount of "Profit/Losses" over the entire period
# 3.Calculate the changes in "Profit/Losses",then find the average of those changes
# 4.The greatest increase in profits (date and amount) over the entire period
# 5.The greatest decrease in losses (date and amount) over the entire period

#OS will allow to create file path across operating systems
#Module for reading CSV files
import os
import csv

budget_data = os.path.join("PyBank","Resources","budget_data.csv")

#Define the variables, list the store data
Total_month = 0
Net_profit = 0
current_month = 0
last_month = 0
Profit_change = 0

Profit_changes = []
month = []


 #read the header row first, will print the date, profit/losses
    #print(f"CSV Header: {csv_header}")
with open(budget_data, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvfile)
    
    for row in csv_reader:
        #total months
        Total_month +=1
        month.append(row[0])
        #net total amount of "Profit\Losses" over entier period
        current_month = int(row[1])
        Net_profit += current_month
        if Total_month > 1:
            Profit_change = current_month - last_month
            Profit_changes.append(Profit_change)
            last_month = current_month

#sum up the avrage of the chnages in "Profit\Loss" over the entier period
sum_profit_loss = sum(Profit_changes)
Avrage_profit_loss = sum_profit_loss/(Total_month -1)

#High & low change in "Profit\loss" over entier period
max_change = max(Profit_changes)
min_change = min(Profit_changes)

#Index vlaue of high and lowest changes of "Profit\Loss" entier period
max_index = Profit_changes.index(max_change)    
min_index = Profit_changes.index(min_change)   

#Look for highest and lowest month
greatest_month = month[max_index]
lowest_month = month[min_index]
       

#Print the analysis on terminal
print("Financial Analysis")
print("-----------------------")
print(f"Total Month:{Total_month}")
print(f"Total: ${Net_profit}")
print(f"Avrage Change: ${Profit_change}")
print(f"Greatest Increase in Profit: {greatest_month} (${max_change})")
print(f"Greatest Decrease in Losses: {lowest_month} (${min_change})")

#Export txt file with the results 
budget_data = os.path.join("PyBank","Output","budget_data.txt")
with open ('budget_data.txt', 'w') as text:
    text.write(" Financial Analysis\n")
    text.write("------------------------------------------\n")
    text.write(f" Total Months:{Total_month}\n")
    text.write(f" Total :${Net_profit}\n")
    text.write(f" Avrage Change:${Profit_change}\n")
    text.write(f" Greatest Increase in Profit:{greatest_month} (${max_change}\n")
    text.write(f" Greatest Decrease in Losses:{lowest_month} (${min_change}\n")