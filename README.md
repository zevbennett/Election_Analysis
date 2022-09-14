# Election_Analysis
Analysis of votes in a recent presidential election 


## Project Overview

1. Calulate total number of votes cast
2. Get a complete list of candidates who recieved votes
3. Calculate total number of votes each candidate recieved
4. Calculate percentage of votes each candidate won
5. Determine the winner of the election by popular vote

## Resources

- Data source: election_results.csv
- Software: Python3, VScode

## Summary

The results of the election show that:

- There were 369,711 votes cast.
- The candidates were:
   1. Charles Caster Tockham
   2. Diana DeGette
   3. Raymon Anthony Doane
- The results were
  - Charles Casper Stockham recieved 23.0% of the vote and 85,213 votes
  - Diana DeGette recieved 73.8% of the vote and 272,892 votes
  - Raymon Anthony Doane recieved 3.1% of the vote and 11,606 votes
- The winner was Diana DeGette with 73.8% of the vote and 272,892 votes.


------

# Deliverable 3: Final Analysis

## Purpose of Election Audit:

The purpose of this analysis is to

1. Determine the winner of the election
2. Find the county with the highest voter turnout
3. Calculate the percentage of the vote all candidates got
4. Calculate the percentage of the vote all counties got

## Election Audit Results:

- Total Votes: 369,711
- Votes by County
  - Jefferson has 10.5% of the vote and 38,855 votes.
  - Denver has 82.8% of the vote and 306,055 votes.
  - Arapahoe has 6.7% of the vote and 24,801 votes.
- Votes by candidate
  - Charles Casper Stockham: 23.0% with 85,213 votes.
  - Diana DeGette: 73.8% with 272,892 votes.
  - Raymon Anthony Doane: 3.1% with 11,606 votes.
- Winner of the Election: Diana DeGette
- County with the most votes: Denver

## Summary:

This script can be used to analyise any election, with any number of candidates and counties. With the caveat that the data must be formatted in a .csv file as follows [Ballot id, County, Candidate].

The modifications necessary would be to change the path to the csv file, and ensure that the file was named election_results.csv, or change the name in the scrip too. 


 ![](Resources/Screen%20Shot%202022-09-14%20at%203.58.17%20PM.png) 

 As you can see here this path would need to be modified. 

 One could also analyse the percentage of votes for each candidate each county voted for. ie, Denver voted as follows (20% for X candidate and 80% for Y candidate)
