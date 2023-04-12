import os
import csv

# create csv path so we can read it
csvpath = os.path.join('Resources', 'election_data.csv')

# open and read csv
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csv_reader)

    # create a list of all the candidates using a for loop 
    candidates = [row[2] for row in csv_reader]

    # find how many total votes by counting the len of the candidates list
    total_votes = len(candidates)

    # create empty dict to store candidate names and number of votes received
    votes_dict = {}

    # for loop to iterate through candidates list 
    for candidate in candidates:

        # if they are already in the dictionary, add 1 vote to their name
        if votes_dict.get(candidate):
            votes_dict[candidate] += 1

        # if they are not in the dictionary already, add them and start them with 1 vote
        else:
            votes_dict[candidate] = 1
    
    #second method of just printing the results and add them to csv as full quotes not variable
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, votes in votes_dict.items():
        print(f"{candidate}: {round(votes/total_votes *100, 3)}% ({votes})")

    print("-------------------------")

    print(f"Winner: {max(set(candidates), key=candidates.count)}")

    print("-------------------------")

# create path for writing to a csv
output_path = os.path.join("analysis", "analysis.csv")

# open the new csv 
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile)

    # write the results to the csv
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    csvwriter.writerow(["-------------------------"])
    for candidate, votes in votes_dict.items():
        csvwriter.writerow([f"{candidate}: {round(votes/total_votes *100, 3)}% ({votes})"])

    csvwriter.writerow(["-------------------------"])

    csvwriter.writerow([f"Winner: {max(set(candidates), key=candidates.count)}"])

    csvwriter.writerow(["-------------------------"])