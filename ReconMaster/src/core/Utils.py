from _datetime import datetime
import configparser
import sys
import os
import os.path
import glob
import gzip
import shutil


def getNowDate():
    return (datetime.now().strftime('%Y%m%d_%H%M%S'))

def getPostDate(daysfuture):
    return (datetime.now())

def getConfigProperty(section_name, key_name):    
    config = configparser.RawConfigParser()
    config.read('config.properties')
    print("CONFIG PROPERTY: "+section_name+" : "+key_name+" : "+config.get(section_name,key_name))
    return config.get(section_name,key_name)

def getInputFiles(filePath):
    infile=open(filePath,'r')
    return infile.readlines()

def parseFileLinks(fileLinks,busDate,busDateParam):
    parsedLinks = []
    for link in fileLinks :
        parsedLinks.append(link.strip().replace(busDateParam,busDate))
    return parsedLinks

def mapColumnandRow(columns,row):
    mappedLines = []
    columnz=columns.split("|")
    counter = 0
    for li in row.split("|"):
        #print(columnz[counter] + "|" + li.strip())
        mappedLines.append(columnz[counter] + "|" + li.strip())
        counter = counter + 1
    return mappedLines

def gzipOldFiles(dirPath):
    files = glob.glob(os.path.join(dirPath+"*.dat"))
    print(files)
    filecount = len(files) 
    print(filecount, " Old Files Present in Output Directory")
    if (len(files) > 0):
        for f in files:
           with open(f, 'rb') as f_in, gzip.open(f+".gz", 'wb') as f_out:
               shutil.copyfileobj(f_in, f_out)
           f_in.close()
           f_out.close()
           print("Deleting File : "+f)
           os.remove(f)