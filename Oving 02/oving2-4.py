def f_to_c():
    f = float(input("Skriv inn antall grader i fahrenheit: "))
    c = ((f - 32) * 5/9)
    print("%.2f i fahrenheit er %.2f grader i celsius" % (f, c))

f_to_c()
