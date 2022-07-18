import datetime
import csv
import os

#Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()

#Print the present time
print("The time right now is", now)

#finalcode
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Election_Analysis","Resources","election_results.csv")
# Open the election results and read the file.
total_votes = 0
candidate_options=[]
candidate_votes = {}
vote_percentage=0
winning_candidate=""
winning_count=0
winning_percentage=0
with open(file_to_load) as election_data:
    print(election_data)
    #To do
    file_reader=csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]+=1
    for candidate_name in candidate_votes:
        vote_percentage = float(candidate_votes[candidate_name]/total_votes*100)
        print(f"{candidate_name}: {vote_percentage:.2f}% ({candidate_votes[candidate_name]:,})")
        if (candidate_votes[candidate_name] > winning_count) and (vote_percentage > winning_percentage):
            winning_count = candidate_votes[candidate_name]
            winning_percentage = vote_percentage
            winning_candidate=candidate_name
    candidate_summary = (f"\nWinner: {winning_candidate}\nWinning Vote Count: {winning_count:,}\nWinning Percentage: {winning_percentage:.1f}%\n")
    print(total_votes)
    print(candidate_options)
    print(candidate_votes)
    print(candidate_summary)



    # __Read and print the header row.
    #headers = next(file_reader)
    #print(headers)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Election_Analysis","Analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Counties in the election:\n---------------- ")

outfile.write("\nArapahoe\nDenver\nJefferson ")

# Close the file
outfile.close()