#!/usr/bin/env python3

#Klaudia Gołębiewska grupa 31A
#Lab06
#gk14366@zut.edu.pl
#przykladowe wywolanie: python Lab06.py -l -L

import re
import sys
import os
import time
import pwd
from stat import *

def checkParameters():
        cat=""
        parOwner=""
        parLong=""
        for i in range(1,len(sys.argv)):
                if(sys.argv[i] != "-l" and sys.argv[i] !="-L"):
                        if (os.path.isdir(sys.argv[i])):
                                cat=sys.argv[i]
                        else:
                                cat="error"

                if(sys.argv[i] == "-l"):
                        parLong=sys.argv[i]
                if(sys.argv[i]=="-L"):
                        parOwner=sys.argv[i]
        return cat,parOwner,parLong


def searchFiles(cat, files,parLong,parOwner):

        for file in sorted(files, key=lambda L: (L.lower(), L)):
                if(file== "." or file== ".."):
                        continue;
                if(parOwner):
                        user=pwd.getpwuid(os.stat(os.path.join(cat,file)).st_uid).pw_name
                        print(user,end =" ")
                if(parLong):
                        getLong(cat,file)
                else:
                        print(file)

def operationOnCatalog(cat,parOwner,parLong):
        if (len(sys.argv)<5):
                if(cat == "error"):
                        sys.exit("bledny katalog")
                else:
                        if(cat==""):
                                cat=os.getcwd()
                files = os.listdir(cat)
                searchFiles(cat,files,parLong,parOwner)
        else:
                 sys.exit("max 3 parametry")

def changeRights(path,words):
        s=""
        if(os.path.isdir(path)):
                s+='d'
        else:
                s+='-'

        for w in words:
                if(w=="0"):
                        s+='---'
                if(w == "1"):
                        s+='--x'
                if(w=="2"):
                        s+= '-w-'
                if (w == "3"):
                        s+= '-wx'
                if (w == "4"):
                        s+= 'r--'
                if (w == "5"):
                        s+= 'r-x'
                if(w == "6"):
                        s+= 'rw-'
                if (w == "7"):
                        s+= 'rwx'

        return s
		
def getLong(cat,file):
        words={}
        path=os.path.join(cat,file)
        statInfo = os.stat(path)
        rights=oct(os.stat(path).st_mode & 0o777)
        words=list(rights[2:])
        changedRights=changeRights(path,words)
        modTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(path)))

        print('{:30s} {:10s} {:19s} {:10s}'.format(file[:30],str(os.stat(path).st_size)[:10] , modTime,changedRights[:10]))


cat,parOwner,parLong=checkParameters()
operationOnCatalog(cat,parOwner,parLong)

