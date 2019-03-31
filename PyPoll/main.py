import os
import csv
csvpath=os.path.join("Resources/election_data.csv")
candidates=[]
total=0
#create dictionary for votes per candidate
candidate_vote={}
#read the data 
with open (csvpath,newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",") 
    #skip header
    next(csvreader,None)
    for row in csvreader:
        #Calculate total votes
        total=total+1
        #find the votes for each candidate 
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_vote[row[2]]=0
        candidate_vote[row[2]]=candidate_vote[row[2]]+1
#export
output=os.path.join("Output/output.txt")
with open (output,"w") as datafile:
    print("Election Results",file=datafile)
    print("-------------------------",file=datafile)
    print("Total Votes: "+str(total), file=datafile)
    print("-------------------------",file=datafile)
    for x in candidates:
        print(str(x)+" "+str("%.3f" % ((candidate_vote[x]/total)*100))+"% ("+str((candidate_vote[x]))+")", file=datafile)
    print("-------------------------", file=datafile)
    #print Winner
    win_num=0
    for x in candidates: 
        if candidate_vote[x]>win_num:
            win_num=candidate_vote[x]
            winner=x
    print("winner: "+str(winner), file=datafile)
    print("-------------------------",file=datafile)
#print summary
with open (output,"r",newline="") as datafile2:
    print(datafile2.read())