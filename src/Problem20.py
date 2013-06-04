def FactorialDigitSum(n):
	
	factorial = 1
	for i in range(2,n+1):
		factorial = factorial * i
	
	digits = str(factorial)
	sum = 0
	for i in range(0,len(digits)):
		sum = sum+int(digits[i])
	
	return sum
	
print FactorialDigitSum(100)