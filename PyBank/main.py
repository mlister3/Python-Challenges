import os

import csv

TMonths = 0
TProfit = 0
GIncrease = ["", 0]
GDecrease = ["", 0]
EndMonthTrans = []
PriorTrans = 0
AvgDelta = 0

#// Paths for the CSV file
Filepath = os.path.join('Resources', 'budget_data.csv')

#print(os.path.abspath(Filepath))

#with open(Filepath) as csv_file:
#    csv_reader = csv.reader(csv_file)
#    print(csv_file)
    
#// This opens the CSV file and the print line is for confirmation
with open(Filepath, encoding='utf') as BData:
    csvreader = csv.reader(BData, delimiter=",")
    print(BData)

    next(BData)

    #// Executes the processes below this for each row of the CSV file
    for row in BData:
        TMonths += 1
        TProfit += int(row[1])

        if int(row[1]) > GIncrease[1]:
            GIncrease[1] = int(row[1])
            GIncrease[0] = row[0]
        if int(row[1]) < GDecrease[1]:
            GDecrease[1] = int(row[1])
            GDecrease[0] = row[0]

        if TMonths > 1:
            EndMonthTrans.append(int(row[1]) - PriorTrans)
            PriorTrans = int(row[1])

AvgDelta = sum(EndMonthTrans) / len(EndMonthTrans)

print("Financial Analysis")
print("------------------------------------")