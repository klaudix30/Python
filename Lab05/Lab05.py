#-*-coding: utf-8 -*-
#!/usr/bin/python3

#Klaudia Gołębiewska grupa 31A
#Lab05
#gk14366@zut.edu.pl
#przykladowe wywolanie: python Lab05.py sciezka_biezacy_katalog sciezka_biezacy_katalog\folder 

import sys
import os
from collections import defaultdict
import re


def checkParameters():
	directory=[]
	if len(sys.argv) == 1:
		sys.exit("Nie podano katalogu")
	else:
		for dir in sys.argv:
			if os.path.isdir(dir):
				directory.append(dir)
			
	return directory

def checkSizeFile(entry):
	if os.path.isfile(entry):
		file = open(entry,"rb")
		content = file.read()
		return content


def displayDuplicate(duplicatedFile):
	
	for duplicate in duplicatedFile:
		for key in duplicate:
			if(len(duplicate[key])>1):
				print('duplicated: (size {}b)'.format(key*len(duplicate[key])))
				for i in duplicate[key]:
					print(i)

def checkDuplicates(duplicatedFile,path):
	for key in duplicatedFile:
		for i in duplicatedFile[key]:
			if(path==i):
				return True
	
def searchDuplicate(path,content,sizeOfFile,directory,duplicated):
	
	for i in range(len(sizeOfFile)):
		for k in range(len(sizeOfFile)):
			if(content[i]==content[k]):
				if checkDuplicates(duplicated,path[i]) is None:
					if sizeOfFile[i] not in duplicated:
						duplicated[sizeOfFile[i]].append(path[i])
					else:
						duplicated[sizeOfFile[i]].append(path[i])	
	return duplicated
	
def searchFiles(directory):
	duplicated=defaultdict(list)
	content=[]
	path=[]
	sizeOfFile=[]
	duplicatedFile=[]
	for dir in directory:
		entries = os.listdir(dir)
		for entry in entries:
			path.append(os.path.join(dir,entry))
			content.append(checkSizeFile(path[-1]))
			sizeOfFile.append(os.stat(path[-1]).st_size)
	duplicatedFile.append(searchDuplicate(path,content,sizeOfFile,dir,duplicated))
	
	return duplicatedFile

directory=checkParameters()
duplicatedFile=searchFiles(directory)
displayDuplicate(duplicatedFile)