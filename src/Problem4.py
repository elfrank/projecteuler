def LargestPalindromeProduct():

	n = 0
	max = 0
	for i in range(1,1000):
		for j in range(1,1000):
			n = i*j
			if isPalindrome(n):
				if n > max:
					max = n
					#print n
	
	return max

def isPalindrome(n):
	w = str(n)
	length = len(w)
	for i in range(0,length/2):
		if w[i] is not w[length-1-i]:
			return False
	return True

print LargestPalindromeProduct()
