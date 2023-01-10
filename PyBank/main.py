import os

import csv

#// Establish Variables
TMonths = 0
TProfit = 0
GIncrease = ["", 0]
GDecrease = ["", 0]
EndMonthTrans = []
PriorTrans = 0
AvgDelta = 0

#// Paths for the CSV file
Filepath = os.path.join('Resources', 'budget_data.csv')

#print(os.path.abspath(Filepath)) // Filepath test

#with open(Filepath) as csv_file:
#    csv_reader = csv.reader(csv_file)
#    print(csv_file)
    
#// This opens the CSV file and the print line is for confirmation
with open(Filepath, encoding='utf') as BData:
    csvreader = csv.reader(BData, delimiter=",")
#   print(BData) // Test reading of the 
#   print(csvreader)

#// skips the headers in the CSV file.
    next(BData)

    #// Executes the processes below this for each row of the CSV file
    for row in csvreader:
#       if (row[1].isdigit): //caused an error that prevented code from registering a negative value
        TMonths = TMonths + 1
        TProfit = TProfit + int(row[1])
#       print(int(row[1])) // test used to see values in 2nd column in CSV file.

            #// in each row, if a month's profits/losses are above the previous record, record the number and the month
        if int(row[1]) > GIncrease[1]:
            GIncrease[1] = int(row[1])
            GIncrease[0] = row[0]
            
            #// Same as above but for greatest decrease and the value signs are flipped.
        if int(row[1]) < GDecrease[1]:
            GDecrease[1] = int(row[1])
            #print(GDecrease[1])
            GDecrease[0] = row[0]
            #print(GDecrease[0])

        #// Adds to the list: the change of value from month to month
        if TMonths > 1:
            EndMonthTrans.append(int(row[1]) - PriorTrans)
            PriorTrans = int(row[1])

#print(EndMonthTrans)

#// Averages the change of values by dividing the sum by the count of items in the string
#if EndMonthTrans > 0:
AvgDelta = sum(EndMonthTrans) / len(EndMonthTrans)

#// Terminal print
print("Financial Analysis")
print("------------------------------------")
print("Total Months: " + str(TMonths))
print("Total: $" + str(TProfit))
print("Average Change: $" + "{:.2f}".format(AvgDelta))
print("Greatest Increase in Profits: " + str(GIncrease[0]) + " ($" + str(GIncrease[1]) + ")")
print("Greatest Decrease in Profits: " + str(GDecrease[0]) + " ($" + str(GDecrease[1]) + ")")

#// Write a text file with analysis
txt_output = os.path.join("analysis", "Analysis_Output.txt")

#print(os.path.abspath(txt_output)) // Test for output file path

#// in the txt output lines, I will demonstate using the f-string function
with open(txt_output, "w") as txt_writer:
    txt_writer.write("Financial Analysis\n")
    txt_writer.write("------------------------------------\n")
    txt_writer.write(f"Total Months: {TMonths}\n")
    txt_writer.write(f"Total: $ {TProfit}\n")
    txt_writer.write(f"Average Change: $ {AvgDelta:.2f}\n")
    txt_writer.write(f"Greatest Increase in Profits: {GIncrease[0]} (${GIncrease[1]})\n")
    txt_writer.write(f"Greatest Decrease in Profits: {GDecrease[0]} (${GDecrease[1]})\n")