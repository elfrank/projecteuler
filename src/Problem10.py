import math

def SummationOfPrimes(n):
	
	sum = 0
	isPrime = [True]*(n+1)
	isPrime[0] = isPrime[1] = False

	for i in range(2,int(math.sqrt(n))+1):
		if isPrime[i]:
			for j in range(i+1,n+1):
				if j%i==0:
					isPrime[j] = False
	
	
	for i in range(len(isPrime)):
		#print "%d:%i" % (i,isPrime[i])
		if isPrime[i]:
			sum = sum + i
	
	return sum

print SummationOfPrimes(2000000)

