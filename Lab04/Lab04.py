#!/usr/bin/python3

#Klaudia Gołębiewska grupa 31A
#Lab04
#gk14366@zut.edu.pl
#wywolanie zad1: python Lab04.py tekst1.txt
#wywolanie zad2: python Lab04.py cipher.txt

import sys
import matplotlib.pyplot as plt
import numpy as np 

def checkParameters():
	if len(sys.argv) == 1:
		sys.exit("Nie podano pliku do odczytania")
	elif len(sys.argv)>2:
		sys.exit("podano za duzo argumentow")
	elif sys.argv[1].endswith('.txt'):
		fileTxt=sys.argv[1]
	else:
		sys.exit("zly format pliku")
	return fileTxt

def checkLetters(char,lettersList,letters):

	if(ord(char)>=ord('A') and ord(char)<=ord('Z') or ord(char)>=ord('a') and ord(char)<=ord('z')):
		letters[char]=0
		lettersList.append(char)
	return letters,lettersList
	
def readFile(fileTxt):
	letters={}
	numberChars=0;
	firstLine=[]
	lettersList=[]
	try:
		with open(fileTxt) as file:
			count = 0
			for line in file:
				count=count+1
				if(fileTxt=="cipher.txt"):
					if(count != 1):
						for char in line:
							numberChars+=1;
							letters,lettersList=checkLetters(char,lettersList,letters)
					else:
						for char in line:
							firstLine.append(char)
				else:
					for char in line:
						numberChars+=1;
						letters,lettersList=checkLetters(char,lettersList,letters)
				
	except FileNotFoundError:
		sys.exit('taki plik nie istnieje')

	
	return numberChars,letters,lettersList,firstLine;


def checkSizeLetter(numberChars,letters,lettersList):
	
	for letter in lettersList:
			letters[letter]+=1
	
	return letters
			
	
		

def countPrecent(numberChars,letters,fileTxt):
	i=0
	tab={}
	listPrecent=[]
	listOfSortedLetters=[]
	for letter in letters:
		tab[letter]=letters[letter]*(100.0/numberChars)
		i=i+tab[letter]
	for letter in sorted(letters, key=letters.get, reverse=True):
		print(letter, letters[letter], tab[letter])
		listOfSortedLetters.append(letter)
		listPrecent.append(tab[letter])
	if(fileTxt!="cipher.txt"):
		displayHist(listOfSortedLetters, listPrecent)
		
	
	return listOfSortedLetters
		

def displayHist(listOfSortedLetters, listPrecent):
	pos = np.arange(len(listOfSortedLetters))
	width = 0.5
	ax = plt.axes()
	ax.set_xticks(pos + (width / 2))
	ax.set_xticklabels(listOfSortedLetters)
	plt.xlabel("litery")
	plt.ylabel("wystepowanie %")
	plt.bar(pos, listPrecent, width, align='center', color='b', edgecolor='red',linewidth=1)
	plt.show()

def decryptLetter(char,listOfSortedLetters,firstLine):
	if char in letters:
		print(firstLine[listOfSortedLetters.index(char)],end='')
	else:
		print(char,end='')
      

def decryptText(listOfSortedLetters,firstLine,fileTxt):
	if(fileTxt=="cipher.txt"):
		try:
			with open(fileTxt) as file:
				count = 0
				for line in file:
					count=count+1
					if(fileTxt=="cipher.txt"):
						if(count != 1):
							for char in line:
								decryptLetter(char,listOfSortedLetters,firstLine)
										
					else:
						sys.exit("bledny plik do odszyfrowania")
				
		except FileNotFoundError:
			print('taki plik nie istnieje')
	
	
fileTxt=checkParameters()	
numberChars,letters,lettersList,firstLine=readFile(fileTxt)
letters=checkSizeLetter(numberChars,letters,lettersList)
listOfSortedLetters=countPrecent(numberChars,letters,fileTxt)
decryptText(listOfSortedLetters,firstLine,fileTxt)