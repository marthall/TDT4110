def antall_alle(filnavn):
	i = 0
	filnavn.seek(0)
	for linje in filnavn:
		# print(linje[-6:-2])
		if linje[-6:-2] == "Alle":
			i += 1
	return i

def gjennomsnitt(filnavn):
	filnavn.seek(0)
	total = 0
	antall = 0
	for linje in filnavn:
		if linje[-6:-2] != "Alle":
			antall += 1
			total += float(list(linje.partition(","))[2])
	return total/antall

def topp_bunn(filnavn):
	filnavn.seek(0)
	topp = 0
	bunn = 50
	for linje in filnavn:
		if linje[-6:-2] != "Alle":
			karakter = float(list(linje.partition(","))[2])
			if karakter > topp:
				topp = karakter
			if karakter < bunn:
				bunn = karakter
	return topp, bunn

def main():
	filnavn = open("poenggrenser_2011.csv", "r")
	print("Antall:\t\t%i" % antall_alle(filnavn))
	print("Gjennomsnitt:\t%.4f" % gjennomsnitt(filnavn))
	# topp, bunn = topp_bunn(filnavn)
	print("Topp:\t\t%.1f\nBunn:\t\t%.1f" % topp_bunn(filnavn))
	filnavn.close()

main()