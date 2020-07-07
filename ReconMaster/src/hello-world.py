import os
import sys
import datetime

infile = open('D:\Mhub_mrtg_loan_20200610.dat', 'r')
count = 0
outfile_Header="BusinessDate|FileName|ColumnName|ColumnValue"
outfile = open('D:\Output.dat', 'w')
columns = ""
dataLines = []
infileName=os.path.basename(infile.name).strip()
businessDate = infileName.strip(".dat").split("_")[len(infileName.split("_"))-1]
print(businessDate)
i=0
while True:    
    # Get next line from file 
    i = i+1
    line = infile.readline()
    str = line.strip()
    if str.startswith("HDR"):
            continue    
    
    if str.startswith("TRL"):
            continue
    
    if (i == 2):
        columns = line.strip()
    else:   
        dataLines.append(line)
        
        
    # if line is empty 
    # end of file is reached 
    if not line: 
        break
   # print("Line{}: {}".format(count, line.strip())) 
 
infile.close()

#Parsing and Writing to Outfile
outfile.write(outfile_Header+ "\n")
print(columns)
colNamesplits=columns.split("|")

for li in dataLines:
    print(li)
    if(len(li) > 0):
        linesplits=li.split("|")
        counter = 0
        for data in linesplits:
             outfile.write((businessDate + "|" + infileName + "|" + colNamesplits[counter] + "|" + data).strip() + "\n")
             counter = counter + 1;
    
outfile.close()



