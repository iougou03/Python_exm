#!/usr/bin/python
import sys

try:
	fhand = open(str(sys.argv[1]),'r')
	number = sys.argv[2]
except (IndexError,FileNotFoundError):
	fileName=input("type file name :")
	try:
		fhand = open(fileName,'r')
		number = input("type number to watch rank :")
	except FileNotFoundError:
		print("Error! No file!")
		sys.exit()

number =int(number)
count=0
wordCount=dict()

while(True):
	line =fhand.readline()
	if not line: break
	for i in line.split():
		if(wordCount.get(i,"N")=="N"):
			wordCount[i] =1
		else:
			wordCount[i] +=1

topRank= sorted(wordCount.items(),reverse = True, key=lambda item:item[1])


for key, val in topRank:
	rank = f'{key:10}=>{val:>5}'    
	print(rank)
	count += 1
	if(count>number): break

fhand.close()
