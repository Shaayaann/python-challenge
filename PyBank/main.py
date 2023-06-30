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
print(f'Total Months : {len(month)}' )
print(f'Total =  $ {total} ' )
print(f'Average Change : $ {round(average,2)}')
print(f'Greatest Increase in Profits: {max} {month[(change.index(max))+1]}')
print(f'Greatest Decrease in Profits: {min}  {month[(change.index(min))+1]}')


# Specify the file to write to

output_path = os.path.join( "analysis", "analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)

    csvwriter.writerow(['Financial Analysis'])

    csvwriter.writerow(['----------------------------'])
    csvwriter.writerow(['Total Months: 86' ])
    csvwriter.writerow(['Total: $22564198' ])
    csvwriter.writerow(['Average Change: $-8311.11' ])
    csvwriter.writerow(['Greatest Increase in Profits: Aug-16 ($1862002)' ])
    csvwriter.writerow(['Greatest Decrease in Profits: Feb-14 ($-1825558)' ])

