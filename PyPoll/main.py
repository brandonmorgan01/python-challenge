#import dependencies 
import os 
import csv

#provide path
csvpath = os.path.join('..', 'resources', 'election_data.csv')

#open CSV file
with open(csvpath, newline='') as csvfile:

    # Specify delimiter and declare variable
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read header
    csv_header = next(csvreader)

    #assign variables
    votes = []

    #print header and border
    print('Election Results')
    print('-------------------------')

    #loop through rows
    for row in csvreader:

        #add voter id's (Column A) to votes list
        votes.append(row[2])
    
    #use number of voter ID's to find number of votes
    total_votes = len(votes)

    #print
    print(f'Total Votes: {total_votes}')
    print('-------------------------')

    #convert votes list to set to see only unique values
    candidates = set(votes)

    #convert back to list, so that it is ordered
    candidates_list = list(candidates)

    #use count fuction to find number of votes for each candidate
    can_1_votes = votes.count(candidates_list[0])
    can_2_votes = votes.count(candidates_list[1])
    can_3_votes = votes.count(candidates_list[2])
    can_4_votes = votes.count(candidates_list[3])

    #find percentage of total vote for each candidate
    can_1_pct = (can_1_votes/total_votes)
    can_2_pct = (can_2_votes/total_votes)
    can_3_pct = (can_3_votes/total_votes)
    can_4_pct = (can_4_votes/total_votes)

    #print
    print(f'{candidates_list[0]}: {round((can_1_pct *100), 3)}% ({can_1_votes})')
    print(f'{candidates_list[1]}: {round((can_2_pct *100), 3)}% ({can_2_votes})')
    print(f'{candidates_list[2]}: {round((can_3_pct *100), 3)}% ({can_3_votes})')
    print(f'{candidates_list[3]}: {round((can_4_pct *100), 3)}% ({can_4_votes})')
    print('-------------------------')

    #determine winner
    if (can_1_votes > can_2_votes) and (can_1_votes > can_3_votes) and (can_1_votes > can_4_votes):
        winner = candidates_list[0]
    elif (can_2_votes > can_1_votes) and (can_2_votes > can_3_votes) and (can_2_votes > can_4_votes):
        winner = candidates_list[1]
    elif (can_3_votes > can_1_votes) and (can_3_votes > can_2_votes) and (can_3_votes > can_4_votes):
        winner = candidates_list[2]
    elif (can_4_votes > can_2_votes) and (can_4_votes > can_3_votes) and (can_4_votes > can_1_votes):
        winner = candidates_list[3]
    
    #print
    print(f'Winner: {winner}')
    print('-------------------------')

#make path for writing 
output_path = os.path.join('..', 'Resources', 'pypoll_output.txt')

#open text file and write
with open (output_path, 'w') as txtfile:
    txtfile.writelines(f'Election Results \n ------------------------- \n')
    txtfile.writelines(f'Total Votes: {total_votes} \n ------------------------- \n')
    txtfile.writelines(f'{candidates_list[0]}: {round((can_1_pct *100), 3)}% ({can_1_votes}) \n')
    txtfile.writelines(f'{candidates_list[1]}: {round((can_2_pct *100), 3)}% ({can_2_votes}) \n')
    txtfile.writelines(f'{candidates_list[2]}: {round((can_3_pct *100), 3)}% ({can_3_votes}) \n')
    txtfile.writelines(f'{candidates_list[3]}: {round((can_4_pct *100), 3)}% ({can_4_votes}) \n')
    txtfile.writelines(f'------------------------- \n Winner: {winner} \n -------------------------')
    

    


