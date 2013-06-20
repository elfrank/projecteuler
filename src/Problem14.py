def CollatzSequence(n, i):
	
	while n > 1:
		if 0==n%2:
			n = n*0.5
		else:
			n = 3*n+1
		i = i+1
	
	return i

def LongestCollatzSequence(n):
	
	max_sequence = 0
	max_n = 0
	dict = {}
	for i in range(1,n):
		total = CollatzSequence(i,1)
		if total > max_sequence:
			max_sequence = total
			max_n = i
	
	return max_n
	
#print CollatzSequence(13,1)
print LongestCollatzSequence(1000000)