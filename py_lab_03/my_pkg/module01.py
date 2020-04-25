#/usr/bin/python

def conversion():
	try:
		bi_num = int(input("input binary number : "),2)
		bin_conversion(bi_num)
	except(ValueError):
		bi_num =print("Error, please type binary number")
		conversion()
		
def bin_conversion(num):
	print("=> OCT> {}".format(format(num,'o')))
	print("=> DEC> {}".format(format(num,'d')))
	print("=> HEX> {}".format(format(num,'X')))


