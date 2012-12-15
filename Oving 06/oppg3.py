from math import sqrt

def user_input():
    vec1 = input("Skriv inn tre tall separert av komma: ")
    vec1 = vec1.split(",")
    for i in range(len(vec1)):
        vec1[i] = float(vec1[i])
    return vec1

def fin_print():
    global vec1, length
    vec1 = user_input()
    length_vec = length(vec1)
    print("Vektor 1: %s" % vec1)
    print("Lengde: %.2f" % length_vec)

def skalar_mult(vec1, skalar):
    for i in range(len(vec1)):
        vec1[i] *= skalar
    return vec1

def length(vec1):
    return sqrt(vec1[0]**2 + vec1[1]**2 + vec1[2]**2)

def indreprodukt(vec1, vec2):
    indreprodukt = 0
    for i in range(3):
        indreprodukt += int(vec1[i])*int(vec2[i])
    return indreprodukt



print("------------------------------")
fin_print()
print("------------------------------")
skalar = int(input("Skriv inn en skalar: "))
vec1mult = skalar_mult(vec1, skalar)
print("Vektor: %s" % vec1mult)
print("Lengde: %.2f" % length(vec1mult))
print("Forhold: %.2f" % skalar)
print("------------------------------")
vec2 = user_input()
indreprodukt = indreprodukt(vec1, vec2)
print("Indreprodukt: %.2f" % indreprodukt)
print("------------------------------")
