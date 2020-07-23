#PyBank Homework


#import modules
import os
import csv


#set path to file
csvpath = os.path.join(r"C:\Users\matt\Desktop\Python-Challenge-Homework\PyBank\Resources\budget_data.csv")


#set variables
total_months = 0
total_profit_loss = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0


#open and read csv file
with open(csvpath, newline='') as csvfile:
    
    #specify delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #header row
    csv_header = next(csvreader)
    row = next(csvreader)
    
    #total number of months 
    previous_profit_loss = int(row[1])
    total_months = total_months + 1

    #total profit and loss
    total_profit_loss = total_profit_loss + int(row[1])

    #greatest increase 
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    
    #for each row after header
    for row in csvreader:
        
        #total number of months
        total_months = total_months+1

        #total profit and loss
        total_profit_loss = total_profit_loss + int(row[1])

        #calculate change from month to month
        profit_loss_change = int(row[1]) - previous_profit_loss
        monthly_change.append(profit_loss_change)
        previous_profit_loss = int(row[1])
        month_count.append(row[0])
        
        #calculate greatest increase (profit)
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        #calculate greatest decrease (loss)
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
        
    #calculate average change
    average_change = sum(monthly_change)/ len(monthly_change)
    
    highest = max(monthly_change)
    lowest = min(monthly_change)


#print the analysis
print(f"Financial Analysis")
print(f"-----------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${highest})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${lowest})")


#export text file
output_file = os.path.join('.', 'PyBank', 'Analysis', 'PyBank_analysis.txt')

with open(output_file, 'w',) as PyBank_export:

    PyBank_export.write(f"Financial Analysis\n")
    PyBank_export.write(f"-----------------------\n")
    PyBank_export.write(f"Total Months: {total_months}\n")
    PyBank_export.write(f"Total: ${total_profit_loss}\n")
    PyBank_export.write(f"Average Change: ${average_change:.2f}\n")
    PyBank_export.write(f"Greatest Increase in Profits: {greatest_increase_month} (${highest})\n")
    PyBank_export.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${lowest})\n")

