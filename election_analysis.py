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

#create a text file to write results to 

file_to_save = os.path.join("analysis", "election_analysis.txt")

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


with open(file_to_save, "w") as txt_file:

        # Print the final vote count to the terminal.

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")

    print(election_results, end="")
    
    # Save the final vote count to the text file.


    txt_file.write(election_results)


    # analysis of the election row by row

    
    for candidate in candidate_votes:

        votes = candidate_votes[candidate]

        vote_percentage = round(float(votes)/float(total_votes)*100, 1)



        if (votes > winning_count) and (vote_percentage > winning_percentage):

            winning_count, winning_percentage = votes, vote_percentage

            winning_candidate = candidate

    
    # write the results of the election by candidate to the text file


        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        txt_file.write(candidate_results)
        #print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")


# this is for checking the results by printing them to the terminal

winning_candidate_summary = (
    f"------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote: {winning_count}\n"
    f"Winning Percentage: {winning_percentage}\n"
    f"------------------------"
    )

#print(winning_candidate_summary)



























# create file


# write to file






# Save the final vote count to the text file.


# candidate results


# winner & statistics









# close the file




# # The data we need to retrieve
# 1. The total number of votes cast

# 2. A complelte list of candidates who received votes
# 3. percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of election based on popular vote.