import os
import csv

pl = []
month = []
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:


    csvreader = csv.reader(csvfile, delimiter=',')

   
    next(csvreader, None)
    for row in csvreader:
        # print(row)
        pl.append(int(row[1]))
        month.append(row[0])
change = []
for i in range(0,len(pl)-1):
    change.append(pl[i+1] - pl[i])

max = max(change)
min = min(change)

# cleaned_data = list(zip(month, pl))
# print(cleaned_data[1][1])

total = sum(pl)
average = sum(change)/len(change)
print('Total Months : ', len(month))
print('Total = ', total, '$$')
print('Average Change :', round(average,2))
print('Greatest Increase in Profits', max , month[(change.index(max))+1])
print('Greatest Decrease in Profits', min , month[(change.index(min))+1])
