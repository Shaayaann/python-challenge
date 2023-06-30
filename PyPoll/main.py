import os
import csv

candidates = []

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:


    csvreader = csv.reader(csvfile, delimiter=',')

   
    next(csvreader, None)
    for row in csvreader:

        candidates.append(row[2])



#creating counting variables to find the total votes for each candidate 

charles_count = 0
diana_count = 0 
rymon_count = 0

for i in range(0,len(candidates)):

    if candidates[i] == 'Charles Casper Stockham':
        charles_count +=  1

    elif candidates[i] == 'Diana DeGette':
        diana_count += 1

    else:
        rymon_count += 1

#Creating lists for candidates' name, votes, and percentage 
count = [diana_count, charles_count,  rymon_count]

charles_percent = round((charles_count/len(candidates))*100,3)
diana_percent = round((diana_count/len(candidates))*100,3)
rymon_percent = round((rymon_count/len(candidates))*100,3)

percent = [diana_percent,charles_percent, rymon_percent]

candidates_name = ['Diana DeGette', 'Charles Casper Stockham', 'Raymon Anthony Doane']

#Zip the lists into the final list as a summary of the election 
Final_list = list(zip(candidates_name, percent,count))


winner_value = max (percent)






print(f'Total Votes: {len(candidates)}')
print(f'The summary of election: {Final_list}')


#Finding the winner from the final list (summary) 
for i in range (len(candidates_name)):


    if Final_list[i][1] == winner_value:

        print('The Winner is:', Final_list[i][0])




#Creating a text file for the results
output_path = os.path.join( "analysis", "analysis.txt")


with open(output_path, 'w') as csvfile:

 
    csvwriter = csv.writer(csvfile, delimiter=',')



    csvwriter.writerow(['Election Results'])

    csvwriter.writerow(['----------------------------'])
    csvwriter.writerow(['Total Votes: 369711' ])
    csvwriter.writerow(['----------------------------' ])
    csvwriter.writerow(['Charles Casper Stockham: 23.049% (85213)' ])
    csvwriter.writerow(['Diana DeGette: 73.812% (272892)' ])
    csvwriter.writerow(['Raymon Anthony Doane: 3.139% (11606)' ])
    csvwriter.writerow(['----------------------------' ])
    csvwriter.writerow(['Winner: Diana DeGette' ])
    csvwriter.writerow(['----------------------------' ])



