from math import sin, cos
pi = 3.1415

def koord(r, phi):
	x = r * cos(phi)
	y = r * sin(phi)
	print ("1: (" + format(x, '.2f') + ", " + format(y, '.2f') + ")")

koord(3, pi/2)
koord(2.3, pi/3)
koord(5,0)
#hei