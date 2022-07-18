# The data we need to retrieve

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote. 

#Import the datetime class from the datatime module
import datetime
import csv
import os

#Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()

#Print the present time
print("The time right now is", now)

#Method1
# c --file_to_load = 'Resources/election_results.csv'
#Open the election results and read the file
# c --election_data = open(file_to_load,'r')
#To do: perform analysis.

#Close the file
# c --election_data.close()

#Method2
#Open the election results and read the file
# c --with open(file_to_load) as election_data:
#To do: perform analysis.
    # c --print(election_data)

#finalcode
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Election_Analysis","Resources","election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    print(election_data)
    #To do
    file_reader=csv.reader(election_data)
    for row in next(file_reader):
        print(row)


    # __Read and print the header row.
    #headers = next(file_reader)
    #print(headers)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Election_Analysis","analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Counties in the election:\n---------------- ")

outfile.write("\nArapahoe\nDenver\nJefferson ")

# Close the file
outfile.close()