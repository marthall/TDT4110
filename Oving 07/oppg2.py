from math import e

def e_func(x):
    return (e**(-1*(x**2)))

def simpson(func, a, b, h):
    dx = (b-a)/h
    ysum = func(a) + func(b)
    for i in range(1,h):
        if i % 2 == 0:
            ysum += 2 *func(a + (i*(dx)))
        else:
            ysum += 4 *func(a + (i*(dx)))
    return (dx/3)*ysum

def simpson_error(func, a, b, error):
    h = 1
    while abs(simpson(func, a, b, 2**h) - simpson(func, a, b, 2**(h+1))) > error:
        h += 1
        print(2**h)
    return (simpson(func, a, b, 2**h))

print(simpson_error(e_func, 0, 1, 10**(-8)))