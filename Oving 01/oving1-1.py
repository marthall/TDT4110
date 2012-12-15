from math import sin, cos
pi = 3.1415

# Converts from polar coordinate to cartesian coordinate.
def polar_to_cartesian(r, phi):
    x = r * cos(phi)
    y = r * sin(phi)
    print ("The cartesian coordinate of (%.1f, %.2f) is (%.2f, %.2f)" % (r, phi, x, y))

polar_to_cartesian(3, pi/2)
polar_to_cartesian(2.3, pi/3)
polar_to_cartesian(5,0)
