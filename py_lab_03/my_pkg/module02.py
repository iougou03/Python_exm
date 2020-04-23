#!/usr/bin/python
import re


def find_common_factor():
	int_lst=[]
	for i in range(2):
		try:	
			arr= input("{}st list: ".format(i+1))
			arr = re.findall("[0-9]+",arr)
			arr = list(map(int,arr))
			int_lst.append(arr)
		except:
			print("You should type a list")
			break
	show_unite(int_lst)
	show_inter(int_lst)


def show_unite(lst):
	union = sorted(lst[0]+lst[1])
	print("=> union ",union)


def show_inter(lst):
	inter=list(set(lst[0])&set(lst[1]))
	print("=> intersection ",inter)
