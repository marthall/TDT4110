f0 = 0
f1 = 1
numbers = []
def fib(number):
    fmin1 = f1
    fmin2 = f0
    for n in range(2, (number+1)):
        f = fmin1 + fmin2
        fmin2 = fmin1
        fmin1 = f
        numbers.append(f)

# fib(10)
# print(numbers)

# def rek_fib(number):
#       if number == 0:
#               return 0
#       elif number == 1:
#               return 1
#       else:
#               return (rek_fib(number-1) + rek_fib(number-2))

def rek_fib(n):
    if n == 0:
        return 1
    else:
        return (rek_fib(n-1)) * n

print(rek_fib(500))
