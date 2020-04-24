#!/usr/bin/python
import my_pkg.module01 as m1
from my_pkg.module02 import find_common_factor 

def conversion():
	try:
		bi_num = int(input("input binary number : "),2)
		m1.bin_conversion(bi_num)
	except(ValueError):
		bi_num =print("Error, please type binary number")
		conversion()

select_menu = ["conversion","union/intersection","exit ?"]

if __name__ == "__main__":	
	while(True):
		print("Select menu :",end=" ")

		for s, num in zip(select_menu, range(len(select_menu))):
			print("{}){}".format(num+1,s),end=" ")

		try: #get select number	
			answer = int(input(),10)
		except:
			print("please type number")
		
		if(answer == 1):
			conversion()
		elif(answer==2):
			find_common_factor()			
		elif(answer== 3):
			print("exit the program...")
			break
		else:
		 	print("wrong number")
		 	continue




