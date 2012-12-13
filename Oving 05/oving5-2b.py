def er_mann():
	kjonn = input("Hvilket kjønn er du? (m/k)" )
	if kjonn == m:
		return True
	elif kjonn == k:
		return False
	else:
		return er_mann()

def alder():
	alder = input("Hvor gammel er du? ")
	if alder == "hade":
		return "hade"
	else:
		alder = int(alder)
		return 16 < alder < 25

def aktiv_sos():
	aktiv_sos = input("Er du aktiv på sosiale medier? (ja/nei)")
	if aktiv_sos == "ja":
		return True
	elif aktiv_sos == "nei":
		return False
	else:
		return aktiv_sos()

def face():
	if er_mann:
		face = input("Mellom 40-45% av Facebook sine brukere er menn. Er du en av disse?(ja/nei) ")
	else:
		face = input("Mellom 55-60% av Facebook sine brukere er kvinner. Er du en av disse?(ja/nei) ")
	if face == "ja":
		return True
	elif face == "nei":
		return False
	else:
		return face()

def timer_sos():
	return input("Hvor mange timer bruker du daglig på sosiale medier?")

i = 0
def main():
	while i == 0:
		er_mann()
		if alder() == "hade":
			break
		if alder():
			