x, y = [1, 2, 4, 5, 3], [2, 4, 5, 4, 1]
range_x, range_y = max(x) - min(x), max(y) - min(y)
rad = []

for i in range(range_x + 2):
    rad.append("x")

print(rad)
