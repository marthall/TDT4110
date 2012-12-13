from skumleskogen import *

hukommelse = {}
nokkel = 0
steg = 0

nodeliste = []
# nokkelnoder = []
# laasenoder = []
# superlaasenoder = []

while not er_utgang():

	n = nummer()
	nodeliste.append(n)

	if n not in hukommelse:
		hukommelse[n] = {"venstre": False, "hoyre": False, "venstre_tom": False, "hoyre_tom": False, "siste_steg": ""}
	
	if er_nokkel():
		# nokkelnoder.append(n)
		plukk_opp()
		nokkel += 1
	
	elif (er_laas() and not er_superlaas()):
		# laasenoder.append(n)
		if nokkel == 1:
			laas_opp()
			nokkel -= 1
		else:
			gaa_tilbake()
			steg += 1
			if hukommelse[nummer()]["siste_steg"] == "hoyre":
				hukommelse[nummer()]["hoyre_tom"] = True
			elif hukommelse[nummer()]["siste_steg"] == "venstre":
				hukommelse[nummer()]["hoyre_tom"] = True
			else:
				print("Fail")
				break

	elif er_superlaas():	
		# superlaasenoder.append(n)
		if nokkel == 2:
			laas_opp()
			nokkel -= 1
		else:
			forrige_node = n
			gaa_tilbake()
			steg += 1
			if hukommelse[nummer()]["siste_steg"] == "hoyre":
				if hukommelse[n]["hoyre_tom"] and hukommelse[n]["venstre_tom"]:
					hukommelse[nummer()]["hoyre_tom"] = True
			elif hukommelse[nummer()]["siste_steg"] == "venstre":
				if hukommelse[n]["hoyre_tom"] and hukommelse[n]["venstre_tom"]:
					hukommelse[nummer()]["hoyre_tom"] = True
			else:
				print("Fail")
				break

	elif er_stank():
		gaa_tilbake()
		if hukommelse[nummer()]["siste_steg"] == "hoyre":
			hukommelse[nummer()]["hoyre_tom"] = True
		elif hukommelse[nummer()]["siste_steg"] == "venstre":
			hukommelse[nummer()]["hoyre_tom"] = True
		else:
			print("Fail")
			break

	elif er_inngang() and hukommelse[n]["venstre"] == True and hukommelse[n]["hoyre"] == True:
	 	hukommelse = {}

	elif er_vanlig() or er_inngang():

		if hukommelse[n]["hoyre"] == False and hukommelse[n]["hoyre_tom"] == False:
			gaa_hoyre()
			steg += 1
			hukommelse[n]["siste_steg"] = "hoyre"
			hukommelse[n]["hoyre"] = True

		elif hukommelse[n]["venstre"] == False and hukommelse[n]["venstre"] == False:
			gaa_venstre()
			steg += 1
			hukommelse[n]["siste_steg"] = "venstre"
			hukommelse[n]["venstre"] = True

		else:
			gaa_tilbake()
			steg += 1
			if hukommelse[nummer()]["siste_steg"] == "hoyre":
				hukommelse[nummer()]["hoyre_tom"] = True
			elif hukommelse[nummer()]["siste_steg"] == "venstre":
				hukommelse[nummer()]["hoyre_tom"] = True
			else:
				print("Fail")
				break


gaa_ut()
print("Victory")
print(steg)
print(nodeliste)
# print(nokkelnoder)
# print(laasenoder)
# print(superlaasenoder)