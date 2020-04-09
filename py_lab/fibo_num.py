#!/usr/bin/python

n = input("Fibonacci number? ")
 
def fibo(i):
	if(i==0 or i==1):
		return 1
	else:
		return fibo(i-1)+fibo(i-2)

n=int(n)
for i in range(n):
	if(i == n-1):
		print(fibo(i))
		final = fibo(i)
		break
	print(fibo(i),end=",")

print("F{0}={1}".format(n,final))
