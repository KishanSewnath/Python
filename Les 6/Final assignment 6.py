letterlijst = []
naam = input('Wat is je naam?: ')
begin = input('Voer uw beginstation in: ')
eind = input('Voer uw eindstation in: ')
def code(invoerstring):
    for letter in invoerstring:
        letter1 = ord(letter)+3
        letter2 = chr(letter1)
        letterlijst.append(letter2)
    codering = ','.join(letterlijst)
    return ('Unieke code: {}'.format(codering))
print(code(naam+begin+eind))
