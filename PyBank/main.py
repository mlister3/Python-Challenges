import os

import csv

TMonths = 0
TProfit = 0
GIncrease = ["", 0]
GDecrease = ["", 0]


Filepath = os.path.join('Resources', 'budget_data.csv')

#print(os.path.abspath(Filepath))

#with open(Filepath) as csv_file:
#    csv_reader = csv.reader(csv_file)
#    print(csv_file)
    
with open(Filepath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvfile)

print("Financial Analysis")
print("------------------------------------")