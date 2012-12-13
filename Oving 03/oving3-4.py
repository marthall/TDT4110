def pris(alder):
	if alder < 5:
		return ("Gratis")
	elif alder >= 6 and alder <= 15:
		return ("10 kr")
	elif alder >= 16 and alder <= 20:
		return ("20 kr")
	elif alder >= 21 and alder <= 25:
		return ("30 kr")
	elif alder >= 26 and alder <= 60:
		return ("40 kr")
	elif alder > 60:
		return ("Gratis")

def skriv(alder):
	a = pris(alder)
	print("Pris: " + a)

alder = int((input("Alder: ")))
skriv(alder)