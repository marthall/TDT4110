from sys import exit
def global_values():
	print("--------------------------------------")
	print("Antall menn:\t\t\t %i" % antall_menn)
	print("Antall kvinner:\t\t\t %i" % antall_kvinner)
	print("Antall sosiale medier:\t\t %i" % antall_sosmedier)
	print("Antall facebook:\t\t %i" % antall_facebook)
	print("Antall timer sosiale medier:\t %i" % antall_timer_sosmedier)
	print("--------------------------------------")
	exit()

i = 0
antall_menn = 0
antall_kvinner = 0
antall_facebook = 0
antall_sosmedier = 0
antall_timer_sosmedier = 0

while i == 0:
	print("--------------------------------------")
	kjonn = None
	alder = None
	aktiv_sosmedier = None
	medlem_facebook = None
	timer_sosmedier = None
	while kjonn != "m" and kjonn != "k":
		kjonn = input("Hvilket kjønn er du?(m/k) ")
		if kjonn == "m":
			antall_menn +=1
		elif kjonn == "k":
			antall_kvinner += 1
		elif kjonn == "hade":
			global_values()
		else:
			print("Ikke gyldig kjønn")
	while alder == None:
		alder = input("Hvor gammel er du? ")
		if alder == "hade":
			global_values()
		else:
			alder = int(alder)
			if alder < 16 or alder > 25:
				print("Du er ikke i den tiltenkte aldersgruppen")
				global_values()
	while aktiv_sosmedier != "ja" and aktiv_sosmedier != "nei":
		aktiv_sosmedier = input("Er du aktiv i sosiale medier?(ja/nei) ")
		if aktiv_sosmedier == "hade":
			global_values()
		elif aktiv_sosmedier == "ja" or aktiv_sosmedier == "nei":
			antall_sosmedier += 1
		else:
			print("Ikke gyldig svar")
	if aktiv_sosmedier == "ja":
		while medlem_facebook != "ja" and medlem_facebook != "nei":
			if kjonn == "m":
				while medlem_facebook != "ja" and medlem_facebook != "nei":
					medlem_facebook = input("Mellom 40-45% av Facebook sine brukere er menn. Er du en av disse?(ja/nei) ")
					if medlem_facebook == "hade":
						global_values()
					elif medlem_facebook == "ja":
						antall_facebook += 1
					elif medlem_facebook == "nei":
						None
					else:
						print("Ikke gyldig svar")
			elif kjonn == "k":
				medlem_facebook = input("Mellom 55-60% av Facebook sine brukere er kvinner. Er du en av disse?(ja/nei) ")
				while medlem_facebook != "ja" and medlem_facebook != "nei":
					if medlem_facebook == "hade":
						global_values()
					elif medlem_facebook == "ja":
						antall_facebook += 1
					elif medlem_facebook == "nei":
						None
					else:
						print("Ikke gyldig svar")
			else:
				None
		while timer_sosmedier == None:
			timer_sosmedier = float(input("Hvor mange timer bruker du i snitt daglig på sosiale medier? "))
			antall_timer_sosmedier += timer_sosmedier

