def biokof(n, k):
	a = 1
	for i in range(k):
		a *= n
		n -= 1
	b = 1
	for i in range(k):
		b *= k
		k -= 1
	return a/b

x = biokof(13, 2)
y = biokof(4,2)
z = biokof(11,1)
q = biokof(4,1)

print(format((x*y*y*z*q/2598960), '.5f'))