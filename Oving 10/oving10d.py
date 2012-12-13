from skumleskogen import *

print("===================================================================")

huk = {}
nokler = 0
n = 0
prove_laas = False
trenger = 2

def nokkel(huk, n, forrige_n, prove_laas, nokler, trenger):
	print("Dette er en nøkkel")
	plukk_opp()
	nokler += 1
	tilbake(huk, n, 1)
	if nokler >= trenger:
		prove_laas = True
	print("Går tilbake")

def laas(huk, n, forrige_n, nokler, trenger):
	if er_superlaas():
		print("Dette er en superlås")
		if nokler >= 2:
			laas_opp()
			nokler -= 2
		else:
			print("Ikke nok nøkler til å låse opp")
			trenger = 2 - nokler
			tilbake(huk, n, 2)

	else:
		print("Dette er en lås")
		if nokler >= 1:
			laas_opp()
			nokler -= 1
		else:
			print("Ikke nok nøkler til å låse opp")
			trenger = 1
			tilbake(huk, n, 2)

def stank():
	print("Det stinker")
	tilbake()

def tilbake(huk, n, forrige_n):
	gaa_tilbake()
	if huk[n]["venstre"] == 1 and huk[n]["hoyre"] == 1:
		forrige_valg(huk, forrige_n, 1)
	elif huk[n]["venstre"] == 2 or huk[n]["hoyre"] == 2:
		forrige_valg(huk, forrige_n, 2)

def forrige_valg(huk, n, tilstand):
	if huk[n]["forrige_valg"] == "hoyre":
		huk[n]["hoyre"] = tilstand
	else:
		huk[n]["venstre"] = tilstand

def venstre(huk, n):
	gaa_venstre()
	huk[n]["venstre"] = 1

def hoyre(huk, n):
	gaa_hoyre()
	huk[n]["hoyre"] = 1



# while not er_utgang():
for i in range(20):
	forrige_n = n
	n = nummer()

	if (n == forrige_n) and (n != 0) and (not er_laas()):
		huk[n]["hoyre"] = 1
		huk[n]["venstre"] = 1

	print("Node nr: \t%i" % n)
	print("Antall nøkler: \t%i" % nokler)

	if n not in huk:
		huk[n] = {"venstre": 0, "hoyre": 0, "forrige_valg": ""}

	if er_nokkel():
		nokkel(huk, n, forrige_n, prove_laas, nokler, trenger)

	elif er_laas():
		laas(huk, n, forrige_n, nokler, trenger)

	elif er_stank():
		stank()

	elif er_vanlig() or er_inngang():
		if (prove_laas and huk[n]["venstre"] == 2) or huk[n]["venstre"] == 0:
			venstre(huk, n)
		elif (prove_laas and huk[n]["hoyre"] == 2) or huk[n]["hoyre"] == 0:
			hoyre(huk, n)
		else:
			tilbake(huk, n, 1)
	print(huk[n])
	print("")
gaa_ut()