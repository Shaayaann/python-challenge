import os
import csv

candidates = []

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:


    csvreader = csv.reader(csvfile, delimiter=',')

   
    next(csvreader, None)
    for row in csvreader:
        # print(row)
        candidates.append(row[2])
        # month.append(row[0])

candidates_name = ['Diana DeGette', 'Charles Casper Stockham', 'Raymon Anthony Doane']
# print(candidates_name)

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

count = [diana_count, charles_count,  rymon_count]

charles_percent = round((charles_count/len(candidates))*100,3)
diana_percent = round((diana_count/len(candidates))*100,3)
rymon_percent = round((rymon_count/len(candidates))*100,3)

percent = [diana_percent,charles_percent, rymon_percent]

winner_value = max (percent)



Final_list = list(zip(candidates_name, percent,count))

print(Final_list)



for i in range (len(candidates_name)):
    # print(Final_list[i][1])

    if Final_list[i][1] == winner_value:

        print('The Winner is:', Final_list[i][0])






#     change.append(pl[i+1] - pl[i])

# max = max(change)
# min = min(change)

# cleaned_data = list(zip(month, pl))
# print(cleaned_data[1][1])

# total = sum(pl)
# average = sum(change)/len(change)
# print('Total Months : ', len(month))
# print('Total = ', total, '$')
# print('Average Change :', round(average,2))
# print('Greatest Increase in Profits', max , month[(change.index(max))+1])
# print('Greatest Decrease in Profits', min , month[(change.index(min))+1])
