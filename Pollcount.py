import csv
import os
    

def main():
    election_file= open("election_results.csv","r")
    outfile = open("Result_of_election.txt","w")
    file_reader = csv.reader(election_file)
    list_canidates=[]
    list_of_votes=[]
    list_of_percent=[]
    canidates_dict={}
    win_canidate=""
    win_count=0
    win_percentage=0.0
    total_votes=0
    canidate_results=""
    largest_county=""
    county_res=""
    max_county=0
    list_county=[]
    county_votes={}

    headers = next(file_reader)
    for line in file_reader:
        county= line[1]
        canidate= line[2]
        if(canidate not in list_canidates):
            list_canidates.append(line[2])
            canidates_dict[canidate]=1
        else:
            canidates_dict[canidate]+=1
        if(county not in list_county):
            list_county.append(county)
            county_votes[county]=1
        else:
            county_votes[county]+=1
        total_votes+=1

    election_res=(
        f"\nElection Results\n"
        f"------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------\n"
    )
    outfile.write(election_res)
    county_res=(
            f"\nCounty Results\n"
            f"------\n"
            f"Total Votes: {total_votes:,}\n"
            f"------\n"
        )
    outfile.write(county_res)
    for city in list_county:
        per_count=(f"\n{city}: {round((county_votes[city]/total_votes)*100,1)}% ({county_votes[city]:,})\n")
        print(per_count)
        outfile.write(per_count)
        if(county_votes[city] > max_county):
            max_county=county_votes[city]
            largest_county=city
    write_large=(
        f"\n------\n"
        f"Largest County: {largest_county}\n"
        f"------\n"
    )
    print(write_large)
    outfile.write(write_large)
    overall_canidate_results=(
        f"\n------\n"
        f"Canidacy Results\n"
        f"------\n"
    )
    outfile.write(overall_canidate_results)
    for y in list_canidates:
        
        percent=canidates_dict[y]/total_votes
        percent=round(percent*100,1)
        print(f"{y}: {percent}% ({canidates_dict[y]:,})\n")
        canidate_results=(
            f"\n{y}: {percent}% ({canidates_dict[y]:,})\n"
        )
        if(canidates_dict[y]>win_count) and (percent>win_percentage):
            win_count=canidates_dict[y]
            win_canidate=y
            win_percentage=percent
        outfile.write(canidate_results)
        outfile.write("\n")
    win_summary=(
        f"------\n"
        f"Winner: {win_canidate}\n"
        f"Winning Vote Count: {win_count:,}\n"
        f"Winning Percentage: {win_percentage}%\n"
        "------\n"
    )
    print(win_summary)
    outfile.write(win_summary)
    outfile.close()
    print(list_canidates)
    print(total_votes)
    print(canidates_dict)
    print(county_votes)
    
    
    election_file.close()
main()