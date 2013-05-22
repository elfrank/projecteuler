from math import sqrt

def LargestPrimeFactor(n):
	i = 2
	number = n
	largest_factor = 0
	while i < sqrt(n):
		if 0==number%i:
			#print i
			largest_factor = i
			number = number/i
		else:
			i = i+1
	
	return largest_factor

print LargestPrimeFactor(600851475143)
