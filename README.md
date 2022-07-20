# Analysis of the Election Audit

## Overview of Election Audit
A Colorado Board of Elections employee has given the following tasks to complete the election audit of a recent local congressional election.
This analysis presents the results of an election audit. It starts with the total amount of votes, followed by the votes and percentage that each county had. The code calculates the largest amount of votes per county, a summary of the results per candidate, and a summary of the winner. All the analysis was done through python with a CSV database. The results are shown both in the terminal if you run the code and in a text file.

1.Calculate the total number of votes cast.
2.Get a complete list of candidates who received votes.
3.Calculate the percentage of votes each candidate received.
4.Calculate the percentage of votes each candidate won.
5.Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv

## Analysis
- election_analysis.txt

## Election Audit Results

### - Votes that were cast in the congressional election

Through the election, the code counted 369,711 votes, this is achieved with a loop that goes through all the file rows. 

### - Number of Votes and percentage of total votes for each county in the precinct

To understand how the votes were distributed, the code calculates each county's total amount of votes and its percentage. It would be important to understand the reason for having very different amounts of votes in each county. 

### - County that had the largest amount of votes

It is seen from these results that Denver has the largest amount of votes. Compared to other counties and the percentage they got, we can say that everything was decided by the people in Denver. 

### - Number of votes and the percentage of the total votes each candidate received

The main reason for this analysis was to understand who was the winner of the election. The code calculates each candidate's total votes and the proportion it represents of the total votes.

### - Winner candidate

The image is taken directly from the text file that can be obtained by running this code. As it is shown, Diana DeGette won with 272,892 votes and 73.8 percent. She won with more than 50 percent compared to the other candidates. 

## Election Audit Summary

The code that was used for this analysis can be used for other election audits.

1. If we want to know which candidate receives more votes of a certain age, the code can be modified in order to change its scope. We need to take into consideration another column or variable and we can get those results into a text file to be used for deeper analysis. 
2. If there is another election in which there are more counties or candidates and we don't want to show all the results, the code can be modified to show only the top 3, 5, or 10 higher results. 

