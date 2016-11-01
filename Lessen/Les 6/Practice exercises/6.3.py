klas = {}
invoer = input('Voer een naam in: ')

while invoer is not '':

    if invoer not in klas:
        klas[invoer] = 1

    else:
        klas[invoer] += 1
    invoer = input('Voer een naam in: ')

for (key, waarde) in klas.items():
    if waarde == 1:
        print('Er is {} student met de naam {}'.format(str(waarde), key))
for (key, waarde) in klas.items():
    if waarde > 1:
        print('Er zijn {} studenten met de naam {}'.format(str(waarde), key))
