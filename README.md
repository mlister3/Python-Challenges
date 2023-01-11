# Python-Challenges
### Python Scripts to Analyze Financial Records and Election Data

> Use Python to write a sctipt that reads a preset CSV file, outputs an analysis in the terminal and export a TXT file with the analysis to a preset folder.

## Background - Requirements - PyBank
> In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

> Your task is to create a Python script that analyzes the records to calculate each of the following values:

- The total number of months included in the dataset

- The net total amount of "Profit/Losses" over the entire period

- The changes in "Profit/Losses" over the entire period, and then the average of those changes

- The greatest increase in profits (date and amount) over the entire period

- The greatest decrease in profits (date and amount) over the entire period

- Your analysis should align with the following results:
```
Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
```
In addition, your final script should both print the analysis to the terminal and export a text file with the results.

## Answer and Process

> See [PyBank main.py](./PyBank/main.py) for Python script solution and notes in code.

| Step | Description |
|--------------|---------------|
| 1. Establish Variables | We know that the instructions require us provide a certain set of values. We esablish those as variables. |
| 2. Pathing for CSV | We need to import `os` and `csv` to read csv files. We set a filepath to the correct folder where the dataset lives. to confirm that the script found the file, we create a print test that will print the path. |
| 3. Reading the CSV | After some attempts, we read the data using `csv.reader` and test to ensure we read properly by making print tests. |
| 4. Processing the Data | First, we skip the headers. Second, we create a for loop that reads each row in the data individually. in this for loop, we cound the rows to get total months, we find the greatest increase, greatest decrease, and gather the differences between the changes in a list. This list is divided by the count of values to get an average change.|
| 5. Data Print and TXT export | Using `print` we make an output that matches the requirements in the instructions. We use `str` or `f` to ensure integers print as strings. For export, we provide the script with a path and test the path before using `.write` to make the txt file that matches the requirements set by the instructions. |
- - -
## Background - Requirements - PyPoll

> In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

>You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

- The total number of votes cast

- A complete list of candidates who received votes

- The percentage of votes each candidate won

- The total number of votes each candidate won

- The winner of the election based on popular vote

- Your analysis should align with the following results:
```
Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
```
In addition, your final script should both print the analysis to the terminal and export a text file with the results.

## Answer and Process

> See [PyPoll main.py](./PyPoll/main.py) for Python script solution and notes in code.

| Step | Description |
|--------------|---------------|
| 1. Establish Variables | We know that the instructions require us provide a certain set of values. We esablish those as variables. |
| 2. Pathing for CSV | We need to import `os` and `csv` to read csv files. We set a filepath to the correct folder where the dataset lives. to confirm that the script found the file, we create a print test that will print the path. |
| 3. Reading the CSV | We read the data using `csv.reader` and test to ensure we read properly by making print tests. |
| 4. Processing the Data | First, we skip the headers. Second, we create a for loop that reads each row in the data individually. in this for loop, we cound the rows to get total votes, we find find and record in a list every unique candidate, count the vots for each candidate, and compare the values for each candidate to see who won.|
| 5. Data Print and TXT export | Using `print` we make an output that matches the requirements in the instructions. To simplify and open the script up to a different data set, we use a for loop to print out the information for each unique candidate. We use `str` or `f` to ensure integers print as strings. For export, we provide the script with a path and test the path before using `.write` to make the txt file that matches the requirements set by the instructions. |

- - -

## References
Data for this dataset was generated by edX Boot Camps LLC, and is intended for educational purposes only.

- - -

© 2022 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
