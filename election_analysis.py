import csv
import os



file_to_load = os.path.join("Resources", "election_results.csv")

total_votes = 0
candidates = []

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)




    # read and print header row

    headers = next(file_reader)
    print(headers)

    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates.append(candidate_name)

print(candidates)
print(total_votes)















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