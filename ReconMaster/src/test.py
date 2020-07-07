import sys
import os
import os.path
import glob
from _datetime import datetime
from core.Utils import *


print(getNowDate())
#print(getConfigProperty("INPUTS","input_list_file"))
#inputFileLinks=getInputFiles(getConfigProperty("INPUTS","input_list_file"))
#print(inputFileLinks)
#for fi in inputFileLinks:
#    head, tail = os.path.split(fi)
#   print("Path is : "+head)
#    print("Name is : "+tail)


from pathlib import Path
import arrow


criticalTime = arrow.now().shift(hours=+5).shift(days=-7)
filesPath="D:\\tempDir\\Output_Files"
for item in Path(filesPath).glob('*.gz'):
    if item.is_file():
        print (str(item.absolute()))
        itemTime = arrow.get(item.stat().st_mtime)
        #print(itemTime)
        print(itemTime-criticalTime)
        if itemTime < criticalTime:
            #remove it
            pass