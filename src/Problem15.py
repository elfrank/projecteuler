
def BinomialCoefficient(n,k):
	f = {}
	f[1] = 1
	for i in range(2,n+1):
		f[i] = f[i-1] * i
	
	return f[n]/((f[k])*f[n-k])
	
def LatticePaths(n):
	return BinomialCoefficient(n+n,20)
	
print LatticePaths(20)