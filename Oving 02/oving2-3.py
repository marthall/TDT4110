def main():
	navn = input("Navnet paa bilen: ")
	brutto = int(input("Bruttopris på bilen [kr]: "))
	vekt = int(input("Vekt paa bilen [kg]: "))
	hk = int(input("Antall hestekriefter paa bilen [hk]: "))
	co2 = float(input("Antall gram Co2-utslipp paa bilen [gram]: "))
	volum = float(input("Motorvolum paa bilen [liter]: "))
	print("")
	beregn_avgift(navn, brutto, vekt, hk, co2, volum)

def beregn_avgift(navn, brutto, vekt, hk, co2, volum):
	Vekt = brutto * vekt * 0.00034
	Hk = brutto * hk * 0.00015
	Co2 = brutto * co2 * 0.004
	Volum = brutto * volum * 0.00055
	Nettopris = Vekt + Hk + Co2 + Volum + brutto
	print("Utsalgspris paa %s vil bli %.2f" %(navn, Nettopris))	

main()
beregn_avgift('Ford Mondeo 1.8', 120000, 1680, 125, 125, 1800)
beregn_avgift('Ford Mondeo 1.0', 130000, 1780, 125, 114, 1000)
beregn_avgift('BMV M5 3.0', 260000, 1980, 350, 150, 3000)
beregn_avgift('BMV M5 1.3', 270000, 1980, 350, 125, 1300)