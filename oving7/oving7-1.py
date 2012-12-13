from math import cos, sin, sqrt

def polynom(x):
	return ((x**5) - (4*(x**3)) + (10*(x**2)) - 10)

def polynom2(x):
	return ((1/4)*x**2 + cos(2*x))

def polynom3(x):
	if x < 0:
		return -sqrt(-x)
	return sqrt(x)

def polynom3_derivative(x):
	if x < 0:
		return (1/(2 * -sqrt(-x)))
	return (1/(2 * sqrt(x)))

def polynom2_derivative(x):
	return ((1/2)*x - 2*sin(2*x))

def polynom_derivative(x):
	return ((5*(x**4)) - (12*(x**2)) + (20*x))

def newton(func, deriv, start, threshold, max_iterations):
	xn = start
	for i in range(max_iterations):
		xn -= (func(xn)/deriv(xn))
	if abs(func(xn)/deriv(xn)) > threshold:
		return False
	return xn

# print(format(newton(polynom, polynom_derivative, 1, 0.000001, 20), '.6f'))
# print(format(newton(polynom, polynom_derivative, -3, 0.000001, 20), '.6f'))
# print(format(newton(polynom, polynom_derivative, -1, 0.000001, 20),'.6f'))
# print(newton(polynom, polynom_derivative, 0.01, 0.000001, 20))
# print(newton(polynom, polynom_derivative, -2.08, 0.000001, 20))
print(newton(polynom2, polynom2_derivative, 1, 10**(-10), 10000))
print(newton(polynom3, polynom3_derivative, 1, 0.001, 20))