#!/usr/bin/python
def SumOfMultiplesOf3And5():
	sum = 0
	i = 3

	while i < 1000:
		
		if 0==i%3 or 0==i%5:
			sum += i
		
		i = i+1
	
	return sum


print SumOfMultiplesOf3And5()
