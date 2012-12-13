def binomial_coefficent(n, k):
	return factorial(n)/(factorial(k)*factorial(n-k))

def factorial(n):
	fac = 1
	for i in range(n,0,-1):
		fac *= i
	return fac

q = binomial_coefficent(13, 2)
r = binomial_coefficent(4,2)
s = binomial_coefficent(11,1)
t = binomial_coefficent(4,1)

possible_two_pairs = q*(r**2)*s*t
possible_hands = 2598960
prob = 100*possible_two_pairs/possible_hands


print("%.2f%%" % prob)