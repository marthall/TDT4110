def equal(streng1, streng2):
    streng1 = list(streng1)
    streng2 = list(streng2)
    if len(streng1) != len(streng2):
        return False
    for i in range(len(streng1)):
        if streng1[i] != streng2[i]:
            return False
    return True

print(equal("hei", "he"))

def reverse(streng):
    return streng[::-1]
    
print(reverse("hei"))

def palindrom(streng):
    gnerts = reverse(streng)
    if streng == gnerts:
        return True
    return False

print(palindrom("agnes i senga"))

def inneholder(streng1, streng2):
    if streng1.find(streng2) == -1:
        return False
    return streng1.find(streng2)


print(inneholder("heisann", "eis"))
