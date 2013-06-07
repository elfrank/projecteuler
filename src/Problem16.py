def PowerDigitSum(n):
	c = str(1<<n)
	sum = 0;
	for i in range (0,len(c)):
		sum = sum + int(c[i])
	return sum

print PowerDigitSum(1000)