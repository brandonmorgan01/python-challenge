# In this challenge, you get to be the boss. You oversee hundreds of employees across the country developing Tuna 2.0, 
# a world-changing snack food based on canned tuna fish. Alas, being the boss isn't all fun, games, and self-adulation. 
# The company recently decided to purchase a new HR system, and unfortunately for you, the new system requires employee 
# records be stored completely differently.

# Your task is to help bridge the gap by creating a Python script able to convert your employee records to the required format. 
# Your script will need to do the following:


# Import the employee_data1.csv and employee_data2.csv files, which currently holds employee records like the below:


# Emp ID,Name,DOB,SSN,State
# 214,Sarah Simpson,1985-12-04,282-01-8166,Florida
# 15,Samantha Lara,1993-09-08,848-80-7526,Colorado
# 411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania

# Then convert and export the data to use the following format instead:


# Emp ID,First Name,Last Name,DOB,SSN,State
# 214,Sarah,Simpson,12/04/1985,***-**-8166,FL
# 15,Samantha,Lara,09/08/1993,***-**-7526,CO
# 411,Stacy,Charles,12/20/1957,***-**-8526,PA


# In summary, the required conversions are as follows:


# The Name column should be split into separate First Name and Last Name columns.
# The DOB data should be re-written into MM/DD/YYYY format.
# The SSN data should be re-written such that the first five numbers are hidden from view.
# The State data should be re-written as simple two-letter abbreviations.


#import dependencies
import os 
import csv
from datetime import datetime

# #provide path
csvpath = os.path.join('..', 'resources', 'employee_data.csv')

#make path for writing 
output_path = os.path.join('..', 'Resources', 'employee_data_output.csv')

#open csvfile
with open(csvpath, newline='') as csvfile:
    
    # specify variable and delimiter
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #skip header
    csvheader = next(csvreader)

    #assign empty lists for columns
    emp_id = []
    first_name = []
    last_name = []
    dob = []
    ssn = []
    state = []


    for row in csvreader:
        #add employee ID's to list
        emp_id.append(row[0])

        #split name column and add first and last names to respective lists
        first_name.append(row[1].split()[0])
        last_name.append(row[1].split()[1])

        #add dob to list
        dob.append(row[2])

        #add SSN to list
        ssn.append(row[3])

        #add state to list
        state.append(row[3])

    # print(emp_id)
    # print(first_name)
    # print(last_name)
    # print(dob)
    # print(ssn)
    # print(state)

#datetime.strptime(d,'%Y %m %d')

    new_dob = (datetime.strptime(d,'%Y-%m-%d') for d in dob)
    dob_list = [datetime.strftime(d, '%m/%d/%Y') for d in new_dob]

    # print(dob_list)

    x = '409-65-7778'
    covered = '***-**-' + x[7:] 
    print(covered)
    # for x in ssn:
    
    
#     #open output csv
#     with open (output_path, 'w') as output:
        
#         for row in csvreader:
#             first = row[0].split()[0]
#             last = row[0].split()[1]
            
# print(first)
        

            


    




