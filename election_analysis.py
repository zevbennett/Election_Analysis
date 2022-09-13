import csv
import os

# import file

file_to_load = os.path.join("Resources", "election_results.csv")

# initialize total vote counter
total_votes = 0

# initalize candidate list

candidates = []

# initialize candidate vote counter dictionary

candidate_votes = {}

# for printing winning candidate

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# analysis


with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)




    # read and print header row

    headers = next(file_reader)
   

    for row in file_reader:

        total_votes += 1

        candidate_name = row[2]


        if candidate_name not in candidates:

            candidates.append(candidate_name)

            candidate_votes[candidate_name] = 0


        candidate_votes[candidate_name] += 1

    for candidate in candidate_votes:

        votes = candidate_votes[candidate]

        vote_percentage = round(float(votes)/float(total_votes)*100, 1)

        if (votes > winning_count) and (vote_percentage > winning_percentage):

            winning_count, winning_percentage = votes, vote_percentage

            winning_candidate = candidate

    

        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote: {winning_count}\n"
    f"Winning Percentage: {winning_percentage}\n"
    f"------------------------"
    )

print(winning_candidate_summary)



















#create a text file to write results to 

file_to_save = os.path.join("analysis", "election_analysis.txt")







# create file


outfile = open(file_to_save, "w")

# write to file

outfile.write("Counties in the Election\n------------------------\n")
outfile.write("Arapahoe\nDenver\nJefferson")
# close the file

outfile.close()




# # The data we need to retrieve
# 1. The total number of votes cast

# 2. A complelte list of candidates who received votes
# 3. percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of election based on popular vote.