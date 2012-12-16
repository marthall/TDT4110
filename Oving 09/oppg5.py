def number_of_all(filename):
    number = 0
    with open(filename) as f:
        for line in f:
            if line.strip().split(",")[1] == '"Alle"':
                number += 1
    return number

def average_score(filename):
    sum = 0
    number = 0
    with open(filename) as f:
        for line in f:
            if not line.strip().split(",")[1] == '"Alle"':
                sum += float(line.strip().split(",")[1])
                number += 1
    return (sum/number)

def max_min(filename):
    max = 0
    min = 60
    with open(filename) as f:
        for line in f:
            line = line.strip().split(",")[1]
            if line != '"Alle"':
                line = float(line)
                if line > max:
                    max = line
                if line < min:
                    min = line
    return (min, max)

print("Antall:        %i" % number_of_all("poenggrenser_2011.csv"))
print("Gjennomsnitt:  %.2f" % average_score("poenggrenser_2011.csv"))
print("Topp:          %.1f\nBunn:          %.1f" % max_min("poenggrenser_2011.csv"))