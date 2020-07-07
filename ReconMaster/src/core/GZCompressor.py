import sys
import os
import os.path
import glob
from _datetime import datetime
from Utils import *


#PREREQUISTE
#GZIP OLD FILES IN OUTPUT DIRECTORY
outFileDir = getConfigProperty("INPUTS","output_directory")
if (os.path.exists(outFileDir)):
    gzipOldFiles(outFileDir)
    print("Compression Completed!!!")


