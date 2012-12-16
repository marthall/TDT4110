def number_of_lines(filename):
    lines = 0
    with open(filename) as f:
        for line in f:
            lines += 1
    return lines

def number_frequency(filename):
    dic = {}
    with open(filename) as f:
        for line in f:
            line = int(line.strip())
            dic[line] = dic.get(line, 0) + 1
    return dic

print(number_of_lines("nummer.txt"))

dic = number_frequency("nummer.txt")
for num, value in dic.items():
    print("%i: %i" % (num, value))