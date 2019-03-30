import os
import csv
csvpath=os.path.join("Resources/election_data.csv.txt")
total=0
khan=0
correy=0
li=0
otooley=0
o="O'Tooley"
#open the file
with open (csvpath,newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",") 
    #skip header
    next(csvreader,None)
    for row in csvreader:
        #Calculate total votes
        total=total+1
        #calculate total voles for Khan
        if row[2]=="Khan":
            khan=khan+1
        #calculate total voles for Coorey
        if row [2]=="Correy":
            correy=correy+1
        #calculate total voles for Li
        if row[2]=="Li":
            li=li+1
        #calculate total voles for O'Tooley
        if row[2]=="O'Tooley":
            otooley=otooley+1
win=max(khan,correy,li,otooley)
if khan==win:
    winner="Khan"
if correy==win:
    winner="Coorey"
if li==win:
    winner="Li"
if otooley==win:
    winner=o   
#print summary           
print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {total}')
print(f'-------------------------')
print(f'Khan: {round((khan/total)*100,3)}% ({khan})')
print(f'Coorey: {round((correy/total)*100,3)}% ({correy})')
print(f'Li: {round((li/total)*100,3)}% ({li})')
print(f'{o}: {round((otooley/total)*100,3)}% ({otooley})')
print(f'-------------------------')
print(f'Winner: {winner}')
print(f'-------------------------')
#export
output=os.path.join("Output/Output.csv")
with open (output,"w",newline="") as datafile:
    writer=csv.writer(datafile)
    writer.writerow(["Election Results"])
    writer.writerow(["-------------------------"])
    writer.writerow(["Total Votes", total])
    writer.writerow(["-------------------------"])
    writer.writerow(["Khan",str(round((khan/total)*100,3))+"%",khan])
    writer.writerow(["Coorey",str(round((correy/total)*100,3))+"%",correy])
    writer.writerow(["Li",str(round((li/total)*100,3))+"%",li])
    writer.writerow([str(o),str(round((otooley/total)*100,3))+"%",otooley])
    writer.writerow(["-------------------------"])
    writer.writerow(["Winner",str(winner)])
    writer.writerow(["-------------------------"])
