def SumOfEvenFibonacciNumbers():

	sum = 0

	x = 0
	y = 1
	z = 0

	while z < 4000000:
		z = x+y
		y = x
		x = z
			
		if(z>4000000):
			break

		if(0==z%2):
			sum += z	
	return sum

print SumOfEvenFibonacciNumbers()
