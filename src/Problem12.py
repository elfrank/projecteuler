import math

def GetDivisorsNumber(n):
	total = 0
	for i in range(1,int(math.sqrt(n))):
		if 0 == n%i:
			total = total + 1
	return total*2

def HighlyDivisibleTriangularNumber(n):
	
	n_divisors = 0
	triangle = 0
	i = 0
	
	while n_divisors <= n:
		triangle_sum = 0
		triangle = triangle + 1
		triangle_sum = int((triangle*(triangle+1))*0.5)
		n_divisors = GetDivisorsNumber(triangle_sum)
	
	return triangle_sum

print HighlyDivisibleTriangularNumber(500)