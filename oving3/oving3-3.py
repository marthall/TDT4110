from math import pi

def sirkel(r):
	r = float(r)
	a = pi*r*r
	a = format(a, '.2f')
	o = 2*pi*r
	o = format(o, '.2f')
	print("Radius:", r)
	print("Areal:", a)
	print("Omkrets:", o)

sirkel(10)
print("10 er et argument")

a = 1

def foo ( a ) :
	a = a ** 2
	print ( a )

foo ( 2)
print ( a )

print("Fordi den første funksjonen tar inn argumentet a=2,")
print("imens print fortsatt bruker den globale verdien.")
