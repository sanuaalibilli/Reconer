import sys
import os
import os.path
import glob
from _datetime import datetime
from Utils import *



#GET INPUT FILE LINKS FROM CONFIG.PROPERTIES
inputFileLinks = getInputFiles(getConfigProperty("INPUTS","input_list_file").strip())


#PARSE INPUT FILE LINKS TO ACTUAL FILE LINKS BY SUBSTITUTING BUSINESS DATE
businessDate = getConfigProperty("INPUTS","business_date")
businessDate_param = getConfigProperty("INPUTS","business_date_param")
parsedInFileLinks = parseFileLinks(inputFileLinks,businessDate,businessDate_param)
print(parsedInFileLinks)

#ITERATOR FOR PROCESSING FILES
for infile in parsedInFileLinks:
    print("PROCESSING FILE : " + infile)
    #CHECK IF FILE EXISTS AND OPEN IT FOR PROCESING
    if not (os.path.exists(infile)):
        print("File Doesnot Exist : " + infile )
        continue
    openInfile = open(infile,"r")
    
    #PREPARE OUTPUT DIRECTORY AND OUT FILE    
    outFileDir = getConfigProperty("INPUTS","output_directory")
    path, name = os.path.split(infile)
    outFileName = getConfigProperty("INPUTS","output_file_prefix")+"_"+name.strip()
    outFileAbsPath=os.path.join(outFileDir,outFileName)
    print("Using Ouput File : " + outFileAbsPath)
    #CREATE OUTPUTFILE DIRECTORY STRUCTURE IF NOT PRESENT
    if not (os.path.exists(outFileDir)):
        print("Output Directory Does not Exist : " + outFileDir )
        print("Creating Output Directory : " + outFileDir )
        os.makedirs(outFileDir)
    #OPEN OUT FILE
    openOutfile = open(outFileAbsPath,"w")
    #ADD HEADERS TO OUTFILE
    openOutfile.write(getConfigProperty("INPUTS","output_file_header")+"\n")
    #READ LINE BY LINE
    i=0 #line counter
    coulmns = "" #variable to store the column names
    while True:
        i = i+1
        line = openInfile.readline()
        str = line.strip()
        
        #BREAK THE LOOP ON END OF FILE
        if not line: 
            break
        
        #SKIPPING HEADER LINE IN FILE
        if str.startswith("HDR"):
           continue    
        
        #SKIPPING FOOTER LINE IN FILE
        if str.startswith("TRL"):
           continue   
        
        #this line is the column names from the input file
        if (i == 2):
           columns = line.strip() 
           print(columns)
        else:
            mappedLine = mapColumnandRow(columns,line)
            for data in mappedLine:
                out_row = businessDate + "|" + name + "|" + data
                openOutfile.write((out_row.strip())+ "\n")
        
               
    #CLOSE OUT FILE
    openOutfile.close()
    #CLOSE THE IN FILE
    openInfile.close()
    