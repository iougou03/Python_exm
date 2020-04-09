#!/usr/bin/python

N= input("Type number :")

N=int(N)
sum =int(0)
for i in range(N):
	temp = input("Add... :")
	sum += int(temp)

avr = sum/N

print("Average that you typed :%.2f" % avr)

