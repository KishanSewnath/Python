studenten = ['jan', 'piet', 'henk', 'hennie', 'jan', 'henk']

teller = {}

for naam in studenten:
    if naam not in teller:
        teller[naam] = 1

    else:
        teller[naam] = teller[naam] + 1

print(teller)
