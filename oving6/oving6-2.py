li = [i for i in range (1,7)]

for i in li:
	if li[i] % 2 == 0:
		li[i] *= -1

li.sort(reverse=True)

print(li)