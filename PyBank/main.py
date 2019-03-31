import os 
import csv
#path to data 
csvpath=os.path.join("Resources/budget_data.csv")
months=[]
total=0
gr8INC=0
previous=0
gr8DEC=0
change=[]
#open the file
with open (csvpath,newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",") 
    #skip header
    next(csvreader,None)
    for row in csvreader:
        # net total amount of profit/losses
        total=int(total)+int(row[1])
        #count total number of months
        months.append(row[0])
        change.append(int(row[1])-previous)
        # greatest increase in profits (date and amount)
        if (int(row[1])-previous)>gr8INC:
            gr8INC=(int(row[1])-previous)
            inc_date=row[0]
        # greatest decrease in losses (date and amount)
        if (int(row[1])-previous)<gr8DEC:
            gr8DEC=(int(row[1])-previous)
            dec_date=row[0]
        previous=int(row[1])
# average of the changes 
    del change[0]
    average=round(sum(change)/(len(months)-1),2)
#save to an output file
output=os.path.join("Output/Output.txt")
with open (output,"w") as datafile:
    print("Financial Analysis",file=datafile)
    print("----------------------------",file=datafile)
    print("Total Months:"+str(len(months)),file=datafile)
    print("Total: $"+str(total), file=datafile)
    print("Average Change: $"+str(average),file=datafile)
    print("Greatest Increase in Profits: "+str(inc_date)+" ($"+str(gr8INC)+")", file=datafile)
    print("Greatest Decrease in Profits: ",str(dec_date)+" ($"+str(gr8DEC)+")", file=datafile)
#print summary

with open (output,"r",newline="") as datafile2:
    print(datafile2.read())