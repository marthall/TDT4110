# Oppgave 1:
import textwrap

a = ("""
	Et høynivå-programmeringsspråk bruker naturlig språkelementer, er lettere forstålig og
	tar ofte ikke for seg minnehåndtering og lignende. Et Lavprogrammeringsspråk ligger tettere
	mot maskinkode og er som oftest mer effektiv enn høynivå, da dette tar for seg mange unødvendige steg
	""")

b = ("""
	Programmtelleren holder kontroll over hvor langt en prosess har kommet. Enten utføres det som
	adressen til instruksjonen som utføres eller til adressen til neste instruksjon.
	""")

c = ("""
	En kompilator tar høynivåspråk og kompilerer det til lavnivåspråk, slik at maskinen kan kjøre koden
	direkte.
	""")

for i in [a,b,c]:
	textwrap.wrap(i)
	print(i)