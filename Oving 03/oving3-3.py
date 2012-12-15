from math import pi

def circle(r):
    area = format(pi*r*r, '.2f')
    circumference = format(2*pi*r, '.2f')
    print("Radius:", radius)
    print("Area:", area)
    print("Circumference:", circumference)

circle(10)
print("10 is an argument")

a = 1

def foo(a) :
    a = a**2
    print(a)

foo(2)
print(a)
