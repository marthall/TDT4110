def gcd(a, b):
    while b != 0:
        gammel_b = b
        b = (a % b)
        a = gammel_b
    return a

def reduce_fraction(a,b):
    kort_teller = a / gcd(a,b)
    kort_nevner = b / gcd(a,b)
    return kort_teller, kort_nevner

teller = int(input("Skriv inn teller: "))
nevner = int(input("Skriv inn nevner: "))

kort_teller,kort_nevner = reduce_fraction(teller,nevner)

print("For teller = %i, nevner = %i er den forkortede brøken (%i/%i)" % (teller, nevner, kort_teller, kort_nevner))
