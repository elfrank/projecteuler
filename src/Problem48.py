def SelfPowers(n):
	sum = 0
	for i in range(1,n+1):
		sum = sum + pow(i,i);
	
	c = str(sum)
	digits = c[-10:]
	
	return digits
	
print SelfPowers(1000)