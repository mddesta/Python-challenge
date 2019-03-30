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
#print result 
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {len(months)}')
print(f'Total: ${total}')
print(f'Average  Change: ${average}')
print(f'Greatest Increase in Profits: {inc_date} (${gr8INC})')
print(f'Greatest Decrease in Profits: {dec_date} (${gr8DEC})')
#save to an output file
output=os.path.join("Output/Output.csv")
with open (output,"w",newline="") as datafile:
    writer=csv.writer(datafile)
    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------------------"])
    writer.writerow(["Total Months",len(months)])
    writer.writerow(["Total","$"+str(total)])
    writer.writerow(["Average Change", "$"+str(average)])
    writer.writerow(["Greatest Increase in Profits", inc_date, "$"+str(gr8INC)])
    writer.writerow(["Greatest Decrease in Profits",dec_date,"$"+str(gr8DEC)])
  