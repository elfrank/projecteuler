def SumSquareDifference(n):
	sum_of_squares = 0
	squares_of_sum = 0
	for i in range(1,n+1):
		sum_of_squares = sum_of_squares+i*i
		squares_of_sum = squares_of_sum+i
	
	squares_of_sum = squares_of_sum*squares_of_sum

	return squares_of_sum-sum_of_squares

print SumSquareDifference(100)
