x = int(input("Skriv inn et heltall: "))
n = 0
for i in range(1,x):
	n = n + i**2
	if n > x:
		print(n-(i**2))
		print(i-1)
		break