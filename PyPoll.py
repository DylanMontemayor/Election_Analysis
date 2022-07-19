import csv
import os

#finalcode
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Election_Analysis","Resources","election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Election_Analysis","Analysis", "election_analysis.txt")

total_votes = 0
candidate_options=[]
candidate_votes = {}
vote_percentage=0
winning_candidate=""
winning_count=0
winning_percentage=0
# Open the election results and read the file.
with open(file_to_load) as election_data:
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
# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save,"w") as txt_file:
    # Write some data to the file.
    txt_file.write("\nElection Results:\n----------------------")

    txt_file.write(f"\nTotal Votes: {total_votes:,}\n----------------------\n")

    for candidate_name in candidate_votes:
        vote_percentage = float(candidate_votes[candidate_name]/total_votes*100)
        candidate_results=(f"{candidate_name}: {vote_percentage:.2f}% ({candidate_votes[candidate_name]:,})\n")
        txt_file.write(candidate_results)
        if (candidate_votes[candidate_name] > winning_count) and (vote_percentage > winning_percentage):
            winning_count = candidate_votes[candidate_name]
            winning_percentage = vote_percentage
            winning_candidate=candidate_name
    candidate_summary = (f"\nWinner: {winning_candidate}\nWinning Vote Count: {winning_count:,}\nWinning Percentage: {winning_percentage:.1f}%\n")
    print(candidate_summary)
    txt_file.write(candidate_summary)
