def SmallestMultiple(n):

	found = False
	i = n
	while not found:
		i = i+n
		for j in range(3,n+1):
			found = True
			if 0!=i%j:
				found = False
				break
	return i

print SmallestMultiple(20)
