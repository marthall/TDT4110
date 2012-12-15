a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

d = b*b-(4*a*c)

if d < 0:
    print("The equation %ix² + %ix + %i = 0 has two imaginary solutions" % (a,b,c))
elif d > 0:
    print("The equation %ix² + %ix + %i = 0 has two real solutions" % (a,b,c))
elif d == 0:
    print("The equation %ix² + %ix + %i = 0 has one real solution" % (a,b,c))
