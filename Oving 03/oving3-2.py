debug = True

a = 7
b = 4

def add(a,b):
	if debug:
		print("Tallene som legges sammen er %s og %s" % (a,b))
	print(a+b)

add(a,b)
