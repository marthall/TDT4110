def pris(age):
    if age < 5:
        return ("Free")
    elif age >= 6 and age <= 15:
        return ("10 kr")
    elif age >= 16 and age <= 20:
        return ("20 kr")
    elif age >= 21 and age <= 25:
        return ("30 kr")
    elif age >= 26 and age <= 60:
        return ("40 kr")
    elif age > 60:
        return ("Free")

def write(age):
    a = price(age)
    print("Price: " + a)

age = int(input("age: "))
write(age)
