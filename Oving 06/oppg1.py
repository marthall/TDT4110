x = int(input("Skriv inn et heltall: "))
n = 0
i = 1
while (n + i**2) <= x:
    n = n + i**2
    print("%s: %s" % (i, n))
    i += 1
