from math import ceil, sqrt
from random import randint

def is_prime(number):
    for i in range(2, ceil(sqrt(number))):
        if number%i == 0:
            return False
    return True

def separate(tall, threshold):
    return [[i for i in tall if i < threshold], [i for i in tall if i >= threshold]]

# oppg 5a
print("-------------------------------")
number = int(input("Tall: "))
print("Er primtall:", is_prime(number))
print("-------------------------------")

# oppg 5b
tall = [randint(1,10) for i in range(10)]
threshold = 5
print("Original liste:", tall)
print("Splittet liste:", separate(tall, threshold))
print("-------------------------------")

# oppg 5c
n = int(input("Skriv inn et tall for å få gangetabellen: ")) + 1
a = [[i*j for j in range(1,n)] for i in range(1,n)]

for k in a:
    for l in k:
        print(l, end="\t")
    print("")
print("-------------------------------")