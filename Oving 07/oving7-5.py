from math import ceil, sqrt

def is_prime(number):
    for i in range(2, ceil(sqrt(number))):
        if number%i == 0:
            return False
    return True

print("-------------------------------")
number = int(input("Tall: "))
print(is_prime(number))
print("-------------------------------")

input("Press en tast for å fortsette")

print("-------------------------------")

def separate(tall, threshold):
    mindre_tall = []
    storre_tall = []
    for i in tall:
        if i < threshold:
            mindre_tall.append(i)
        else:
            storre_tall.append(i)
    return mindre_tall, storre_tall

tall = [1,2,3,4,5,6,7,8,9,10]
threshold = 5
print(separate(tall, threshold))

print("-------------------------------")

n = int(input("Skriv inn et tall for å få gangetabellen: "))

a = [[i*j for j in range(1,n)] for i in range(1,n)]

for k in a:
    for l in k:
        print(l, end="\t")
    print("")

print("-------------------------------")
