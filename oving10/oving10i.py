from skumleskogen2 import *

hukommelse = {}
nokkel = 0

while not er_utgang():

	n = nummer()

	if n not in hukommelse:
		hukommelse[n] = {"venstre": False, "hoyre": False}
	
	if er_nokkel():
		plukk_opp()
		nokkel += 1
	
	elif er_laas():
		if nokkel >= 1:
			laas_opp()
			nokkel -= 1
		gaa_tilbake()

	elif er_superlaas():
		if nokkel >= 2:
			laas_opp()
		gaa_tilbake()

	elif er_stank():
		gaa_tilbake()
	
	elif er_inngang() and hukommelse[n]["venstre"] == True and hukommelse[n]["hoyre"] == True:
		hukommelse = {}

	elif er_vanlig() or er_inngang():
		if hukommelse[n]["hoyre"] == False:
			gaa_hoyre()
			hukommelse[n]["hoyre"] = True
		elif hukommelse[n]["venstre"] == False:
			gaa_venstre()
			hukommelse[n]["venstre"] = True
		else:
			gaa_tilbake()

gaa_ut()
print("Victory")