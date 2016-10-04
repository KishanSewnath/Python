lijst = []

invoer = '5-9-7-1-7-8-3-2-4-8-7-9'
gesplit = invoer.split('-')
gesort = sorted(gesplit)

for nummer in gesort:
    lijst.append(int(nummer))


grootste_waarde = max(lijst)
kleinste_waarde = min(lijst)
aantal_getallen = len(lijst)
som_getallen = sum(lijst)

print('Gesorteerde list van ints: ' + str(lijst))
print('Grootste getal : ' + str(grootste_waarde) + ' en Kleinste getal: ' + str(kleinste_waarde))
print('Aantal getallen: ' + str(aantal_getallen) + ' en Som van de getallen: ' + str(som_getallen))
print('Gemiddelde: ' + str(som_getallen/aantal_getallen))
