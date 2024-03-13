import csv
import os
# Set path for file
csvpath = r'D:\James\Data Analytics Bootcamp\Module 2 Python\Homework\Starter_Code\Starter_Code\Python-Challenge\PyBank\Resources\budget_data.csv'

#initialise the profit/loss variable
total_profit_loss = 0
row_total = 0
previous_profit_loss = 0

#create lists to store the changes for each row
change_list = []
dates = []
#open the csv in read mode 
with open(csvpath) as csvfile:
    #create a csv reader object
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the Header row as we dont want to read this
    next(csvreader)
    #loop through the rows in the csv file
    for rows in csvreader:
        #extract the profit/loss values from the 2nd column which is index 1
            profit_loss = int(rows[1])
            #store the dates
            each_date = rows[0]      
            dates.append(each_date)
            #add the profit or loss to the total
            total_profit_loss += profit_loss
            #count the number of rows
            row_total += 1
            #calculate the change in the profit/loss compared to the previous period
            change = profit_loss - previous_profit_loss
            #update the change list with the change
            change_list.append(change)
            #update the profit/loss for the next iteration
            previous_profit_loss = profit_loss

        

#calculate the average change
average_change = sum(change_list) / (len(change_list)-1)      

#find max and min change (or greatest profit and greatest loss)
max_change = max(change_list)
min_change = min(change_list)
#find the index for the maximum and minimum change in change_list
index_max = change_list.index(max_change)
index_min = change_list.index(min_change)
#obtain associated date for the maximum change
date_max = dates[index_max]
date_min = dates[index_min]

#print the number of months (rows)
print(f'Total months: {row_total} months')
#print the total profit/loss
print(f'Total: ${total_profit_loss}')
#print the average changes
print(f'Average Change: {average_change} ')
#print maximum change 
print(f'Greatest Increase in profits: {date_max} (${max_change}) ')   
#print minimum change
print(f'Greatest Decrease in profits: {date_min} (${min_change}) ')  

#output_path = r'D:\James\Data Analytics Bootcamp\Module 2 Python\Homework\Starter_Code\Starter_Code\PyBank'
with open('Analysis/output.txt', 'w') as file:
    file.write(f"Financial Analysis\n\n")
    file.write(f"--------------------------\n\n")
    file.write(f"Total Months: {row_total}\n")
    file.write(f"Total: ${total_profit_loss}\n")
    file.write(f"Average Change: {average_change}\n")
    file.write(f"Greatest Increase in profits: ${max_change}\n")
    file.write(f"Greatest Decrease: {min_change}\n")
    
print("Output has been written to output.txt file.")
