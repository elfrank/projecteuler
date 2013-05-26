import math

def SpecialPythagoreanTriplet():
	for a in range(3,1000):
		for b in range(a+1,1000):
			c = math.sqrt(a*a+b*b)
			if c > b:
				if 1000==(a+b+c):
					#print "%d %d %d" % (a,b,c)
					return a*b*c

print SpecialPythagoreanTriplet()

