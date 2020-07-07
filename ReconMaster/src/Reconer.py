import sys
import os
import os.path
import glob
from _datetime import datetime


dirPath = input("Enter the root folder: ")
today = (datetime.now().strftime('%Y%m%d_%H%M%S'))
print(today)
infiles = glob.glob(dirPath)

for inf in infiles:
    print("Processing File: "+ inf)
    count = 0
    outfile_Header="BusinessDate|FileName|ColumnName|ColumnValue"    
    columns = ""
    dataLines = []
    infileName=os.path.basename(open(inf).name)
    businessDate = infileName.strip(".dat").split("_")[len(infileName.split("_"))-1]
    #print(businessDate)
    outFolder=os.path.join(os.path.dirname(inf.strip()),("Output_"+today))
    #print("Output Folder: "+outFolder)
    if not (os.path.exists(outFolder)):
        print("Creating Ouput Directory : " + outFolder )
        os.makedirs(outFolder)
    outfilename = os.path.join(outFolder,(infileName.strip(".dat") + "_output.dat"))
    #print(outfilename)
    infile=open(inf,"r")
    outfile = open(outfilename, 'w')
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
    
