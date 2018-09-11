# import dependencies 
import os
import csv

# Provide Path
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# open CSV file
with open(csvpath, newline='') as csvfile:

    # Specify delimiter and declare variable
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read header
    csv_header = next(csvreader)

    # assign variables as empty lists
    months = []
    net = []
    
    # print Title & border
    print('Financial Analysis')
    print('----------------------------')

    # Loop through rows
    for row in csvreader:

        #add each value in column A (months) to months list
        months.append(row[0])

        # add each value in Column B (Profit/Losses) to net list
        net.append(int(row[1]))

    # find number of values in months list
    total_months = len(months)

    # print
    print(f'Total Months: {total_months}')

    # sum all values in net list to find total Profits/losses
    total_net = sum(net)

    # print
    print(f'Total: ${total_net}')

    # calculate average change in "Profit/Losses" between months over the entire period
    average_change = round((total_net/ total_months), 2)

    # print
    print(f'Average Change: ${average_change}')

    # Find greatest increase in profits (date and amount) over the entire period (max value in net list)
    max_increase = max(net)

    # The greatest decrease in losses (date and amount) over the entire period (min value in net list)
    max_decrease = min(net)

    # zip net and months list into dictionary 
    month_by_revenue = dict(zip(net, months))

    #find month with greatest increase
    max_month = month_by_revenue.get(int(max_increase))

    #find month with greatest decrease
    min_month = month_by_revenue.get(int(max_decrease))

    #print
    print(f'Greatest Increase in Profits: {max_month} (${max_increase})')

    #print
    print(f'Greatest Decrease in Profits: {min_month} (${max_decrease})')

#make path for writing 
output_path = os.path.join('..', 'Resources', 'pybank_output.txt')

#open text file and write
with open (output_path, 'w') as txtfile:
    txtfile.writelines(f'Financial Data \n ---------------------------- \n')
    txtfile.writelines(f'Total Months: {total_months} \n')
    txtfile.writelines(f'Total: ${total_net} \n')
    txtfile.writelines(f'Average Change: ${average_change} \n')
    txtfile.writelines(f'Greatest Increase in Profits: {max_month} (${max_increase}) \n')
    txtfile.writelines(f'Greatest Decrease in Profits: {min_month} (${max_decrease})')

        
        