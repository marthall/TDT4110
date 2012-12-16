cheeses = {
  'cheddar':
    ('A235-4', 'A236-1', 'A236-2', 'A236-3', 'A236-5', 'C31-1', 'C31-2'),
  'mozarella':
    ('Q456-9', 'Q456-8', 'A234-5', 'Q457-1', 'Q457-2'),
  'brie':
    ('ZLAFS55-4', 'ZLAFS55-9', 'GOMBOS-7', 'A236-4'),
  'geitost':
    ('SPAZ-1', 'SPAZ-3', 'EMACS45-0'),
  'port salut':
    ('B15-1', 'B15-2', 'B15-3', 'B15-4', 'B16-1', 'B16-2', 'B16-4'),
  'camembert':
    ('A243-1', 'A234-2', 'A234-3', 'A234-4', 'A235-1', 'A235-2', 'A235-3'),
  'ridder':
    ('GOMBOS-4', 'B16-3'),
}

infected_cheeses = []
infected_vaults = ["A234", "A235", "B13", "B15", "C31"]

def a():
    return(cheeses["port salut"])

def b(ch, inf_ch, inf_va):
    for i in range(len(ch.items())):
        for j in inf_va:
            for k in list(ch.items())[i][1]:
                if j in k:
                    inf_ch.append(list(ch.keys())[i])
    return(set(inf_ch))

def c(ch, inf_ch, inf_va):
    inf = list(b(ch, inf_ch, inf_va))
    for i in list(ch.items()):
        if i[0] not in inf:
            for j in i[1]:
                print("%-10s\t%s" % (j,i[0]))


print(a())
print("")
print(b(cheeses, infected_cheeses, infected_vaults))
print("")
c(cheeses, infected_cheeses, infected_vaults)
