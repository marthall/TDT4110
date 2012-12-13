tall = [i for i in range(1,10)]


def number_of_lines(filename):
	filename.seek(0)
	i = 0
	for line in filename:
		i += 1
	return i

def number_frequency(filename):
	frequency = {}
	for i in tall:
		frequency[i] = 0
		filename.seek(0)
		for line in filename:
			if int(line) == i:
				frequency[i] += 1
	return frequency

def main():
	filename = open("nummer.txt", "r")
	frequency = number_frequency(filename)
	for i in frequency.items():
		print(i)
	filename.close()

main()