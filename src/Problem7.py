def Prime10001st(n):
	i = 4
	count = 2
	isPrime = True
	while count < n:
		i=i+1
		
		for j in range(2,i):
			if 0==i%j:
				isPrime = False
				break
		if isPrime:
			count = count+1
		else:
			isPrime = True
		
		#print "i:%d, count:%d"%(i,count)
	
	return i

print Prime10001st(10001)
