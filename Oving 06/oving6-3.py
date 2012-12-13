def user_input():
	vec1 = input("Skriv inn tre tall separert av komma: ")
	vec1 = vec1.split(",")
	for i in range(len(vec1)):
		vec1[i] = int(vec1[i])
	return vec1

def skalar_mult():
	vec2 = []
	vec1 = user_input()
	len_list(vec1)
	skalar = int(input("Skriv inn en skalar: "))
	for i in range(len(vec1)):
		vec2.append(skalar * vec1[i])
	vec1 += vec2
	len_list(vec1)
	print((len(vec1))/((len(vec1)-len(vec2))))
	return vec1

def print_li():
	print(user_input())
	print(skalar_mult())

def len_list(x):
	print(len(x))
	

#user_input()
print_li()
