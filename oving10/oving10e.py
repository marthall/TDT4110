from skumleskogen import *

print("==============================================================================")

huk = {}
nokler = 0
n = 0
prove_laas = False
trenger = 2
pappanode = 0

def nokkel(huk, n, forrige_n, prove_laas, nokler, trenger):
	print("Dette er en nøkkel")
	nokler += 1
	tilbake(huk, n)
	if nokler >= trenger:
		prove_laas = True
	plukk_opp()
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
			tilbake(huk, n)

	else:
		print("Dette er en lås")
		if nokler >= 1:
			laas_opp()
			nokler -= 1
		else:
			print("Ikke nok nøkler til å låse opp")
			trenger = 1
			tilbake(huk, n)

def stank():
	print("Det stinker")
	tilbake()

def tilbake(huk, n):
	print("Går tilbake")
	if huk[n]["venstre"] == 1 and huk[n]["hoyre"] == 1:
		if huk[pappanode]["forrige_valg"] == "hoyre":
			huk[pappanode]["hoyre"] = 1
		else:
			huk[pappanode]["venstre"] = 1

	elif huk[n]["venstre"] == 2 or huk[n]["hoyre"] == 2:
		if huk[pappanode]["forrige_valg"] == "hoyre":
			huk[pappanode]["hoyre"] = 2
		else:
			huk[pappanode]["venstre"] = 2

	elif huk[n]["venstre"] == 0 and huk[n]["hoyre"] == 0:
		if huk[n]["forrige_valg"] == "hoyre":
			huk[pappanode]["hoyre"] = 2
			print("Pappanoden gikk til høyre for å komme hit")
		else:
			huk[pappanode]["venstre"] = 2
			print("Pappanoden gikk til venstre for å komme hit")
	gaa_tilbake()

def venstre(huk, n):
	print("Går til venstre")
	huk[n]["venstre"] = 1
	huk[n]["forrige_valg"] = "venstre"
	gaa_venstre()

def hoyre(huk, n):
	print("Går til hoyre")
	huk[n]["hoyre"] = 1
	huk[n]["forrige_valg"] = "hoyre"
	gaa_hoyre()



# while not er_utgang():
for i in range(10):
	forrige_n = n
	n = nummer()

	if (n == forrige_n) and (n != 0) and (not er_laas()):
		huk[n]["hoyre"] = 1
		huk[n]["venstre"] = 1

	print("Node nr: \t%i" % n)
	print("Antall nøkler: \t%i" % nokler)

	if n not in huk:
		huk[n] = {"venstre": 0, "hoyre": 0, "forrige_valg": "", "pappanode": forrige_n}

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
			tilbake(huk, n)
	print(huk[n])
	print("")
gaa_ut()