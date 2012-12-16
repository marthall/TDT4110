import random

def pick_sentence(sentences):
    return sentences[random.randint(0, len(sentences)-1)]

def print_sentence(a,b,c):
    print("%s %s%s" % (a,b,c))

def intro_text():
    for i in range(20):
        print("\n")
    print("Hei, jeg heter Eliza og vil gjerne snakke med deg.")
    print("Ikke start svar med stor bokstav og bruk hele setninger.")
    print("Skriv 'hade' hvis du vil avslutte samtalen")
    print("**************************************************")
    print("\n")

def main():
    answer = "ikke hade"
    questions = ['Hva gjoer du', 'Hvordan gaar det', 'Hvorfor heter du',
                'Liker du aa hete', 'Foeler du deg bra', 'Hva har du gjort idag',
                'Hva tenker du om framtida', 'Hva gjoer deg glad', 'Hva gjoer deg trist']
    follow_ups = ['Hvorfor sier du', 'Hva mener du med', 'Hvor lenge har du sagt',
                 'Hvilke tanker har du om', 'Kan du si litt mer om',
                 'Naar tenkte du foerste gang paa']
    responses = ['Fint du sier det', 'Det skjoenner jeg godt', 'Saa dumt da', 'Foeler meg ogsaa saann',
                'Blir trist av det du sier', 'Saa bra', 'Du er jammen frekk']
    intro_text()
    name = input("Hva heter du? ")

    while answer != "hade":
        pass
        sentence = pick_sentence(questions)
        print_sentence(sentence, name, "?")
        answer = input("Svar: ")
        follow_up = pick_sentence(follow_ups)
        print_sentence(follow_up, answer, "?")
        answer = input("Svar: ")
        resp = pick_sentence(responses)
        print_sentence(resp, name, ".")

main()
