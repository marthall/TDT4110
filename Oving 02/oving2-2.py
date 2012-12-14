x = 5
y = 3
def main() :
	x = 7
	y = 3
	print(x, y)			# Disse tallene er de lokale verdiene til funksjonen 'main()'
	miks(y, x)
	tull()
	print(x, y,)		# Dette er igjen 'main()'s verdier

def miks(x, y):
	x = 5
	y = 4
	print(x, y,)		# Disse tallene er de lokale verdiene til funkjsonen 'miks'

def tull():
	print(x, y,)		# Siden 'tull()' ikke har noen lokale verdier printer den ut de globale verdiene

main ()