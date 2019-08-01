'''
    Name: PyBank Script
    Author: Diana Dumitrascu
    Date: Jan 31, 2019
    
    Description: This script analyzes the 'budget_data.csv' file and exports the following calculations to a text file:
        - Total Months
        - Total Profit / Losses
        - Average Change
        - Greatest Increase in Profits
        - Greatest Decrease in Profits
    
    About the 'budget_data.csv file:
    - the file contains two columns: 'Date' and 'Profit/Losses'
    - each row contains a unique month
'''

import csv
path = "budget_data.csv"

#Read the file and store every row into an array
budget_data = []
with open(path,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")
    for row in csvreader:
        budget_data.append(row)

#Variable initiation before starting looping through the rows
#Variable initioation is calculated between the first and second row
count = len(budget_data) - 1
total = int(budget_data[1][1]) + int(budget_data[2][1])
first_change = int(budget_data[2][1]) - int(budget_data[1][1])
total_changes = first_change
max_increase_val = first_change
max_increase_month = budget_data[2][0]
max_decrease_val = first_change
max_decrease_month = budget_data[2][0]

#Loop through every row and compare each row with the previous row
for i in range (3,count + 1):
    total += int(budget_data[i][1])
    change= int(budget_data[i][1]) - int(budget_data[i-1][1])
    total_changes += change
    if change > max_increase_val:
        max_increase_val = change
        max_increase_month = budget_data[i][0]
    elif change < max_decrease_val:
        max_decrease_val = change
        max_decrease_month = budget_data[i][0]

#Print results to the console
text = "Financial Analysis\n"
text += "----------------------------\n"
text += "Total Months: " + str(count) + "\n"
text += "Total: " + str(total) + "\n"
text += "Average Change: " + str(round(total_changes/(count-1),2)) + "\n"
text += "Greatest Increase in Profit: " + max_increase_month + " ($" + str(max_increase_val) + ")" + "\n"
text += "Greatest Decrease in Profits: " + max_decrease_month + " ($" + str(max_decrease_val) + ")"
print(text)

#Here is a simpler way to caculate average change that does not need a loop
#avg_change = (int(budget_data[count][1]) - int(budget_data[1][1]))/(count-1)

#Write results to file
output_path = "results.txt"
f = open(output_path,"w")
f.write(text)
f.close()
