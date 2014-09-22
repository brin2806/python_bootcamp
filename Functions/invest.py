

def invest(amount, rate, time):
	print ("principal amount: ${}".format(amount))
	print ("annual rate of return : {}".format(rate))
	for n in range (1,time+1):
		print ("year {}: ${}".format(n, amount*((1 + rate)**n)))
		n = n+1

print (invest(2000,0.025,5))	